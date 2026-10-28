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

import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
# The public address of the site. Set SITE_URL in the Cloudflare Pages project when the domain changes.
SITE = os.environ.get("SITE_URL", "https://aldier.pages.dev").rstrip("/")

# Main navigation. Each entry opens a panel: columns of links on the left and
# up to three featured programmes on the right.
NAV = [
    {
        "label": "Industries",
        "href": "industries/",
        "intro": "We serve institutions across fifteen industries, with dedicated teams for the public sector, education and financial services.",
        "columns": [
            ("Focus industries", [
                ("Public Sector and Government", "industries/public-sector/"),
                ("Education", "industries/education/"),
                ("Financial Services", "industries/financial-services/"),
            ]),
            ("Across the economy", [
                ("All industries", "industries/"),
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
        "label": "Capabilities",
        "href": "practices/",
        "intro": "Five practices serving the full agenda of an institution, engaged individually or together.",
        "columns": [
            ("Our practices", [
                ("Strategy and Transformation", "practices/strategy/"),
                ("Technology and Data", "practices/technology/"),
                ("Cybersecurity and Digital Risk", "practices/cybersecurity/"),
                ("Design and Experience", "practices/design/"),
                ("Communications and Public Affairs", "practices/communications/"),
            ]),
        ],
        "featured": [
            ("Aldier Studio", "The design and build studio of Aldier.", "studio/"),
            ("The Board Programme", "Briefings and simulations for directors on risk, technology and reputation.", "board-programme/"),
        ],
    },
    {
        "label": "Studio",
        "href": "studio/",
    },
    {
        "label": "Insights",
        "href": "insights/",
        "intro": "Perspectives, board briefings and research from across our practices.",
        "columns": [
            ("Featured insights", [
                ("All insights", "insights/"),
                ("Where transformations fail", "insights/the-joins/"),
                ("Before the breach", "insights/before-the-breach/"),
                ("The handover", "insights/the-handover/"),
            ]),
            ("Research and publishing", [
                ("The Aldier Institute", "institute/"),
                ("The Aldier Review", "review/"),
                ("The Aldier Podcast", "podcast/"),
                ("Aldier Conversations", "conversations/"),
                ("Subscribe", "subscribe/"),
            ]),
        ],
        "featured": [
            ("The Aldier Podcast", "Conversations with the people who build institutions. Season one coming soon.", "podcast/"),
            ("The Aldier Review", "The journal of Aldier. Coming soon.", "review/"),
            ("Aldier Conversations", "Leaders in conversation about the decisions that shaped their institutions.", "conversations/"),
        ],
    },
    {
        "label": "About",
        "href": "about/",
        "intro": "A multidisciplinary advisory firm. We help leaders set direction and see it through.",
        "columns": [
            ("Who we are", [
                ("About Aldier", "about/"),
                ("How we work", "about/#how-we-work"),
                ("Professional standards", "about/standards/"),
                ("Social impact", "about/social-impact/"),
                ("Our work", "work/"),
            ]),
            ("Connect", [
                ("Newsroom", "newsroom/"),
                ("Careers", "careers/"),
                ("Contact", "contact/"),
                ("Subscribe", "subscribe/"),
            ]),
        ],
        "featured": [
            ("GENIVY", "The international guild of students for which Aldier serves as Founding Partner.", "work/genivy/"),
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
        ("The Aldier Podcast", "podcast/"),
        ("Aldier Conversations", "conversations/"),
        ("The Board Programme", "board-programme/"),
    ]),
    ("Aldier", [
        ("About Aldier", "about/"),
        ("Industries", "industries/"),
        ("Our work", "work/"),
        ("Insights", "insights/"),
        ("Newsroom", "newsroom/"),
        ("Social impact", "about/social-impact/"),
        ("Careers", "careers/"),
        ("Contact", "contact/"),
    ]),
]

CHEV = '<svg class="ad-chev" width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M4 2l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
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
      <div><p class="ad-eyebrow">The Aldier Briefing</p><h2>Our latest perspectives and research, once a month.</h2></div>
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
    <div class="ad-foot__top">
      <p class="ad-foot__tag">Clear decisions. <em>Lasting institutions.</em></p>
      <ul class="ad-foot__quick"><li><a href="{{{{root}}}}careers/">Careers</a></li><li><a href="{{{{root}}}}insights/">Insights</a></li><li><a href="{{{{root}}}}podcast/">Podcast</a></li><li><a href="{{{{root}}}}newsroom/">Newsroom</a></li><li><a href="{{{{root}}}}about/">About</a></li><li><a href="{{{{root}}}}subscribe/">Subscribe</a></li></ul>
      <div class="ad-foot__assist"><h2>How can we assist you?</h2><p>Tell us about the challenge in front of you. A partner reads every enquiry and replies in confidence.</p><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/">Contact us {ARROW}</a></div>
    </div>
    <div class="ad-foot__main">
      <a class="ad-foot__logo" href="{{{{root}}}}"><img src="{{{{root}}}}assets/brand/aldier-logo-dark.svg" alt="Aldier" width="150" height="44"></a>
      <div class="ad-foot__cols">{cols}</div>
    </div>
    <div class="ad-foot__follow"><span>Follow us</span><a href="https://www.instagram.com/aldierco/" rel="noopener" aria-label="Aldier on Instagram"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor"/></svg></a></div>
    <div class="ad-foot__base">
      <span>&copy; 2026 Aldier. All rights reserved.</span>
      <ul><li><a href="{{{{root}}}}privacy/">Privacy</a></li><li><a href="{{{{root}}}}privacy/#cookies">Cookies</a></li><li><a href="{{{{root}}}}terms/">Terms of use</a></li><li><a href="{{{{root}}}}accessibility/">Accessibility</a></li><li><a href="{{{{root}}}}about/standards/">Professional standards</a></li><li><a href="{{{{root}}}}recruitment-fraud/">Recruitment fraud</a></li><li><a href="{{{{root}}}}sitemap/">Site map</a></li></ul>
    </div>
  </div>
</footer>"""


def schema(data: dict, canonical: str, site: str, image: str) -> str:
    """Structured data, as the leading firms publish it, so search engines understand the firm and its articles."""
    org = {"@type": "Organization", "@id": f"{site}/#organization", "name": "Aldier", "url": f"{site}/",
           "logo": f"{site}/assets/brand/apple-touch-icon.png",
           "description": "Aldier is a multidisciplinary advisory firm working across strategy, technology, cybersecurity, design and communications.",
           "sameAs": ["https://www.instagram.com/aldierco/"]}
    graph = [org]
    if canonical.rstrip("/") == site:
        graph.append({"@type": "WebSite", "@id": f"{site}/#website", "url": f"{site}/", "name": "Aldier", "publisher": {"@id": f"{site}/#organization"},
                      "potentialAction": {"@type": "SearchAction", "target": f"{site}/search/?q={{query}}", "query-input": "required name=query"}})
    if data.get("slug") == "essay":
        graph.append({"@type": "Article", "headline": data["title"], "description": data["description"], "image": f"{site}/{image}",
                      "mainEntityOfPage": canonical, "publisher": {"@id": f"{site}/#organization"}, "author": {"@id": f"{site}/#organization"}, "inLanguage": "en-GB"})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + "</script>"


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
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{data['description']}">
<meta name="twitter:image" content="{SITE}/{image}">
<link rel="apple-touch-icon" href="{root}assets/brand/apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
{schema(data, canonical, SITE, image)}
<meta name="theme-color" content="#0b0e1c">
<link rel="icon" href="{root}assets/brand/aldier-mark.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
{preload_tag}
<link rel="stylesheet" href="{root}assets/css/aldier.css?v={VERSION}">
</head>
<body class="ad-page ad-page--{data.get('slug', 'page')}" data-header="{header_mode}">
<a class="ad-skip" href="#main">Skip to content</a>
<header class="ad-header">
  <div class="ad-util"><div class="ad-wrap ad-util__row"><ul><li><a href="{{{{root}}}}newsroom/">Newsroom</a></li><li><a href="{{{{root}}}}podcast/">Podcast</a></li><li><a href="{{{{root}}}}subscribe/">Subscribe</a></li><li><a href="{{{{root}}}}contact/">Contact</a></li></ul><span class="ad-util__loc"><svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M1.5 8h13M8 1.5c2 2 2.6 4.2 2.6 6.5S10 12.5 8 14.5M8 1.5C6 3.5 5.4 5.7 5.4 8S6 12.5 8 14.5" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>Global &nbsp;|&nbsp; English</span></div></div>
  <div class="ad-wrap ad-header__row">
    <a class="ad-logo" href="{{{{root}}}}" aria-label="Aldier, home">
      <img class="ad-logo--onDark" src="{{{{root}}}}assets/brand/aldier-logo-dark.svg" alt="" width="128" height="37">
      <img class="ad-logo--onLight" src="{{{{root}}}}assets/brand/aldier-logo-light.svg" alt="" width="128" height="37">
    </a>
    <nav class="ad-nav" id="ad-nav" aria-label="Main">
      <ul class="ad-nav__list">{menu()}</ul>
      <a class="ad-search-link" href="{{{{root}}}}search/" aria-label="Search"><svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><circle cx="7.5" cy="7.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m11.6 11.6 4.4 4.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="ad-search-link__label">Search</span></a>
      <a class="ad-btn ad-nav__cta" href="{{{{root}}}}contact/">Contact us</a>
    </nav>
    <button class="ad-menu" type="button" aria-expanded="false" aria-controls="ad-nav"><span class="ad-menu__bars" aria-hidden="true"><i></i><i></i></span><span class="ad-menu__label">Menu</span></button>
  </div>
</header>
<main id="main">
{body.strip()}
</main>
{footer(data.get('brief', 'yes') != 'no')}
<script src="{{{{root}}}}assets/js/aldier.js?v={VERSION}" defer></script>
</body>
</html>
"""
    return html.replace("{{arrow}}", ARROW).replace("{{chev}}", CHEV).replace("{{root}}", root)


import hashlib
VERSION = hashlib.sha1(b"".join((Path(__file__).resolve().parent / "assets" / f).read_bytes() for f in ("css/aldier.css", "js/aldier.js"))).hexdigest()[:10]


def kind(url: str) -> str:
    first = url.split("/")[0]
    return {
        "": "Pages", "practices": "Capabilities", "industries": "Industries", "insights": "Insights",
        "studio": "Programmes", "institute": "Programmes", "review": "Programmes", "conversations": "Programmes", "board-programme": "Programmes",
        "work": "Our work", "newsroom": "Newsroom", "podcast": "Programmes", "about": "About", "careers": "Careers", "recruitment-fraud": "Careers",
        "privacy": "Legal", "terms": "Legal", "accessibility": "Legal", "contact": "Pages", "subscribe": "Pages", "sitemap": "Legal",
    }.get(first, "Pages")


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    count = 0
    pages = []
    for source in sorted(SRC.rglob("*.html")):
        data, body = settings(source.read_text(encoding="utf-8"))
        pages.append((source, data, body))
    entries = []
    for source, data, body in pages:
        rel = source.relative_to(SRC)
        if rel.name != "index.html" or str(rel.parent) in ("search",):
            continue
        url = "" if str(rel.parent) == "." else str(rel.parent).replace("\\", "/") + "/"
        text = re.sub(r"<script.*?</script>|<[^>]+>", " ", body, flags=re.S)
        text = re.sub(r"\{\{[a-z]+\}\}", " ", text)
        entries.append({"t": data.get("title", ""), "d": data.get("description", ""), "u": url, "k": kind(url), "x": " ".join(text.split())[:1800]})
    (DIST).mkdir(exist_ok=True)
    (DIST / "search.json").write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")
    groups = {}
    for e in sorted(entries, key=lambda e: e["u"]):
        groups.setdefault(e["k"], []).append(e)
    order = ["Pages", "Capabilities", "Industries", "Insights", "Programmes", "Our work", "Newsroom", "About", "Careers", "Legal"]
    cols = "".join(
        f'<div><h2 class="ad-eyebrow">{k}</h2><ul>' + "".join(f'<li><a href="{{{{root}}}}{e["u"]}">{e["t"]}</a></li>' for e in groups[k]) + "</ul></div>"
        for k in order if k in groups
    )
    sm_body = f"""<section class="ad-rhero"><div class="ad-wrap"><p class="ad-eyebrow">Site map</p><h1 id="page-title" class="ad-h1">Site map</h1><p class="ad-lede">Every page on the Aldier website.</p></div></section>
<section class="ad-sec ad-sec--tight"><div class="ad-wrap ad-sitemap">{cols}</div></section>"""
    pages.append((SRC / "sitemap" / "index.html", {"title": "Site map", "description": "A complete list of pages on the Aldier website, grouped by section.", "header": "light", "slug": "legal"}, sm_body))
    for source, data, body in pages:
        out = DIST / source.relative_to(SRC)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(data, body, source), encoding="utf-8")
        count += 1
    shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("photos.json", ".DS_Store", "fraunces-*", "LICENSE-fraunces.txt"))
    css = DIST / "assets" / "css" / "aldier.css"
    text = re.sub(r"/\*.*?\*/", "", css.read_text(encoding="utf-8"), flags=re.S)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*([{};,>])\s*", r"\1", text).replace(";}", "}")
    css.write_text(text.strip(), encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    (DIST / "site.webmanifest").write_text(json.dumps({"name": "Aldier", "short_name": "Aldier", "start_url": "/", "display": "browser", "background_color": "#ffffff", "theme_color": "#0b0e1c",
        "icons": [{"src": "/assets/brand/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}, {"src": "/assets/brand/icon-512.png", "sizes": "512x512", "type": "image/png"}]}), encoding="utf-8")
    for name in ("_headers", "_redirects"):
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
