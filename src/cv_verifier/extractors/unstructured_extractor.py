"""Unstructured extraction engine implementation."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

import unstructured
from unstructured.partition.pdf import partition_pdf

from importlib.metadata import version

from cv_verifier.extractors.base import BaseExtractor, ExtractionResult


class UnstructuredExtractor(BaseExtractor):
    """Document element parser and text extractor using Unstructured."""

    name: str = "Unstructured"

    def get_version(self) -> str:
        try:
            return version("unstructured")
        except Exception:
            return getattr(unstructured, "__version__", "unknown")

    def _extract_impl(self, pdf_path: Path) -> ExtractionResult:
        # Use fast text-based strategy for native digital vector PDFs compiled by Typst
        elements = partition_pdf(
            filename=str(pdf_path),
            strategy="fast",
            include_page_breaks=True,
        )

        element_texts: List[str] = []
        categories: Counter[str] = Counter()
        page_texts: List[str] = []
        current_page: List[str] = []

        for el in elements:
            category = getattr(el, "category", type(el).__name__)
            categories[category] += 1
            text = str(el).strip()

            if category == "PageBreak":
                if current_page:
                    page_texts.append("\n".join(current_page))
                    current_page = []
            elif text:
                element_texts.append(text)
                current_page.append(text)

        if current_page or not page_texts:
            page_texts.append("\n".join(current_page))

        full_text = "\n\n".join(element_texts)

        return ExtractionResult(
            engine_name=self.name,
            engine_version=self.get_version(),
            success=True,
            raw_text=full_text,
            page_texts=page_texts,
            extra_info={
                "total_elements": len(elements),
                "element_categories": dict(categories),
                "strategy": "fast",
            },
        )
