"""CV Verifier: Multi-Engine PDF Text Extraction and ATS Verification Suite."""

from cv_verifier.ats_analyzer import ATSAnalyzer, ATSAuditResult, ContactCheckResult, SectionCheckResult
from cv_verifier.extractors import ALL_EXTRACTORS, BaseExtractor, ExtractionResult, get_all_extractors, get_extractor
from cv_verifier.reporter import VerificationReporter

__version__ = "0.1.0"

__all__ = [
    "ALL_EXTRACTORS",
    "BaseExtractor",
    "ExtractionResult",
    "ATSAnalyzer",
    "ATSAuditResult",
    "ContactCheckResult",
    "SectionCheckResult",
    "VerificationReporter",
    "get_all_extractors",
    "get_extractor",
]
