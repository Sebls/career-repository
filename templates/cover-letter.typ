// ============================================================================
// Shared Cover Letter Typst Template
// Professional 1-page cover letter matching CV typography & design
// ============================================================================

#let cover-letter-document(
  title: "Cover Letter",
  author: "Candidate Name",
  paper: "a4",
  font: ("Charter", "Libertinus Serif", "New Computer Modern", "Times New Roman"),
  body
) = {
  set document(title: title, author: author)
  set page(
    paper: paper,
    margin: (x: 2.0cm, top: 2.0cm, bottom: 2.0cm),
  )
  set text(
    font: font,
    size: 10pt,
    fill: rgb("#111827"),
    lang: "en",
    spacing: 100%,
  )
  set par(
    justify: true,
    leading: 0.65em,
    spacing: 1.2em,
  )

  // Configure links
  show link: set text(fill: rgb("#0284c7"))

  body
}

// Letter header (Applicant contact info)
#let letter-header(
  name: "",
  title: "",
  location: "",
  email: "",
  phone: "",
  linkedin: "",
  github: "",
  website: ""
) = {
  block(width: 100%, [
    #text(size: 18pt, weight: "bold", fill: rgb("#0f172a"))[#name]
    
    #if title != "" {
      v(-4pt)
      text(size: 10.5pt, style: "italic", fill: rgb("#334155"))[#title]
    }
    
    #v(-2pt)
    #let items = ()
    #if location != "" { items.push(location) }
    #if email != "" { items.push(link("mailto:" + email)[#email]) }
    #if phone != "" { items.push(link("tel:" + phone)[#phone]) }
    #if linkedin != "" { items.push(link("https://linkedin.com/in/" + linkedin)[linkedin.com/in/#linkedin]) }
    #if github != "" { items.push(link("https://github.com/" + github)[github.com/#github]) }
    #if website != "" { items.push(link(website)[#website.replace("https://", "")]) }

    #text(size: 8.5pt, fill: rgb("#475569"))[
      #items.join("  |  ")
    ]
    #v(4pt)
    #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
  ])
  v(10pt)
}

// Recipient block
#let letter-recipient(
  date: "",
  recipient-name: "Hiring Team",
  recipient-title: "",
  company: "",
  location: ""
) = {
  block(width: 100%, [
    #if date != "" [
      #text(fill: rgb("#475569"))[#date]
      #v(8pt)
    ]
    #text(weight: "bold", fill: rgb("#0f172a"))[#recipient-name] \
    #if recipient-title != "" [#recipient-title \ ]
    #if company != "" [#company \ ]
    #if location != "" [#location \ ]
  ])
  v(10pt)
}

// Letter Subject
#let letter-subject(subject) = {
  block(width: 100%, [
    #text(weight: "bold", fill: rgb("#0f172a"))[Re: #subject]
  ])
  v(6pt)
}

// Salutation
#let letter-salutation(salutation: "Dear Hiring Team,") = {
  [#salutation]
  v(4pt)
}

// Sign-off
#let letter-closing(
  closing: "Sincerely,",
  name: "Candidate Name"
) = {
  v(12pt)
  block(width: 100%, [
    #closing \
    #v(16pt)
    #text(weight: "bold", fill: rgb("#0f172a"))[#name]
  ])
}
