"""Base classes and data structures for PDF extraction engines."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
import time
from typing import Any, Dict, List, Optional


@dataclass
class ExtractionResult:
    """Standardized representation of text extraction output from any PDF engine."""

    engine_name: str
    engine_version: str
    success: bool
    raw_text: str = ""
    page_texts: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    extraction_time_ms: float = 0.0
    character_count: int = 0
    word_count: int = 0
    line_count: int = 0
    error_message: Optional[str] = None
    extra_info: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.raw_text:
            self.character_count = len(self.raw_text)
            self.word_count = len(self.raw_text.split())
            self.line_count = len(self.raw_text.splitlines())


class BaseExtractor(ABC):
    """Abstract Base Class for PDF text extraction engines."""

    name: str = "base"

    @abstractmethod
    def get_version(self) -> str:
        """Return the installed version of the underlying library."""
        raise NotImplementedError

    @abstractmethod
    def _extract_impl(self, pdf_path: Path) -> ExtractionResult:
        """Engine-specific extraction implementation."""
        raise NotImplementedError

    def extract(self, pdf_path: Path | str) -> ExtractionResult:
        """Execute extraction with automatic performance timing and error handling."""
        path = Path(pdf_path)
        if not path.is_file():
            return ExtractionResult(
                engine_name=self.name,
                engine_version=self.get_version(),
                success=False,
                error_message=f"File not found: {path}",
            )

        start_time = time.perf_counter()
        try:
            result = self._extract_impl(path)
            duration_ms = (time.perf_counter() - start_time) * 1000.0
            result.extraction_time_ms = round(duration_ms, 2)
            result.character_count = len(result.raw_text)
            result.word_count = len(result.raw_text.split())
            result.line_count = len(result.raw_text.splitlines())
            return result
        except Exception as exc:
            duration_ms = (time.perf_counter() - start_time) * 1000.0
            return ExtractionResult(
                engine_name=self.name,
                engine_version=self.get_version(),
                success=False,
                extraction_time_ms=round(duration_ms, 2),
                error_message=f"{type(exc).__name__}: {str(exc)}",
            )
