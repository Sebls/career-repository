"""Unit tests for ATS analyzer and markdown reporter."""

from __future__ import annotations

from pathlib import Path
import pytest

from cv_verifier.ats_analyzer import ATSAnalyzer, ATSAuditResult, ContactCheckResult
from cv_verifier.extractors.base import ExtractionResult
from cv_verifier.reporter import ApplicationVerificationReporter, VerificationReporter


def test_contact_info_detection():
    """Verify that contact info detection correctly identifies profile details."""
    sample_text = (
        "Alex Doe\n"
        "San Francisco, CA | alex.doe@example.com | +1 (555) 019-2834\n"
        "linkedin.com/in/alexdoe | github.com/alexdoe | https://alexdoe.dev\n"
    )
    analyzer = ATSAnalyzer(is_french=False)
    result = analyzer.analyze_contact_info(sample_text)

    assert result.name_detected is True
    assert result.email_detected is True
    assert result.phone_detected is True
    assert result.location_detected is True
    assert result.linkedin_detected is True
    assert result.github_detected is True
    assert result.website_detected is True
    assert result.score == 100.0


def test_section_detection_english():
    """Verify standard section heading recognition in English."""
    sample_text = (
        "Summary\nProfile statement here.\n"
        "Experience\nSoftware Engineer at Company\n"
        "Education\nMaster of Science\n"
        "Projects\nDistributed System\n"
        "Skills\nPython, Docker, PyTorch\n"
    )
    analyzer = ATSAnalyzer(is_french=False, doc_type="cv")
    result = analyzer.analyze_sections(sample_text)

    assert result.detected_sections["Experience"] is True
    assert result.detected_sections["Education"] is True
    assert result.detected_sections["Projects"] is True
    assert result.detected_sections["Skills"] is True
    assert result.score == 100.0


def test_section_detection_french():
    """Verify standard section heading recognition in French."""
    sample_text = (
        "Expérience Professionnelle\nIngénieur IA\n"
        "Formation\nMaster Informatique\n"
        "Projets\nSystème distribué\n"
        "Compétences Techniques\nPython, Rust, Docker\n"
    )
    analyzer = ATSAnalyzer(is_french=True, doc_type="cv")
    result = analyzer.analyze_sections(sample_text)

    assert result.detected_sections["Expérience"] is True
    assert result.detected_sections["Formation"] is True
    assert result.detected_sections["Projets"] is True
    assert result.detected_sections["Compétences"] is True
    assert result.score == 100.0


def test_cover_letter_structure_english():
    """Verify cover letter structural element detection in English."""
    sample_text = (
        "Alex Doe\n"
        "San Francisco, CA | alex.doe@example.com\n"
        "Hiring Team\nTech Innovations Inc.\nSan Francisco, CA\n\n"
        "Re: Machine Learning Engineer Application\n\n"
        "Dear Hiring Team,\n\n"
        "I am writing to express my enthusiasm for the role...\n\n"
        "Sincerely,\n\n"
        "Alex Doe\n"
    )
    analyzer = ATSAnalyzer(is_french=False, doc_type="cover_letter")
    result = analyzer.analyze_sections(sample_text)

    assert result.detected_sections["Recipient / Addressee"] is True
    assert result.detected_sections["Subject Line"] is True
    assert result.detected_sections["Salutation"] is True
    assert result.detected_sections["Closing / Sign-off"] is True
    assert result.detected_sections["Sign-off Name"] is True
    assert result.score == 100.0


def test_cover_letter_structure_french():
    """Verify cover letter structural element detection in French."""
    sample_text = (
        "Alex Doe\n"
        "Paris, France | alex.doe@example.com\n"
        "Madame, Monsieur,\n"
        "Équipe de recrutement\n\n"
        "Objet : Candidature au poste d'Ingénieur IA\n\n"
        "Madame, Monsieur,\n\n"
        "Je vous présente ma candidature avec un vif intérêt...\n\n"
        "Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.\n\n"
        "Alex Doe\n"
    )
    analyzer = ATSAnalyzer(is_french=True, doc_type="cover_letter")
    result = analyzer.analyze_sections(sample_text)

    assert result.detected_sections["Destinataire / Entreprise"] is True
    assert result.detected_sections["Objet / Référence"] is True
    assert result.detected_sections["Salutation"] is True
    assert result.detected_sections["Formule de Politesse / Closing"] is True
    assert result.detected_sections["Sign-off Name"] is True
    assert result.score == 100.0


def test_jaccard_similarity():
    """Verify Jaccard text similarity calculation."""
    t1 = "Alex Doe software engineer python machine learning"
    t2 = "Alex Doe machine learning python developer"
    sim = ATSAnalyzer.compute_jaccard_similarity(t1, t2)
    assert sim > 50.0


def test_reporter_markdown_generation(tmp_path: Path):
    """Verify Markdown report generation for CV."""
    ext = ExtractionResult(
        engine_name="PyMuPDF",
        engine_version="1.24.0",
        success=True,
        raw_text="Alex Doe\nalex.doe@example.com\nExperience\nEducation\nSkills\nProjects",
    )
    analyzer = ATSAnalyzer(is_french=False, doc_type="cv")
    audit = analyzer.audit_extraction(ext)

    out_file = tmp_path / "test_report.md"
    reporter = VerificationReporter(
        pdf_path="cv/en/cv.pdf",
        extractions=[ext],
        audits=[audit],
        is_french=False,
        doc_type="cv",
    )
    saved = reporter.write_to_file(out_file)
    assert saved.exists()
    content = saved.read_text(encoding="utf-8")
    assert "# PDF ATS Extraction & Verification Report" in content
    assert "PyMuPDF" in content


def test_reporter_cover_letter_markdown(tmp_path: Path):
    """Verify Markdown report generation for Cover Letter."""
    ext = ExtractionResult(
        engine_name="PyMuPDF",
        engine_version="1.24.0",
        success=True,
        raw_text="Alex Doe\nalex.doe@example.com\nDear Hiring Team,\nRe: AI Engineer\nSincerely,\nAlex Doe",
    )
    analyzer = ATSAnalyzer(is_french=False, doc_type="cover_letter")
    audit = analyzer.audit_extraction(ext)

    out_file = tmp_path / "test_cl_report.md"
    reporter = VerificationReporter(
        pdf_path="application/cover-letter/cover-letter.pdf",
        extractions=[ext],
        audits=[audit],
        is_french=False,
        doc_type="cover_letter",
    )
    saved = reporter.write_to_file(out_file)
    assert saved.exists()
    content = saved.read_text(encoding="utf-8")
    assert "# Cover Letter Extraction & Verification Report" in content
    assert "Structural & Component Recognition Matrix" in content


def test_application_verification_reporter_combined(tmp_path: Path):
    """Verify combined Application Verification Reporter generation."""
    cv_ext = ExtractionResult(
        engine_name="PyMuPDF",
        engine_version="1.24.0",
        success=True,
        raw_text="Alex Doe\nalex.doe@example.com\nExperience\nEducation\nSkills\nProjects",
    )
    cv_analyzer = ATSAnalyzer(is_french=False, doc_type="cv")
    cv_audit = cv_analyzer.audit_extraction(cv_ext)
    cv_reporter = VerificationReporter("application/cv/cv.pdf", [cv_ext], [cv_audit], is_french=False, doc_type="cv")

    cl_ext = ExtractionResult(
        engine_name="PyMuPDF",
        engine_version="1.24.0",
        success=True,
        raw_text="Alex Doe\nalex.doe@example.com\nDear Hiring Team,\nRe: AI Engineer\nSincerely,\nAlex Doe",
    )
    cl_analyzer = ATSAnalyzer(is_french=False, doc_type="cover_letter")
    cl_audit = cl_analyzer.audit_extraction(cl_ext)
    cl_reporter = VerificationReporter("application/cover-letter/cover-letter.pdf", [cl_ext], [cl_audit], is_french=False, doc_type="cover_letter")

    app_reporter = ApplicationVerificationReporter(cv_reporter=cv_reporter, cover_letter_reporter=cl_reporter)
    out_file = tmp_path / "cv_app_verification.md"
    saved = app_reporter.write_to_file(out_file)

    assert saved.exists()
    content = saved.read_text(encoding="utf-8")
    assert "# Application Extraction & ATS Verification Report" in content
    assert "# Part I: Curriculum Vitae (CV) ATS Verification" in content
    assert "# Part II: Cover Letter ATS & Structure Verification" in content
