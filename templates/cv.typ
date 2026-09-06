// ============================================================================
// Shared CV Typst Template - Exact LaTeX Style Replica
// Matches RenderCV / LaTeX geometry, Charter typography, FA icons & section rules
// ============================================================================

// FontAwesome Icons loaded from assets/
#let icon-box(path) = box(height: 0.82em, baseline: 0.08em, image(path))

#let fa-map-marker = icon-box("../assets/map-marker.svg")
#let fa-envelope = icon-box("../assets/envelope.svg")
#let fa-phone = icon-box("../assets/phone.svg")
#let fa-linkedin = icon-box("../assets/linkedin.svg")
#let fa-github = icon-box("../assets/github.svg")
#let fa-home = icon-box("../assets/home.svg")

#let cv-document(
  title: "Curriculum Vitae",
  author: "Candidate Name",
  paper: "us-letter",
  font: ("Charter", "Libertinus Serif", "New Computer Modern"),
  body,
) = {
  set document(title: title, author: author)
  set page(
    paper: paper,
    margin: (x: 1.25cm, top: 0.35cm, bottom: 0.35cm),
  )
  set text(
    font: font,
    size: 8.6pt,
    fill: rgb("#000000"),
    lang: "en",
    spacing: 100%,
  )
  set par(
    justify: true,
    leading: 0.42em,
    first-line-indent: 0pt,
  )

  // Links in black without underline (exact LaTeX style)
  show link: set text(fill: rgb("#000000"))

  body
}

// Header component matching LaTeX \begin{header} ... \end{header}
#let cv-header(
  name: "Candidate Name",
  title: "",
  location: "City, Country",
  email: "candidate@example.com",
  phone: "+1 (555) 019-2834",
  linkedin: "candidate",
  github: "candidate",
  website: "https://candidate.dev",
) = {
  let items = ()
  if location != "" { items.push([#fa-map-marker #location]) }
  if email != "" { items.push([#fa-envelope #link("mailto:" + email)[#email]]) }
  if phone != "" { items.push([#fa-phone #link("tel:" + phone)[#phone]]) }
  if linkedin != "" { items.push([#fa-linkedin #link("https://www.linkedin.com/in/" + linkedin)[#linkedin]]) }
  if github != "" { items.push([#fa-github #link("https://github.com/" + github)[#github]]) }
  if website != "" { items.push([#fa-home #link(website)[#website.replace("https://", "")]]) }

  align(center)[
    #text(size: 19pt, weight: "bold")[#name] \
    #if title != "" [
      #v(-4pt)
      #text(size: 9.2pt, style: "italic")[#title] \
      #v(-4pt)
    ] else [
      #v(-4pt)
    ]
    #text(size: 8.6pt)[
      #items.join([ #h(3.5pt) | #h(3.5pt) ])
    ]
  ]
  v(1pt)
}

// Section Header matching LaTeX \section{...} with \titlerule
#let cv-section(title) = {
  v(2.5pt)
  text(size: 10pt, weight: "bold")[#title]
  v(-3.5pt)
  line(length: 100%, stroke: 0.5pt + rgb("#000000"))
  v(1.0pt)
}

// Onecolentry Profile block
#let cv-profile(body) = {
  block(
    width: 100%,
    text(size: 8.6pt, style: "italic")[#body],
  )
}

// Twocolentry Education item
#let cv-education(
  institution: "",
  degree: "",
  dates: "",
  gpa: none,
) = {
  block(
    width: 100%,
    below: 2.5pt,
    [
      #grid(
        columns: (1fr, auto),
        align: (left, right),
        [
          #text(weight: "bold")[#institution], #degree
        ],
        [
          #dates
        ],
      )
      #if gpa != none [
        #v(-1.5pt)
        #set list(marker: [•], body-indent: 4.5pt, tight: true)
        - #gpa
      ]
    ],
  )
}

// Experience Item matching LaTeX \item \textbf{Role} - \textit{Company} (Dates) – Location (Contract)
#let cv-experience(
  role: "",
  company: "",
  dates: "",
  location: "",
  contract: "",
  bullets: (),
) = {
  block(
    width: 100%,
    below: 2.8pt,
    [
      #text(weight: "bold")[#role] - #text(style: "italic")[#company] (#dates) – #location#if contract != "" [ (#contract)]
      #if bullets.len() > 0 [
        #v(-1.8pt)
        #set list(marker: [•], body-indent: 4.5pt, tight: true, spacing: 1.8pt)
        #for b in bullets [
          - #b
        ]
      ]
    ],
  )
}

// Experience Item for French format matching \textbf{Company} - \textit{Role} (Dates) – Location
#let cv-experience-fr(
  company: "",
  role: "",
  dates: "",
  location: "",
  bullets: (),
) = {
  block(
    width: 100%,
    below: 2.8pt,
    [
      #text(weight: "bold")[#company] - #text(style: "italic")[#role] (#dates) – #location
      #if bullets.len() > 0 [
        #v(-1.8pt)
        #set list(marker: [•], body-indent: 4.5pt, tight: true, spacing: 1.8pt)
        #for b in bullets [
          - #b
        ]
      ]
    ],
  )
}

// Project Item matching \href{url}{\faIcon{github} \textbf{Name}} — \textit{Context} (Date)
#let cv-project(
  name: "",
  role: "",
  dates: "",
  url: "",
  bullets: (),
) = {
  block(
    width: 100%,
    below: 2.8pt,
    [
      #if url != "" [
        #link(url)[#fa-github #text(weight: "bold")[#name]]
      ] else [
        #text(weight: "bold")[#name]
      ] — #text(style: "italic")[#role] (#dates)
      #if bullets.len() > 0 [
        #v(-1.8pt)
        #set list(marker: [•], body-indent: 4.5pt, tight: true, spacing: 1.8pt)
        #for b in bullets [
          - #b
        ]
      ]
    ],
  )
}

// Skills Item matching \begin{onecolentry} \textbf{Category:} ... \end{onecolentry}
#let cv-skill(category, items) = {
  block(
    width: 100%,
    below: 1.2pt,
    [
      #text(weight: "bold")[#category:] #items
    ],
  )
}
