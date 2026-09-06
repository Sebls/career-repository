# ==============================================================================
# Career Repository Makefile
# Automates Typst CV compilation and job application branch workflows
# ==============================================================================

TYPST ?= $(shell command -v typst 2>/dev/null || echo /opt/homebrew/bin/typst)
YEAR ?= $(shell date +%Y)
DATE ?= $(shell date +%Y-%m-%d)
LANG ?= en

UV ?= $(shell command -v uv 2>/dev/null || echo $$HOME/.local/bin/uv)

.PHONY: all help build build-en build-fr build-app new-application clean check-typst check-uv sync test verify verify-en verify-fr verify-app

# Default target
all: build

help:
	@echo "Career Repository Management"
	@echo "============================"
	@echo "Usage:"
	@echo "  make build                     Build both English and French canonical CVs"
	@echo "  make build-en                  Build English CV (cv/en/cv.pdf)"
	@echo "  make build-fr                  Build French CV (cv/fr/cv.pdf)"
	@echo "  make build-app                 Build application CV (and cover letter if present)"
	@echo "  make sync                      Install / sync Python verification dependencies with uv"
	@echo "  make test                      Run pytest extraction and ATS analyzer unit tests"
	@echo "  make verify                    Compile & verify both canonical CVs (PyMuPDF, pdfplumber, pypdf, pdfminer, unstructured)"
	@echo "  make verify-en                 Compile & run ATS extraction verification on English CV"
	@echo "  make verify-fr                 Compile & run ATS extraction verification on French CV"
	@echo "  make verify-app                Compile & run ATS extraction verification on Application (CV and Cover Letter if present)"
	@echo "  make new-application          Create a new application branch and setup directory"
	@echo "         COMPANY=<name>         Company slug (e.g. mistral-ai)"
	@echo "         ROLE=<role>            Role slug (e.g. ai-engineering-intern)"
	@echo "         [LANG=en|fr]           Language choice (default: en)"
	@echo "  make check-typst               Verify Typst compiler is installed"
	@echo "  make clean                     Remove build preview artifacts"

check-typst:
	@if ! command -v $(TYPST) >/dev/null 2>&1; then \
		echo "Error: Typst compiler not found. Please install via 'brew install typst'."; \
		exit 1; \
	fi

build: check-typst build-en build-fr
	@echo "✅ All canonical CVs compiled successfully."

build-en: check-typst
	@echo "Compiling English CV..."
	@$(TYPST) compile --root . cv/en/cv.typ cv/en/cv.pdf
	@echo "✅ Generated cv/en/cv.pdf"

build-fr: check-typst
	@echo "Compiling French CV..."
	@$(TYPST) compile --root . cv/fr/cv.typ cv/fr/cv.pdf
	@echo "✅ Generated cv/fr/cv.pdf"

build-app: check-typst
	@if [ ! -f application/cv/cv.typ ]; then \
		echo "Error: application/cv/cv.typ not found. Are you on an application branch?"; \
		exit 1; \
	fi
	@echo "Compiling application CV..."
	@$(TYPST) compile --root . application/cv/cv.typ application/cv/cv.pdf
	@echo "✅ Generated application/cv/cv.pdf"
	@if [ -f application/cover-letter/cover-letter.typ ]; then \
		echo "Compiling application Cover Letter..."; \
		$(TYPST) compile --root . application/cover-letter/cover-letter.typ application/cover-letter/cover-letter.pdf; \
		echo "✅ Generated application/cover-letter/cover-letter.pdf"; \
	fi

new-application:
	@if [ -z "$(COMPANY)" ] || [ -z "$(ROLE)" ]; then \
		echo "Error: Missing required arguments."; \
		echo "Usage: make new-application COMPANY=<company-slug> ROLE=<role-slug> [LANG=en|fr]"; \
		echo "Example: make new-application COMPANY=mistral-ai ROLE=ai-engineering-intern LANG=en"; \
		exit 1; \
	fi
	@BRANCH="apply/$(YEAR)/$(COMPANY)/$(ROLE)"; \
	echo "Creating application branch: $$BRANCH from main..."; \
	git checkout main || git checkout -b main; \
	git checkout -b "$$BRANCH"; \
	mkdir -p application/cv; \
	if [ ! -f application/job.md ]; then \
		printf -- "---\ncompany: $(COMPANY)\nrole: $(ROLE)\nyear: $(YEAR)\nlocation: Paris, France\nlanguage: $(LANG)\nstatus: preparing\nurl: \"\"\ndate_found: $(DATE)\ndate_applied: \"\"\n---\n\n## Job Description\n\n<!-- Paste the full job description here -->\n" > application/job.md; \
		echo "Created application/job.md"; \
	fi; \
	if [ ! -f application/notes.md ]; then \
		printf -- "# Application Notes: $(ROLE) at $(COMPANY)\n\n## Key Contacts & Timeline\n- **Date Found:** $(DATE)\n- **Date Applied:** \n- **Contact Person:** \n\n## Strategic Alignment & Talking Points\n- Primary hook:\n- Key project to emphasize:\n\n## Interview Log\n- [ ] Recruiter Screening:\n- [ ] Technical Interview:\n- [ ] Final Interview:\n" > application/notes.md; \
		echo "Created application/notes.md"; \
	fi; \
	if [ "$(LANG)" = "fr" ]; then \
		cp cv/fr/content.typ application/cv/content.typ; \
		cp cv/fr/cv.typ application/cv/cv.typ; \
	else \
		cp cv/en/content.typ application/cv/content.typ; \
		cp cv/en/cv.typ application/cv/cv.typ; \
	fi; \
	echo "Initialized application/cv/ from cv/$(LANG)/"; \
	$(TYPST) compile --root . application/cv/cv.typ application/cv/cv.pdf; \
	echo ""; \
	echo "✨ Application branch '$$BRANCH' is ready!"; \
	echo "Next steps:"; \
	echo "  1. Paste the job posting into application/job.md"; \
	echo "  2. Use .agents/prompts/analyze-job.md to analyze requirements"; \
	echo "  3. Tailor application/cv/cv.typ (and content.typ)"; \
	echo "  4. (Optional) Create application/cover-letter/cover-letter.typ"; \
	echo "  5. Run 'make verify-app' to compile PDFs & audit ATS parsing"; \
	echo "  6. Commit changes to $$BRANCH"


check-uv:
	@if ! command -v $(UV) >/dev/null 2>&1; then \
		echo "Error: uv package manager not found. Please install via 'curl -LsSf https://astral.sh/uv/install.sh | sh' or 'brew install uv'."; \
		exit 1; \
	fi

sync: check-uv
	@echo "Syncing Python dependencies with uv..."
	@$(UV) sync
	@echo "✅ Python dependencies synced."

test: check-uv
	@echo "Running verification test suite..."
	@$(UV) run pytest -v
	@echo "✅ All tests passed."

verify: check-uv build verify-en verify-fr
	@echo "✅ All canonical CV ATS verifications completed."

verify-en: check-uv build-en
	@echo "Running multi-engine ATS verification on English CV..."
	@$(UV) run cv-verify cv/en/cv.pdf --output verification/cv_en_verification.md

verify-fr: check-uv build-fr
	@echo "Running multi-engine ATS verification on French CV..."
	@$(UV) run cv-verify cv/fr/cv.pdf --output verification/cv_fr_verification.md

verify-app: check-uv build-app
	@echo "Running multi-engine ATS verification on Application package..."
	@$(UV) run cv-verify --app --output verification/cv_app_verification.md

clean:
	@rm -f *.png cv_page-*.png cv_*preview*.png
	@echo "Cleaned preview images."

