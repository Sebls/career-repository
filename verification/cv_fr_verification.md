# PDF ATS Extraction & Verification Report

**Target Document:** `cv/fr/cv.pdf`  
**Document Type:** `Curriculum Vitae (CV)`  
**Language:** `French (fr)`  
**Generated:** 2026-09-06 11:14:04  
**Engines Tested:** 5 (`PyMuPDF`, `pdfplumber`, `pypdf`, `pdfminer.six`, `Unstructured`)  

---

## 1. Executive Summary

### Overall Status: 🟢 **OPTIMAL ATS COMPLIANCE** (Average Score: **100.0%**)

| Engine       | Version   | Status   | Score   | Time (ms)   |   Words |   Chars | Contacts   | Structure   |
|--------------|-----------|----------|---------|-------------|---------|---------|------------|-------------|
| PyMuPDF      | 1.28.2    | ✅ PASS   | 100.0%  | 15.41 ms    |     342 |    2394 | 100.0%     | 100.0%      |
| pdfplumber   | 0.11.10   | ✅ PASS   | 100.0%  | 66.17 ms    |     342 |    2379 | 100.0%     | 100.0%      |
| pypdf        | 6.17.0    | ✅ PASS   | 100.0%  | 15.67 ms    |     343 |    2389 | 100.0%     | 100.0%      |
| pdfminer.six | 20260107  | ✅ PASS   | 100.0%  | 42.37 ms    |     342 |    2418 | 100.0%     | 100.0%      |
| Unstructured | 0.27.5    | ✅ PASS   | 100.0%  | 776.66 ms   |     338 |    2392 | 100.0%     | 100.0%      |

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

| Engine       | Expérience   | Formation   | Compétences   | Projets   |
|--------------|--------------|-------------|---------------|-----------|
| PyMuPDF      | ✅            | ✅           | ✅             | ✅         |
| pdfplumber   | ✅            | ✅           | ✅             | ✅         |
| pypdf        | ✅            | ✅           | ✅             | ✅         |
| pdfminer.six | ✅            | ✅           | ✅             | ✅         |
| Unstructured | ✅            | ✅           | ✅             | ✅         |

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
- **Extraction Time:** 15.41 ms | **Words:** 342 | **Characters:** 2394
- **PDF Metadata:** `{'format': 'PDF 1.7', 'title': 'Curriculum Vitae', 'author': 'Alex Doe', 'creator': 'Typst 0.15.1', 'creationDate': "D:20260906111352+02'00", 'modDate': "D:20260906111352+02'00"}`
- **Engine Details:** `{'page_count': 1, 'total_blocks': 15, 'extracted_links': ['mailto:alex.doe@example.com', 'tel:+33 6 12 34 56 78', 'https://www.linkedin.com/in/alexdoe', 'https://github.com/alexdoe', 'https://alexdoe.dev', 'https://github.com/alexdoe/search-engine']}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Ingénieur IA & Logiciel
 Paris, France | 
 alex.doe@example.com | 
 +33 6 12 34 56 78 | 
 alexdoe | 
 alexdoe | 
 alexdoe.dev
Profil
Ingénieur IA & Logiciel avec une solide expérience en développement logiciel et en déploiement de services d’intelligence artificielle en production. 
Passionné par les architectures backend évolutives, les modèles de langage et les systèmes intelligents prêts pour la production.
Formation
Grande École d’Ingénieurs, Diplôme d’Ingénieur (équivalent M.Sc.)
2024 – 2026
Université de Technologie, Licence en Informatique (B.Sc.)
2020 – 2024
Expérience
Tech Innovations France - Ingénieur Machine Learning (janv. 2025 – présent) – Paris, France
• Conçu et déployé des endpoints d’inférence multimodale pour la production, traitant d’importants volumes de requêtes quotidiennes avec une 
faible latence.
• Étendu des architectures de deep learning et automatisé les pipelines de validation et d’évaluation des modèles.
• Construit des pipelines de données scalables, réduisant le temps de traitement de 50 % grâce à des workflows automatisés et reproductibles.
Solutions Numériques - Ingénieur logiciel (mars 2023 – déc. 2024) – Lyon, France
• Optimisé les pipelines de traitement de données et l’utilisation des ressources dans des environnements conteneurisés.
• Développé des scripts Python et des outils internes pour automatiser les tests et le contrôle qualité des données.
• Conçu et maintenu des services backend avec PostgreSQL et FastAPI en appliquant les principes d’architecture propre.
Projets
 Moteur de recherche sémantique — Projet open source (2024)
• Développement d’un moteur de recherche sémantique basé sur des modèles transformers et l’indexation vectorielle.
• Implémentation d’une architecture full-stack propre utilisant Next.js et FastAPI avec tests automatisés et documentation complète.
Compétences
Compétences transversales: Adaptabilité • Communication • Travail en équipe • Résolution de problèmes
Langages de programmation: Python (Pandas, NumPy, PyTorch, FastAPI) • TypeScript • C/C++
Bases de données: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systèmes: Linux • Git • GitHub Actions • Tests logiciels • CI/CD • Docker
Intelligence artificielle: LLM • RAG • Embeddings vectoriels • Vision par ordinateur • Évaluation de modèles
Langues: Français (langue maternelle) • Anglais (C1) • Espagnol (B2)
```

### 📄 pdfplumber (v0.11.10)
- **Extraction Time:** 66.17 ms | **Words:** 342 | **Characters:** 2379
- **PDF Metadata:** `{'Title': 'Curriculum Vitae', 'Author': 'Alex Doe', 'Creator': 'Typst 0.15.1', 'ModDate': "D:20260906111352+02'00", 'CreationDate': "D:20260906111352+02'00"}`
- **Engine Details:** `{'page_count': 1, 'total_tables': 0, 'visual_word_elements': 342}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Ingénieur IA & Logiciel
Paris, France | alex.doe@example.com | +33 6 12 34 56 78 | alexdoe | alexdoe | alexdoe.dev
Profil
Ingénieur IA & Logiciel avec une solide expérience en développement logiciel et en déploiement de services d’intelligence artificielle en production.
Passionné par les architectures backend évolutives, les modèles de langage et les systèmes intelligents prêts pour la production.
Formation
Grande École d’Ingénieurs, Diplôme d’Ingénieur (équivalent M.Sc.) 2024 – 2026
Université de Technologie, Licence en Informatique (B.Sc.) 2020 – 2024
Expérience
Tech Innovations France - Ingénieur Machine Learning (janv. 2025 – présent) – Paris, France
• Conçu et déployé des endpoints d’inférence multimodale pour la production, traitant d’importants volumes de requêtes quotidiennes avec une
faible latence.
• Étendu des architectures de deep learning et automatisé les pipelines de validation et d’évaluation des modèles.
• Construit des pipelines de données scalables, réduisant le temps de traitement de 50 % grâce à des workflows automatisés et reproductibles.
Solutions Numériques - Ingénieur logiciel (mars 2023 – déc. 2024) – Lyon, France
• Optimisé les pipelines de traitement de données et l’utilisation des ressources dans des environnements conteneurisés.
• Développé des scripts Python et des outils internes pour automatiser les tests et le contrôle qualité des données.
• Conçu et maintenu des services backend avec PostgreSQL et FastAPI en appliquant les principes d’architecture propre.
Projets
Moteur de recherche sémantique — Projet open source (2024)
• Développement d’un moteur de recherche sémantique basé sur des modèles transformers et l’indexation vectorielle.
• Implémentation d’une architecture full-stack propre utilisant Next.js et FastAPI avec tests automatisés et documentation complète.
Compétences
Compétences transversales: Adaptabilité • Communication • Travail en équipe • Résolution de problèmes
Langages de programmation: Python (Pandas, NumPy, PyTorch, FastAPI) • TypeScript • C/C++
Bases de données: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systèmes: Linux • Git • GitHub Actions • Tests logiciels • CI/CD • Docker
Intelligence artificielle: LLM • RAG • Embeddings vectoriels • Vision par ordinateur • Évaluation de modèles
Langues: Français (langue maternelle) • Anglais (C1) • Espagnol (B2)
```

### 📄 pypdf (v6.17.0)
- **Extraction Time:** 15.67 ms | **Words:** 343 | **Characters:** 2389
- **PDF Metadata:** `{'/Title': 'Curriculum Vitae', '/Author': 'Alex Doe', '/Creator': 'Typst 0.15.1', '/ModDate': "D:20260906111352+02'00", '/CreationDate': "D:20260906111352+02'00"}`
- **Engine Details:** `{'page_count': 1, 'is_encrypted': False}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Ingénieur IA & Logiciel
 Paris, France |  alex.doe@example.com |  +33 6 12 34 56 78 |  alexdoe |  alexdoe |  alexdoe.dev
Profil
Ingénieur IA & Logiciel avec une solide expérience en développement logiciel et en déploiement de services d’intelligence artificielle en production. 
Passionné par les architectures backend évolutives, les modèles de langage et les systèmes intelligents prêts pour la production.
Formation
Grande École d’Ingénieurs, Diplôme d’Ingénieur (équivalent M.Sc.) 2024 – 2026
Université de Technologie, Licence en Informatique (B.Sc.) 2020 – 2024
Expérience
Tech Innovations France - Ingénieur Machine Learning (janv. 2025 – présent) – Paris, France
• Conçu et déployé des endpoints d’inférence multimodale pour la production, traitant d’importants volumes de requêtes quotidiennes avec une 
faible latence.
• Étendu des architectures de deep learning et automatisé les pipelines de validation et d’évaluation des modèles.
• Construit des pipelines de données scalables, réduisant le temps de traitement de 50 % grâce à des workflows automatisés et reproductibles.
Solutions Numériques - Ingénieur logiciel (mars 2023 – déc. 2024) – Lyon, France
• Optimisé les pipelines de traitement de données et l’utilisation des ressources dans des environnements conteneurisés.
• Développé des scripts Python et des outils internes pour automatiser les tests et le contrôle qualité des données.
• Conçu et maintenu des services backend avec PostgreSQL et FastAPI en appliquant les principes d’architecture propre.
Projets
 Moteur de recherche sémantique — Projet open source (2024)
• Développement d’un moteur de recherche sémantique basé sur des modèles transformers et l’indexation vectorielle.
• Implémentation d’une architecture full-stack propre utilisant Next.js et FastAPI avec tests automatisés et documentation complète.
Compétences
Compétences transversales: Adaptabilité • Communication • Travail en équipe • Résolution de problèmes
Langages de programmation: Python (Pandas, NumPy , PyTorch, FastAPI) • TypeScript • C/C++
Bases de données: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systèmes: Linux • Git • GitHub Actions • Tests logiciels • CI/CD • Docker
Intelligence artificielle: LLM • RAG • Embeddings vectoriels • Vision par ordinateur • Évaluation de modèles
Langues: Français (langue maternelle) • Anglais (C1) • Espagnol (B2)
```

### 📄 pdfminer.six (v20260107)
- **Extraction Time:** 42.37 ms | **Words:** 342 | **Characters:** 2418
- **Engine Details:** `{'page_count': 1, 'total_layout_elements': 24, 'laparams': {'line_margin': 0.5, 'word_margin': 0.1}}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe
Ingénieur IA & Logiciel
 Paris, France  | 
 alex.doe@example.com  | 
 +33 6 12 34 56 78  | 
 alexdoe  | 
 alexdoe  | 
 alexdoe.dev
Profil
Ingénieur  IA  &  Logiciel  avec  une  solide  expérience  en  développement  logiciel  et  en  déploiement  de  services  d’intelligence  artificielle  en  production. 
Passionné par les architectures backend évolutives, les modèles de langage et les systèmes intelligents prêts pour la production.
Formation
Grande École d’Ingénieurs, Diplôme d’Ingénieur (équivalent M.Sc.)
Université de Technologie, Licence en Informatique (B.Sc.)
Expérience
2024 – 2026
2020 – 2024
Tech Innovations France - Ingénieur Machine Learning (janv. 2025 – présent) – Paris, France
• Conçu et déployé des endpoints d’inférence multimodale pour la production, traitant d’importants volumes de requêtes quotidiennes avec une 
faible latence.
• Étendu des architectures de deep learning et automatisé les pipelines de validation et d’évaluation des modèles.
• Construit des pipelines de données scalables, réduisant le temps de traitement de 50 % grâce à des workflows automatisés et reproductibles.
Solutions Numériques - Ingénieur logiciel (mars 2023 – déc. 2024) – Lyon, France
• Optimisé les pipelines de traitement de données et l’utilisation des ressources dans des environnements conteneurisés.
• Développé des scripts Python et des outils internes pour automatiser les tests et le contrôle qualité des données.
• Conçu et maintenu des services backend avec PostgreSQL et FastAPI en appliquant les principes d’architecture propre.
Projets
 Moteur de recherche sémantique — Projet open source (2024)
• Développement d’un moteur de recherche sémantique basé sur des modèles transformers et l’indexation vectorielle.
• Implémentation d’une architecture full-stack propre utilisant Next.js et FastAPI avec tests automatisés et documentation complète.
Compétences
Compétences transversales: Adaptabilité • Communication • Travail en équipe • Résolution de problèmes
Langages de programmation: Python (Pandas, NumPy, PyTorch, FastAPI) • TypeScript • C/C++
Bases de données: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)
Infrastructure & Systèmes: Linux • Git • GitHub Actions • Tests logiciels • CI/CD • Docker
Intelligence artificielle: LLM • RAG • Embeddings vectoriels • Vision par ordinateur • Évaluation de modèles
Langues: Français (langue maternelle) • Anglais (C1) • Espagnol (B2)
```

### 📄 Unstructured (v0.27.5)
- **Extraction Time:** 776.66 ms | **Words:** 338 | **Characters:** 2392
- **Engine Details:** `{'total_elements': 23, 'element_categories': {'Header': 2, 'Title': 9, 'EmailAddress': 1, 'UncategorizedText': 3, 'NarrativeText': 3, 'ListItem': 4, 'PageBreak': 1}, 'strategy': 'fast'}`
- **Audit Findings:**
  - ✅ All 6 contact and profile identifiers detected cleanly.
  - ✅ All standard CV section headings detected.

```text
Alex Doe

Ingénieur IA & Logiciel

Paris, France |

alex.doe@example.com |

+33 6 12 34 56 78 |

alexdoe |

alexdoe |

alexdoe.dev

Profil

Ingénieur IA & Logiciel avec une solide expérience en développement logiciel et en déploiement de services d’intelligence artificielle en production. Passionné par les architectures backend évolutives, les modèles de langage et les systèmes intelligents prêts pour la production.

Formation

Grande École d’Ingénieurs, Diplôme d’Ingénieur (équivalent M.Sc.) Université de Technologie, Licence en Informatique (B.Sc.)

Expérience

Tech Innovations France - Ingénieur Machine Learning (janv. 2025 – présent) – Paris, France

Conçu et déployé des endpoints d’inférence multimodale pour la production, traitant d’importants volumes de requêtes quotidiennes avec une

faible latence.

Étendu des architectures de deep learning et automatisé les pipelines de validation et d’évaluation des modèles. • Construit des pipelines de données scalables, réduisant le temps de traitement de 50 % grâce à des workflows automatisés et reproductibles. Solutions Numériques - Ingénieur logiciel (mars 2023 – déc. 2024) – Lyon, France

Optimisé les pipelines de traitement de données et l’utilisation des ressources dans des environnements conteneurisés. • Développé des scripts Python et des outils internes pour automatiser les tests et le contrôle qualité des données. • Conçu et maintenu des services backend avec PostgreSQL et FastAPI en appliquant les principes d’architecture propre. Projets

Moteur de recherche sémantique — Projet open source (2024)

Développement d’un moteur de recherche sémantique basé sur des modèles transformers et l’indexation vectorielle. • Implémentation d’une architecture full-stack propre utilisant Next.js et FastAPI avec tests automatisés et documentation complète. Compétences

Compétences transversales: Adaptabilité • Communication • Travail en équipe • Résolution de problèmes Langages de programmation: Python (Pandas, NumPy, PyTorch, FastAPI) • TypeScript • C/C++ Bases de données: SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB) Infrastructure & Systèmes: Linux • Git • GitHub Actions • Tests logiciels • CI/CD • Docker Intelligence artificielle: LLM • RAG • Embeddings vectoriels • Vision par ordinateur • Évaluation de modèles Langues: Français (langue maternelle) • Anglais (C1) • Espagnol (B2)

2024 – 2026 2020 – 2024
```
