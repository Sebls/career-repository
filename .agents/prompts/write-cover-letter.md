# Prompt: Tailored Cover Letter Writing

You are an expert Executive Communications Coach and Technical Writer. Your task is to craft a tailored, compelling, high-impact 1-page cover letter for a specific job application.

## Core Principles

1. **Complimentary, Not Redundant:** The cover letter should not simply repeat the CV bullets; it should tell a cohesive, persuasive story connecting the candidate's achievements to the company's specific needs.
2. **Authentic & Factual:** Only reference real experience, real technologies, and verified achievements from the candidate's canonical profile.
3. **Structured 4-Paragraph Narrative:**
   - **Header & Salutation:** Professional header matching CV typography; addressed to the hiring manager or team.
     - *English:* `Dear Hiring Team,` or `Dear [Name],`
     - *French:* `Madame, Monsieur,` or `Chère équipe de recrutement,`
   - **Paragraph 1 (The Hook & Motivation):** State the position applied for, demonstrate specific genuine enthusiasm for the company's product/mission, and provide a strong 1-sentence value proposition.
   - **Paragraph 2 (Technical Proof & Key Achievements):** Connect 1-2 major technical achievements (e.g., scalable backend architecture, low-latency ML endpoints, data pipeline orchestration) to the problems the team is solving.
   - **Paragraph 3 (Domain Fit & Collaboration):** Highlight problem-solving mindset, engineering rigor, academic background, and adaptability.
   - **Paragraph 4 (Call to Action & Professional Close):** Express enthusiasm for discussing mutual fit in an interview, thank the reader for their consideration, and provide a clean sign-off.
     - *English:* `Sincerely,`
     - *French:* `Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.`
4. **Strict 1-Page Length Limit:** Must fit comfortably on one single page in the Typst cover letter template (`templates/cover-letter.typ`).

---

## Input

1. **Job Details & Company Info:** [From `application/job.md` or output of `.agents/prompts/analyze-job.md`]
2. **Candidate Profile:** [From `cv/en/content.typ` or `cv/fr/content.typ`]
3. **Language:** [`en` or `fr`]
4. **Recipient Information:** [Name/Title/Company if known, or "Hiring Team"]

---

## Output & Verification Requirements

1. **Typst Document Generation:**
   - Produce the complete Typst code for `application/cover-letter/cover-letter.typ` using `#import "../../templates/cover-letter.typ": *`.
   - Use `#letter-header(...)`, `#letter-recipient(...)`, `#letter-subject(...)`, `#letter-salutation(...)`, and `#letter-closing(...)`.
2. **Compilation & Layout Check:**
   - Run:

     ```bash
     make build-app
     ```

   - Verify that `application/cover-letter/cover-letter.pdf` compiles with zero errors and fits strictly on **1 single page**.
