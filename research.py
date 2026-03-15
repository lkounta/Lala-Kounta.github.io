# ──────────────────────────────────────────────────────────────
# research.py  —  Edit this file to update the Research section
# Then run:  python3 build.py
# ──────────────────────────────────────────────────────────────
# Each project dict:
#   status      "current" | "past"
#   funder      Name of funding agency (shown as a tag)
#   role        Your role (shown as a tag)
#   years       Display string, e.g. "2025–2026"
#   amount      Optional, e.g. "$264,433"   (omit or set to "" to hide)
#   title       Project title
#   description Plain text description (& will be auto-escaped)
# ──────────────────────────────────────────────────────────────

SECTION_DESC = (
    "I investigate how large-scale ocean–atmosphere dynamics and climate intervention "
    "strategies shape extreme events, with a focus on translating Earth System Model "
    "outputs into actionable, decision-relevant data products for researchers, resource "
    "managers, and policymakers across the globe."
)

PROJECTS = [
    {
        "status":  "current",
        "funder":  "Environmental Defense Fund",
        "role":    "co-Principal Investigator",
        "years":   "2025–2026",
        "amount":  "$264,433",
        "title":   "Solar Radiation Modification, Extreme Events & Biotic Interactions",
        "description": (
            "This project asks how solar radiation modification (SRM) will alter the frequency "
            "and co-occurrence of multi-variable extreme events and, in turn, affect ecological "
            "structure and function. Building on Dr. Kounta's extreme event detection framework, "
            "the team develops analysis-ready indicators across temperature, moisture, "
            "precipitation, UV, ozone, pH, and dissolved oxygen that inform both the risks and "
            "benefits of future mitigation scenarios. Co-investigators include Phoebe Zarnetske, "
            "Alisha Shah, Kelly Kasper, and Lifeng Luo."
        ),
    },
    {
        "status":  "current",
        "funder":  "World Academy of Sciences / UNESCO",
        "role":    "Principal Investigator",
        "years":   "2024–present",
        "amount":  "$68,390",
        "title":   "Monitoring the Senegalese Coast for Sustainable Oceans",
        "description": (
            "Led by Dr. Kounta as PI, this UNESCO-TWAS program establishes long-term monitoring "
            "of the Senegalese coast to support sustainable ocean management. The program also "
            "includes a financial support and mentoring component for top-performing female "
            "students in marine sciences at Cheikh Anta Diop University, implemented through "
            "IUPA to strengthen gender equity and academic excellence in West Africa."
        ),
    },
    {
        "status":  "current",
        "funder":  "National Science Foundation",
        "role":    "Research Scientist",
        "years":   "2023–present",
        "amount":  "",
        "title":   "Potential Ecological Impacts of Climate Intervention via Solar Radiation Modification",
        "description": (
            "Using a big-data approach on CESM output from two SAI scenarios (ARISE-SAI-1.0 and "
            "ARISE-SAI-1.5) and a baseline SSP2-4.5, this project quantifies how stratospheric "
            "aerosol injection alters marine heatwave (MHW) frequency, maximum intensity, and "
            "duration across global marine provinces over historical (1990–2009), present "
            "(2015–2034), and future (2050–2069) periods. Results show SAI reduces global average "
            "MHW severity but with pronounced regional heterogeneity—highlighting the need for "
            "region-specific impact assessments and equitable governance frameworks."
        ),
    },
    {
        "status":  "past",
        "funder":  "Lenfest Ocean Program",
        "role":    "Key Personnel",
        "years":   "2023–2024",
        "amount":  "",
        "title":   "Inclusive Management of the Cayar and Ufoyaal Kassa-Bandial Marine Protected Areas (Senegal)",
        "description": (
            "Research conducted in partnership with local communities and fisheries stakeholders "
            "to inform inclusive, equitable management of two ecologically critical marine "
            "protected areas in Senegal. The project produced evidence-based recommendations for "
            "conservation planning and governance of these coastal zones."
        ),
    },
    {
        "status":  "past",
        "funder":  "IBEEM, Michigan State University",
        "role":    "co-Principal Investigator",
        "years":   "2022–2023",
        "amount":  "$75,000",
        "title":   "Environmental Variability and Life Histories of Global Ecological Communities",
        "description": (
            "This interdisciplinary project characterizes how interannual and seasonal temperature "
            "variability shapes the life histories of the world's birds. Results published in "
            "Ecology Letters (Youngflesh et al., 2025) show that species experiencing high "
            "inter-annual variability tend toward a slower pace of life, while high intra-annual "
            "(seasonal) variability produces the opposite effect. Dr. Kounta's climate science "
            "and HPC expertise was integral to quantifying appropriate spatiotemporal climate measures."
        ),
    },
    {
        "status":  "past",
        "funder":  "Future Climate for Africa",
        "role":    "co-Principal Investigator",
        "years":   "2017–2019",
        "amount":  "",
        "title":   "SCUS-2050: Exploring the Future of the Southern Canary Upwelling System",
        "description": (
            "The southern Canary Upwelling System (SCUS) off Mauritania, Senegal, and Guinea is "
            "among the world's most productive oceanic regions and a critical food and livelihood "
            "source for West African coastal communities. This project used numerical models and "
            "reanalysis data to project future changes to the SCUS under climate change scenarios, "
            "providing foundational insights into the vulnerability of marine ecosystems in the region."
        ),
    },
]
