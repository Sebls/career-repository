"""Unit tests for all PDF extraction engines."""

from __future__ import annotations

from pathlib import Path
import pytest

from cv_verifier.extractors import ALL_EXTRACTORS, get_all_extractors, get_extractor
from cv_verifier.extractors.base import ExtractionResult
from cv_verifier.extractors.pdfminer_extractor import PDFMinerExtractor
from cv_verifier.extractors.pdfplumber_extractor import PDFPlumberExtractor
from cv_verifier.extractors.pymupdf_extractor import PyMuPDFExtractor
from cv_verifier.extractors.pypdf_extractor import PyPDFExtractor
from cv_verifier.extractors.unstructured_extractor import UnstructuredExtractor

EN_PDF = Path("cv/en/cv.pdf")
FR_PDF = Path("cv/fr/cv.pdf")


@pytest.mark.parametrize("extractor_cls", ALL_EXTRACTORS)
def test_extract_english_cv(extractor_cls):
    """Test that every extractor cleanly parses the English canonical CV."""
    if not EN_PDF.exists():
        pytest.skip("cv/en/cv.pdf does not exist")

    extractor = extractor_cls()
    result: ExtractionResult = extractor.extract(EN_PDF)

    assert result.success is True, f"{extractor.name} failed: {result.error_message}"
    assert result.word_count > 100, f"{extractor.name} extracted unexpectedly few words: {result.word_count}"
    assert "Alex" in result.raw_text, f"{extractor.name} did not extract candidate name"
    assert result.extraction_time_ms >= 0


@pytest.mark.parametrize("extractor_cls", ALL_EXTRACTORS)
def test_extract_french_cv(extractor_cls):
    """Test that every extractor cleanly parses the French canonical CV."""
    if not FR_PDF.exists():
        pytest.skip("cv/fr/cv.pdf does not exist")

    extractor = extractor_cls()
    result: ExtractionResult = extractor.extract(FR_PDF)

    assert result.success is True, f"{extractor.name} failed: {result.error_message}"
    assert result.word_count > 100, f"{extractor.name} extracted unexpectedly few words: {result.word_count}"
    assert "Alex" in result.raw_text, f"{extractor.name} did not extract candidate name"


def test_extractor_registry_get_by_name():
    """Verify extractor resolution by name."""
    assert isinstance(get_extractor("pymupdf"), PyMuPDFExtractor)
    assert isinstance(get_extractor("pdfplumber"), PDFPlumberExtractor)
    assert isinstance(get_extractor("pypdf"), PyPDFExtractor)
    assert isinstance(get_extractor("pdfminer.six"), PDFMinerExtractor)
    assert isinstance(get_extractor("unstructured"), UnstructuredExtractor)


def test_missing_file_handling():
    """Verify graceful error reporting when PDF does not exist."""
    extractor = PyMuPDFExtractor()
    result = extractor.extract(Path("non_existent_file.pdf"))
    assert result.success is False
    assert "File not found" in str(result.error_message)
