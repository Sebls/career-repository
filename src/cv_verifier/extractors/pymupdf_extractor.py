"""PyMuPDF (fitz) extraction engine implementation."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pymupdf

from cv_verifier.extractors.base import BaseExtractor, ExtractionResult


class PyMuPDFExtractor(BaseExtractor):
    """Text and layout extractor using PyMuPDF (pymupdf)."""

    name: str = "PyMuPDF"

    def get_version(self) -> str:
        return getattr(pymupdf, "__version__", "unknown")

    def _extract_impl(self, pdf_path: Path) -> ExtractionResult:
        doc = pymupdf.open(pdf_path)
        page_texts: List[str] = []
        raw_metadata: Dict[str, Any] = {}

        try:
            raw_metadata = dict(doc.metadata) if doc.metadata else {}
            total_blocks = 0
            links: List[str] = []

            for page in doc:
                text = page.get_text("text")
                page_texts.append(text)
                
                # Extract block information
                blocks = page.get_text("blocks")
                total_blocks += len(blocks)

                # Extract embedded URI links
                for link in page.get_links():
                    uri = link.get("uri")
                    if uri and uri not in links:
                        links.append(uri)

            full_text = "\n\n".join(page_texts)

            return ExtractionResult(
                engine_name=self.name,
                engine_version=self.get_version(),
                success=True,
                raw_text=full_text,
                page_texts=page_texts,
                metadata=raw_metadata,
                extra_info={
                    "page_count": len(doc),
                    "total_blocks": total_blocks,
                    "extracted_links": links,
                },
            )
        finally:
            doc.close()
