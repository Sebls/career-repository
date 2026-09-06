// ============================================================================
// Canonical French CV Content (Generic Template)
// ============================================================================

#let personal = (
  name: "Alex Doe",
  title: "Ingénieur IA & Logiciel",
  location: "Paris, France",
  email: "alex.doe@example.com",
  phone: "+33 6 12 34 56 78",
  linkedin: "alexdoe",
  github: "alexdoe",
  website: "https://alexdoe.dev",
)

#let profile = [
  Ingénieur IA & Logiciel avec une solide expérience en développement logiciel et en déploiement de services d'intelligence artificielle en production. Passionné par les architectures backend évolutives, les modèles de langage et les systèmes intelligents prêts pour la production.
]

#let education = (
  (
    institution: "Grande École d’Ingénieurs",
    degree: [Diplôme d’Ingénieur (équivalent M.Sc.)],
    dates: "2024 – 2026",
    gpa: none,
  ),
  (
    institution: "Université de Technologie",
    degree: [Licence en Informatique (B.Sc.)],
    dates: "2020 – 2024",
    gpa: none,
  ),
)

#let experience = (
  (
    company: "Tech Innovations France",
    role: "Ingénieur Machine Learning",
    dates: "janv. 2025 – présent",
    location: "Paris, France",
    bullets: (
      [Conçu et déployé des endpoints d’inférence multimodale pour la production, traitant d'importants volumes de requêtes quotidiennes avec une faible latence.],
      [Étendu des architectures de deep learning et automatisé les pipelines de validation et d’évaluation des modèles.],
      [Construit des pipelines de données scalables, réduisant le temps de traitement de 50 % grâce à des workflows automatisés et reproductibles.],
    ),
  ),
  (
    company: "Solutions Numériques",
    role: "Ingénieur logiciel",
    dates: "mars 2023 – déc. 2024",
    location: "Lyon, France",
    bullets: (
      [Optimisé les pipelines de traitement de données et l’utilisation des ressources dans des environnements conteneurisés.],
      [Développé des scripts Python et des outils internes pour automatiser les tests et le contrôle qualité des données.],
      [Conçu et maintenu des services backend avec PostgreSQL et FastAPI en appliquant les principes d'architecture propre.],
    ),
  ),
)

#let projects = (
  (
    name: "Moteur de recherche sémantique",
    role: "Projet open source",
    dates: "2024",
    url: "https://github.com/alexdoe/search-engine",
    bullets: (
      [Développement d’un moteur de recherche sémantique basé sur des modèles transformers et l'indexation vectorielle.],
      [Implémentation d’une architecture full-stack propre utilisant Next.js et FastAPI avec tests automatisés et documentation complète.],
    ),
  ),
)

#let skills = (
  ("Compétences transversales", "Adaptabilité • Communication • Travail en équipe • Résolution de problèmes"),
  ("Langages de programmation", "Python (Pandas, NumPy, PyTorch, FastAPI) • TypeScript • C/C++"),
  ("Bases de données", "SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)"),
  ("Infrastructure & Systèmes", "Linux • Git • GitHub Actions • Tests logiciels • CI/CD • Docker"),
  ("Intelligence artificielle", "LLM • RAG • Embeddings vectoriels • Vision par ordinateur • Évaluation de modèles"),
  ("Langues", "Français (langue maternelle) • Anglais (C1) • Espagnol (B2)"),
)
