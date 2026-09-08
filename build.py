#!/usr/bin/env python3
"""
Generates wylie-chang.com in English, French, Spanish and Portuguese.

English lives at the root; the others at /fr/, /es/, /pt/.
Run:  python3 build.py
"""

import os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "fr", "es", "pt"]
PAGES = ["index", "research", "writing", "teaching", "cv", "contact"]

# Long-form pieces are hand-written and English-only for now.
LONGFORM = ["oration.html", "gratitude.html"]


def base(lang):
    return "/" if lang == "en" else "/%s/" % lang


# ---------------------------------------------------------------- navigation
NAV = {
    "en": [("research", "Research"), ("writing", "Writing"),
           ("teaching", "Teaching"), ("cv", "CV"), ("contact", "Contact")],
    "fr": [("research", "Recherche"), ("writing", "Écrits"),
           ("teaching", "Enseignement"), ("cv", "CV"), ("contact", "Contact")],
    "es": [("research", "Investigación"), ("writing", "Escritos"),
           ("teaching", "Docencia"), ("cv", "CV"), ("contact", "Contacto")],
    "pt": [("research", "Pesquisa"), ("writing", "Escritos"),
           ("teaching", "Ensino"), ("cv", "CV"), ("contact", "Contato")],
}

TITLES = {                       # page labels and <title> stems
    "research":  {"en": "Research", "fr": "Recherche", "es": "Investigación", "pt": "Pesquisa"},
    "writing":   {"en": "Writing", "fr": "Écrits", "es": "Escritos", "pt": "Escritos"},
    "teaching":  {"en": "Teaching", "fr": "Enseignement", "es": "Docencia", "pt": "Ensino"},
    "cv":        {"en": "Curriculum Vitae", "fr": "Curriculum vitæ", "es": "Currículum vítae", "pt": "Currículo"},
    "contact":   {"en": "Contact", "fr": "Contact", "es": "Contacto", "pt": "Contato"},
    "publications": {"en": "Publications", "fr": "Publications", "es": "Publicaciones", "pt": "Publicações"},
    "journal":   {"en": "Journal Articles", "fr": "Articles de revue", "es": "Artículos de revista", "pt": "Artigos"},
    "progress":  {"en": "In Progress", "fr": "En cours", "es": "En curso", "pt": "Em andamento"},
    "conference":{"en": "Conference Presentations", "fr": "Communications", "es": "Ponencias", "pt": "Apresentações"},
}

# ---------------------------------------------------------------------- home
BIO = {
"en": "My name is Wylie Chang 張振曦. I am a researcher in the Department of Emergency Medicine at Massachusetts General Hospital in the Emergency Medical Services group. I study emergency medicine, with a particular focus on shared decision-making in psychiatric emergencies. My research is guided by questions about social order, interpersonal cooperation, and the exercise of agency within medical institutions. I maintain interests in the organization, governance, and legitimacy of institutions and the history of science and medicine. Before turning toward medicine, I led several civic organizations, including Democracy House, Register2Vote.org, and Lead for America. I completed science coursework at Harvard University and read Philosophy, Politics, and Economics at Tufts University.",
"fr": "Je m’appelle Wylie Chang 張振曦. Je suis chercheur au département de médecine d’urgence du Massachusetts General Hospital, au sein du groupe des services médicaux d’urgence. J’étudie la médecine d’urgence, en m’intéressant particulièrement à la décision partagée dans les urgences psychiatriques. Mes recherches sont guidées par des questions portant sur l’ordre social, la coopération interpersonnelle et l’exercice de l’agentivité au sein des institutions médicales. Je m’intéresse également à l’organisation, à la gouvernance et à la légitimité des institutions, ainsi qu’à l’histoire des sciences et de la médecine. Avant de me tourner vers la médecine, j’ai dirigé plusieurs organisations civiques, dont Democracy House, Register2Vote.org et Lead for America. J’ai suivi un cursus scientifique à l’université Harvard et étudié la philosophie, la politique et l’économie à l’université Tufts.",
"es": "Me llamo Wylie Chang 張振曦. Soy investigador en el Departamento de Medicina de Urgencias del Massachusetts General Hospital, en el grupo de servicios médicos de emergencia. Estudio la medicina de urgencias, con especial atención a la toma de decisiones compartida en las urgencias psiquiátricas. Mi investigación se guía por preguntas sobre el orden social, la cooperación interpersonal y el ejercicio de la agencia dentro de las instituciones médicas. Mantengo interés por la organización, la gobernanza y la legitimidad de las instituciones, y por la historia de la ciencia y de la medicina. Antes de dedicarme a la medicina, dirigí varias organizaciones cívicas, entre ellas Democracy House, Register2Vote.org y Lead for America. Cursé estudios de ciencias en la Universidad Harvard y estudié Filosofía, Política y Economía en la Universidad Tufts.",
"pt": "Meu nome é Wylie Chang 張振曦. Sou pesquisador no Departamento de Medicina de Emergência do Massachusetts General Hospital, no grupo de serviços médicos de emergência. Estudo medicina de emergência, com atenção particular à decisão compartilhada em emergências psiquiátricas. Minha pesquisa é guiada por perguntas sobre ordem social, cooperação interpessoal e o exercício da agência dentro das instituições médicas. Mantenho interesse pela organização, governança e legitimidade das instituições e pela história da ciência e da medicina. Antes de me voltar para a medicina, liderei várias organizações cívicas, entre elas Democracy House, Register2Vote.org e Lead for America. Cursei disciplinas de ciências na Universidade Harvard e estudei Filosofia, Política e Economia na Universidade Tufts.",
}

PHOTO_ALT = {
"en": "A crowd seated on a low wall at dusk, looking up at the sky, with hills behind.",
"fr": "Une assemblée assise sur un muret au crépuscule, le regard tourné vers le ciel, des collines à l’arrière-plan.",
"es": "Un grupo sentado sobre un muro bajo al atardecer, mirando al cielo, con colinas al fondo.",
"pt": "Um grupo sentado sobre um muro baixo ao entardecer, olhando para o céu, com colinas ao fundo.",
}

# ------------------------------------------------------------------ research
RESEARCH = {
"en": ["My primary line of research concerns shared decision-making in emergency medicine, particularly in psychiatric emergencies and other encounters in which the conditions for ordinary deliberation are complicated by uncertain capacity and lack of rapport. I am interested in how patients and clinicians establish workable forms of cooperation under these conditions, and how trust, authority, and responsibility are negotiated in acute care. Drawing on clinical models of shared decision-making, Anselm Strauss’s concept of negotiated order, and practices from civic organizing and advocacy, I examine how clinical relationships can support patient agency.",
       "I also maintain a line of research on emergency medical services, examining how decentralized systems and the discretion delegated to dispatchers, clinicians, and organizations shape variation in care and outcomes. A further area of my work examines civic engagement and political participation in healthcare settings."],
"fr": ["Mon principal axe de recherche porte sur la décision partagée en médecine d’urgence, en particulier dans les urgences psychiatriques et dans les situations où les conditions d’une délibération ordinaire sont compliquées par une capacité incertaine et par l’absence de lien de confiance. Je m’intéresse à la manière dont patients et cliniciens établissent des formes de coopération praticables dans ces conditions, et à la façon dont la confiance, l’autorité et la responsabilité se négocient dans les soins aigus. En m’appuyant sur les modèles cliniques de la décision partagée, sur la notion d’ordre négocié d’Anselm Strauss et sur des pratiques issues de l’organisation civique et du plaidoyer, j’examine comment les relations cliniques peuvent soutenir l’agentivité du patient.",
       "Je poursuis également des recherches sur les services médicaux d’urgence, en examinant comment les systèmes décentralisés et le pouvoir d’appréciation délégué aux régulateurs, aux cliniciens et aux organisations produisent des variations dans les soins et les résultats. Un autre volet de mon travail porte sur l’engagement civique et la participation politique dans les établissements de santé."],
"es": ["Mi principal línea de investigación aborda la toma de decisiones compartida en medicina de urgencias, en particular en las urgencias psiquiátricas y en aquellos encuentros en los que las condiciones para la deliberación ordinaria se ven complicadas por una capacidad incierta y por la falta de vínculo. Me interesa cómo pacientes y clínicos establecen formas viables de cooperación en esas condiciones, y cómo se negocian la confianza, la autoridad y la responsabilidad en la atención aguda. A partir de los modelos clínicos de decisión compartida, del concepto de orden negociado de Anselm Strauss y de prácticas provenientes de la organización cívica y la incidencia, examino cómo las relaciones clínicas pueden sostener la agencia del paciente.",
       "También mantengo una línea de investigación sobre los servicios médicos de emergencia, en la que examino cómo los sistemas descentralizados y la discrecionalidad delegada a operadores, clínicos y organizaciones producen variaciones en la atención y en los resultados. Otra área de mi trabajo examina la participación cívica y política en los entornos sanitarios."],
"pt": ["Minha principal linha de pesquisa trata da decisão compartilhada em medicina de emergência, particularmente em emergências psiquiátricas e em encontros nos quais as condições para a deliberação comum são complicadas por capacidade incerta e pela ausência de vínculo. Interesso-me por como pacientes e clínicos estabelecem formas viáveis de cooperação nessas condições, e por como confiança, autoridade e responsabilidade são negociadas no cuidado agudo. Apoiando-me em modelos clínicos de decisão compartilhada, no conceito de ordem negociada de Anselm Strauss e em práticas da organização cívica e da advocacia, examino como as relações clínicas podem sustentar a agência do paciente.",
       "Mantenho também uma linha de pesquisa sobre os serviços médicos de emergência, examinando como sistemas descentralizados e a discricionariedade delegada a operadores, clínicos e organizações produzem variações no cuidado e nos desfechos. Outra área do meu trabalho examina o engajamento cívico e a participação política em ambientes de saúde."],
}

PROFILES = {
"en": 'You can find my peer-reviewed articles on my profile at <a class="link" href="https://scholar.google.com/citations?user=UE97hJIAAAAJ&amp;hl=en">Google Scholar</a>. My ORCID is <a class="link" href="https://orcid.org/0009-0002-3935-5418">0009-0002-3935-5418</a>.',
"fr": 'Mes articles évalués par les pairs sont disponibles sur mon profil <a class="link" href="https://scholar.google.com/citations?user=UE97hJIAAAAJ&amp;hl=en">Google Scholar</a>. Mon identifiant ORCID est <a class="link" href="https://orcid.org/0009-0002-3935-5418">0009-0002-3935-5418</a>.',
"es": 'Mis artículos revisados por pares están disponibles en mi perfil de <a class="link" href="https://scholar.google.com/citations?user=UE97hJIAAAAJ&amp;hl=en">Google Scholar</a>. Mi ORCID es <a class="link" href="https://orcid.org/0009-0002-3935-5418">0009-0002-3935-5418</a>.',
"pt": 'Meus artigos revisados por pares estão disponíveis no meu perfil do <a class="link" href="https://scholar.google.com/citations?user=UE97hJIAAAAJ&amp;hl=en">Google Scholar</a>. Meu ORCID é <a class="link" href="https://orcid.org/0009-0002-3935-5418">0009-0002-3935-5418</a>.',
}

# Citations are never translated — a work is cited in the language it was published in.
ENTRIES = {
"journal": [
 (None, "Prehospital sedation and physical restraint of older adults presenting with behavioral health emergencies: a nationwide cross-sectional study",
  'Peters GA, Bongiorno DM, Misra A, <span class="self">Chang WD</span>, Allerhand T, Kennedy M, Dorsett M, Rosen T, Goldberg SA, Cash RA',
  'Accepted at <cite>Journal of the American Geriatrics Society</cite>, 2026'),
 ("https://doi.org/10.1080/10903127.2026.2690618", "Cardiac arrest during interfacility transport with emergency medical services: a nationwide cross-sectional study",
  'Peters GA, Misra A, Samadian KD, <span class="self">Chang WD</span>, Chandran KG, Kurwitz JA, Muszalski C, Wilcox SR, Goldberg SA, Cash RE',
  '<cite>Prehospital Emergency Care</cite>, 2026'),
 ("https://pubmed.ncbi.nlm.nih.gov/42561178/", "Healthcare-led get-out-the-vote efforts as treatments for public health and democracy",
  'Hunter K, Shepherd M, Izatt H, Nielson D, <span class="self">Chang WD</span>, Martin AF',
  '<cite>American Journal of Public Health</cite>, 2026'),
 ("https://doi.org/10.1542/peds.2024-068207", "Parent perspectives on health care&ndash;based voter engagement: a qualitative study",
  'Jones MN, Doan TN, Lipps L, Dennis T, Ruxin T, Kopp SJ, Liu V, Shyamsundar S, Beck AF, Izatt H, McCann JA, <span class="self">Chang WD</span>, Sandoval L, Camara S, Copeland KA',
  '<cite>Pediatrics</cite>, 2025'),
],
"progress": [
 (None, "Voter engagement among federal benefits recipients and the impact of multi-program enrollment",
  'Lauterwasser S, <span class="self">Chang WD</span>, Scheinert T, Martin AF', None),
],
"conference": [
 (None, "Practicing solidarity: lessons from EMS and community organizing",
  '<span class="self">Chang WD</span>',
  'National Emergency Medical Services Physicians Annual Meeting, Tampa, FL, January 2026'),
 (None, "Patient characteristics and short-term outcomes associated with helicopter EMS versus ground ambulance transport for out-of-hospital cardiac arrest",
  'Misra A, <span class="self">Chang WD</span>, Peters GA, Goldberg SA, Norman J, Seethala R, Cash RE',
  'National Association of EMS Physicians Annual Meeting, Tampa, FL, January 2026'),
],
}

# ------------------------------------------------------------------- writing
WRITING_INTRO = {
"en": "I enjoy writing and speaking in various contexts. Some examples of recent work are below.",
"fr": "J’écris et je prends la parole dans des contextes variés. Voici quelques exemples de travaux récents.",
"es": "Escribo y hablo en público en contextos diversos. A continuación, algunos ejemplos de trabajos recientes.",
"pt": "Escrevo e falo em contextos variados. Abaixo, alguns exemplos de trabalhos recentes.",
}

PIECES = {
"en": [("/gratitude.html", "&ldquo;The &lsquo;Way&rsquo; of Gratitude.&rdquo;", "Oration, Appleton Chapel, Harvard University, February 2025."),
       ("/oration.html", "Officiant Oration for the wedding of Nina Roussille and Ameet Kallarackal.", "Aix-en-Provence, France, June 2026.")],
"fr": [("/gratitude.html", "&ldquo;The &lsquo;Way&rsquo; of Gratitude.&rdquo;", "Allocution, Appleton Chapel, université Harvard, février 2025."),
       ("/oration.html", "Allocution de célébrant pour le mariage de Nina Roussille et Ameet Kallarackal.", "Aix-en-Provence, France, juin 2026.")],
"es": [("/gratitude.html", "&ldquo;The &lsquo;Way&rsquo; of Gratitude.&rdquo;", "Alocución, Appleton Chapel, Universidad Harvard, febrero de 2025."),
       ("/oration.html", "Alocución como oficiante en la boda de Nina Roussille y Ameet Kallarackal.", "Aix-en-Provence, Francia, junio de 2026.")],
"pt": [("/gratitude.html", "&ldquo;The &lsquo;Way&rsquo; of Gratitude.&rdquo;", "Alocução, Appleton Chapel, Universidade Harvard, fevereiro de 2025."),
       ("/oration.html", "Alocução como celebrante no casamento de Nina Roussille e Ameet Kallarackal.", "Aix-en-Provence, França, junho de 2026.")],
}

ENGLISH_NOTE = {
"en": None,
"fr": "Ces textes sont disponibles en anglais uniquement.",
"es": "Estos textos están disponibles solo en inglés.",
"pt": "Estes textos estão disponíveis apenas em inglês.",
}

# ------------------------------------------------------------------ teaching
COURSES = {
"en": [("The American Soul", None,
        "As more Americans identify as spiritual but not religious, this course asks what spirituality means in twenty-first-century America, and what that implies for civic life. Through contemplative practice in class, personal reflection, and discussion of primary texts, images, and stories, students examine their own assumptions about religion, spirituality, and contemplative traditions in the United States."),
       ("Literature of Confinement", "Tufts University, Department of English &middot; with Dr. Hilary Binda",
        "I had the opportunity to assist with this course, taught by Dr. Hilary Binda."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative &middot; co-authored with Dr. Hilary Binda",
        "A syllabus written for the inaugural curriculum of the Tufts Prison Initiative, in which Tufts undergraduates took credit-bearing seminars alongside incarcerated men at Souza-Baranowski Correctional Center, a maximum-security prison in Lancaster, Massachusetts. The course explores confinement through three themes: education in prison, marginalized identities in captivity, and social movements to reform and abolish prisons.")],
"fr": [("The American Soul", None,
        "Alors qu’un nombre croissant d’Américains se disent spirituels sans être religieux, ce cours interroge ce que signifie la spiritualité dans l’Amérique du XXI<sup>e</sup> siècle et ce qu’elle implique pour la vie civique. À travers la pratique contemplative en classe, la réflexion personnelle et la discussion de textes, d’images et de récits, les étudiants examinent leurs propres présupposés sur la religion, la spiritualité et les traditions contemplatives aux États-Unis."),
       ("Literature of Confinement", "Université Tufts, département d’anglais &middot; avec la D<sup>re</sup> Hilary Binda",
        "J’ai eu l’occasion de participer à ce cours, dispensé par la D<sup>re</sup> Hilary Binda."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative &middot; coécrit avec la D<sup>re</sup> Hilary Binda",
        "Un programme rédigé pour le curriculum inaugural de la Tufts Prison Initiative, dans le cadre de laquelle des étudiants de Tufts ont suivi des séminaires crédités aux côtés d’hommes incarcérés au Souza-Baranowski Correctional Center, une prison de haute sécurité à Lancaster, dans le Massachusetts. Le cours aborde l’enfermement selon trois axes : l’éducation en prison, les identités marginalisées en captivité, et les mouvements sociaux visant à réformer et à abolir les prisons.")],
"es": [("The American Soul", None,
        "A medida que más estadounidenses se identifican como espirituales pero no religiosos, este curso pregunta qué significa la espiritualidad en la América del siglo XXI y qué implica para la vida cívica. Mediante la práctica contemplativa en clase, la reflexión personal y la discusión de textos, imágenes e historias, los estudiantes examinan sus propios supuestos sobre la religión, la espiritualidad y las tradiciones contemplativas en Estados Unidos."),
       ("Literature of Confinement", "Universidad Tufts, Departamento de Inglés &middot; con la Dra. Hilary Binda",
        "Tuve la oportunidad de colaborar en este curso, impartido por la Dra. Hilary Binda."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative &middot; coescrito con la Dra. Hilary Binda",
        "Un programa escrito para el currículo inaugural de la Tufts Prison Initiative, en el que estudiantes de Tufts cursaron seminarios con créditos junto a hombres encarcelados en el Souza-Baranowski Correctional Center, una prisión de máxima seguridad en Lancaster, Massachusetts. El curso explora el encierro a partir de tres ejes: la educación en prisión, las identidades marginadas en cautiverio y los movimientos sociales para reformar y abolir las prisiones.")],
"pt": [("The American Soul", None,
        "À medida que mais estadunidenses se identificam como espiritualizados, mas não religiosos, este curso pergunta o que significa espiritualidade nos Estados Unidos do século XXI e o que isso implica para a vida cívica. Por meio da prática contemplativa em sala, da reflexão pessoal e da discussão de textos, imagens e histórias, os estudantes examinam seus próprios pressupostos sobre religião, espiritualidade e tradições contemplativas nos Estados Unidos."),
       ("Literature of Confinement", "Universidade Tufts, Departamento de Inglês &middot; com a Dra. Hilary Binda",
        "Tive a oportunidade de colaborar neste curso, ministrado pela Dra. Hilary Binda."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative &middot; coescrito com a Dra. Hilary Binda",
        "Um programa escrito para o currículo inaugural da Tufts Prison Initiative, no qual estudantes de Tufts cursaram seminários com créditos ao lado de homens encarcerados no Souza-Baranowski Correctional Center, uma prisão de segurança máxima em Lancaster, Massachusetts. O curso explora o confinamento a partir de três eixos: a educação na prisão, as identidades marginalizadas em cativeiro e os movimentos sociais para reformar e abolir as prisões.")],
}

# ------------------------------------------------------------------ cv, contact
CV_TEXT = {
"en": "A copy of my curriculum vitae is available on request.",
"fr": "Mon curriculum vitæ est disponible sur demande.",
"es": "Una copia de mi currículum vítae está disponible a solicitud.",
"pt": "Uma cópia do meu currículo está disponível mediante solicitação.",
}

CONTACT_LEAD = {
"en": "I can be reached at",
"fr": "Vous pouvez me joindre à",
"es": "Puede escribirme a",
"pt": "Você pode entrar em contato comigo em",
}


# --------------------------------------------------------------------- render
def head(lang, page, title):
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="https://wylie-chang.com%s%s">'
        % (l, base(l), "" if page == "index" else page + ".html")
        for l in LANGS)
    return """<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
%s
<link rel="alternate" hreflang="x-default" href="https://wylie-chang.com/%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div class="shell">
""" % (lang, title, alts, "" if page == "index" else page + ".html")


def sidebar(lang, page):
    items = []
    for slug, label in NAV[lang]:
        cur = ' aria-current="page"' if slug == page else ''
        items.append('      <a href="%s%s.html"%s>%s</a>' % (base(lang), slug, cur, label))
    langs = []
    for i, l in enumerate(LANGS):
        target = base(l) + ("" if page == "index" else page + ".html")
        cur = ' aria-current="true"' if l == lang else ''
        if i:
            langs.append('<span class="sep">&middot;</span>')
        langs.append('<a href="%s"%s lang="%s">%s</a>' % (target, cur, l, l.upper()))
    home = ' aria-current="page"' if page == "index" else ''
    return """  <header>
    <a class="name" href="%s"%s>Wylie Chang</a>
    <nav class="nav">
%s
    </nav>
    <p class="langs">%s</p>
  </header>
""" % (base(lang), home, "\n".join(items), "".join(langs))


def entry_html(link, title, authors, source):
    t = ('<a class="title title-link" href="%s">%s</a>' % (link, title)) if link \
        else ('<span class="title">%s</span>' % title)
    out = ['      <div class="entry">', "        " + t,
           '        <span class="authors">%s</span>' % authors]
    if source:
        out.append('        <span class="source">%s</span>' % source)
    out.append("      </div>")
    return "\n".join(out)


def build_page(lang, page):
    L = lambda k: TITLES[k][lang]
    stem = "Wylie Chang" if page == "index" else "%s &mdash; Wylie Chang" % L(page)
    out = [head(lang, page, stem), sidebar(lang, page)]

    if page == "index":
        out.append('  <main class="main--home">\n    <div class="column">')
        out.append('      <figure class="photo-col">\n        <img class="photo" src="/photo.jpg" width="800" height="1067" alt="%s">\n      </figure>' % PHOTO_ALT[lang])
        out.append("      <p>%s</p>\n    </div>\n  </main>" % BIO[lang])

    elif page == "research":
        out.append('  <main>\n    <h1 class="label">%s</h1>\n\n    <div class="column">' % L("research"))
        for p in RESEARCH[lang]:
            out.append("      <p>%s</p>" % p)
        out.append('      <p class="profiles">%s</p>\n    </div>' % PROFILES[lang])
        out.append('\n    <div class="column bibliography">\n      <h2 class="label">%s</h2>' % L("publications"))
        for group in ("journal", "progress", "conference"):
            out.append('\n      <h3 class="group">%s</h3>\n' % L(group))
            for e in ENTRIES[group]:
                out.append(entry_html(*e))
        out.append("    </div>\n  </main>")

    elif page == "writing":
        out.append('  <main>\n    <h1 class="label">%s</h1>\n\n    <div class="column">' % L("writing"))
        out.append("      <p>%s</p>" % WRITING_INTRO[lang])
        note = ENGLISH_NOTE[lang]
        if note:
            out.append('      <p class="profiles">%s</p>' % note)
        out.append('\n      <div style="margin-top:3.5rem">')
        for href, title, where in PIECES[lang]:
            out.append('        <div class="piece">\n          <a class="title title-link" href="%s">%s</a>\n          <span class="where">%s</span>\n        </div>' % (href, title, where))
        out.append("      </div>\n    </div>\n  </main>")

    elif page == "teaching":
        out.append('  <main>\n    <h1 class="label">%s</h1>\n\n    <div class="column">' % L("teaching"))
        for name, meta, desc in COURSES[lang]:
            out.append('      <div class="course">\n        <h2 class="group">%s</h2>' % name)
            if meta:
                out.append('        <span class="course-meta">%s</span>' % meta)
            out.append("        <p>%s</p>\n      </div>\n" % desc)
        out.append("    </div>\n  </main>")

    elif page == "cv":
        out.append('  <main>\n    <h1 class="label">%s</h1>\n    <div class="column">\n      <p>%s</p>\n    </div>\n  </main>' % (L("cv"), CV_TEXT[lang]))

    elif page == "contact":
        out.append('  <main>\n    <h1 class="label">%s</h1>\n    <div class="column">\n      <p class="address">%s<br>\n        wdc [@] mail.ch<br>\n        wdchang [@] bwh.harvard.edu\n      </p>\n    </div>\n  </main>' % (L("contact"), CONTACT_LEAD[lang]))

    out.append("</div>\n</body>\n</html>\n")
    return "\n".join(out)


def main():
    written = []
    for lang in LANGS:
        outdir = ROOT if lang == "en" else os.path.join(ROOT, lang)
        os.makedirs(outdir, exist_ok=True)
        for page in PAGES:
            path = os.path.join(outdir, page + ".html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(build_page(lang, page))
            written.append(os.path.relpath(path, ROOT))
    print("wrote %d pages" % len(written))
    for w in written:
        print("  " + w)


if __name__ == "__main__":
    main()
