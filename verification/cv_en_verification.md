# PDF ATS Extraction & Verification Report

**Target Document:** `cv/en/cv.pdf`  
**Document Type:** `Curriculum Vitae (CV)`  
**Language:** `English (en)`  
**Generated:** 2026-09-06 11:13:58  
**Engines Tested:** 5 (`PyMuPDF`, `pdfplumber`, `pypdf`, `pdfminer.six`, `Unstructured`)  

---

## 1. Executive Summary

### Overall Status: 🟢 **OPTIMAL ATS COMPLIANCE** (Average Score: **100.0%**)

| Engine       | Version   | Status   | Score   | Time (ms)   |   Words |   Chars | Contacts   | Structure   |
|--------------|-----------|----------|---------|-------------|---------|---------|------------|-------------|
| PyMuPDF      | 1.28.2    | ✅ PASS   | 100.0%  | 36.97 ms    |     313 |    2225 | 100.0%     | 100.0%      |
| pdfplumber   | 0.11.10   | ✅ PASS   | 100.0%  | 65.64 ms    |     313 |    2211 | 100.0%     | 100.0%      |
| pypdf        | 6.17.0    | ✅ PASS   | 100.0%  | 16.93 ms    |     314 |    2220 | 100.0%     | 100.0%      |
| pdfminer.six | 20260107  | ✅ PASS   | 100.0%  | 42.68 ms    |     313 |    2230 | 100.0%     | 100.0%      |
| Unstructured | 0.27.5    | ✅ PASS   | 100.0%  | 944.97 ms   |     310 |    2224 | 100.0%     | 100.0%      |

---

## 2. Contact & Identity Parsing Matrix

Verifies whether typical ATS parsers accurately extract candidate contact info without dropped fields.

| Engine       | Name   | Email   | Phone   | Location   | LinkedIn   | GitHub   | Website   |
|--------------|--------|---------|---------|------------|------------|----------|-----------|
| PyMuPDF      | ✅      | ✅       | ✅       | ✅          | ✅          | ✅        | ✅         |
| pdfplumber   | ✅      | ✅       | ✅       | ✅          | ✅          | ✅        | ✅         |
| pypdf        | ✅      | ✅       | ✅       | ✅          | ✅          | ✅        | ✅         |
| pdfminer.six | ✅      | ✅       | ✅       | ✅          | ✅          | ✅        | ✅         |
| Unstructured | ✅      | ✅       | ✅       | ✅          | ✅          | ✅        | ✅         |

---

## 3. Section Recognition Matrix

Verifies whether standard CV section headings are clearly recognized.

| Engine       | Experience   | Education   | Skills   | Projects   |
|--------------|--------------|-------------|----------|------------|
| PyMuPDF      | ✅            | ✅           | ✅        | ✅          |
| pdfplumber   | ✅            | ✅           | ✅        | ✅          |
| pypdf        | ✅            | ✅           | ✅        | ✅          |
| pdfminer.six | ✅            | ✅           | ✅        | ✅          |
| Unstructured | ✅            | ✅           | ✅        | ✅          |

---

## 4. Cross-Engine Concordance Matrix

Measures word-level Jaccard similarity across the 5 parsing libraries. High similarity (>90%) indicates robust and standard PDF text flow.

| Engine       | PyMuPDF   | pdfplumber   | pypdf   | pdfminer.six   | Unstructured   |
|--------------|-----------|--------------|---------|----------------|----------------|
| PyMuPDF      | 100.0%    | 100.0%       | 100.0%  | 100.0%         | 100.0%         |
| pdfplumber   | 100.0%    | 100.0%       | 100.0%  | 100.0%         | 100.0%         |
| pypdf        | 100.0%    | 100.0%       | 100.0%  | 100.0%         | 100.0%         |
| pdfminer.six | 100.0%    | 100.0%       | 100.0%  | 100.0%         | 100.0%         |
| Unstructured | 100.0%    | 100.0%       | 100.0%  | 100.0%         | 100.0%         |

---

## 5. Extracted Text per Engine (LLM Verification Dump)

Below are the exact raw extracted text bodies parsed by each library for detailed inspection by LLM agents.

### 📄 PyMuPDF (v1.28.2)
- **Extraction Time:** 36.97 ms | **Words:** 313 | **Characters:** 2225
- **PDF Metadata:** `{'format': 'PDF 1.7', 'title': 'Curriculum Vitae', 'author': 'Alex Doe', 'creator': 'Typst 0.15.1', 'creationDate': "D:20260906111351+02'00", 'modDate': "D:20260906111351+02'00"}`
- **Engine Details:** `{'page_count': 1, 'total_blocks': 15, 'extracted_links': ['mailto:alex.doe@example.com', 'tel:+1 (555) 019-2834', 'https://www.linkedin.com/in/alexdoe', 'https://github.com/alexdoe', 'https://alexdoe.dev', 'https://github.com/alexdoe/search-engine']}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Software & AI Engineer
 San Francisco, CA | 
 alex.doe@example.com | 
 +1 (555) 019-2834 | 
 alexdoe | 
 alexdoe | 
 alexdoe.dev
Profile
Software & AI Engineer with experience in production software engineering and deploying scalable AI services. Interested in machine learning platforms, 
backend architectures, and production-grade intelligent systems.
Education
State University, Master of Science in Computer Science
2024 – 2026
Tech Institute, Bachelor of Science in Software Engineering (GPA: 3.9/4.0)
2020 – 2024
Experience
Machine Learning Engineer - Tech Innovations Inc. (Jan 2025 – Present) – San Francisco, CA
• Designed and deployed production-ready inference endpoints, processing high-volume daily requests with sub-100ms latency.
• Architected agent workflows and tool ecosystems with persistent memory and structured model-interaction workflows.
• Built scalable data pipelines for large-scale datasets, reducing processing runtime by 50% through automated validations.
Software Engineer - Cloud Solutions Corp. (Mar 2023 – Dec 2024) – New York, NY
• Optimized backend service workflows and reduced API latency by 60% across containerized microservices.
• Automated testing and dataset validation pipelines via Python scripts, eliminating manual QA overhead.
• Developed and maintained backend services integrating external APIs and PostgreSQL databases applying clean architecture.
Projects
 OpenSearch Engine — Open Source Project (2024)
• Developed an open-source semantic search engine applying transformer-based embeddings and vector indexing.
• Implemented a clean full-stack architecture using Next.js (TypeScript) for frontend and FastAPI (Python) for backend.
Skills
Programming Languages: Python • TypeScript • C/C++ • Go
Frameworks & Libraries: FastAPI • React • Next.js • Pandas • NumPy • PyTorch • TensorFlow
Databases: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systems: Linux • Git • GitHub Actions • Testing • CI/CD • Docker
Cloud: AWS (EC2, S3) • GCP (Compute Engine, Cloud Storage)
Artificial Intelligence: LLM Systems • Vector Embeddings • RAG • Computer Vision • Model Evaluation & Reproducibility
Languages: English (Native) • Spanish (B2) • French (B1)
```

### 📄 pdfplumber (v0.11.10)
- **Extraction Time:** 65.64 ms | **Words:** 313 | **Characters:** 2211
- **PDF Metadata:** `{'Title': 'Curriculum Vitae', 'Author': 'Alex Doe', 'Creator': 'Typst 0.15.1', 'ModDate': "D:20260906111351+02'00", 'CreationDate': "D:20260906111351+02'00"}`
- **Engine Details:** `{'page_count': 1, 'total_tables': 0, 'visual_word_elements': 313}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Software & AI Engineer
San Francisco, CA | alex.doe@example.com | +1 (555) 019-2834 | alexdoe | alexdoe | alexdoe.dev
Profile
Software & AI Engineer with experience in production software engineering and deploying scalable AI services. Interested in machine learning platforms,
backend architectures, and production-grade intelligent systems.
Education
State University, Master of Science in Computer Science 2024 – 2026
Tech Institute, Bachelor of Science in Software Engineering (GPA: 3.9/4.0) 2020 – 2024
Experience
Machine Learning Engineer - Tech Innovations Inc. (Jan 2025 – Present) – San Francisco, CA
• Designed and deployed production-ready inference endpoints, processing high-volume daily requests with sub-100ms latency.
• Architected agent workflows and tool ecosystems with persistent memory and structured model-interaction workflows.
• Built scalable data pipelines for large-scale datasets, reducing processing runtime by 50% through automated validations.
Software Engineer - Cloud Solutions Corp. (Mar 2023 – Dec 2024) – New York, NY
• Optimized backend service workflows and reduced API latency by 60% across containerized microservices.
• Automated testing and dataset validation pipelines via Python scripts, eliminating manual QA overhead.
• Developed and maintained backend services integrating external APIs and PostgreSQL databases applying clean architecture.
Projects
OpenSearch Engine — Open Source Project (2024)
• Developed an open-source semantic search engine applying transformer-based embeddings and vector indexing.
• Implemented a clean full-stack architecture using Next.js (TypeScript) for frontend and FastAPI (Python) for backend.
Skills
Programming Languages: Python • TypeScript • C/C++ • Go
Frameworks & Libraries: FastAPI • React • Next.js • Pandas • NumPy • PyTorch • TensorFlow
Databases: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systems: Linux • Git • GitHub Actions • Testing • CI/CD • Docker
Cloud: AWS (EC2, S3) • GCP (Compute Engine, Cloud Storage)
Artificial Intelligence: LLM Systems • Vector Embeddings • RAG • Computer Vision • Model Evaluation & Reproducibility
Languages: English (Native) • Spanish (B2) • French (B1)
```

### 📄 pypdf (v6.17.0)
- **Extraction Time:** 16.93 ms | **Words:** 314 | **Characters:** 2220
- **PDF Metadata:** `{'/Title': 'Curriculum Vitae', '/Author': 'Alex Doe', '/Creator': 'Typst 0.15.1', '/ModDate': "D:20260906111351+02'00", '/CreationDate': "D:20260906111351+02'00"}`
- **Engine Details:** `{'page_count': 1, 'is_encrypted': False}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Software & AI Engineer
 San Francisco, CA |  alex.doe@example.com |  +1 (555) 019-2834 |  alexdoe |  alexdoe |  alexdoe.dev
Profile
Software & AI Engineer with experience in production software engineering and deploying scalable AI services. Interested in machine learning platforms, 
backend architectures, and production-grade intelligent systems.
Education
State University, Master of Science in Computer Science 2024 – 2026
Tech Institute, Bachelor of Science in Software Engineering (GPA: 3.9/4.0) 2020 – 2024
Experience
Machine Learning Engineer - Tech Innovations Inc. (Jan 2025 – Present) – San Francisco, CA
• Designed and deployed production-ready inference endpoints, processing high-volume daily requests with sub-100ms latency .
• Architected agent workflows and tool ecosystems with persistent memory and structured model-interaction workflows.
• Built scalable data pipelines for large-scale datasets, reducing processing runtime by 50% through automated validations.
Software Engineer - Cloud Solutions Corp. (Mar 2023 – Dec 2024) – New York, NY
• Optimized backend service workflows and reduced API latency by 60% across containerized microservices.
• Automated testing and dataset validation pipelines via Python scripts, eliminating manual QA overhead.
• Developed and maintained backend services integrating external APIs and PostgreSQL databases applying clean architecture.
Projects
 OpenSearch Engine — Open Source Project (2024)
• Developed an open-source semantic search engine applying transformer-based embeddings and vector indexing.
• Implemented a clean full-stack architecture using Next.js (TypeScript) for frontend and FastAPI (Python) for backend.
Skills
Programming Languages: Python • TypeScript • C/C++ • Go
Frameworks & Libraries: FastAPI • React • Next.js • Pandas • NumPy • PyTorch • TensorFlow
Databases: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systems: Linux • Git • GitHub Actions • Testing • CI/CD • Docker
Cloud: AWS (EC2, S3) • GCP (Compute Engine, Cloud Storage)
Artificial Intelligence: LLM Systems • Vector Embeddings • RAG • Computer Vision • Model Evaluation & Reproducibility
Languages: English (Native) • Spanish (B2) • French (B1)
```

### 📄 pdfminer.six (v20260107)
- **Extraction Time:** 42.68 ms | **Words:** 313 | **Characters:** 2230
- **Engine Details:** `{'page_count': 1, 'total_layout_elements': 22, 'laparams': {'line_margin': 0.5, 'word_margin': 0.1}}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Software & AI Engineer
 San Francisco, CA  | 
 alex.doe@example.com  | 
 +1 (555) 019-2834  | 
 alexdoe  | 
 alexdoe  | 
 alexdoe.dev
Profile
Software & AI Engineer with experience in production software engineering and deploying scalable AI services. Interested in machine learning platforms, 
backend architectures, and production-grade intelligent systems.
Education
State University, Master of Science in Computer Science
Tech Institute, Bachelor of Science in Software Engineering (GPA: 3.9/4.0)
2024 – 2026
2020 – 2024
Experience
Machine Learning Engineer - Tech Innovations Inc. (Jan 2025 – Present) – San Francisco, CA
• Designed and deployed production-ready inference endpoints, processing high-volume daily requests with sub-100ms latency.
• Architected agent workflows and tool ecosystems with persistent memory and structured model-interaction workflows.
• Built scalable data pipelines for large-scale datasets, reducing processing runtime by 50% through automated validations.
Software Engineer - Cloud Solutions Corp. (Mar 2023 – Dec 2024) – New York, NY
• Optimized backend service workflows and reduced API latency by 60% across containerized microservices.
• Automated testing and dataset validation pipelines via Python scripts, eliminating manual QA overhead.
• Developed and maintained backend services integrating external APIs and PostgreSQL databases applying clean architecture.
Projects
 OpenSearch Engine — Open Source Project (2024)
• Developed an open-source semantic search engine applying transformer-based embeddings and vector indexing.
• Implemented a clean full-stack architecture using Next.js (TypeScript) for frontend and FastAPI (Python) for backend.
Skills
Programming Languages: Python • TypeScript • C/C++ • Go
Frameworks & Libraries: FastAPI • React • Next.js • Pandas • NumPy • PyTorch • TensorFlow
Databases: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systems: Linux • Git • GitHub Actions • Testing • CI/CD • Docker
Cloud: AWS (EC2, S3) • GCP (Compute Engine, Cloud Storage)
Artificial Intelligence: LLM Systems • Vector Embeddings • RAG • Computer Vision • Model Evaluation & Reproducibility
Languages: English (Native) • Spanish (B2) • French (B1)
```

### 📄 Unstructured (v0.27.5)
- **Extraction Time:** 944.97 ms | **Words:** 310 | **Characters:** 2224
- **Engine Details:** `{'total_elements': 21, 'element_categories': {'Header': 2, 'Title': 8, 'EmailAddress': 1, 'UncategorizedText': 4, 'NarrativeText': 2, 'ListItem': 3, 'PageBreak': 1}, 'strategy': 'fast'}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe

Software & AI Engineer

San Francisco, CA |

alex.doe@example.com |

+1 (555) 019-2834 |

alexdoe |

alexdoe |

alexdoe.dev

Profile

Software & AI Engineer with experience in production software engineering and deploying scalable AI services. Interested in machine learning platforms, backend architectures, and production-grade intelligent systems.

Education

State University, Master of Science in Computer Science Tech Institute, Bachelor of Science in Software Engineering (GPA: 3.9/4.0)

2024 – 2026 2020 – 2024

Experience

Machine Learning Engineer - Tech Innovations Inc. (Jan 2025 – Present) – San Francisco, CA

Designed and deployed production-ready inference endpoints, processing high-volume daily requests with sub-100ms latency. • Architected agent workflows and tool ecosystems with persistent memory and structured model-interaction workflows. • Built scalable data pipelines for large-scale datasets, reducing processing runtime by 50% through automated validations. Software Engineer - Cloud Solutions Corp. (Mar 2023 – Dec 2024) – New York, NY

Optimized backend service workflows and reduced API latency by 60% across containerized microservices. • Automated testing and dataset validation pipelines via Python scripts, eliminating manual QA overhead. • Developed and maintained backend services integrating external APIs and PostgreSQL databases applying clean architecture. Projects

OpenSearch Engine — Open Source Project (2024)

Developed an open-source semantic search engine applying transformer-based embeddings and vector indexing. • Implemented a clean full-stack architecture using Next.js (TypeScript) for frontend and FastAPI (Python) for backend. Skills

Programming Languages: Python • TypeScript • C/C++ • Go Frameworks & Libraries: FastAPI • React • Next.js • Pandas • NumPy • PyTorch • TensorFlow Databases: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB) Infrastructure & Systems: Linux • Git • GitHub Actions • Testing • CI/CD • Docker Cloud: AWS (EC2, S3) • GCP (Compute Engine, Cloud Storage) Artificial Intelligence: LLM Systems • Vector Embeddings • RAG • Computer Vision • Model Evaluation & Reproducibility Languages: English (Native) • Spanish (B2) • French (B1)
```
