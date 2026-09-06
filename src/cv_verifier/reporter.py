"""Markdown and Terminal Report Generator for PDF ATS Verification."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from tabulate import tabulate

from cv_verifier.ats_analyzer import ATSAnalyzer, ATSAuditResult
from cv_verifier.extractors.base import ExtractionResult


class VerificationReporter:
    """Generates structured Markdown reports and terminal output for LLM and ATS auditing."""

    def __init__(
        self,
        pdf_path: Path | str,
        extractions: List[ExtractionResult],
        audits: List[ATSAuditResult],
        is_french: bool = False,
        doc_type: str = "cv",
    ) -> None:
        self.pdf_path = Path(pdf_path)
        self.extractions = extractions
        self.audits = audits
        self.is_french = is_french
        self.doc_type = doc_type.lower().replace("-", "_")
        self.audit_by_engine: Dict[str, ATSAuditResult] = {a.engine_name: a for a in audits}
        self.extraction_by_engine: Dict[str, ExtractionResult] = {e.engine_name: e for e in extractions}

    def generate_markdown(self) -> str:
        """Construct a comprehensive Markdown verification report for this document."""
        lines: List[str] = []
        doc_title = "Cover Letter" if self.doc_type == "cover_letter" else "PDF ATS"

        # Title and Header
        lines.append(f"# {doc_title} Extraction & Verification Report")
        lines.append("")
        lines.append(f"**Target Document:** `{self.pdf_path}`  ")
        lines.append(f"**Document Type:** `{'Cover Letter' if self.doc_type == 'cover_letter' else 'Curriculum Vitae (CV)'}`  ")
        lines.append(f"**Language:** `{'French (fr)' if self.is_french else 'English (en)'}`  ")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ")
        lines.append(f"**Engines Tested:** {len(self.extractions)} (`PyMuPDF`, `pdfplumber`, `pypdf`, `pdfminer.six`, `Unstructured`)  ")
        lines.append("")
        lines.append("---")
        lines.append("")

        # 1. Executive Summary & Scorecard
        avg_score = round(sum(a.overall_score for a in self.audits) / len(self.audits), 1) if self.audits else 0.0
        all_passed = all(a.status == "PASS" for a in self.audits)
        
        status_badge = "🟢 **OPTIMAL ATS COMPLIANCE**" if all_passed else ("🟡 **MINOR WARNINGS**" if avg_score >= 70.0 else "🔴 **CRITICAL ATS ISSUES**")
        
        lines.append("## 1. Executive Summary")
        lines.append("")
        lines.append(f"### Overall Status: {status_badge} (Average Score: **{avg_score}%**)")
        lines.append("")

        # Engine Comparison Table
        table_rows = []
        for ext in self.extractions:
            aud = self.audit_by_engine.get(ext.engine_name)
            score_str = f"{aud.overall_score}%" if aud else "N/A"
            status_str = f"✅ {aud.status}" if aud and aud.status == "PASS" else f"⚠️ {aud.status if aud else 'ERR'}"
            table_rows.append([
                ext.engine_name,
                ext.engine_version,
                status_str,
                f"{score_str}",
                f"{ext.extraction_time_ms} ms",
                str(ext.word_count),
                str(ext.character_count),
                f"{aud.contact_check.score}%" if aud else "N/A",
                f"{aud.section_check.score}%" if aud else "N/A",
            ])

        headers = [
            "Engine",
            "Version",
            "Status",
            "Score",
            "Time (ms)",
            "Words",
            "Chars",
            "Contacts",
            "Structure",
        ]
        lines.append(tabulate(table_rows, headers=headers, tablefmt="github"))
        lines.append("")
        lines.append("---")
        lines.append("")

        # 2. Contact & Identity Information Matrix
        lines.append("## 2. Contact & Identity Parsing Matrix")
        lines.append("")
        lines.append("Verifies whether typical ATS parsers accurately extract candidate contact info without dropped fields.")
        lines.append("")

        contact_rows = []
        for ext in self.extractions:
            aud = self.audit_by_engine.get(ext.engine_name)
            if not aud:
                continue
            c = aud.contact_check
            contact_rows.append([
                ext.engine_name,
                "✅" if c.name_detected else "❌",
                "✅" if c.email_detected else "❌",
                "✅" if c.phone_detected else "❌",
                "✅" if c.location_detected else "❌",
                "✅" if c.linkedin_detected else "❌",
                "✅" if c.github_detected else "❌",
                "✅" if c.website_detected else "❌",
            ])

        contact_headers = [
            "Engine",
            "Name",
            "Email",
            "Phone",
            "Location",
            "LinkedIn",
            "GitHub",
            "Website",
        ]
        lines.append(tabulate(contact_rows, headers=contact_headers, tablefmt="github"))
        lines.append("")
        lines.append("---")
        lines.append("")

        # 3. Section / Structure Recognition Matrix
        if self.doc_type == "cover_letter":
            lines.append("## 3. Structural & Component Recognition Matrix")
            lines.append("")
            lines.append("Verifies whether standard cover letter structural components (Recipient, Subject, Salutation, Closing, Sign-off Name) are clearly parsed.")
        else:
            lines.append("## 3. Section Recognition Matrix")
            lines.append("")
            lines.append("Verifies whether standard CV section headings are clearly recognized.")
        lines.append("")

        section_names = list(self.audits[0].section_check.detected_sections.keys()) if self.audits else []
        section_rows = []
        for ext in self.extractions:
            aud = self.audit_by_engine.get(ext.engine_name)
            if not aud:
                continue
            row = [ext.engine_name]
            for sname in section_names:
                row.append("✅" if aud.section_check.detected_sections.get(sname, False) else "❌")
            section_rows.append(row)

        sec_headers = ["Engine"] + section_names
        lines.append(tabulate(section_rows, headers=sec_headers, tablefmt="github"))
        lines.append("")
        lines.append("---")
        lines.append("")

        # 4. Cross-Engine Concordance Matrix (Jaccard Similarity)
        lines.append("## 4. Cross-Engine Concordance Matrix")
        lines.append("")
        lines.append("Measures word-level Jaccard similarity across the 5 parsing libraries. High similarity (>90%) indicates robust and standard PDF text flow.")
        lines.append("")

        engine_names = [e.engine_name for e in self.extractions]
        matrix_rows = []
        for e1 in self.extractions:
            row = [e1.engine_name]
            for e2 in self.extractions:
                sim = ATSAnalyzer.compute_jaccard_similarity(e1.raw_text, e2.raw_text)
                row.append(f"{sim}%")
            matrix_rows.append(row)

        sim_headers = ["Engine"] + engine_names
        lines.append(tabulate(matrix_rows, headers=sim_headers, tablefmt="github"))
        lines.append("")
        lines.append("---")
        lines.append("")

        # 5. Raw Text Extraction per Engine (for LLM verification)
        lines.append("## 5. Extracted Text per Engine (LLM Verification Dump)")
        lines.append("")
        lines.append("Below are the exact raw extracted text bodies parsed by each library for detailed inspection by LLM agents.")
        lines.append("")

        for ext in self.extractions:
            aud = self.audit_by_engine.get(ext.engine_name)
            lines.append(f"### 📄 {ext.engine_name} (v{ext.engine_version})")
            lines.append(f"- **Extraction Time:** {ext.extraction_time_ms} ms | **Words:** {ext.word_count} | **Characters:** {ext.character_count}")
            if ext.metadata:
                clean_meta = {k: v for k, v in ext.metadata.items() if v}
                lines.append(f"- **PDF Metadata:** `{clean_meta}`")
            if ext.extra_info:
                lines.append(f"- **Engine Details:** `{ext.extra_info}`")
            if aud and aud.findings:
                lines.append("- **Audit Findings:**")
                for f in aud.findings:
                    lines.append(f"  - {f}")
            lines.append("")
            lines.append("```text")
            lines.append(ext.raw_text.strip() if ext.raw_text else "[NO TEXT EXTRACTED]")
            lines.append("```")
            lines.append("")

        return "\n".join(lines)

    def write_to_file(self, output_path: Path | str) -> Path:
        """Write the generated Markdown report to the target destination."""
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        content = self.generate_markdown()
        out.write_text(content, encoding="utf-8")
        return out


class ApplicationVerificationReporter:
    """Generates a combined verification report for applications with CV and optional Cover Letter."""

    def __init__(
        self,
        cv_reporter: VerificationReporter,
        cover_letter_reporter: Optional[VerificationReporter] = None,
    ) -> None:
        self.cv_reporter = cv_reporter
        self.cover_letter_reporter = cover_letter_reporter

    def generate_markdown(self) -> str:
        """Construct a unified Markdown report covering the entire application package."""
        if not self.cover_letter_reporter:
            return self.cv_reporter.generate_markdown()

        lines: List[str] = []
        lines.append("# Application Extraction & ATS Verification Report")
        lines.append("")
        lines.append(f"**CV Target:** `{self.cv_reporter.pdf_path}`  ")
        lines.append(f"**Cover Letter Target:** `{self.cover_letter_reporter.pdf_path}`  ")
        lines.append(f"**Language:** `{'French (fr)' if self.cv_reporter.is_french else 'English (en)'}`  ")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ")
        lines.append(f"**Engines Tested:** {len(self.cv_reporter.extractions)} (`PyMuPDF`, `pdfplumber`, `pypdf`, `pdfminer.six`, `Unstructured`)  ")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Application Overview Summary
        cv_avg = round(sum(a.overall_score for a in self.cv_reporter.audits) / len(self.cv_reporter.audits), 1) if self.cv_reporter.audits else 0.0
        cl_avg = round(sum(a.overall_score for a in self.cover_letter_reporter.audits) / len(self.cover_letter_reporter.audits), 1) if self.cover_letter_reporter.audits else 0.0
        
        cv_pass = all(a.status == "PASS" for a in self.cv_reporter.audits)
        cl_pass = all(a.status == "PASS" for a in self.cover_letter_reporter.audits)
        
        app_status = "🟢 **APPLICATION READY (ALL PASS)**" if (cv_pass and cl_pass) else "🟡 **APPLICATION WITH WARNINGS**"
        
        lines.append("## Executive Application Summary")
        lines.append("")
        lines.append(f"### Status: {app_status}")
        lines.append(f"- **Curriculum Vitae ATS Score:** **{cv_avg}%** ({'PASS' if cv_pass else 'CHECK'})")
        lines.append(f"- **Cover Letter Score:** **{cl_avg}%** ({'PASS' if cl_pass else 'CHECK'})")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Section I: Curriculum Vitae
        lines.append("# Part I: Curriculum Vitae (CV) ATS Verification")
        lines.append("")
        cv_md = self.cv_reporter.generate_markdown()
        # Drop the top header to avoid duplicate title
        cv_parts = cv_md.split("\n---\n\n", 1)
        if len(cv_parts) > 1:
            lines.append(cv_parts[1])
        else:
            lines.append(cv_md)

        lines.append("")
        lines.append("---")
        lines.append("")

        # Section II: Cover Letter
        lines.append("# Part II: Cover Letter ATS & Structure Verification")
        lines.append("")
        cl_md = self.cover_letter_reporter.generate_markdown()
        cl_parts = cl_md.split("\n---\n\n", 1)
        if len(cl_parts) > 1:
            lines.append(cl_parts[1])
        else:
            lines.append(cl_md)

        return "\n".join(lines)

    def write_to_file(self, output_path: Path | str) -> Path:
        """Write the combined Markdown report to the target destination."""
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        content = self.generate_markdown()
        out.write_text(content, encoding="utf-8")
        return out

