"""pdfminer.six extraction engine implementation."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pdfminer
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LAParams, LTTextContainer

from cv_verifier.extractors.base import BaseExtractor, ExtractionResult


class PDFMinerExtractor(BaseExtractor):
    """Layout-aware text extractor using pdfminer.six."""

    name: str = "pdfminer.six"

    def get_version(self) -> str:
        return getattr(pdfminer, "__version__", "unknown")

    def _extract_impl(self, pdf_path: Path) -> ExtractionResult:
        laparams = LAParams(
            line_margin=0.5,
            word_margin=0.1,
            char_margin=2.0,
            boxes_flow=0.5,
            detect_vertical=False,
        )

        page_texts: List[str] = []
        total_layout_elements = 0

        for page_layout in extract_pages(str(pdf_path), laparams=laparams):
            page_content = []
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    page_content.append(element.get_text())
                    total_layout_elements += 1
            page_texts.append("".join(page_content))

        full_text = "\n\n".join(page_texts)

        return ExtractionResult(
            engine_name=self.name,
            engine_version=self.get_version(),
            success=True,
            raw_text=full_text,
            page_texts=page_texts,
            extra_info={
                "page_count": len(page_texts),
                "total_layout_elements": total_layout_elements,
                "laparams": {
                    "line_margin": laparams.line_margin,
                    "word_margin": laparams.word_margin,
                },
            },
        )
