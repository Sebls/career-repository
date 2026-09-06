---
name: cv-workflow
description: End-to-end Standard Operating Procedure (SOP) for creating, tailoring, and managing job-specific applications, compiling Typst documents, and running the 5-engine ATS verification pipeline.
---

# Skill: Job Application Workflow & ATS Verification

This skill guides the end-to-end lifecycle for creating, tailoring, compiling, and verifying job applications in this repository.

---

## 1. Branch Architecture & Naming Convention

Every job application is isolated in its own permanent git branch created from `main`:

```text
apply/<year>/<company>/<role>
```

**Examples:**

- `apply/2026/mistral-ai/ai-engineering-intern`
- `apply/2026/openai/software-engineer`
- `apply/2026/airbus/data-scientist`

> [!NOTE]
> Application branches serve as historical records of what was submitted and are **not** merged back into `main`.

---

## 2. Step-by-Step Execution Workflow

### Step 1: Initialize Application Branch

Run the automated Makefile target from the workspace root:

```bash
make new-application COMPANY=mistral-ai ROLE=ai-engineering-intern LANG=en
```

This target will:

1. Ensure the workspace is clean and branch from `main`.
2. Create and switch to branch `apply/<year>/<company>/<role>`.
3. Create the `application/` directory structure:

   ```text
   application/
   ├── job.md
   ├── notes.md
   └── cv/
       ├── cv.typ
       └── (content.typ if customized)
   ```

4. Pre-populate `application/job.md` with YAML frontmatter and copy the selected language base (`cv/en/` or `cv/fr/`).

---

### Step 2: Document the Job Description

In `application/job.md`, fill in the YAML frontmatter and paste the full job description below:

```markdown
---
company: Mistral AI
role: AI Engineering Intern
year: 2026
location: Paris, France
language: en
status: preparing
url: https://...
date_found: 2026-09-05
date_applied:
---

## Job Description
[Paste full text here]
```

---

### Step 3: Analyze Requirements & ATS Targets

Use prompt `.agents/prompts/analyze-job.md` to extract:

- Hard technical requirements vs nice-to-have qualifications.
- Verbatim keyword tokens and acronym pairs (e.g., `LLM (Large Language Model)`) for ATS validation.
- Alignment points with the candidate's canonical experience.

---

### Step 4: Tailor the CV

1. Open `application/cv/cv.typ` (and customize content).
2. Follow prompt `.agents/prompts/tailor-cv.md`:
   - Match the target professional title.
   - Refocus the profile summary narrative hook.
   - Prioritize relevant experience bullets using the PAR format (Problem-Action-Result).
   - Reorder skill lines and categories to feature target tech stack first.
3. **Strict Invariant:** Never invent experience, metrics, companies, or dates.

---

### Step 5: (Optional) Generate Cover Letter

If the job application requires a cover letter:

1. Create `application/cover-letter/cover-letter.typ`.
2. Follow prompt `.agents/prompts/write-cover-letter.md`.
3. Use template `#import "../../templates/cover-letter.typ": *`.

---

### Step 6: Compile and Run Multi-Engine ATS Verification

Run the verification target:

```bash
make verify-app
```

This automated target will:

1. Compile `application/cv/cv.typ` to `application/cv/cv.pdf`.
2. Compile `application/cover-letter/cover-letter.typ` (if present) to `application/cover-letter/cover-letter.pdf`.
3. Execute the 5-engine ATS verification pipeline (`PyMuPDF`, `pdfplumber`, `pypdf`, `pdfminer.six`, `Unstructured`) across both documents.
4. Generate the comprehensive audit report in `verification/cv_app_verification.md` (containing Part I for the CV and Part II for the Cover Letter if present).

---

### Step 7: Analyze the Parsed Content & Audit Scorecard

Open and inspect `verification/cv_app_verification.md`:

1. **Overall ATS Score & Health:**
   - Confirm **100% Score** across all 5 engines for both CV and Cover Letter (if included).
2. **Contact & Identity Parsing Matrix:**
   - Ensure Candidate Name, Email, Phone, Location, LinkedIn, GitHub, and Website are extracted with zero missing fields in both documents.
3. **Section & Structural Recognition Matrix:**
   - For CV: Ensure *Experience*, *Education*, *Skills*, and *Projects* headings are detected cleanly.
   - For Cover Letter: Ensure *Recipient/Addressee*, *Subject Line*, *Salutation*, *Closing*, and *Sign-off Name* are detected cleanly.
4. **Cross-Engine Concordance:**
   - Check that word-overlap similarity exceeds **90%** across all engines for both documents.
5. **Parsed Content Analysis (LLM Text Dumps):**
   - Inspect the verbatim text extracted by PyMuPDF / pdfplumber.
   - Verify that target keywords from `application/job.md` appear in the parsed text without character corruption, missing hyphens, or broken ligatures.
6. **Physical Layout Check:**
   - Confirm `application/cv/cv.pdf` fits **strictly on 1 single page** (A4 format).
   - Confirm `application/cover-letter/cover-letter.pdf` (if created) fits **strictly on 1 single page** (A4 format).

---

### Step 8: (Optional) Teardown Audit with Resume Destroyer

For high-stakes roles:

1. Ingest parsed text from Section 5 of `verification/cv_app_verification.md` into prompt `.agents/prompts/resume-destroyer.md`.
2. Review the brutal teardown and implement high-signal recommendations.

---

### Step 9: Commit Application Snapshot

Once verified and inspected:

```bash
git add application/ verification/cv_app_verification.md
git commit -m "feat(application): prepare tailored CV, ATS verification report, and job metadata for $(COMPANY)"
```

---

### Step 10: Track Status & Interview Notes

Update `application/notes.md` throughout the hiring process:

- Recruiter contact info
- Screening notes & feedback
- Technical interview prep & question logs
- Status updates (`status: interview`, `status: offer`, etc.)
