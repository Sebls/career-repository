"""pypdf extraction engine implementation."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pypdf
from pypdf import PdfReader

from cv_verifier.extractors.base import BaseExtractor, ExtractionResult


class PyPDFExtractor(BaseExtractor):
    """Text extractor using modern pypdf."""

    name: str = "pypdf"

    def get_version(self) -> str:
        return getattr(pypdf, "__version__", "unknown")

    def _extract_impl(self, pdf_path: Path) -> ExtractionResult:
        reader = PdfReader(str(pdf_path))
        page_texts: List[str] = []
        raw_metadata: Dict[str, Any] = {}

        if reader.metadata:
            raw_metadata = {k: str(v) for k, v in reader.metadata.items()}

        for page in reader.pages:
            text = page.extract_text() or ""
            page_texts.append(text)

        full_text = "\n\n".join(page_texts)

        return ExtractionResult(
            engine_name=self.name,
            engine_version=self.get_version(),
            success=True,
            raw_text=full_text,
            page_texts=page_texts,
            metadata=raw_metadata,
            extra_info={
                "page_count": len(reader.pages),
                "is_encrypted": reader.is_encrypted,
            },
        )
