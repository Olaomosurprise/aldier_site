"""Build the Aldier site into dist/.

Each page lives in src/ as an HTML fragment that starts with a comment block
of settings, for example:

    <!--
    title: Strategy and Transformation
    description: One sentence for search and sharing.
    header: dark
    -->

The fragment is wrapped in the shared head, header, menus and footer, links
written as {{root}} are made relative to the page, and the result is written
to dist/<same path>. Assets and the Pages Functions folder are copied across.

Usage:
    python3 build.py
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
SITE = "https://aldier.co"

# Main navigation. Each entry opens a panel: columns of links on the left and
# up to three featured programmes on the right.
NAV = [
    {
        "label": "Industries",
        "href": "industries/",
        "intro": "Fifteen industries, with the deepest knowledge where decisions reach the most people.",
        "columns": [
            ("Industries of depth", [
                ("Public Sector and Government", "industries/public-sector/"),
                ("Education", "industries/education/"),
                ("Financial Services", "industries/financial-services/"),
            ]),
            ("Across the economy", [
                ("All fifteen industries", "industries/"),
                ("Healthcare and Life Sciences", "industries/#healthcare"),
                ("Energy, Power and Natural Resources", "industries/#energy"),
                ("Telecoms, Media and Technology", "industries/#tmt"),
            ]),
        ],
        "featured": [
            ("The Aldier Institute", "Research on how institutions perform, and why some earn trust that lasts.", "institute/"),
        ],
    },
    {
        "label": "Practices",
        "href": "practices/",
        "intro": "Five disciplines, one team, one partner accountable from the first decision to the public announcement.",
        "columns": [
            ("Practices", [
                ("Strategy and Transformation", "practices/strategy/"),
                ("Technology and Data", "practices/technology/"),
                ("Cybersecurity and Digital Risk", "practices/cybersecurity/"),
                ("Design and Experience", "practices/design/"),
                ("Communications and Public Affairs", "practices/communications/"),
            ]),
        ],
        "featured": [
            ("Aldier Studio", "Design, film and digital products, made by the people who advised on them.", "studio/"),
            ("The Board Programme", "Private briefings and rehearsals for boards on risk, technology and reputation.", "board-programme/"),
        ],
    },
    {
        "label": "Studio",
        "href": "studio/",
    },
    {
        "label": "Insights",
        "href": "insights/",
        "intro": "What we are learning, published when it is ready and signed by the people who wrote it.",
        "columns": [
            ("Read", [
                ("All perspectives", "insights/"),
                ("The joins", "insights/the-joins/"),
                ("Before the breach", "insights/before-the-breach/"),
                ("The handover", "insights/the-handover/"),
            ]),
            ("Programmes", [
                ("The Aldier Institute", "institute/"),
                ("The Aldier Review", "review/"),
                ("Aldier Conversations", "conversations/"),
                ("The Aldier Briefing", "insights/#briefing"),
            ]),
        ],
        "featured": [
            ("The Aldier Review", "The firm's journal of institutional performance. The first issue is in preparation.", "review/"),
            ("Aldier Conversations", "Leaders in conversation about the decisions that shaped their institutions.", "conversations/"),
        ],
    },
    {
        "label": "About",
        "href": "about/",
        "intro": "A multidisciplinary firm built around one rule: the people who advise also answer for the result.",
        "columns": [
            ("The firm", [
                ("About Aldier", "about/"),
                ("How we work", "about/#how-we-work"),
                ("Independence", "about/#independence"),
                ("Our work", "work/"),
            ]),
            ("Connect", [
                ("Careers", "careers/"),
                ("Contact", "contact/"),
                ("The Aldier Briefing", "insights/#briefing"),
            ]),
        ],
        "featured": [
            ("GENIVY", "Aldier is Founding Partner to an international guild of students.", "work/genivy/"),
        ],
    },
    {
        "label": "Careers",
        "href": "careers/",
    },
]

FOOTER = [
    ("Practices", [
        ("Strategy and Transformation", "practices/strategy/"),
        ("Technology and Data", "practices/technology/"),
        ("Cybersecurity and Digital Risk", "practices/cybersecurity/"),
        ("Design and Experience", "practices/design/"),
        ("Communications and Public Affairs", "practices/communications/"),
    ]),
    ("Programmes", [
        ("Aldier Studio", "studio/"),
        ("The Aldier Institute", "institute/"),
        ("The Aldier Review", "review/"),
        ("Aldier Conversations", "conversations/"),
        ("The Board Programme", "board-programme/"),
    ]),
    ("The firm", [
        ("About Aldier", "about/"),
        ("Industries", "industries/"),
        ("Our work", "work/"),
        ("Insights", "insights/"),
        ("Careers", "careers/"),
        ("Contact", "contact/"),
    ]),
]

ARROW = '<svg class="ad-ico" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h9M8.5 4.5 12 8l-3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'


def settings(text: str) -> tuple[dict, str]:
    match = re.match(r"\s*<!--(.*?)-->", text, re.S)
    if not match:
        raise ValueError("page has no settings block")
    data = {}
    for line in match.group(1).strip().splitlines():
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data, text[match.end():]


def menu() -> str:
    items = []
    for i, entry in enumerate(NAV):
        if "columns" not in entry:
            items.append(f'<li><a class="ad-nav__top" href="{{{{root}}}}{entry["href"]}">{entry["label"]}</a></li>')
            continue
        cols = "".join(
            f'<div class="ad-mega__col"><p class="ad-mega__head">{head}</p><ul>'
            + "".join(f'<li><a href="{{{{root}}}}{href}">{label}</a></li>' for label, href in links)
            + "</ul></div>"
            for head, links in entry["columns"]
        )
        feats = "".join(
            f'<a class="ad-mega__feat" href="{{{{root}}}}{href}"><b>{name}</b><span>{blurb}</span></a>'
            for name, blurb, href in entry["featured"]
        )
        items.append(
            f'<li class="ad-nav__item"><button class="ad-nav__top" type="button" aria-expanded="false" aria-controls="mega-{i}">{entry["label"]}<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 3.5 5 6.5 8 3.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></button>'
            f'<div class="ad-mega" id="mega-{i}"><div class="ad-wrap ad-mega__grid">'
            f'<div class="ad-mega__intro"><a class="ad-mega__title" href="{{{{root}}}}{entry["href"]}">{entry["label"]} {ARROW}</a><p>{entry["intro"]}</p></div>'
            f'<div class="ad-mega__cols">{cols}</div>'
            f'<div class="ad-mega__side"><p class="ad-mega__head">Featured</p>{feats}</div>'
            f"</div></div></li>"
        )
    return "".join(items)


def footer(brief: bool = True) -> str:
    cols = "".join(
        f'<div><h2>{head}</h2><ul>' + "".join(f'<li><a href="{{{{root}}}}{href}">{label}</a></li>' for label, href in links) + "</ul></div>"
        for head, links in FOOTER
    )
    brief_html = """<div class="ad-foot__brief" id="footer-briefing">
      <div><p class="ad-eyebrow">The Aldier Briefing</p><h2>One considered note a month on the decisions institutions face.</h2></div>
      <form class="ad-sub" action="{{root}}api/enquiry" method="post" data-enquiry>
        <input type="hidden" name="form" value="briefing">
        <label class="ad-vh" for="foot-email">Email address</label>
        <input id="foot-email" name="email" type="email" autocomplete="email" placeholder="Your email address" required>
        <input class="ad-hp" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="ad-btn ad-btn--light" type="submit">Subscribe</button>
        <p class="ad-sub__note" role="status">Published monthly. See the <a href="{{root}}privacy/">privacy notice</a> for how we hold your address.</p>
      </form>
    </div>""" if brief else ""
    return f"""<footer class="ad-foot">
  <div class="ad-wrap">
    {brief_html}
    <div class="ad-foot__main">
      <a class="ad-foot__logo" href="{{{{root}}}}"><img src="{{{{root}}}}assets/brand/aldier-logo-dark.svg" alt="Aldier" width="150" height="44"></a>
      <div class="ad-foot__cols">{cols}</div>
    </div>
    <div class="ad-foot__base">
      <span>&copy; 2026 Aldier. All rights reserved.</span>
      <ul><li><a href="{{{{root}}}}privacy/">Privacy</a></li><li><a href="{{{{root}}}}terms/">Terms of use</a></li><li><a href="{{{{root}}}}accessibility/">Accessibility</a></li><li><a href="https://www.instagram.com/aldierco/" rel="noopener">Instagram</a></li></ul>
    </div>
  </div>
</footer>"""


def page(data: dict, body: str, path: Path) -> str:
    depth = len(path.relative_to(SRC).parts) - 1
    root = "/" if data.get("absolute") == "yes" else "../" * depth
    title = data["title"]
    full_title = "Aldier" if title == "Aldier" else f"{title} | Aldier"
    header_mode = data.get("header", "dark")
    image = data.get("image", "assets/film/decide.jpg")
    url_path = str(path.relative_to(SRC).parent).replace(".", "")
    canonical = f"{SITE}/{url_path}/" if url_path else f"{SITE}/"
    preload = data.get("preload", "")
    preload_tag = f'<link rel="preload" href="{root}{preload}" as="image" fetchpriority="high">' if preload else ""
    html = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{data['description']}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aldier">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{data['description']}">
<meta property="og:image" content="{SITE}/{image}">
<meta name="theme-color" content="#0b0e1c">
<link rel="icon" href="{root}assets/brand/aldier-mark.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
{preload_tag}
<link rel="stylesheet" href="{root}assets/css/aldier.css">
</head>
<body class="ad-page ad-page--{data.get('slug', 'page')}" data-header="{header_mode}">
<a class="ad-skip" href="#main">Skip to content</a>
<header class="ad-header">
  <div class="ad-wrap ad-header__row">
    <a class="ad-logo" href="{{{{root}}}}" aria-label="Aldier, home">
      <img class="ad-logo--onDark" src="{{{{root}}}}assets/brand/aldier-logo-dark.svg" alt="" width="128" height="37">
      <img class="ad-logo--onLight" src="{{{{root}}}}assets/brand/aldier-logo-light.svg" alt="" width="128" height="37">
    </a>
    <nav class="ad-nav" id="ad-nav" aria-label="Main">
      <ul class="ad-nav__list">{menu()}</ul>
      <a class="ad-btn ad-nav__cta" href="{{{{root}}}}contact/">Contact us</a>
    </nav>
    <button class="ad-menu" type="button" aria-expanded="false" aria-controls="ad-nav"><span class="ad-menu__bars" aria-hidden="true"><i></i><i></i></span><span class="ad-menu__label">Menu</span></button>
  </div>
</header>
<main id="main">
{body.strip()}
</main>
{footer(data.get('brief', 'yes') != 'no')}
<script src="{{{{root}}}}assets/js/aldier.js" defer></script>
</body>
</html>
"""
    return html.replace("{{arrow}}", ARROW).replace("{{root}}", root)


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    count = 0
    for source in sorted(SRC.rglob("*.html")):
        data, body = settings(source.read_text(encoding="utf-8"))
        out = DIST / source.relative_to(SRC)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(data, body, source), encoding="utf-8")
        count += 1
    shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("photos.json", ".DS_Store", "fraunces-*", "LICENSE-fraunces.txt"))
    for name in ("_headers", "_redirects", "robots.txt"):
        if (ROOT / name).exists():
            shutil.copy(ROOT / name, DIST / name)
    urls = sorted(
        str(p.relative_to(DIST).parent).replace(".", "")
        for p in DIST.rglob("index.html")
        if "assets" not in p.parts
    )
    sitemap = "".join(f"<url><loc>{SITE}/{u + '/' if u else ''}</loc></url>" for u in urls)
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap}</urlset>\n',
        encoding="utf-8",
    )
    print(f"Built {count} pages into dist/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
