"""CLI Entrypoint for CV PDF Extraction and ATS Verification."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import List, Optional, Tuple

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from cv_verifier.ats_analyzer import ATSAnalyzer, ATSAuditResult
from cv_verifier.extractors import ALL_EXTRACTORS, get_all_extractors, get_extractor
from cv_verifier.extractors.base import BaseExtractor, ExtractionResult
from cv_verifier.reporter import ApplicationVerificationReporter, VerificationReporter

console = Console()


def detect_job_language(job_path: Path) -> Optional[bool]:
    """Inspect application/job.md to determine target language."""
    if not job_path.is_file():
        return None
    try:
        content = job_path.read_text(encoding="utf-8")
        match = re.search(r"^language:\s*(en|fr)\b", content, re.MULTILINE)
        if match:
            return match.group(1).lower() == "fr"
    except Exception:
        pass
    return None


def run_verification_for_pdf(
    pdf_path: Path,
    output_path: Optional[Path] = None,
    is_french: Optional[bool] = None,
    engines: Optional[List[str]] = None,
    doc_type: Optional[str] = None,
    skip_write: bool = False,
) -> Tuple[List[ExtractionResult], List[ATSAuditResult], Path, VerificationReporter]:
    """Execute multi-engine extraction and ATS audit on a specific PDF."""
    if not pdf_path.is_file():
        console.print(f"[bold red]Error: Target PDF not found at {pdf_path}[/bold red]")
        sys.exit(1)

    # Detect language if not explicitly provided
    if is_french is None:
        is_french = "/fr/" in str(pdf_path) or "_fr" in pdf_path.name.lower()

    # Detect doc type if not provided
    if doc_type is None:
        doc_type = "cover_letter" if ("cover-letter" in str(pdf_path) or "cover_letter" in str(pdf_path) or "lettre" in str(pdf_path)) else "cv"
    else:
        doc_type = doc_type.lower().replace("-", "_")

    if engines:
        extractors = [get_extractor(name) for name in engines]
    else:
        extractors = get_all_extractors()

    doc_label = "Cover Letter" if doc_type == "cover_letter" else "Curriculum Vitae"

    console.print(
        Panel.fit(
            f"[bold cyan]Auditing {doc_label} ATS Compatibility[/bold cyan]\n"
            f"[yellow]Target:[/yellow] {pdf_path}\n"
            f"[yellow]Document Type:[/yellow] {doc_label}\n"
            f"[yellow]Language:[/yellow] {'French' if is_french else 'English'}\n"
            f"[yellow]Engines:[/yellow] {', '.join(e.name for e in extractors)}",
            title="🔍 CV Verifier",
        )
    )

    analyzer = ATSAnalyzer(is_french=is_french, doc_type=doc_type)
    extractions: List[ExtractionResult] = []
    audits: List[ATSAuditResult] = []

    for extractor in extractors:
        with console.status(f"[bold green]Running {extractor.name}...[/bold green]"):
            ext_res = extractor.extract(pdf_path)
            audit_res = analyzer.audit_extraction(ext_res)
            extractions.append(ext_res)
            audits.append(audit_res)

    # Determine output markdown path
    if not output_path:
        stem = pdf_path.stem
        if "cv/en" in str(pdf_path):
            filename = "cv_en_verification.md"
        elif "cv/fr" in str(pdf_path):
            filename = "cv_fr_verification.md"
        elif "application" in str(pdf_path):
            filename = "cv_app_verification.md" if doc_type == "cv" else "cover_letter_app_verification.md"
        else:
            filename = f"{stem}_verification.md"
        output_path = Path("verification") / filename

    reporter = VerificationReporter(
        pdf_path=pdf_path,
        extractions=extractions,
        audits=audits,
        is_french=is_french,
        doc_type=doc_type,
    )

    saved_path = output_path
    if not skip_write:
        saved_path = reporter.write_to_file(output_path)

    # Render Rich Terminal Summary Table
    table = Table(title=f"ATS Extraction Results ({pdf_path.name} - {doc_label})", show_header=True)
    table.add_column("Engine", style="cyan", no_wrap=True)
    table.add_column("Version", style="dim")
    table.add_column("Status", justify="center")
    table.add_column("Score", justify="right")
    table.add_column("Time", justify="right")
    table.add_column("Words", justify="right")
    table.add_column("Chars", justify="right")
    table.add_column("Contacts", justify="right")
    table.add_column("Structure", justify="right")

    for ext, aud in zip(extractions, audits):
        status_style = (
            "[bold green]PASS[/bold green]"
            if aud.status == "PASS"
            else ("[bold yellow]WARN[/bold yellow]" if aud.status == "WARN" else "[bold red]FAIL[/bold red]")
        )
        table.add_row(
            str(ext.engine_name),
            str(ext.engine_version),
            status_style,
            f"{aud.overall_score}%",
            f"{ext.extraction_time_ms} ms",
            str(ext.word_count),
            str(ext.character_count),
            f"{aud.contact_check.score}%",
            f"{aud.section_check.score}%",
        )

    console.print(table)
    if not skip_write:
        console.print(f"\n[bold green]✅ Full verification report written to:[/bold green] [cyan]{saved_path}[/cyan]\n")

    return extractions, audits, saved_path, reporter


def run_application_verification(
    app_dir: Path = Path("application"),
    output_path: Optional[Path] = None,
    is_french: Optional[bool] = None,
    engines: Optional[List[str]] = None,
) -> Path:
    """Run verification for an application package, auditing CV and Cover Letter if present."""
    cv_pdf = app_dir / "cv" / "cv.pdf"
    cl_pdf = app_dir / "cover-letter" / "cover-letter.pdf"

    if not cv_pdf.is_file():
        console.print(f"[bold red]Error: Application CV not found at {cv_pdf}[/bold red]")
        sys.exit(1)

    if is_french is None:
        detected_lang = detect_job_language(app_dir / "job.md")
        if detected_lang is not None:
            is_french = detected_lang
        else:
            is_french = False

    target_output = output_path or Path("verification") / "cv_app_verification.md"

    if cl_pdf.is_file():
        console.print("[bold cyan]Found Cover Letter in application package. Auditing both CV and Cover Letter...[/bold cyan]\n")
        _, _, _, cv_reporter = run_verification_for_pdf(
            cv_pdf,
            is_french=is_french,
            engines=engines,
            doc_type="cv",
            skip_write=True,
        )
        _, _, _, cl_reporter = run_verification_for_pdf(
            cl_pdf,
            is_french=is_french,
            engines=engines,
            doc_type="cover_letter",
            skip_write=True,
        )
        app_reporter = ApplicationVerificationReporter(
            cv_reporter=cv_reporter,
            cover_letter_reporter=cl_reporter,
        )
        saved_path = app_reporter.write_to_file(target_output)
        console.print(f"\n[bold green]✅ Unified application verification report (CV + Cover Letter) written to:[/bold green] [cyan]{saved_path}[/cyan]\n")
        return saved_path
    else:
        _, _, saved_path, _ = run_verification_for_pdf(
            cv_pdf,
            output_path=target_output,
            is_french=is_french,
            engines=engines,
            doc_type="cv",
            skip_write=False,
        )
        return saved_path


@click.command()
@click.argument("pdf_path", type=click.Path(exists=False, path_type=Path), required=False)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Target Markdown report path (defaults to verification/<name>_verification.md)",
)
@click.option(
    "--all-canonical",
    is_flag=True,
    help="Run verification on both English and French canonical CVs",
)
@click.option(
    "--app",
    is_flag=True,
    help="Run verification on application package (CV and Cover Letter if present)",
)
@click.option(
    "--doc-type",
    type=click.Choice(["cv", "cover-letter", "cover_letter"], case_sensitive=False),
    default=None,
    help="Explicitly specify document type (auto-detected by default)",
)
@click.option(
    "--french/--english",
    default=None,
    help="Explicitly specify language (auto-detected if omitted)",
)
@click.option(
    "--engine",
    "-e",
    multiple=True,
    help="Specify engine(s) to run (pymupdf, pdfplumber, pypdf, pdfminer, unstructured)",
)
def main(
    pdf_path: Optional[Path],
    output: Optional[Path],
    all_canonical: bool,
    app: bool,
    doc_type: Optional[str],
    french: Optional[bool],
    engine: tuple[str, ...],
) -> None:
    """Extract and audit PDF text using PyMuPDF, pdfplumber, pypdf, pdfminer.six, and Unstructured."""
    selected_engines = list(engine) if engine else None

    if all_canonical:
        en_path = Path("cv/en/cv.pdf")
        fr_path = Path("cv/fr/cv.pdf")
        if not en_path.is_file() or not fr_path.is_file():
            console.print("[yellow]Compiling canonical CVs first...[/yellow]")
        run_verification_for_pdf(en_path, is_french=False, engines=selected_engines, doc_type="cv")
        run_verification_for_pdf(fr_path, is_french=True, engines=selected_engines, doc_type="cv")
        return

    if app or (pdf_path and str(pdf_path) == "application/cv/cv.pdf" and not doc_type):
        run_application_verification(output_path=output, is_french=french, engines=selected_engines)
        return

    if not pdf_path:
        console.print("[bold red]Error: Please provide a PDF path or use --all-canonical / --app[/bold red]")
        sys.exit(1)

    run_verification_for_pdf(
        pdf_path,
        output_path=output,
        is_french=french,
        engines=selected_engines,
        doc_type=doc_type,
    )


if __name__ == "__main__":
    main()

