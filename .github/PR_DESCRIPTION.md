## Typst Migration, Multi-Engine ATS Verifier & AI Agent Workflows

## 1. Summary

This pull request completely modernizes the career document repository. It deprecates legacy LaTeX templates in favor of a high-performance **Typst** typesetting architecture, implements a comprehensive Python-based **multi-engine ATS (Applicant Tracking System) verification suite** (`cv_verifier`), and introduces a standardized set of **AI agent workflows and skills** (`.agents/`) for automated tailoring, job analysis, cover letter drafting, and closed-loop verification.

---

## 2. Key Features & Architectural Changes

### A. Typst Typesetting Engine
* **Compilation Speed**: Replaces multi-second LaTeX builds with sub-50ms Typst compilation and live preview capabilities.
* **Modular Content Architecture**:
  * Shared reusable layout templates in [`templates/cv.typ`](templates/cv.typ) and [`templates/cover-letter.typ`](templates/cover-letter.typ).
  * Fully localized canonical profiles for English ([`cv/en/content.typ`](cv/en/content.typ)) and French ([`cv/fr/content.typ`](cv/fr/content.typ)).
* **Vector Asset Integration**: Crisp, lightweight SVG contact icons (`envelope`, `github`, `home`, `linkedin`, `map-marker`, `phone`).
* **Strict 1-Page Layout Standard**: Single-column layout devoid of complex multi-column tables, nested sidebars, floating text frames, or canvas artifacts known to trigger parsing corruptions in ATS software.

### B. Multi-Engine ATS Verification Suite (`cv_verifier`)
A dedicated Python package designed to extract and audit rendered PDFs across 5 distinct PDF text extraction engines:
* **Extraction Backends**:
  1. `PyMuPDF` (`fitz` v1.28.x): High-speed native text and character positioning parser.
  2. `pdfplumber` (v0.11.x): Positional layout and bounding-box extractor.
  3. `pypdf` (v6.17.x): Pure-Python baseline text stream extractor.
  4. `pdfminer.six` (v2026.x): Low-level font and layout tree analyzer.
  5. `unstructured` (v0.27.x): Enterprise partitioner widely used in RAG and enterprise document pipelines.
* **Scoring & Heuristic Evaluation (0–100 Score)**:
  * **Contact & Identity Detection (100%)**: Verifies presence of candidate name, email, phone, location, LinkedIn, GitHub, and portfolio URLs without dropped fields.
  * **Section & Structural Validation (100%)**:
    * **CVs**: Validates detection of core sections (*Experience / Expérience*, *Education / Formation*, *Skills / Compétences*, *Projects / Projets*).
    * **Cover Letters**: Validates detection of formal letter components (*Recipient / Addressee*, *Subject Line*, *Salutation*, *Sign-off Closing*, *Candidate Name*).
  * **Cross-Engine Concordance (>90%)**: Computes word-level Jaccard similarity across all 5 engines to detect hidden rendering or stream encoding anomalies.
  * **Physical Layout Invariant**: Strictly enforces the 1-page A4 format limit for both CVs and Cover Letters.
* **Dual-Document Application Package Auditing**:
  * Running `make verify-app` / `cv-verify --app` automatically audits both `application/cv/cv.pdf` and `application/cover-letter/cover-letter.pdf` (if present), outputting a unified audit report to `verification/cv_app_verification.md` with Part I (CV) and Part II (Cover Letter).

### C. AI Agent Skills & Application Prompts (`.agents/`)
* **Standard Operating Procedures (Skills)**:
  * [`cv-workflow`](.agents/skills/cv-workflow/SKILL.md): Complete lifecycle SOP covering Git branching (`apply/<year>/<company>/<role>`), job metadata tracking (`application/job.md`), tailoring, cover letter generation, and 5-engine verification.
  * [`cv-rules`](.agents/skills/cv-rules/SKILL.md): Strict anti-hallucination invariants (never fabricate dates, metrics, companies, or technologies), typography constraints, and ATS parsing benchmarks.
* **Prompt Workflows**:
  * [`analyze-job.md`](.agents/prompts/analyze-job.md): Extracts core technical requirements, acronym pairs, and ATS keywords from job postings.
  * [`tailor-cv.md`](.agents/prompts/tailor-cv.md): Guides localized ATS keyword insertion and bullet point refocusing without inventing qualifications.
  * [`write-cover-letter.md`](.agents/prompts/write-cover-letter.md): Crafts targeted 4-paragraph 1-page professional cover letters.
  * [`resume-destroyer.md`](.agents/prompts/resume-destroyer.md): Ruthless critical review pass checking for fluff, vague claims, and formatting violations using the real extracted text dump.

### D. Tooling & Build Automation
* **Dependency Management**: Standardized using `uv` with reproducible locking in `uv.lock`.
* **Build Orchestration**: Comprehensive `Makefile` exposing developer workflows:
  * `make build`: Compiles both English and French canonical CVs (`cv/en/cv.pdf`, `cv/fr/cv.pdf`).
  * `make verify`: Compiles and audits both canonical CVs across all 5 engines.
  * `make verify-en` / `make verify-fr`: Audits English or French canonical CV.
  * `make verify-app`: Compiles and audits application package (CV and Cover Letter if present).
  * `make new-application COMPANY=<slug> ROLE=<slug> [LANG=en|fr]`: Creates isolated application branch and scaffolds `application/` directory.
  * `make test`: Runs automated pytest test suite.
  * `make sync`: Installs/syncs virtual environment dependencies.

---

## 3. Legacy Deprecation & Cleanup

The following legacy components have been systematically decommissioned:
* **LaTeX Build Trees**: Removed legacy LaTeX build trees (`cv_en.tex`, `cv_fr.tex`, and `main_cv.tex`).
* **Legacy Prompts**: Replaced unstructured prompt files in `prompt/` with the standardized `.agents/` architecture.

---

## 4. Verification & Test Suite Results

### Automated Tests (`pytest`)
All **21 test cases** pass across Python extraction backends, scoring algorithms, Cover Letter structural analysis, and reporting routines:
```text
tests/test_ats_analysis.py .........                                     [ 42%]
tests/test_extractors.py ............                                    [100%]
======================== 21 passed, 5 warnings in 8.32s ========================
```

### ATS Audit Scorecard

* **Canonical English CV (`cv/en/cv.pdf`)**: **100.0%** across PyMuPDF, pdfplumber, pypdf, pdfminer.six, Unstructured.
* **Canonical French CV (`cv/fr/cv.pdf`)**: **100.0%** across PyMuPDF, pdfplumber, pypdf, pdfminer.six, Unstructured.
* **Application Package (CV + Cover Letter)**: **100.0%** across all 5 engines with 0 missing contact fields, clean structural recognition, and >90% concordance.
