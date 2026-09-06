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

// Profile
#cv-section("Profile")
#cv-profile(profile)

// Education
#cv-section("Education")
#for edu in education [
  #cv-education(
    institution: edu.institution,
    degree: edu.degree,
    dates: edu.dates,
    gpa: edu.gpa,
  )
]

// Experience
#cv-section("Experience")
#for exp in experience [
  #cv-experience(
    role: exp.role,
    company: exp.company,
    dates: exp.dates,
    location: exp.location,
    contract: exp.contract,
    bullets: exp.bullets,
  )
]

// Projects
#cv-section("Projects")
#for proj in projects [
  #cv-project(
    name: proj.name,
    role: proj.role,
    dates: proj.dates,
    url: proj.url,
    bullets: proj.bullets,
  )
]

// Skills
#cv-section("Skills")
#for (category, items) in skills [
  #cv-skill(category, items)
]
