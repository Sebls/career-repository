---
name: cv-rules
description: Strict, non-negotiable rules for maintaining, generating, tailoring, and verifying CVs in this repository, including anti-hallucination laws and ATS parsing benchmarks.
---

# Skill: CV Rules, Core Constraints & ATS Verification Standards

This skill defines the strict, non-negotiable rules for generating, maintaining, and tailoring CVs in this repository.

---

## 1. Truth Preservation & Anti-Hallucination Laws

> [!CAUTION]
> The purpose of tailoring is to present real experience in the best possible light for a target role, **NEVER** to invent or fabricate qualifications.

### Absolute Invariants

- **Dates & Tenures:** Never alter employment dates, graduation dates, or project timelines.
- **Companies & Institutions:** Never fabricate or alter verified company names or academic institutions.
- **Academic Credentials & GPA:** Degrees, honors, and verified GPAs are immutable.
- **Unused Technologies:** Never add technologies, libraries, or frameworks that the candidate has never worked with.
- **Fabricated Metrics:** Never fabricate benchmark percentages, request throughputs, latency numbers, or dataset sizes.

### Permitted Tailoring Levers

- **Professional Title:** Can be adapted to match the target position (e.g. *AI Engineer*, *Machine Learning Engineer*, *Backend AI Software Engineer*).
- **Profile / Summary:** Can be rewritten to focus on the key themes and requirements of the role.
- **Bullet Point Re-ordering & Phrasing:** Experience bullets can be reordered to lead with the most relevant achievements, and phrasing can be tuned to incorporate target keywords truthfully.
- **Skill Priority & Hierarchy:** Technical skills can be reordered so that the primary languages and tools required by the employer appear first.
- **Project Selection:** Highlight projects directly demonstrating the relevant competencies.

---

## 2. Document Layout & Length Constraints

1. **Strict 1-Page Rule:**
   - The canonical CV and all tailored CVs must fit on **exactly ONE page** (A4 format).
   - Any overflow onto a second page is considered a failure.
2. **Typography & ATS Friendliness:**
   - Use clean, standard serif or sans-serif fonts supported in Typst (`Charter`, `Libertinus Serif`, `Helvetica`, `Inter`).
   - Maintain clear heading hierarchy (`#cv-section`).
   - Ensure all contact items are selectable plain text with functional hyperlink metadata.
   - Use standard bullet lists rather than custom graphics to ensure ATS parsers can read every line.

---

## 3. Automated Multi-Engine ATS Verification Standard

Every CV compiled in this repository (canonical or tailored) must pass the automated ATS extraction audit:

1. **Multi-Engine Audit Gate:**
   - Canonical CVs must pass `make verify` (generating `verification/cv_en_verification.md` and `verification/cv_fr_verification.md`).
   - Application CVs must pass `make verify-app` (generating `verification/cv_app_verification.md`).
2. **Quality & Compliance Thresholds:**
   - **Contact & Identity Extraction (100%):** Name, email, phone, location, LinkedIn, GitHub, and portfolio website must all parse accurately across all 5 engines (`PyMuPDF`, `pdfplumber`, `pypdf`, `pdfminer.six`, `Unstructured`).
   - **Section Detection (100%):** Core sections (*Experience / Expériences*, *Education / Formation*, *Skills / Compétences*, *Projects / Projets*, *Profile / Profil*) must be recognized cleanly.
   - **Cross-Engine Concordance (>90%):** High word-level Jaccard similarity across parsers ensures no multi-column flow corruptions or hidden text artifacts.
3. **Parsed Text Stream Inspection (Section 5 Analysis):**
   - The verbatim parsed text dump in Section 5 must be reviewed to verify:
     - No ligature collapse or missing spacing (e.g. `fi` / `fl` parsing cleanly).
     - Plain text bullet formatting parses cleanly without embedded control characters or symbol corruption.
     - Target keywords from the job description appear verbatim in the extracted text stream.

---

## 4. Multilingual Consistency

1. **Canonical Parity:**
   - The canonical profile must exist and be maintained in both English (`cv/en/`) and French (`cv/fr/`).
   - Both versions must represent the same factual experience while adapting naturally to French/English professional idioms.
2. **Language in Applications:**
   - Tailor only the required language for the target company:
     - French roles / France domestic market -> `cv/fr/`
     - International / US / European English roles -> `cv/en/`

---

## 5. Generalization to `main`

If an improvement discovered during tailoring (e.g. a cleaner metric description, better phrasing, or a newly completed project) is broadly valuable:

- Manually apply the improvement to `main` (`cv/en/content.typ` and `cv/fr/content.typ`).
- Recompile base CVs and run verification (`make build && make verify`).
- Do NOT merge application-specific branches into `main`.
