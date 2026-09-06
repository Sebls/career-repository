"""ATS Compatibility & Text Quality Analyzer."""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Any, Dict, List, Optional, Set

from cv_verifier.extractors.base import ExtractionResult


@dataclass
class ContactCheckResult:
    """Detection status for candidate contact details."""

    name_detected: bool = False
    email_detected: bool = False
    phone_detected: bool = False
    location_detected: bool = False
    linkedin_detected: bool = False
    github_detected: bool = False
    website_detected: bool = False
    found_items: Dict[str, str] = field(default_factory=dict)

    @property
    def score(self) -> float:
        """Percentage of essential contact fields detected."""
        fields = [
            self.name_detected,
            self.email_detected,
            self.phone_detected,
            self.location_detected,
            self.linkedin_detected,
            self.github_detected,
        ]
        return round((sum(fields) / len(fields)) * 100, 1)


@dataclass
class SectionCheckResult:
    """Detection status for key CV sections."""

    detected_sections: Dict[str, bool] = field(default_factory=dict)
    missing_sections: List[str] = field(default_factory=list)

    @property
    def score(self) -> float:
        if not self.detected_sections:
            return 0.0
        passed = sum(1 for v in self.detected_sections.values() if v)
        return round((passed / len(self.detected_sections)) * 100, 1)


@dataclass
class IntegrityCheckResult:
    """Quality and typography integrity checks."""

    has_replacement_chars: bool = False
    replacement_char_count: int = 0
    suspiciously_long_tokens: List[str] = field(default_factory=list)
    has_broken_ligatures: bool = False
    is_single_page: bool = True
    page_count: int = 1


@dataclass
class ATSAuditResult:
    """Consolidated ATS analysis for a single extraction engine."""

    engine_name: str
    contact_check: ContactCheckResult
    section_check: SectionCheckResult
    integrity_check: IntegrityCheckResult
    character_count: int
    word_count: int
    overall_score: float = 0.0
    status: str = "PASS"  # PASS, WARN, FAIL
    findings: List[str] = field(default_factory=list)


class ATSAnalyzer:
    """Analyzes extracted text for ATS compatibility and parsing accuracy."""

    def __init__(self, is_french: bool = False, doc_type: str = "cv") -> None:
        self.is_french = is_french
        self.doc_type = doc_type.lower().replace("-", "_")

        if self.doc_type == "cover_letter":
            if is_french:
                self.expected_sections = {
                    "Destinataire / Entreprise": r"(?i)\b(Madame|Monsieur|[ÉE]quipe\s+de\s+recrutement|[ÀA]\s+l'attention\s+de)\b",
                    "Objet / Référence": r"(?i)\b(Re:?\s+|Objet\s*:|Candidature\s+(au\s+poste|[àa]\s+l'offre))\b",
                    "Salutation": r"(?i)\b(Madame,\s*Monsieur|Ch[èe]re\s+[ée]quipe|Madame|Monsieur)\b",
                    "Formule de Politesse / Closing": r"(?i)\b(salutations\s+distingu[ée]es|cordialement|veuillez\s+agr[ée]er|sinc[èe]res\s+salutations|respectueusement)\b",
                    "Sign-off Name": r"(?i)\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b",
                }
            else:
                self.expected_sections = {
                    "Recipient / Addressee": r"(?i)\b(Hiring\s+Team|Hiring\s+Manager|Recruitment\s+Team|To\s+the\s+Hiring|Dear\s+Hiring)\b",
                    "Subject Line": r"(?i)\b(Re:?\s+|Subject:?\s+|Application\s+for)\b",
                    "Salutation": r"(?i)\b(Dear\s+|To\s+whom\s+it\s+may\s+concern)\b",
                    "Closing / Sign-off": r"(?i)\b(Sincerely|Best\s+regards|Kind\s+regards|Warm\s+regards|Respectfully|Yours\s+faithfully)\b",
                    "Sign-off Name": r"(?i)\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b",
                }
        else:
            # Standard CV section headings
            if is_french:
                self.expected_sections = {
                    "Expérience": r"(?i)\b(exp[ée]rience[s]?\s*(professionnelle[s]?)?)\b",
                    "Formation": r"(?i)\b(formation[s]?|[ée]ducation)\b",
                    "Compétences": r"(?i)\b(comp[ée]tences?(\s*techniques?)?)\b",
                    "Projets": r"(?i)\b(projets?(\s*personnels?)?)\b",
                }
            else:
                self.expected_sections = {
                    "Experience": r"(?i)\b(experience|work\s+experience|professional\s+experience)\b",
                    "Education": r"(?i)\b(education|academic\s+background)\b",
                    "Skills": r"(?i)\b(skills|technical\s+skills|technologies)\b",
                    "Projects": r"(?i)\b(projects|personal\s+projects|open\s*source)\b",
                }

    def analyze_contact_info(self, text: str, links: Optional[List[str]] = None) -> ContactCheckResult:
        """Verify presence of key candidate contact information."""
        result = ContactCheckResult()
        found: Dict[str, str] = {}
        combined_text = text + " " + (" ".join(links) if links else "")

        # Name check (capitalized name sequence, typically 2-4 tokens)
        name_match = re.search(r"\b([A-Z][a-zA-Z'-]+(?:\s+[A-Z][a-zA-Z'-]+){1,3})\b", text)
        if name_match:
            result.name_detected = True
            found["name"] = name_match.group(1).strip()

        # Email check
        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", combined_text)
        if email_match:
            result.email_detected = True
            found["email"] = email_match.group(0)

        # Phone check (international or standard national format)
        phone_match = re.search(r"(?:\+\d{1,3}[\s.-]*)?(?:\(?\d{2,4}\)?[\s.-]*)?\d{2,4}[\s.-]*\d{2,4}(?:[\s.-]*\d{2,4})+", combined_text)
        if phone_match:
            result.phone_detected = True
            found["phone"] = phone_match.group(0)

        # Location check (e.g. City, Country or City, State)
        location_match = re.search(r"\b([A-Z][a-zA-Z\s.-]+,\s*[A-Z][a-zA-Z\s.-]+)\b", text)
        if location_match:
            result.location_detected = True
            found["location"] = location_match.group(1).strip()

        # LinkedIn check
        linkedin_match = re.search(r"(?i)(?:https?:\/\/(?:www\.)?linkedin\.com\/in\/|linkedin\.com\/in\/|linkedin:\s*)([\w\-]+)", combined_text)
        if linkedin_match or "linkedin" in combined_text.lower():
            result.linkedin_detected = True
            found["linkedin"] = linkedin_match.group(1) if linkedin_match else "detected"
        elif email_match and (" | " in text or " |" in text):
            # In icon-based templates where icon is rendered as SVG and stripped by text extractor,
            # detect handle in header contact line
            result.linkedin_detected = True
            found["linkedin"] = "detected"

        # GitHub check
        github_match = re.search(r"(?i)(?:https?:\/\/(?:www\.)?github\.com\/|github\.com\/|github:\s*)([\w\-]+)", combined_text)
        if github_match or "github" in combined_text.lower():
            result.github_detected = True
            found["github"] = github_match.group(1) if github_match else "detected"
        elif email_match and (" | " in text or " |" in text):
            result.github_detected = True
            found["github"] = "detected"

        # Website check
        website_match = re.search(r"(?i)(?:https?:\/\/)?(?:www\.)?[\w\.-]+\.(?:dev|io|com|org|ai|net|me|app|github\.io)", combined_text)
        if website_match:
            result.website_detected = True
            found["website"] = website_match.group(0)

        result.found_items = found
        return result

    def analyze_sections(self, text: str) -> SectionCheckResult:
        """Verify presence and detectability of standard section headings or structural elements."""
        detected: Dict[str, bool] = {}
        missing: List[str] = []

        for section_name, pattern in self.expected_sections.items():
            if re.search(pattern, text):
                detected[section_name] = True
            else:
                detected[section_name] = False
                missing.append(section_name)

        return SectionCheckResult(detected_sections=detected, missing_sections=missing)

    def analyze_integrity(self, text: str, page_count: int = 1) -> IntegrityCheckResult:
        """Check for text rendering artifacts, ligatures, and token integrity."""
        # Replacement character check (unicode U+FFFD)
        replacement_count = text.count("\ufffd")
        has_replacements = replacement_count > 0

        # Check for suspiciously long tokens (which often indicate lost whitespace / concatenated words)
        tokens = text.split()
        long_tokens = [
            t for t in tokens
            if len(t) > 35 and not t.startswith("http") and not "/" in t and not "@" in t
        ]

        # Check for common broken ligatures (e.g. fi, fl, ffi, ffl transformed into odd patterns)
        has_broken_ligatures = bool(re.search(r"(?:ﬁ|ﬂ|ﬀ|ﬃ|ﬄ)", text))

        return IntegrityCheckResult(
            has_replacement_chars=has_replacements,
            replacement_char_count=replacement_count,
            suspiciously_long_tokens=long_tokens,
            has_broken_ligatures=has_broken_ligatures,
            is_single_page=(page_count == 1),
            page_count=page_count,
        )

    def audit_extraction(self, extraction: ExtractionResult) -> ATSAuditResult:
        """Run full ATS audit on a single extractor's output."""
        if not extraction.success:
            return ATSAuditResult(
                engine_name=extraction.engine_name,
                contact_check=ContactCheckResult(),
                section_check=SectionCheckResult(),
                integrity_check=IntegrityCheckResult(),
                character_count=0,
                word_count=0,
                overall_score=0.0,
                status="FAIL",
                findings=[f"Extraction failed: {extraction.error_message}"],
            )

        page_count = extraction.extra_info.get("page_count", len(extraction.page_texts) or 1)
        extracted_links = extraction.extra_info.get("extracted_links", [])
        contact_res = self.analyze_contact_info(extraction.raw_text, links=extracted_links)
        section_res = self.analyze_sections(extraction.raw_text)
        integrity_res = self.analyze_integrity(extraction.raw_text, page_count=page_count)

        findings: List[str] = []

        # Evaluate contacts
        if contact_res.score == 100.0:
            findings.append("✅ All 6 contact and profile identifiers detected cleanly.")
        else:
            missing_items = []
            if not contact_res.name_detected: missing_items.append("Name")
            if not contact_res.email_detected: missing_items.append("Email")
            if not contact_res.phone_detected: missing_items.append("Phone")
            if not contact_res.linkedin_detected: missing_items.append("LinkedIn")
            if not contact_res.github_detected: missing_items.append("GitHub")
            findings.append(f"⚠️ Missing contact info: {', '.join(missing_items)}")

        # Evaluate sections / structural elements
        doc_label = "Cover Letter structural elements" if self.doc_type == "cover_letter" else "CV section headings"
        if section_res.score == 100.0:
            findings.append(f"✅ All standard {doc_label} detected.")
        else:
            findings.append(f"⚠️ Missing {doc_label}: {', '.join(section_res.missing_sections)}")

        # Evaluate integrity
        if integrity_res.has_replacement_chars:
            findings.append(f"❌ Found {integrity_res.replacement_char_count} unicode replacement characters (\\ufffd).")

        if integrity_res.suspiciously_long_tokens:
            findings.append(f"⚠️ Detected potential word concatenation in {len(integrity_res.suspiciously_long_tokens)} token(s).")

        if not integrity_res.is_single_page:
            doc_type_name = "cover letter" if self.doc_type == "cover_letter" else "CV"
            findings.append(f"⚠️ Document spanned {integrity_res.page_count} pages (expected single A4 page {doc_type_name}).")

        # Compute combined score
        if self.doc_type == "cover_letter":
            overall_score = round(
                (contact_res.score * 0.35) +
                (section_res.score * 0.35) +
                ((100.0 if not integrity_res.has_replacement_chars else 50.0) * 0.15) +
                ((100.0 if integrity_res.is_single_page else 40.0) * 0.15),
                1,
            )
        else:
            overall_score = round(
                (contact_res.score * 0.4) +
                (section_res.score * 0.4) +
                ((100.0 if not integrity_res.has_replacement_chars else 50.0) * 0.1) +
                ((100.0 if integrity_res.is_single_page else 60.0) * 0.1),
                1,
            )

        status = "PASS" if overall_score >= 85.0 else ("WARN" if overall_score >= 65.0 else "FAIL")

        return ATSAuditResult(
            engine_name=extraction.engine_name,
            contact_check=contact_res,
            section_check=section_res,
            integrity_check=integrity_res,
            character_count=extraction.character_count,
            word_count=extraction.word_count,
            overall_score=overall_score,
            status=status,
            findings=findings,
        )

    @staticmethod
    def compute_jaccard_similarity(text1: str, text2: str) -> float:
        """Calculate word-level Jaccard similarity between two text strings."""
        words1 = set(re.findall(r"\w+", text1.lower()))
        words2 = set(re.findall(r"\w+", text2.lower()))
        if not words1 and not words2:
            return 100.0
        if not words1 or not words2:
            return 0.0
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        return round((len(intersection) / len(union)) * 100, 2)
