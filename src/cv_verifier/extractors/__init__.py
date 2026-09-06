"""Extraction engine module registry."""

from __future__ import annotations

from typing import Dict, List, Type

from cv_verifier.extractors.base import BaseExtractor, ExtractionResult
from cv_verifier.extractors.pdfminer_extractor import PDFMinerExtractor
from cv_verifier.extractors.pdfplumber_extractor import PDFPlumberExtractor
from cv_verifier.extractors.pymupdf_extractor import PyMuPDFExtractor
from cv_verifier.extractors.pypdf_extractor import PyPDFExtractor
from cv_verifier.extractors.unstructured_extractor import UnstructuredExtractor

ALL_EXTRACTORS: List[Type[BaseExtractor]] = [
    PyMuPDFExtractor,
    PDFPlumberExtractor,
    PyPDFExtractor,
    PDFMinerExtractor,
    UnstructuredExtractor,
]

EXTRACTOR_MAP: Dict[str, Type[BaseExtractor]] = {
    "pymupdf": PyMuPDFExtractor,
    "pdfplumber": PDFPlumberExtractor,
    "pypdf": PyPDFExtractor,
    "pdfminer": PDFMinerExtractor,
    "pdfminer.six": PDFMinerExtractor,
    "unstructured": UnstructuredExtractor,
}


def get_all_extractors() -> List[BaseExtractor]:
    """Instantiate and return all available extraction engines."""
    return [cls() for cls in ALL_EXTRACTORS]


def get_extractor(name: str) -> BaseExtractor:
    """Retrieve a specific extraction engine by name."""
    normalized = name.strip().lower()
    if normalized not in EXTRACTOR_MAP:
        raise ValueError(
            f"Unknown extractor: {name}. Available: {list(EXTRACTOR_MAP.keys())}"
        )
    return EXTRACTOR_MAP[normalized]()


__all__ = [
    "BaseExtractor",
    "ExtractionResult",
    "PyMuPDFExtractor",
    "PDFPlumberExtractor",
    "PyPDFExtractor",
    "PDFMinerExtractor",
    "UnstructuredExtractor",
    "ALL_EXTRACTORS",
    "EXTRACTOR_MAP",
    "get_all_extractors",
    "get_extractor",
]
