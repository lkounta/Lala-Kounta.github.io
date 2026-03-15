#!/usr/bin/env python3
"""
build.py — Render index.html from content files.

Usage:
    python3 build.py

Edit about.py, research.py, or cv.py to update content,
then run this script to regenerate index.html.
"""
import html as _html
from about    import HERO, ABOUT_PARAGRAPHS, INFO_CARDS
from research import SECTION_DESC, PROJECTS
from cv       import (CV_UPDATED, APPOINTMENTS, EDUCATION,
                      GRANTS, PUBLICATIONS, TEACHING, SKILLS)

# ── helpers ──────────────────────────────────────────────────

def h(text):
    """Escape plain text for safe HTML output."""
    return _html.escape(str(text))

def paras(paragraphs):
    return "\n".join(f"      <p>{h(p)}</p>" for p in paragraphs)

def cv_entries(entries):
    rows = []
    for e in entries:
        rows.append(
            f'        <div class="cv-entry">'
            f'<div class="cv-year">{h(e["years"])}</div>'
            f'<div>'
            f'<span class="cv-title">{h(e["title"])}</span>'
            f'<span class="cv-org">{h(e["org"])}</span>'
            f'</div></div>'
        )
    return "\n".join(rows)

def education_entries(entries):
    rows = []
    for e in entries:
        inner = "".join(
            f'<span class="cv-title">{h(d["title"])}</span>'
            f'<span class="cv-org">{h(d["org"])}</span>'
            for d in e["degrees"]
        )
        rows.append(
            f'        <div class="cv-entry">'
            f'<div class="cv-year">{h(e["year"])}</div>'
            f'<div>{inner}</div></div>'
        )
    return "\n".join(rows)

def project_cards(projects):
    cards = []
    for p in projects:
        css   = "project-card" + (" past" if p["status"] == "past" else "")
        s_tag = ("past" if p["status"] == "past" else "current")
        s_lbl = ("Completed" if p["status"] == "past" else "Current")
        amt   = (f'&nbsp;|&nbsp; {h(p["amount"])}' if p.get("amount") else "")
        cards.append(f"""
      <div class="{css}">
        <div class="project-meta">
          <span class="tag {s_tag}">{s_lbl}</span>
          <span class="tag funder">{h(p["funder"])}</span>
          <span class="tag role">{h(p["role"])}</span>
          <span class="project-year">{h(p["years"])}{amt}</span>
        </div>
        <h3>{h(p["title"])}</h3>
        <p>{h(p["description"])}</p>
      </div>""")
    return "\n".join(cards)

def info_cards(cards):
    items = []
    for c in cards:
        items.append(f"""
      <div class="info-card">
        <span class="info-icon">{c["icon"]}</span>
        <div>
          <div class="info-label">{h(c["label"])}</div>
          <div class="info-body">{c["body"]}</div>
        </div>
      </div>""")
    return "\n".join(items)

def grant_items(grants):
    items = []
    for g in grants:
        items.append(
            f'          <div class="award-item">'
            f'<div class="award-name">{g["name"]}</div>'
            f'<div class="award-amt">{h(g["amount"])}</div>'
            f'</div>'
        )
    return "\n".join(items)

def pub_items(pubs):
    items = []
    for p in pubs:
        items.append(f"          <li>{p}</li>")
    return "\n".join(items)

def skill_pills(skills):
    return "\n".join(
        f'          <span class="skill-pill">{h(s)}</span>' for s in skills
    )

# ── CSS (unchanged from original) ────────────────────────────

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --navy:        #0a2342;
      --teal:        #1a7a8a;
      --teal-light:  #e6f4f6;
      --gold:        #c8963e;
      --bg:          #f5f6f8;
      --card:        #ffffff;
      --text:        #1a1a2e;
      --muted:       #5a6278;
      --border:      #dde1e9;
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Georgia', 'Times New Roman', serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.75;
      font-size: 16px;
    }

    /* ── NAV ── */
    nav { position: sticky; top: 0; background: var(--navy); z-index: 100; }
    nav .nav-inner {
      max-width: 1000px; margin: 0 auto;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 1.5rem;
    }
    .nav-name {
      color: #fff; font-size: 0.9rem; font-weight: bold;
      letter-spacing: 0.04em; padding: 1rem 0; font-family: sans-serif;
    }
    nav ul { display: flex; list-style: none; gap: 0.2rem; }
    nav a {
      display: block; padding: 1rem 1rem;
      color: rgba(255,255,255,0.72); text-decoration: none;
      font-family: sans-serif; font-size: 0.8rem;
      text-transform: uppercase; letter-spacing: 0.09em; transition: color 0.2s;
    }
    nav a:hover { color: #fff; }

    /* ── HERO ── */
    .hero {
      background: linear-gradient(135deg, var(--navy) 0%, #14496b 100%);
      color: #fff; padding: 5rem 1.5rem 4rem; text-align: center;
    }
    .hero-badge {
      display: inline-block;
      background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.25);
      border-radius: 100px; padding: 0.3rem 1rem;
      font-family: sans-serif; font-size: 0.75rem;
      letter-spacing: 0.1em; text-transform: uppercase;
      margin-bottom: 1.5rem; color: rgba(255,255,255,0.85);
    }
    .hero h1 { font-size: 2.8rem; font-weight: normal; letter-spacing: 0.01em; margin-bottom: 0.5rem; }
    .hero h1 em { color: var(--gold); font-style: normal; }
    .hero .subtitle {
      font-family: sans-serif; font-size: 1rem;
      color: rgba(255,255,255,0.75); max-width: 620px; margin: 0 auto 0.5rem;
    }
    .hero .affil {
      font-family: sans-serif; font-size: 0.85rem;
      color: rgba(255,255,255,0.55); margin-bottom: 2rem;
    }
    .hero-links { display: flex; justify-content: center; gap: 0.8rem; flex-wrap: wrap; }
    .hero-link {
      display: inline-flex; align-items: center; gap: 0.4rem;
      padding: 0.5rem 1.2rem; border-radius: 6px;
      font-family: sans-serif; font-size: 0.82rem; font-weight: 600;
      text-decoration: none; transition: opacity 0.2s, transform 0.15s;
    }
    .hero-link:hover { opacity: 0.85; transform: translateY(-1px); }
    .hero-link.primary { background: var(--gold); color: #fff; }
    .hero-link.outline { border: 1.5px solid rgba(255,255,255,0.5); color: #fff; }
    .hero-link.cv-btn  { background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.5); color: #fff; }

    /* ── SECTIONS ── */
    .section-wrap { max-width: 1000px; margin: 0 auto; padding: 4.5rem 1.5rem; }
    .section-wrap + .section-wrap { border-top: 1px solid var(--border); }
    .alt-bg { background: #fff; }
    .section-label {
      display: inline-block;
      font-family: sans-serif; font-size: 0.7rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.14em;
      color: var(--teal); margin-bottom: 0.35rem;
    }
    h2 { font-size: 1.9rem; font-weight: normal; color: var(--navy); }
    .section-desc { margin-top: 0.5rem; color: var(--muted); font-size: 0.95rem; max-width: 680px; }
    .section-header {
      margin-bottom: 2.5rem;
      display: flex; align-items: flex-end; justify-content: space-between;
      flex-wrap: wrap; gap: 1rem;
    }
    .section-header-text { flex: 1; }

    .dl-cv-btn {
      display: inline-flex; align-items: center; gap: 0.4rem;
      padding: 0.5rem 1.1rem; border-radius: 6px;
      background: var(--teal); color: #fff;
      font-family: sans-serif; font-size: 0.8rem; font-weight: 600;
      text-decoration: none; white-space: nowrap;
      transition: opacity 0.2s, transform 0.15s; flex-shrink: 0;
    }
    .dl-cv-btn:hover { opacity: 0.85; transform: translateY(-1px); }
    .cv-updated { font-family: sans-serif; font-size: 0.72rem; color: var(--muted); margin-top: 0.3rem; }

    /* ── ABOUT ── */
    .about-body { margin-bottom: 2.5rem; }
    .about-body p { font-size: 1.02rem; line-height: 1.85; color: var(--text); }
    .about-body p + p { margin-top: 1.1rem; }
    .cards-grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem;
    }
    .info-card {
      background: var(--card); border: 1px solid var(--border);
      border-radius: 10px; padding: 1.2rem 1.4rem;
      display: flex; gap: 0.9rem; align-items: flex-start;
    }
    .info-icon { font-size: 1.25rem; flex-shrink: 0; margin-top: 0.1rem; }
    .info-label {
      font-family: sans-serif; font-size: 0.68rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.1em;
      color: var(--muted); margin-bottom: 0.25rem;
    }
    .info-body { font-size: 0.88rem; line-height: 1.55; }
    .info-body a { color: var(--teal); text-decoration: none; }
    .info-body a:hover { text-decoration: underline; }

    /* ── RESEARCH ── */
    .projects-list { display: flex; flex-direction: column; gap: 1.6rem; }
    .project-card {
      background: var(--card); border: 1px solid var(--border);
      border-left: 4px solid var(--teal);
      border-radius: 0 10px 10px 0; padding: 1.5rem 1.7rem;
    }
    .project-card.past { border-left-color: #8fa8be; }
    .project-meta { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-bottom: 0.65rem; align-items: center; }
    .tag {
      display: inline-block; font-family: sans-serif;
      font-size: 0.68rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.07em;
      padding: 0.18rem 0.55rem; border-radius: 4px;
    }
    .tag.current { background: var(--teal-light); color: var(--teal); }
    .tag.past    { background: #eef0f4; color: #6b7280; }
    .tag.funder  { background: #fdf3e4; color: #a07228; }
    .tag.role    { background: #eef0f4; color: var(--navy); }
    .project-year { font-family: sans-serif; font-size: 0.78rem; color: var(--muted); margin-left: auto; }
    .project-card h3 { font-size: 1.08rem; color: var(--navy); margin-bottom: 0.5rem; font-style: italic; }
    .project-card p  { font-size: 0.92rem; color: var(--muted); line-height: 1.7; }

    /* ── CV ── */
    .cv-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem 3rem; }
    .cv-block h3 {
      font-family: sans-serif; font-size: 0.68rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.12em; color: var(--teal);
      border-bottom: 1px solid var(--border); padding-bottom: 0.4rem; margin-bottom: 1.2rem;
    }
    .cv-entry {
      display: grid; grid-template-columns: 76px 1fr;
      gap: 0.4rem 0.9rem; margin-bottom: 1.1rem; font-size: 0.87rem;
    }
    .cv-year  { color: var(--gold); font-family: sans-serif; font-weight: 700; font-size: 0.78rem; padding-top: 0.1rem; line-height: 1.4; }
    .cv-title { font-weight: bold; color: var(--navy); display: block; }
    .cv-org   { color: var(--muted); display: block; line-height: 1.4; }
    .pub-list { list-style: none; display: flex; flex-direction: column; gap: 0.9rem; }
    .pub-list li { font-size: 0.86rem; line-height: 1.65; padding-left: 0.9rem; border-left: 2px solid var(--border); }
    .pub-list li strong { color: var(--navy); }
    .pub-list li a { color: var(--teal); text-decoration: none; font-size: 0.8rem; }
    .pub-list li a:hover { text-decoration: underline; }
    .award-list { display: flex; flex-direction: column; gap: 0.75rem; }
    .award-item { display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; font-size: 0.87rem; }
    .award-name { color: var(--text); flex: 1; line-height: 1.4; }
    .award-amt  { font-family: sans-serif; font-weight: 700; color: var(--teal); white-space: nowrap; font-size: 0.8rem; }
    .skills-wrap { display: flex; flex-wrap: wrap; gap: 0.45rem; }
    .skill-pill {
      background: var(--teal-light); color: var(--teal);
      border-radius: 100px; padding: 0.22rem 0.75rem;
      font-family: sans-serif; font-size: 0.78rem; font-weight: 600;
    }

    /* ── FOOTER ── */
    footer {
      background: var(--navy); color: rgba(255,255,255,0.45);
      text-align: center; padding: 2rem 1rem;
      font-family: sans-serif; font-size: 0.78rem;
    }
    footer a { color: rgba(255,255,255,0.65); text-decoration: none; }
    footer a:hover { color: #fff; }
    footer p + p { margin-top: 0.35rem; }

    /* ── RESPONSIVE ── */
    @media (max-width: 700px) {
      .hero h1 { font-size: 2rem; }
      .cv-grid  { grid-template-columns: 1fr; }
      .project-year { margin-left: 0; }
      .section-header { flex-direction: column; align-items: flex-start; }
    }
"""

# ── template ─────────────────────────────────────────────────

def render():
    name_parts = HERO["name"].split(" ", 2)          # "Dr. Lala Kounta"
    first_two  = " ".join(name_parts[:2])            # "Dr. Lala"
    last       = " ".join(name_parts[2:])            # "Kounta"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{h(HERO["name"])} — Ocean &amp; Climate Scientist</title>
  <style>{CSS}  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <span class="nav-name">{h(HERO["name"])}</span>
    <ul>
      <li><a href="#about">About</a></li>
      <li><a href="#research">Research</a></li>
      <li><a href="#cv">CV</a></li>
    </ul>
  </div>
</nav>

<!-- HERO -->
<header class="hero">
  <div class="hero-badge">{h(HERO["badge"])}</div>
  <h1><em>{h(first_two)}</em> {h(last)}</h1>
  <p class="subtitle">{h(HERO["subtitle"])}</p>
  <p class="affil">{h(HERO["affiliation"])}</p>
  <div class="hero-links">
    <a href="mailto:{h(HERO["email"])}" class="hero-link primary">&#9993;&nbsp; {h(HERO["email"])}</a>
    <a href="{h(HERO["cv_file"])}" download class="hero-link cv-btn">&#8595;&nbsp; Download CV</a>
    <a href="{h(HERO["orcid"])}" target="_blank" class="hero-link outline">ORCID</a>
    <a href="{h(HERO["linkedin"])}" target="_blank" class="hero-link outline">LinkedIn</a>
  </div>
</header>


<!-- ════════ ABOUT ════════ -->
<section id="about">
  <div class="section-wrap">
    <div class="section-header">
      <div class="section-header-text">
        <span class="section-label">Who I am</span>
        <h2>About Me</h2>
      </div>
    </div>
    <div class="about-body">
{paras(ABOUT_PARAGRAPHS)}
    </div>
    <div class="cards-grid">
{info_cards(INFO_CARDS)}
    </div>
  </div>
</section>


<!-- ════════ RESEARCH ════════ -->
<section id="research" class="alt-bg">
  <div class="section-wrap">
    <div class="section-header">
      <div class="section-header-text">
        <span class="section-label">Projects</span>
        <h2>My Research</h2>
        <p class="section-desc">{h(SECTION_DESC)}</p>
      </div>
    </div>
    <div class="projects-list">
{project_cards(PROJECTS)}
    </div>
  </div>
</section>


<!-- ════════ CV ════════ -->
<section id="cv">
  <div class="section-wrap">
    <div class="section-header">
      <div class="section-header-text">
        <span class="section-label">Curriculum Vitae</span>
        <h2>CV</h2>
      </div>
      <div style="text-align:right;">
        <a href="{h(HERO["cv_file"])}" download class="dl-cv-btn">&#8595;&nbsp; Download Full CV</a>
        <div class="cv-updated">Last updated: {h(CV_UPDATED)}</div>
      </div>
    </div>

    <div class="cv-grid">

      <div class="cv-block">
        <h3>Academic Appointments</h3>
{cv_entries(APPOINTMENTS)}
      </div>

      <div class="cv-block">
        <h3>Education</h3>
{education_entries(EDUCATION)}
      </div>

      <div class="cv-block">
        <h3>Awards &amp; Grants</h3>
        <div class="award-list">
{grant_items(GRANTS)}
        </div>
      </div>

      <div class="cv-block">
        <h3>Selected Publications</h3>
        <ul class="pub-list">
{pub_items(PUBLICATIONS)}
        </ul>
      </div>

      <div class="cv-block">
        <h3>Teaching</h3>
{cv_entries(TEACHING)}
      </div>

      <div class="cv-block">
        <h3>Technical Skills</h3>
        <div class="skills-wrap">
{skill_pills(SKILLS)}
        </div>
      </div>

    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <p>
    {h(HERO["name"])} &nbsp;&middot;&nbsp;
    <a href="mailto:{h(HERO["email"])}">{h(HERO["email"])}</a> &nbsp;&middot;&nbsp;
    <a href="{h(HERO["orcid"])}" target="_blank">ORCID</a> &nbsp;&middot;&nbsp;
    <a href="{h(HERO["linkedin"])}" target="_blank">LinkedIn</a>
  </p>
  <p>Department of Integrative Biology, Michigan State University &mdash; East Lansing, MI 48824</p>
</footer>

</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(page)
    print("✓  index.html rebuilt successfully.")

if __name__ == "__main__":
    render()
