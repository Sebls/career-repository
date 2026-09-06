#import "../../templates/cv.typ": *
#import "content.typ": *

#show: cv-document.with(
  title: "Curriculum Vitae",
  author: personal.name,
)

// Header
#cv-header(
  name: personal.name,
  title: personal.title,
  location: personal.location,
  email: personal.email,
  phone: personal.phone,
  linkedin: personal.linkedin,
  github: personal.github,
  website: personal.website,
)

// Profil
#cv-section("Profil")
#cv-profile(profile)

// Formation
#cv-section("Formation")
#for edu in education [
  #cv-education(
    institution: edu.institution,
    degree: edu.degree,
    dates: edu.dates,
    gpa: edu.gpa,
  )
]

// Expérience
#cv-section("Expérience")
#for exp in experience [
  #cv-experience-fr(
    company: exp.company,
    role: exp.role,
    dates: exp.dates,
    location: exp.location,
    bullets: exp.bullets,
  )
]

// Projets
#cv-section("Projets")
#for proj in projects [
  #cv-project(
    name: proj.name,
    role: proj.role,
    dates: proj.dates,
    url: proj.url,
    bullets: proj.bullets,
  )
]

// Compétences
#cv-section("Compétences")
#for (category, items) in skills [
  #cv-skill(category, items)
]
