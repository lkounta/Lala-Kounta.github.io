# ──────────────────────────────────────────────────────────────
# cv.py  —  Edit this file to update the CV section
# Then run:  python3 build.py
# ──────────────────────────────────────────────────────────────

CV_UPDATED = "March 2026"   # ← change this when you upload a new PDF

# ── Academic Appointments ────────────────────────────────────
# Each entry: years, title, org
APPOINTMENTS = [
    {
        "years": "2024–now",
        "title": "Research Associate",
        "org":   "IBEEM, Dept. of Integrative Biology, Michigan State University",
    },
    {
        "years": "2023–2024",
        "title": "Post-doctoral Fellow",
        "org":   "IBEEM, Michigan State University",
    },
    {
        "years": "2022–2023",
        "title": "African Futures Research Leadership Fellow",
        "org":   "Alliance for African Partnership, MSU",
    },
    {
        "years": "2021–2022",
        "title": "Visiting Scientist",
        "org":   "Oceanic Platform of the Canary Islands (PLOCAN), Spain",
    },
    {
        "years": "2020–2022",
        "title": "Lecturer",
        "org":   "Cheikh Anta Diop University & Gaston Berger University, Senegal",
    },
    {
        "years": "2020–",
        "title": "Visiting Scientist",
        "org":   "African Institute of Mathematical Sciences (AIMS), Rwanda",
    },
]

# ── Education ────────────────────────────────────────────────
# Each entry: year, degrees (list of {title, org})
EDUCATION = [
    {
        "year": "2019",
        "degrees": [
            {"title": "PhD in Environmental Sciences",
             "org":   "Sorbonne University, Paris, France"},
            {"title": "PhD in Physical Oceanography & Climate Sciences",
             "org":   "Cheikh Anta Diop University, Dakar, Senegal"},
        ],
    },
    {
        "year": "2013",
        "degrees": [
            {"title": "MS in Meteorology, Oceanography & Land Management",
             "org":   "UCAD, Dakar, Senegal"},
        ],
    },
    {
        "year": "2012",
        "degrees": [
            {"title": "MS in Physics",
             "org":   "UCAD, Dakar, Senegal"},
        ],
    },
    {
        "year": "2011",
        "degrees": [
            {"title": "BS in Physics and Chemistry",
             "org":   "UCAD, Dakar, Senegal"},
        ],
    },
]

# ── Awards & Grants ──────────────────────────────────────────
# Each entry: name (HTML ok for <strong>), years, amount
GRANTS = [
    {
        "name":   "<strong>Environmental Defense Fund</strong> (co-PI) — 2025–2026",
        "amount": "$264,433",
    },
    {
        "name":   "<strong>World Academy of Sciences / UNESCO</strong> (PI) — 2025–2026",
        "amount": "$68,390",
    },
    {
        "name":   "<strong>IBEEM, MSU</strong> Interdisciplinary Project (co-PI) — 2022–2023",
        "amount": "$75,000",
    },
    {
        "name":   "<strong>African Futures Research Leadership Fellowship</strong>, MSU — 2022–2023",
        "amount": "$50,000",
    },
    {
        "name":   "<strong>Faculty for the Future Program Fellowship</strong> — 2022–2024",
        "amount": "$60,000",
    },
]

# ── Publications ─────────────────────────────────────────────
# Each entry: html (full citation as HTML, use <strong> for your name,
#             <em> for journal, <a> for DOI link)
PUBLICATIONS = [
    (
        '<strong>Kounta, L.</strong> et al. (under review). Climate Intervention through '
        'Stratospheric Aerosol Injection may partially mitigate marine heatwaves. '
        '<a href="https://doi.org/10.22541/essoar.176442822.27571009/v3" target="_blank">Preprint &#8599;</a>'
    ),
    (
        'Youngflesh, C., Kapsar, K., Uscanga, A., Williams, P.J., Doser, J.W., '
        '<strong>Kounta, L.</strong> &amp; Zarnetske, P.L. (2025). Environmental Variability '
        'Shapes Life History of the World\'s Birds. <em>Ecology Letters</em>, 28:e70077. '
        '<a href="https://doi.org/10.1111/ele.70077" target="_blank">DOI &#8599;</a>'
    ),
    (
        '<strong>Kounta, L.</strong>, Capet, X., Jouanno, J., Kolodziejczyk, N., Sow, B., '
        '&amp; Gaye, A.T. (2018). A Model Perspective on the Dynamics of the Shadow Zone of '
        'the Eastern Tropical North Atlantic. <em>Ocean Science</em>, 14(5), 971–997. '
        '<a href="https://doi.org/10.5194/os-14-971-2018" target="_blank">DOI &#8599;</a>'
    ),
    (
        'Ndoye, S., Capet, X., Estrade, P., Machu, E., <strong>Kounta, L.</strong> et al. '
        '(2018). A Numerical Modeling Study of the Southern Senegal Upwelling Shelf. '
        '<em>African Journal of Environmental Science and Technology</em>, 12(12), 487–500.'
    ),
    (
        'Hermes, J., Reason, C., <strong>Kounta, L.</strong> et al. (2021). Policy Brief 10: '
        'Extremes, Abrupt Changes and Managing Risks. '
        '<a href="https://www.researchgate.net/publication/363915007" target="_blank">Link &#8599;</a>'
    ),
]

# ── Teaching ─────────────────────────────────────────────────
# Each entry: years, title, org
TEACHING = [
    {
        "years": "2025",
        "title": "Spatial Ecology (Lab Instructor)",
        "org":   "College of Natural Science, MSU",
    },
    {
        "years": "2018–2024",
        "title": "Probability & Statistics",
        "org":   "École Supérieure Polytechnique / UCAD, Senegal",
    },
    {
        "years": "2018–2022",
        "title": "Physical Oceanography",
        "org":   "École Supérieure Polytechnique / UCAD & Gaston Berger University",
    },
    {
        "years": "2019–2022",
        "title": "Ocean Modelling & Thermodynamics",
        "org":   "IUPA, UCAD; École Supérieure des Génies des Procédés, Senegal",
    },
    {
        "years": "2020–2022",
        "title": "Coastal Climate & Climate Variability",
        "org":   "Faculté des Lettres et Sciences Humaines, UCAD",
    },
]

# ── Technical Skills ─────────────────────────────────────────
SKILLS = [
    "Python", "R", "MATLAB", "SQL", "CDO", "NetCDF",
    "HPC", "Cloud Computing", "Machine Learning", "GIS",
    "Numerical Modeling", "Big Data Analysis",
    "Data Visualization", "Bias Adjustment", "Statistical Downscaling",
]
