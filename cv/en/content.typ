// ============================================================================
// Canonical English CV Content (Generic Template)
// ============================================================================

#let personal = (
  name: "Alex Doe",
  title: "Software & AI Engineer",
  location: "San Francisco, CA",
  email: "alex.doe@example.com",
  phone: "+1 (555) 019-2834",
  linkedin: "alexdoe",
  github: "alexdoe",
  website: "https://alexdoe.dev",
)

#let profile = [
  *Software & AI Engineer* with experience in production software engineering and deploying scalable AI services. Interested in machine learning platforms, backend architectures, and production-grade intelligent systems.
]

#let education = (
  (
    institution: "State University",
    degree: [*Master of Science in Computer Science*],
    dates: "2024 – 2026",
    gpa: none,
  ),
  (
    institution: "Tech Institute",
    degree: [*Bachelor of Science in Software Engineering* (GPA: 3.9/4.0)],
    dates: "2020 – 2024",
    gpa: none,
  ),
)

#let experience = (
  (
    role: "Machine Learning Engineer",
    company: "Tech Innovations Inc.",
    dates: "Jan 2025 – Present",
    location: "San Francisco, CA",
    contract: "",
    bullets: (
      [Designed and deployed production-ready *inference endpoints*, processing high-volume daily requests with sub-100ms latency.],
      [Architected *agent workflows* and tool ecosystems with persistent memory and structured model-interaction workflows.],
      [Built *scalable data pipelines* for large-scale datasets, reducing processing runtime by 50% through automated validations.],
    ),
  ),
  (
    role: "Software Engineer",
    company: "Cloud Solutions Corp.",
    dates: "Mar 2023 – Dec 2024",
    location: "New York, NY",
    contract: "",
    bullets: (
      [Optimized backend service workflows and reduced API latency by 60% across containerized microservices.],
      [Automated testing and dataset validation pipelines via Python scripts, eliminating manual QA overhead.],
      [Developed and maintained backend services integrating external APIs and PostgreSQL databases applying clean architecture.],
    ),
  ),
)

#let projects = (
  (
    name: "OpenSearch Engine",
    role: "Open Source Project",
    dates: "2024",
    url: "https://github.com/alexdoe/search-engine",
    bullets: (
      [Developed an open-source semantic search engine applying *transformer-based embeddings* and vector indexing.],
      [Implemented a clean full-stack architecture using Next.js (TypeScript) for frontend and FastAPI (Python) for backend.],
    ),
  ),
)

#let skills = (
  ("Programming Languages", "Python • TypeScript • C/C++ • Go"),
  ("Frameworks & Libraries", "FastAPI • React • Next.js • Pandas • NumPy • PyTorch • TensorFlow"),
  ("Databases", "SQL (PostgreSQL, SQLite) • NoSQL (Redis, MongoDB)"),
  ("Infrastructure & Systems", "Linux • Git • GitHub Actions • Testing • CI/CD • Docker"),
  ("Cloud", "AWS (EC2, S3) • GCP (Compute Engine, Cloud Storage)"),
  (
    "Artificial Intelligence",
    "LLM Systems • Vector Embeddings • RAG • Computer Vision • Model Evaluation & Reproducibility",
  ),
  ("Languages", "English (Native) • Spanish (B2) • French (B1)"),
)
