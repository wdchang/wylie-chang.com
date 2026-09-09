#!/usr/bin/env python3
"""
Generates wylie-chang.com in English, French, Spanish and Portuguese.

English lives at the root; the others at /fr/, /es/, /pt/.
Run:  python3 build.py
"""

import os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "fr", "es"]   # Portuguese translations remain below, unused
PAGES = ["index", "research", "writing", "teaching", "arts", "cv", "contact"]

# Long-form pieces are hand-written and English-only for now.
LONGFORM = ["oration.html", "gratitude.html"]


def base(lang):
    return "/" if lang == "en" else "/%s/" % lang


# ---------------------------------------------------------------- navigation
NAV = {
    "en": [("research", "Research"), ("writing", "Writing"),
           ("teaching", "Teaching"), ("arts", "Arts"), ("cv", "CV"), ("contact", "Contact")],
    "fr": [("research", "Recherche"), ("writing", "Écrits"),
           ("teaching", "Enseignement"), ("arts", "Arts"), ("cv", "CV"), ("contact", "Contact")],
    "es": [("research", "Investigación"), ("writing", "Escritos"),
           ("teaching", "Docencia"), ("arts", "Artes"), ("cv", "CV"), ("contact", "Contacto")],
    "pt": [("research", "Pesquisa"), ("writing", "Escritos"),
           ("teaching", "Ensino"), ("cv", "CV"), ("contact", "Contato")],
}

TITLES = {                       # page labels and <title> stems
    "research":  {"en": "Research", "fr": "Recherche", "es": "Investigación", "pt": "Pesquisa"},
    "writing":   {"en": "Writing", "fr": "Écrits", "es": "Escritos", "pt": "Escritos"},
    "teaching":  {"en": "Teaching", "fr": "Enseignement", "es": "Docencia", "pt": "Ensino"},
    "arts":      {"en": "Arts", "fr": "Arts", "es": "Artes", "pt": "Artes"},
    "cv":        {"en": "Curriculum Vitae", "fr": "Curriculum vitæ", "es": "Currículum vítae", "pt": "Currículo"},
    "contact":   {"en": "Contact", "fr": "Contact", "es": "Contacto", "pt": "Contato"},
    "publications": {"en": "Publications", "fr": "Publications", "es": "Publicaciones", "pt": "Publicações"},
    "journal":   {"en": "Journal Articles", "fr": "Articles de revue", "es": "Artículos de revista", "pt": "Artigos"},
    "progress":  {"en": "In Progress", "fr": "En cours", "es": "En curso", "pt": "Em andamento"},
    "conference":{"en": "Conference Presentations", "fr": "Communications", "es": "Ponencias", "pt": "Apresentações"},
}

# ---------------------------------------------------------------------- home
BIO = {
"en": [
 "I am an EMT and researcher. I currently contribute to research at the Department of Emergency Medicine at Massachusetts General Hospital, in the Emergency Medical Services group. I study how patients and clinicians make decisions together under conditions of uncertainty and urgency.",
 "I’m especially interested in psychiatric emergencies and the questions of agency, authority, and responsibility that arise.",
 "My other primary interests are institutional governance; the history of science and medicine; and the role of healthcare institutions in civic life and democracy.",
 "Previously, I led civic organizations, including Democracy House, Register2Vote.org, and Lead for America. I studied Philosophy, Politics, and Economics at Tufts University and completed science coursework at Harvard University.",
 "I live in Cambridge, Massachusetts.",
],
"fr": [
 "Je suis technicien médical d’urgence (EMT) et chercheur. Je contribue actuellement aux travaux du département de médecine d’urgence du Massachusetts General Hospital, au sein du groupe des services médicaux d’urgence. J’étudie la manière dont patients et cliniciens prennent ensemble des décisions dans des conditions d’incertitude et d’urgence.",
 "Je m’intéresse particulièrement aux urgences psychiatriques et aux questions d’agentivité, d’autorité et de responsabilité qui s’y posent.",
 "Mes autres centres d’intérêt principaux sont la gouvernance institutionnelle ; l’histoire des sciences et de la médecine ; et le rôle des institutions de santé dans la vie civique et la démocratie.",
 "Auparavant, j’ai dirigé des organisations civiques, dont Democracy House, Register2Vote.org et Lead for America. J’ai étudié la philosophie, la politique et l’économie à l’université Tufts et suivi un cursus scientifique à l’université Harvard.",
 "Je vis à Cambridge, dans le Massachusetts.",
],
"es": [
 "Soy técnico en emergencias médicas (EMT) e investigador. Actualmente colaboro en la investigación del Departamento de Medicina de Urgencias del Massachusetts General Hospital, en el grupo de servicios médicos de emergencia. Estudio cómo pacientes y clínicos toman decisiones conjuntamente en condiciones de incertidumbre y urgencia.",
 "Me interesan especialmente las urgencias psiquiátricas y las preguntas sobre agencia, autoridad y responsabilidad que allí surgen.",
 "Mis otros intereses principales son la gobernanza institucional; la historia de la ciencia y de la medicina; y el papel de las instituciones sanitarias en la vida cívica y la democracia.",
 "Anteriormente dirigí organizaciones cívicas, entre ellas Democracy House, Register2Vote.org y Lead for America. Estudié Filosofía, Política y Economía en la Universidad Tufts y cursé estudios de ciencias en la Universidad Harvard.",
 "Vivo en Cambridge, Massachusetts.",
],
}

PHOTO_ALT = {
"en": "A crowd seated on a low wall at dusk, looking up at the sky, with hills behind.",
"fr": "Une assemblée assise sur un muret au crépuscule, le regard tourné vers le ciel, des collines à l’arrière-plan.",
"es": "Un grupo sentado sobre un muro bajo al atardecer, mirando al cielo, con colinas al fondo.",
"pt": "Um grupo sentado sobre um muro baixo ao entardecer, olhando para o céu, com colinas ao fundo.",
}

# ------------------------------------------------------------------ research
RESEARCH = {
"en": [
 "My primary line of research concerns shared decision-making in emergency medicine, particularly in psychiatric emergencies and other encounters in which the conditions for ordinary deliberation are complicated by uncertain capacity and lack of rapport. I am interested in how patients and clinicians establish workable forms of cooperation under these conditions, and how trust, authority, and responsibility are negotiated in acute care.",
 "Drawing on clinical models of shared decision-making, Anselm Strauss’s concept of negotiated order, and practices from civic organizing and advocacy, I examine how clinicians can protect patient agency during crises.",
 "I also maintain a line of research on emergency medical services, examining how decentralized systems and the discretion delegated to dispatchers, clinicians, and organizations shape variation in care and outcomes.",
 "A further area of my work examines civic engagement in healthcare settings.",
],
"fr": [
 "Mon principal axe de recherche porte sur la décision partagée en médecine d’urgence, en particulier dans les urgences psychiatriques et dans les situations où les conditions d’une délibération ordinaire sont compliquées par une capacité incertaine et par l’absence de lien de confiance. Je m’intéresse à la manière dont patients et cliniciens établissent des formes de coopération praticables dans ces conditions, et à la façon dont la confiance, l’autorité et la responsabilité se négocient dans les soins aigus.",
 "En m’appuyant sur les modèles cliniques de la décision partagée, sur la notion d’ordre négocié d’Anselm Strauss et sur des pratiques issues de l’organisation civique et du plaidoyer, j’examine comment les cliniciens peuvent protéger l’agentivité du patient en situation de crise.",
 "Je poursuis également des recherches sur les services médicaux d’urgence, en examinant comment les systèmes décentralisés et le pouvoir d’appréciation délégué aux régulateurs, aux cliniciens et aux organisations produisent des variations dans les soins et les résultats.",
 "Un autre volet de mon travail porte sur l’engagement civique dans les établissements de santé.",
],
"es": [
 "Mi principal línea de investigación aborda la toma de decisiones compartida en medicina de urgencias, en particular en las urgencias psiquiátricas y en aquellos encuentros en los que las condiciones para la deliberación ordinaria se ven complicadas por una capacidad incierta y por la falta de vínculo. Me interesa cómo pacientes y clínicos establecen formas viables de cooperación en esas condiciones, y cómo se negocian la confianza, la autoridad y la responsabilidad en la atención aguda.",
 "A partir de los modelos clínicos de decisión compartida, del concepto de orden negociado de Anselm Strauss y de prácticas provenientes de la organización cívica y la incidencia, examino cómo los clínicos pueden proteger la agencia del paciente durante las crisis.",
 "También mantengo una línea de investigación sobre los servicios médicos de emergencia, en la que examino cómo los sistemas descentralizados y la discrecionalidad delegada a operadores, clínicos y organizaciones producen variaciones en la atención y en los resultados.",
 "Otra área de mi trabajo examina la participación cívica en los entornos sanitarios.",
],
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
  'National Emergency Medical Services Physicians Annual Meeting, Tampa, FL, January 2026',
  'Best New Speaker (top two presentations)'),
 (None, "Patient characteristics and short-term outcomes associated with helicopter EMS versus ground ambulance transport for out-of-hospital cardiac arrest",
  'Misra A, <span class="self">Chang WD</span>, Peters GA, Goldberg SA, Norman J, Seethala R, Cash RE',
  'National Association of EMS Physicians Annual Meeting, Tampa, FL, January 2026'),
],
}

# ------------------------------------------------------------------- writing
WRITING_INTRO = {
"en": "Selected writing and spoken work from the past few years.",
"fr": "Choix d’écrits et de prises de parole de ces dernières années.",
"es": "Selección de escritos e intervenciones orales de los últimos años.",
"pt": "Seleção de escritos e intervenções orais dos últimos anos.",
}

# Reverse chronological: most recent first.
PIECES = {
"en": [("/oration.html", "May you keep dancing", "Officiant oration, Marriage of Nina Roussille and Ameet Kallarackal, Aix-en-Provence, France, 20 June 2026."),
       ("/gratitude.html", "The &lsquo;way&rsquo; of gratitude: A Daoist reflection on awe", "Morning Prayers, Appleton Chapel, Harvard University, 10 February 2025.")],
"fr": [("/oration.html", "May you keep dancing", "Allocution de célébrant, mariage de Nina Roussille et Ameet Kallarackal, Aix-en-Provence, France, 20 juin 2026."),
       ("/gratitude.html", "The &lsquo;way&rsquo; of gratitude: A Daoist reflection on awe", "Morning Prayers, Appleton Chapel, université Harvard, 10 février 2025.")],
"es": [("/oration.html", "May you keep dancing", "Alocución como oficiante, boda de Nina Roussille y Ameet Kallarackal, Aix-en-Provence, Francia, 20 de junio de 2026."),
       ("/gratitude.html", "The &lsquo;way&rsquo; of gratitude: A Daoist reflection on awe", "Morning Prayers, Appleton Chapel, Universidad Harvard, 10 de febrero de 2025.")],
"pt": [("/oration.html", "May you keep dancing", "Alocução como celebrante, casamento de Nina Roussille e Ameet Kallarackal, Aix-en-Provence, França, 20 de junho de 2026."),
       ("/gratitude.html", "The &lsquo;way&rsquo; of gratitude: A Daoist reflection on awe", "Morning Prayers, Appleton Chapel, Universidade Harvard, 10 de fevereiro de 2025.")],
}

ENGLISH_NOTE = {
"en": None,
"fr": "Ces textes sont disponibles en anglais uniquement.",
"es": "Estos textos están disponibles solo en inglés.",
"pt": "Estes textos estão disponíveis apenas em inglês.",
}

# ------------------------------------------------------------------ teaching
COURSES = {
"en": [("The American Soul", "Tufts University, 2018 &middot; with Hayley Oliver-Smith",
        "As more Americans identify as spiritual but not religious, this course asks what spirituality means in twenty-first-century America, and what that implies for civic life. Through contemplative practice in class, personal reflection, and discussion of primary texts, images, and stories, students examine their own assumptions about religion, spirituality, and contemplative traditions in the United States."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative, 2018 &middot; co-authored with Dr. Hilary Binda",
        "A syllabus written for the inaugural curriculum of the Tufts Prison Initiative, in which Tufts undergraduates took credit-bearing seminars alongside incarcerated men at Souza-Baranowski Correctional Center, a maximum-security prison in Lancaster, Massachusetts. The course explores confinement through three themes: education in prison, marginalized identities in captivity, and social movements to reform and abolish prisons.")],
"fr": [("The American Soul", "Université Tufts, 2018 &middot; avec Hayley Oliver-Smith",
        "Alors qu’un nombre croissant d’Américains se disent spirituels sans être religieux, ce cours interroge ce que signifie la spiritualité dans l’Amérique du XXI<sup>e</sup> siècle et ce qu’elle implique pour la vie civique. À travers la pratique contemplative en classe, la réflexion personnelle et la discussion de textes, d’images et de récits, les étudiants examinent leurs propres présupposés sur la religion, la spiritualité et les traditions contemplatives aux États-Unis."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative, 2018 &middot; coécrit avec la D<sup>re</sup> Hilary Binda",
        "Un programme rédigé pour le curriculum inaugural de la Tufts Prison Initiative, dans le cadre de laquelle des étudiants de Tufts ont suivi des séminaires crédités aux côtés d’hommes incarcérés au Souza-Baranowski Correctional Center, une prison de haute sécurité à Lancaster, dans le Massachusetts. Le cours aborde l’enfermement selon trois axes : l’éducation en prison, les identités marginalisées en captivité, et les mouvements sociaux visant à réformer et à abolir les prisons.")],
"es": [("The American Soul", "Universidad Tufts, 2018 &middot; con Hayley Oliver-Smith",
        "A medida que más estadounidenses se identifican como espirituales pero no religiosos, este curso pregunta qué significa la espiritualidad en la América del siglo XXI y qué implica para la vida cívica. Mediante la práctica contemplativa en clase, la reflexión personal y la discusión de textos, imágenes e historias, los estudiantes examinan sus propios supuestos sobre la religión, la espiritualidad y las tradiciones contemplativas en Estados Unidos."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative, 2018 &middot; coescrito con la Dra. Hilary Binda",
        "Un programa escrito para el currículo inaugural de la Tufts Prison Initiative, en el que estudiantes de Tufts cursaron seminarios con créditos junto a hombres encarcelados en el Souza-Baranowski Correctional Center, una prisión de máxima seguridad en Lancaster, Massachusetts. El curso explora el encierro a partir de tres ejes: la educación en prisión, las identidades marginadas en cautiverio y los movimientos sociales para reformar y abolir las prisiones.")],
"pt": [("The American Soul", "Universidade Tufts, 2018 &middot; com Hayley Oliver-Smith",
        "À medida que mais estadunidenses se identificam como espiritualizados, mas não religiosos, este curso pergunta o que significa espiritualidade nos Estados Unidos do século XXI e o que isso implica para a vida cívica. Por meio da prática contemplativa em sala, da reflexão pessoal e da discussão de textos, imagens e histórias, os estudantes examinam seus próprios pressupostos sobre religião, espiritualidade e tradições contemplativas nos Estados Unidos."),
       ("Prison Justice &amp; Education", "Tufts Prison Initiative, 2018 &middot; coescrito com a Dra. Hilary Binda",
        "Um programa escrito para o currículo inaugural da Tufts Prison Initiative, no qual estudantes de Tufts cursaram seminários com créditos ao lado de homens encarcerados no Souza-Baranowski Correctional Center, uma prisão de segurança máxima em Lancaster, Massachusetts. O curso explora o confinamento a partir de três eixos: a educação na prisão, as identidades marginalizadas em cativeiro e os movimentos sociais para reformar e abolir as prisões.")],
}

# ------------------------------------------------------------------ cv, contact
ARTS_TEXT = {
"en": 'I lead an arts community space in Cambridge. Learn more at <a class="link" href="https://farwellarts.com">Farwell Arts</a>.',
"fr": 'Je dirige un espace communautaire consacré aux arts à Cambridge. Pour en savoir plus : <a class="link" href="https://farwellarts.com">Farwell Arts</a>.',
"es": 'Dirijo un espacio comunitario dedicado a las artes en Cambridge. Más información en <a class="link" href="https://farwellarts.com">Farwell Arts</a>.',
"zh": '我在麻州劍橋主持一個藝術社群空間。更多資訊請見 <a class="link" href="https://farwellarts.com">Farwell Arts</a>。',
}

TEACHING_NOTE = {
"en": "Course syllabi available upon request.",
# "programme(s) de cours" keeps the wording consistent with how the Prison
# Justice syllabus is described in each language above.
"fr": "Les programmes de cours sont disponibles sur demande.",
"es": "Los programas de los cursos están disponibles a solicitud.",
"pt": "Os programas dos cursos estão disponíveis mediante solicitação.",
"zh": "課程大綱可依需求提供。",
}

TUTORING = {
"en": ("Tutoring",
 "I also accept a limited number of clients for tutoring in the following areas:",
 [("Test preparation", ["MCAT and general standardized test strategy and planning"]),
  ("Natural sciences", ["Inorganic and organic chemistry",
                        "Physics (typical first-year university sequence)",
                        "Biology (molecular, cellular, organismic, evolutionary)",
                        "Biochemistry"]),
  ("Humanities", ["Creative non-fiction", "Narrative non-fiction", "Speechwriting",
                  "Applications for graduate school and fellowships"])]),

"fr": ("Cours particuliers",
 "J’accepte également un nombre limité d’élèves en cours particuliers dans les domaines suivants :",
 [("Préparation aux examens", ["MCAT et stratégie générale de préparation aux tests standardisés"]),
  ("Sciences", ["Chimie inorganique et organique",
                "Physique (première année universitaire)",
                "Biologie (moléculaire, cellulaire, organismique, évolutive)",
                "Biochimie"]),
  ("Sciences humaines", ["Non-fiction créative", "Non-fiction narrative",
                         "Rédaction de discours",
                         "Candidatures aux études supérieures et aux bourses"])]),

"es": ("Tutorías",
 "También acepto un número limitado de alumnos para tutorías en las siguientes áreas:",
 [("Preparación de exámenes", ["MCAT y estrategia general para exámenes estandarizados"]),
  ("Ciencias naturales", ["Química inorgánica y orgánica",
                          "Física (primer curso universitario)",
                          "Biología (molecular, celular, organísmica, evolutiva)",
                          "Bioquímica"]),
  ("Humanidades", ["No ficción creativa", "No ficción narrativa", "Redacción de discursos",
                   "Solicitudes de posgrado y becas"])]),

"zh": ("個別指導",
 "我也接受少量學生進行個別指導，領域如下：",
 [("考試準備", ["MCAT 及標準化測驗的整體策略與規劃"]),
  ("自然科學", ["無機化學與有機化學",
              "物理（大學一年級課程）",
              "生物學（分子、細胞、個體、演化）",
              "生物化學"]),
  ("人文", ["創意非虛構寫作", "敘事非虛構寫作", "演講稿寫作",
           "研究所與獎助學金申請"])]),
}

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



# ------------------------------------------------- Traditional Chinese (zh-Hant)
LANGS.append("zh")

HREFLANG = {"en": "en", "fr": "fr", "es": "es", "pt": "pt", "zh": "zh-Hant"}
LANG_LABEL = {"en": "EN", "fr": "FR", "es": "ES", "pt": "PT", "zh": "中文"}

# On the Chinese pages his Chinese name leads; elsewhere the romanisation does.
NAME = {l: "Wylie Chang" for l in LANGS}
NAME["zh"] = "張振曦"

# Latin pages lead with the romanisation; the Chinese page leads with 張振曦.
_LATIN = 'Wylie Daniel<br>Chen-hsi Chang<span class="name-zh">張振曦</span>'
MASTHEAD = {l: _LATIN for l in LANGS}
MASTHEAD["zh"] = '<span class="name-zh lead">張振曦</span>Wylie Daniel<br>Chen-hsi Chang'

NAV["zh"] = [("research", "研究"), ("writing", "文章"),
             ("teaching", "教學"), ("arts", "藝術"), ("cv", "履歷"), ("contact", "聯絡")]

for _k, _v in {
    "research": "研究", "writing": "文章", "teaching": "教學", "arts": "藝術",
    "cv": "履歷", "contact": "聯絡", "publications": "著作",
    "journal": "期刊論文", "progress": "進行中", "conference": "研討會發表",
}.items():
    TITLES[_k]["zh"] = _v

BIO["zh"] = [
 "我是一名緊急醫療技術員（EMT）與研究員，目前參與麻省總醫院急診醫學部緊急醫療服務組的研究工作。我研究病人與臨床人員如何在不確定與緊急的情況下共同做出決定。",
 "我特別關注精神科急症，以及其中浮現的能動性、權威與責任等問題。",
 "我的其他主要興趣包括機構治理、科學與醫學史，以及醫療機構在公民生活與民主中的角色。",
 "此前，我曾領導多個公民組織，包括 Democracy House、Register2Vote.org 與 Lead for America。我在塔夫茨大學主修哲學、政治學與經濟學，並在哈佛大學修習理科課程。",
 "我住在麻州劍橋。",
]

PHOTO_ALT["zh"] = "黃昏時分，一群人坐在矮牆上仰望天空，背景是連綿的山丘。"

RESEARCH["zh"] = [
 "我的主要研究方向是急診醫學中的共享決策，特別是精神科急症，以及那些因決策能力不確定、醫病之間尚未建立信任關係而使一般審議條件受到干擾的情境。我關心病人與臨床人員在這些條件下如何建立可行的合作方式，以及信任、權威與責任如何在急性照護中被協商。",
 "我援引共享決策的臨床模型、Anselm Strauss 的「協商秩序」概念，以及公民組織與倡議工作的實踐，探討臨床人員如何在危機中保護病人的能動性。",
 "我也持續研究緊急醫療服務，探討分權化的系統，以及授予派遣人員、臨床人員與機構的裁量權，如何造成照護方式與治療結果的差異。",
 "我工作的另一個面向，是醫療場域中的公民參與。",
]

PROFILES["zh"] = '我的同儕審查論文可於 <a class="link" href="https://scholar.google.com/citations?user=UE97hJIAAAAJ&amp;hl=en">Google Scholar</a> 個人頁面查閱。我的 ORCID 為 <a class="link" href="https://orcid.org/0009-0002-3935-5418">0009-0002-3935-5418</a>。'

WRITING_INTRO["zh"] = "近年文章與演講選錄。"
ENGLISH_NOTE["zh"] = "以下文稿僅有英文版本。"

PIECES["zh"] = [
 ("/oration.html", "May you keep dancing",
  "證婚致詞，Nina Roussille 與 Ameet Kallarackal 的婚禮，法國普羅旺斯艾克斯，2026 年 6 月 20 日。"),
 ("/gratitude.html", "The &lsquo;way&rsquo; of gratitude: A Daoist reflection on awe",
  "Morning Prayers，哈佛大學 Appleton Chapel，2025 年 2 月 10 日。"),
]

COURSES["zh"] = [
 ("The American Soul", "塔夫茨大學，2018 &middot; 與 Hayley Oliver-Smith 合作",
  "隨著愈來愈多美國人自認「有靈性但不屬於任何宗教」，本課程探問：在二十一世紀的美國，靈性意味著什麼，又對公民生活有何影響。透過課堂上的靜觀練習、個人省思，以及對文本、影像與故事的討論，學生檢視自己對於美國宗教、靈性與靜觀傳統的既有假設。"),
 ("Prison Justice &amp; Education", "塔夫茨監獄計畫，2018 &middot; 與 Hilary Binda 博士合著",
  "這份課程大綱是為塔夫茨監獄計畫（Tufts Prison Initiative）的首屆課程所撰寫。在該計畫中，塔夫茨大學的大學部學生與麻州蘭卡斯特 Souza-Baranowski 懲教中心（一所最高戒護等級的監獄）的受刑人一同修習可採計學分的研討課。本課程從三個主題探討監禁：獄中教育、囚禁中的邊緣身分，以及改革與廢除監獄的社會運動。"),
]

CV_TEXT["zh"] = "我的履歷可依需求提供。"
CONTACT_LEAD["zh"] = "歡迎透過以下方式與我聯絡："


# --------------------------------------------------------------------- render
def head(lang, page, title):
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="https://wylie-chang.com%s%s">'
        % (HREFLANG[l], base(l), "" if page == "index" else page + ".html")
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
""" % (HREFLANG[lang], title, alts, "" if page == "index" else page + ".html")


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
        langs.append('<a href="%s"%s lang="%s">%s</a>' % (target, cur, HREFLANG[l], LANG_LABEL[l]))
    home = ' aria-current="page"' if page == "index" else ''
    return """  <header>
    <a class="name" href="%s"%s>%s</a>
    <nav class="nav">
%s
    </nav>
    <p class="langs">%s</p>
  </header>
""" % (base(lang), home, MASTHEAD[lang], "\n".join(items), "".join(langs))


def entry_html(link, title, authors, source, award=None):
    t = ('<a class="title title-link" href="%s">%s</a>' % (link, title)) if link \
        else ('<span class="title">%s</span>' % title)
    out = ['      <div class="entry">', "        " + t,
           '        <span class="authors">%s</span>' % authors]
    if source:
        out.append('        <span class="source">%s</span>' % source)
    if award:
        out.append('        <span class="award">%s</span>' % award)
    out.append("      </div>")
    return "\n".join(out)


def build_page(lang, page):
    L = lambda k: TITLES[k][lang]
    stem = NAME[lang] if page == "index" else "%s &mdash; %s" % (L(page), NAME[lang])
    out = [head(lang, page, stem), sidebar(lang, page)]

    if page == "index":
        out.append('  <main class="main--home">\n    <div class="column">')
        out.append('      <figure class="photo-col">\n        <img class="photo" src="/photo.jpg" width="800" height="1067" alt="%s">\n      </figure>' % PHOTO_ALT[lang])
        for para in BIO[lang]:
            out.append("      <p>%s</p>" % para)
        out.append("    </div>\n  </main>")

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
        out.append('      <p class="profiles">%s</p>' % TEACHING_NOTE[lang])
        head_, intro, areas = TUTORING[lang]
        out.append('\n      <div class="tutoring">')
        out.append('        <h2 class="group">%s</h2>' % head_)
        out.append('        <p>%s</p>' % intro)
        out.append('        <ul class="areas">')
        for aname, items in areas:
            out.append('          <li><span class="area-name">%s</span>' % aname)
            out.append('            <ul>')
            for it in items:
                out.append('              <li>%s</li>' % it)
            out.append('            </ul>')
            out.append('          </li>')
        out.append('        </ul>\n      </div>')
        out.append("    </div>\n  </main>")

    elif page == "arts":
        out.append('  <main>\n    <h1 class="label">%s</h1>\n    <div class="column">\n      <p>%s</p>\n    </div>\n  </main>' % (L("arts"), ARTS_TEXT[lang]))

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
