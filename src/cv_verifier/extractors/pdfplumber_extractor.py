"""pdfplumber extraction engine implementation."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pdfplumber

from cv_verifier.extractors.base import BaseExtractor, ExtractionResult


class PDFPlumberExtractor(BaseExtractor):
    """Text and visual layout extractor using pdfplumber."""

    name: str = "pdfplumber"

    def get_version(self) -> str:
        return getattr(pdfplumber, "__version__", "unknown")

    def _extract_impl(self, pdf_path: Path) -> ExtractionResult:
        page_texts: List[str] = []
        raw_metadata: Dict[str, Any] = {}
        total_tables = 0
        total_words = 0

        with pdfplumber.open(pdf_path) as pdf:
            raw_metadata = dict(pdf.metadata) if pdf.metadata else {}
            
            for page in pdf.pages:
                text = page.extract_text(layout=False) or ""
                page_texts.append(text)

                tables = page.extract_tables()
                total_tables += len(tables)

                words = page.extract_words()
                total_words += len(words)

            full_text = "\n\n".join(page_texts)

            return ExtractionResult(
                engine_name=self.name,
                engine_version=self.get_version(),
                success=True,
                raw_text=full_text,
                page_texts=page_texts,
                metadata=raw_metadata,
                extra_info={
                    "page_count": len(pdf.pages),
                    "total_tables": total_tables,
                    "visual_word_elements": total_words,
                },
            )
