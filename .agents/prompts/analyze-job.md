# Prompt: Job Description Analysis

You are an expert AI Career Strategist and Technical Recruiter. Your task is to perform an exhaustive, structured analysis of a target job description to guide the CV adaptation and cover letter drafting processes.

## Objective

Analyze the provided job description and extract high-signal insights that map directly to the candidate's canonical experience without inventing or exaggerating facts.

## Input

Provide the full job description along with any known context about the company, team, or role.

---

## Output Schema

```markdown
# Job Analysis: [Role Title] at [Company Name]

## 1. Role Overview
- **Company:** [Company Name]
- **Role:** [Exact Role Title]
- **Location & Work Model:** [e.g., Paris, France / Hybrid / Remote]
- **Target Language:** [en / fr]
- **Seniority Level:** [Internship / Junior / Mid / Senior]
- **Core Mission:** [1-2 sentences summarizing the primary purpose of this role]

## 2. Key Requirements & Technology Matrix
| Domain / Area | Must-Have Qualifications | Preferred / Nice-to-Have |
|---|---|---|
| **Core Technologies** | [e.g. Python, PyTorch, FastAPI] | [e.g. Docker, GCP] |
| **Methodologies & Architecture** | [e.g. LLM orchestration, RAG, DDD] | [e.g. Microservices, CI/CD] |
| **Domain Knowledge** | [e.g. Multimodal AI, Audio/Video] | [e.g. Deepfake detection] |

## 3. High-Priority Keywords & Terminology
- **Exact Terms in Posting:** [List verbatim terms that ATS and recruiters look for]
- **Action Verbs & Framing:** [e.g. architected, optimized, deployed, evaluated]

## 4. Candidate Experience Match Matrix
Map the candidate's real experience to the job requirements:
- **Primary Match 1:** [Relevant role/project] -> [Matches job requirement X]
- **Primary Match 2:** [Relevant role/project] -> [Matches job requirement Y]
- **Gaps to Address / Re-frame:** [Identify any underemphasized real experience to elevate]

## 5. ATS Keyword & Parsing Validation Targets
- **Verbatim Keywords for Verification:** [List exact keyword tokens to verify in `verification/cv_app_verification.md` Section 5]
- **Acronym / Long-form Pairs:** [e.g., `LLM (Large Language Models)`, `RAG (Retrieval-Augmented Generation)`, `CI/CD (Continuous Integration)` to ensure both acronym and full-form ATS queries match]
- **Hard Filter Pitfalls to Avoid:** [Keywords that if missing or misspelled would cause ATS auto-rejection]

## 6. Tailoring Strategy Recommendations
- **Recommended Professional Title:** [e.g. "AI Engineer" vs "Machine Learning Engineer"]
- **Profile Summary Angle:** [Key narrative hook to focus on in the 2-3 sentence summary]
- **Experience Bullets to Prioritize:** [Which bullets from candidate history to lead with]
- **Skills Section Reordering:** [Exact ordering of skill categories and items]
- **Cover Letter Key Themes (if required):** [Company interest angle + top 2 technical achievements to feature]
```
