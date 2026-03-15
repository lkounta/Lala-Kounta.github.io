# ──────────────────────────────────────────────────────────────
# about.py  —  Edit this file to update the About Me section
# Then run:  python3 build.py
# ──────────────────────────────────────────────────────────────

HERO = {
    "badge":       "Research Associate — Michigan State University",
    "name":        "Dr. Lala Kounta",
    "subtitle":    "Ocean & Climate Scientist | Climate Extremes & Solar Radiation Modification",
    "affiliation": "Dept. of Integrative Biology — Institute for Biodiversity, Ecology, Evolution & Macrosystems",
    "email":       "kountala@msu.edu",
    "orcid":       "https://orcid.org/0000-0002-0239-0212",
    "linkedin":    "https://www.linkedin.com/in/lala-kounta",
    "cv_file":     "files/CV_Dr_Lala_Kounta.pdf",
}

# Plain text — use real Unicode characters (—, ', &, etc.)
ABOUT_PARAGRAPHS = [
    (
        "My research program is centered on understanding the ocean's circulation and its "
        "response to large-scale atmospheric variability. I study abiotic extreme events and "
        "their drivers across historical, present, and future climates, and I explore the "
        "potential of climate intervention strategies—such as solar radiation modification and "
        "marine cloud brightening—to mitigate the impacts of global warming and evaluate their "
        "effects on natural systems. In all of my disciplinary and interdisciplinary work, I "
        "advance understanding of the physical processes underlying climate change across "
        "scenarios in order to improve predictions about climate change impacts."
    ),
    (
        "I hold a master's degree in Physics and a master's degree in Meteorology, Oceanography, "
        "and Land Management, along with dual PhDs in Environmental Sciences (Sorbonne University, "
        "Paris) and Physical Oceanography and Climate Sciences (Cheikh Anta Diop University, "
        "Dakar). My foundational expertise lies in the dynamics of the Canary Current Upwelling "
        "System and the West African Monsoon. Since joining Michigan State University in 2022 as "
        "an African Futures Research Leadership Fellow, my work has expanded to global climate "
        "change, geoengineering impacts, and interdisciplinary ecology."
    ),
    (
        "Looking ahead, I aim to serve as a bridge between world-class Earth System Models and "
        "the communities that need robust, decision-relevant information on weather and climate "
        "risks—translating model output and observational datasets into co-designed, actionable "
        "indicators that inform adaptation and policy decisions, ultimately supporting global "
        "efforts to mitigate climate change and protect biodiversity."
    ),
]

# Each card: icon, label, and body (HTML allowed in body for links / <br>)
INFO_CARDS = [
    {
        "icon":  "📍",
        "label": "Location",
        "body":  "East Lansing, Michigan, USA<br>288 Farm Lane, MSU",
    },
    {
        "icon":  "🎓",
        "label": "Education",
        "body":  (
            "PhD Environmental Sciences, Sorbonne Univ. (2019)<br>"
            "PhD Physical Oceanography &amp; Climate, UCAD (2019)<br>"
            "MS Meteorology &amp; Oceanography, UCAD (2013)"
        ),
    },
    {
        "icon":  "🔬",
        "label": "Research Focus",
        "body":  (
            "Ocean dynamics &middot; climate extremes &middot; solar geoengineering "
            "&middot; marine heatwaves &middot; West African upwelling "
            "&middot; stakeholder-relevant data products"
        ),
    },
    {
        "icon":  "💻",
        "label": "Technical Skills",
        "body":  (
            "Python &middot; R &middot; MATLAB &middot; SQL &middot; CDO "
            "&middot; NetCDF &middot; HPC &middot; Cloud Computing "
            "&middot; Machine Learning &middot; GIS"
        ),
    },
    {
        "icon":  "🌍",
        "label": "Affiliations",
        "body":  (
            "African Meteorological Society &middot; Society for Women in Marine Science "
            "&middot; American Geosciences Union &middot; Assoc. of Climate Change Officers"
        ),
    },
    {
        "icon":  "📰",
        "label": "Media Coverage",
        "body":  (
            "<em>El Pa&iacute;s</em> (2022) &middot; Future Climate for Africa News (2019) "
            "&middot; IRD Talents (2017) &middot; African Women feature (2025)"
        ),
    },
]
