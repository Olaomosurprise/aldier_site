"""Writes the industries index and the three industries of depth into src/.

Run from the project root: python3 content/industries.py
"""

from pathlib import Path

from practices import img, video

SRC = Path(__file__).resolve().parent.parent / "src" / "industries"

ALL = [
    ("public-sector", "Public Sector and Government", "Ministries, agencies, regulators and state enterprises delivering services citizens can see working.", True),
    ("education", "Education", "Universities, schools and the systems that fund and regulate them.", True),
    ("financial-services", "Financial Services", "Banks, insurers, asset managers, payments companies and the regulators who supervise them.", True),
    ("healthcare", "Healthcare and Life Sciences", "Hospitals, health insurers and public health programmes, where service design is a matter of life and death.", False),
    ("energy", "Energy, Power and Natural Resources", "Generation, distribution, oil and gas and mining, in markets where reform and investment move together.", False),
    ("tmt", "Telecoms, Media and Technology", "Operators, broadcasters, publishers and technology companies whose products shape public life.", False),
    ("consumer", "Consumer and Retail", "Brands and retailers competing on trust, distribution and the experience of buying.", False),
    ("real-estate", "Real Estate and Infrastructure", "Developers, investors and public owners of buildings, cities and the networks that connect them.", False),
    ("transport", "Transport and Logistics", "Ports, airlines, rail, roads and the companies that move goods across them.", False),
    ("agriculture", "Agriculture and Food Systems", "Producers, processors and the programmes that finance and protect them.", False),
    ("manufacturing", "Manufacturing and Industrials", "Factories and industrial groups improving productivity, safety and supply resilience.", False),
    ("creative", "Creative and Cultural Industries", "Film, music, fashion, publishing and the institutions that sustain them.", False),
    ("hospitality", "Hospitality and Travel", "Hotels, tourism boards and destinations designing experiences people return to.", False),
    ("development", "Development and Social Impact", "Foundations, multilaterals and non-profits measuring what their money changes.", False),
    ("private-capital", "Private Capital", "Private equity, venture and infrastructure investors, from diligence to value creation.", False),
]

DEPTH = [
    {
        "slug": "public-sector",
        "name": "Public Sector and Government",
        "hero": "civic-hall",
        "hero_alt": "A stone civic building facing an empty square",
        "purpose": "Public services that deliver for citizens, and reforms that last.",
        "lede": "Governments are judged by what citizens experience: the licence issued on time, the clinic that is open, the payment that arrives. We help ministries, agencies and regulators design reforms that can be delivered, and build the institutions that sustain them through changes of leadership.",
        "statement": "Most of the work of reform happens after the announcement: in procurement, systems, people and the persistence to see it through. That is where we spend most of our time.",
        "questions": [
            ("How do we turn a manifesto into a delivery plan?", "Priorities translated into programmes with owners, budgets and measures that a delivery unit can track week by week."),
            ("Which services should go digital first, and how?", "Services chosen by volume and pain, redesigned around citizens, and built on infrastructure the state owns."),
            ("How do we buy technology without being captured by it?", "Procurement strategies, specifications and contracts that keep the state in control of its systems and data."),
            ("How do we protect citizens' data?", "Data protection programmes and security readiness for agencies that hold sensitive records."),
            ("How do we explain a difficult reform?", "Public engagement and communication that prepares citizens for change before it reaches them."),
            ("How do we make reform outlast its sponsors?", "Institutions, rules and capabilities designed to continue after the people who launched them have moved on."),
        ],
        "inner": "towers",
        "inner_alt": "Office towers rising into a blue sky",
        "spot_title": "Building delivery units",
        "spot_text": "We help governments establish small, senior delivery units that track commitments against evidence, escalate problems early and publish progress that citizens can check.",
    },
    {
        "slug": "education",
        "name": "Education",
        "hero": "university-colonnade",
        "hero_alt": "The white colonnade of a university building",
        "purpose": "Universities that run well, and graduates ready for work.",
        "lede": "A university runs housing, transport, catering, security, health and finance for thousands of people, all in service of teaching and research. We help universities and education systems strengthen their finances, operations and student experience, and prepare graduates for the labour market.",
        "statement": "Students judge a university by its hostels, its portals, its queues and the jobs that follow graduation. The academic mission depends on everything around it.",
        "questions": [
            ("How do we fund growth without raising fees beyond reach?", "Financial strategy, auxiliary enterprise and partnerships that diversify income responsibly."),
            ("How do we modernise the student journey?", "Admissions, records, payments and learning platforms redesigned around students and staff."),
            ("How do we prepare graduates for work?", "Employer partnerships, work-based learning and career services measured by outcomes."),
            ("How do we protect research and student data?", "Security and data protection suited to open campuses and international collaboration."),
            ("How do we compete for international students and partners?", "Positioning, identity and the experience prospective students meet online and on arrival."),
            ("How do we govern a multi-campus institution?", "Operating models, decision rights and shared services for growing systems."),
        ],
        "inner": "lecture",
        "inner_alt": "Students listening in a lecture hall",
        "spot_title": "GENIVY",
        "spot_text": "GENIVY is the international guild of students that Aldier helped found. Owned by its members, it organises the work already present on university campuses and pays students to run it. Aldier serves as its Founding Partner.",
        "spot_link": "work/genivy/",
    },
    {
        "slug": "financial-services",
        "name": "Financial Services",
        "hero": "bank-portico",
        "hero_alt": "The columned portico of a stone banking hall",
        "purpose": "Growth with the controls that customers and regulators depend on.",
        "lede": "Financial institutions are trusted with other people's savings, and that trust is regulated, audited and tested every day. We help banks, insurers, payments companies and their regulators grow while strengthening the controls their customers depend on.",
        "statement": "Customers rarely think about their bank until something goes wrong. Our work is to make that moment rare, and to ensure the institution is ready when it comes.",
        "questions": [
            ("Where should we grow, and what should we stop?", "Portfolio strategy, product economics and the operating model to serve chosen segments profitably."),
            ("How do we replace core systems safely?", "Core banking and insurance platform selection, migration planning and delivery assurance."),
            ("Are we ready for a cyber incident?", "Readiness against supervisory expectations, incident rehearsal and third-party risk."),
            ("How do we meet new regulation efficiently?", "Regulatory change programmes that leave durable capabilities behind once the deadline has passed."),
            ("How do we serve customers better on every channel?", "Service design for branches, apps and contact centres, built from customer evidence."),
            ("How do we explain results, deals and setbacks?", "Investor, regulatory and public communication around results, transactions and incidents."),
        ],
        "inner": "blue-facade",
        "inner_alt": "A building facade in saturated blue",
        "spot_title": "Risk and compliance designed into products",
        "spot_text": "We bring risk, security and compliance specialists into product teams from the first design, so that new products launch with their controls in place.",
    },
]


def depth_page(d: dict) -> str:
    qs = "".join(f'<div class="ad-card"><h3>{q}</h3><p>{a}</p></div>' for q, a in d["questions"])
    link = d.get("spot_link")
    spot_link = f'<a class="ad-link" href="{{{{root}}}}{link}">Read the case study {{{{arrow}}}}</a>' if link else '<a class="ad-link" href="{{root}}contact/">Contact us {{arrow}}</a>'
    return f"""<!--
title: {d['name']}
description: {d['purpose']} {d['lede']}
header: dark
slug: industry-{d['slug']}
image: assets/photos/{d['hero']}-1600.webp
preload: assets/photos/{d['hero']}-1600.webp
-->
<section class="ad-phero" aria-labelledby="page-title">
  <div class="ad-phero__media">{img(d['hero'], d['hero_alt'], '100vw').replace(' loading="lazy"', ' fetchpriority="high"')}</div>
  <div class="ad-wrap ad-phero__body">
    <p class="ad-phero__crumb"><a href="{{{{root}}}}industries/">Industries</a> / {d['name']}</p>
    <p class="ad-eyebrow">Industry</p>
    <h1 id="page-title" class="ad-h1">{d['name']}</h1>
    <p class="ad-lede"><b>{d['purpose']}</b> {d['lede']}</p>
  </div>
</section>

<section class="ad-sec ad-statement ad-on-light" aria-label="Perspective">
  <div class="ad-wrap"><p class="ad-eyebrow">Our perspective</p><p class="ad-lit" data-light>{d['statement']}</p></div>
</section>

<section class="ad-sec ad-mist" aria-labelledby="q-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">How we help clients</p><h2 id="q-title" class="ad-h2">Questions we help leaders answer</h2></div><p>Most draw on more than one of our practices.</p></div>
    <div class="ad-cards">{qs}</div>
  </div>
</section>

<section class="ad-sec ad-dark" aria-labelledby="spot-title">
  <div class="ad-wrap ad-split ad-split--flip">
    <div class="ad-split__media" data-reveal>{img(d['inner'], d['inner_alt'])}</div>
    <div data-reveal>
      <p class="ad-eyebrow">Our work</p>
      <h2 id="spot-title" class="ad-h2">{d['spot_title']}</h2>
      <p class="ad-lede">{d['spot_text']}</p>
      {spot_link}
    </div>
  </div>
</section>

<section class="ad-sec ad-on-light" aria-labelledby="pr-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Capabilities</p><h2 id="pr-title" class="ad-h2">Our practices in {d['name']}</h2></div></div>
    <ul class="ad-pills">
      <li><a href="{{{{root}}}}practices/strategy/">Strategy and Transformation</a></li>
      <li><a href="{{{{root}}}}practices/technology/">Technology and Data</a></li>
      <li><a href="{{{{root}}}}practices/cybersecurity/">Cybersecurity and Digital Risk</a></li>
      <li><a href="{{{{root}}}}practices/design/">Design and Experience</a></li>
      <li><a href="{{{{root}}}}practices/communications/">Communications and Public Affairs</a></li>
    </ul>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" aria-labelledby="close-title">
  <div class="ad-wrap">
    <p class="ad-eyebrow" style="justify-content:center">{d['name']}</p>
    <h2 id="close-title" class="ad-h2 ad-mt-s">Connect with our {d['name']} team</h2>
    <p class="ad-lede">Tell us about the challenge in front of you. A partner will reply in confidence.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/?topic={d['name'].replace(' ', '%20')}">Contact us {{{{arrow}}}}</a></div>
  </div>
</section>
"""


def index() -> str:
    items = "".join(
        (f'<li id="{s}"><h3><a href="{{{{root}}}}industries/{s}/" style="text-decoration:none;color:var(--blue)">{n}</a></h3><p>{t}</p></li>' if deep else f'<li id="{s}"><h3>{n}</h3><p>{t}</p></li>')
        for s, n, t, deep in ALL
    )
    tiles = "".join(
        f'<a class="ad-tile ad-tile--shade" href="{{{{root}}}}industries/{d["slug"]}/" data-reveal><div class="ad-tile__media">{img(d["hero"], "", "(max-width: 900px) 100vw, 33vw")}</div><p class="ad-tile__type">Industry</p><h3>{d["name"]}</h3><p>{d["purpose"]}</p></a>'
        for d in DEPTH
    )
    return f"""<!--
title: Industries
description: Aldier serves institutions across fifteen industries, with dedicated teams for the public sector, education and financial services.
header: dark
slug: industries
image: assets/film/city.jpg
preload: assets/film/city.jpg
-->
<section class="ad-phero" aria-labelledby="page-title">
  <div class="ad-phero__media">{video('city')}</div>
  <div class="ad-wrap ad-phero__body">
    <p class="ad-eyebrow">Industries</p>
    <h1 id="page-title" class="ad-h1">Industries</h1>
    <p class="ad-lede">We serve institutions across fifteen industries, with dedicated teams for the public sector, education and financial services, where decisions reach the most citizens, students and savers.</p>
  </div>
</section>

<section class="ad-sec ad-on-light" aria-labelledby="depth-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Featured industries</p><h2 id="depth-title" class="ad-h2">Our focus industries</h2></div><p>Dedicated sector teams, supported by research through the Aldier Institute.</p></div>
    <div class="ad-depth" style="margin-top:0">{tiles}</div>
  </div>
</section>

<section class="ad-sec ad-mist" aria-labelledby="all-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Across the economy</p><h2 id="all-title" class="ad-h2">All industries</h2></div><p>In every industry, we build each team from the practices the engagement requires, with specialist advisers where the sector demands them.</p></div>
    <ul class="ad-ilist">{items}</ul>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" aria-labelledby="close-title">
  <div class="ad-wrap">
    <h2 id="close-title" class="ad-h2">Discuss your industry's priorities</h2>
    <p class="ad-lede">Tell us about your organisation and the challenge in front of it. A partner will reply in confidence.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/">Contact us {{{{arrow}}}}</a></div>
  </div>
</section>
"""


def main() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    (SRC / "index.html").write_text(index(), encoding="utf-8")
    for d in DEPTH:
        out = SRC / d["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(depth_page(d), encoding="utf-8")
    print("industries written")


if __name__ == "__main__":
    main()
