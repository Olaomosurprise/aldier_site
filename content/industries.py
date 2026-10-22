"""Writes the industries index and one page per industry into src/industries/.

Run from the project root: python3 content/industries.py
"""

from pathlib import Path

from practices import img, video, subnav

SRC = Path(__file__).resolve().parent.parent / "src" / "industries"

PRACTICE_LINKS = [
    ("Strategy and Transformation", "practices/strategy/"),
    ("Technology and Data", "practices/technology/"),
    ("Cybersecurity and Digital Risk", "practices/cybersecurity/"),
    ("Design and Experience", "practices/design/"),
    ("Communications and Public Affairs", "practices/communications/"),
]

INDUSTRIES = [
    {
        "slug": "agriculture",
        "name": "Agriculture and Food Systems",
        "hero": "fields", "hero_alt": "Cultivated fields stretching to the horizon",
        "purpose": "More productive, resilient and better-financed food systems.",
        "lede": "We work with producers, processors, input suppliers and the programmes that finance them to raise productivity, reduce losses between farm and market, and build the data and partnerships that make the sector investable.",
        "statement": "Most of the value lost in food systems disappears between the farm and the market: in storage, transport, finance and information. That is where we focus.",
        "questions": [
            ("Where should we invest along the value chain?", "Value-chain economics, sourcing models and the partnerships that secure supply."),
            ("How do we reach smallholders at scale?", "Aggregation, extension and payment models designed with farmers, tested in the field and costed before scale-up."),
            ("How do we use data and digital tools?", "Platforms for traceability, credit scoring and market information that farmers and buyers will actually use."),
            ("How do we make a programme investable?", "Business cases, risk sharing and reporting that give lenders and development funders confidence."),
        ],
    },
    {
        "slug": "creative",
        "name": "Creative and Cultural Industries",
        "hero": "ind-creative", "hero_alt": "A film crew at work on a lit soundstage",
        "purpose": "Creative businesses built to grow and to last.",
        "lede": "We help studios, labels, publishers, fashion houses and cultural institutions strengthen their business models, protect their rights, reach audiences directly and build the organisations their talent deserves.",
        "statement": "Creative work travels further than ever, yet much of its value is captured by others. Ownership of rights, data and audience relationships decides who benefits.",
        "questions": [
            ("How do we turn creative success into a durable business?", "Strategy, operating models and financing for companies built around talent."),
            ("How do we own the relationship with our audience?", "Direct channels, digital products and the data to understand who is listening, watching and buying."),
            ("How do we protect and monetise our rights?", "Rights management, licensing strategy and the systems that track what is owed."),
            ("How should a cultural institution evolve?", "Programming, visitor experience, funding and digital strategy for museums, theatres and festivals."),
        ],
    },
    {
        "slug": "development",
        "name": "Development and Social Impact",
        "hero": "ind-development", "hero_alt": "Children sitting on steps with their books",
        "purpose": "Programmes that measure, and deliver, the change they promise.",
        "lede": "We work with foundations, multilateral institutions and non-profits on strategy, programme design and delivery, and on the evidence that shows what their funding achieves.",
        "statement": "Funders increasingly ask what changed, for whom and at what cost. Programmes designed to answer those questions from the start deliver more, and attract more support.",
        "questions": [
            ("Where should we focus our resources?", "Portfolio strategy grounded in evidence of need, cost and likely impact."),
            ("How do we design a programme that scales?", "Delivery models, partnerships and operating plans built for the second phase as well as the pilot."),
            ("How do we measure what we achieve?", "Results frameworks, data systems and evaluations that boards and funders trust."),
            ("How do we strengthen our own organisation?", "Governance, leadership, systems and safeguarding for organisations growing quickly."),
        ],
    },
    {
        "slug": "education",
        "name": "Education",
        "hero": "university-colonnade", "hero_alt": "The white colonnade of a university building",
        "purpose": "Institutions that run well, and graduates ready for work.",
        "lede": "We work with universities, schools, education systems and the organisations that fund and supply them, on finances, operations, the student experience and the transition from learning to work.",
        "statement": "Students judge an institution by its services as much as its teaching: housing, portals, payments, safety and the jobs that follow graduation. The academic mission depends on everything around it.",
        "questions": [
            ("How do we fund growth responsibly?", "Financial strategy, auxiliary enterprise and partnerships that diversify income."),
            ("How do we modernise the student journey?", "Admissions, records, payments and learning platforms redesigned around students and staff."),
            ("How do we prepare graduates for work?", "Employer partnerships, work-based learning and career services measured by outcomes."),
            ("How do we protect research and student data?", "Security and data protection suited to open campuses and international collaboration."),
            ("How do we compete for students and partners?", "Positioning, identity and the experience prospective students meet online and on arrival."),
            ("How do we govern a growing institution?", "Operating models, decision rights and shared services for multi-campus systems."),
        ],
        "spot": ("GENIVY", "GENIVY is the international guild of students that Aldier helped found. Owned by its members, it organises the work already present on university campuses and pays students to run it.", "work/genivy/", "Read the case study", "lecture", "Students listening in a lecture hall"),
    },
    {
        "slug": "energy",
        "name": "Energy, Power and Natural Resources",
        "hero": "solar", "hero_alt": "Rows of solar panels under an open sky",
        "purpose": "Reliable, affordable energy, and resources developed responsibly.",
        "lede": "We work with generators, distributors, oil and gas companies, miners, regulators and investors on strategy, operational performance, capital projects and the transition to cleaner energy.",
        "statement": "Energy markets are being reshaped by reform, new technology and the cost of capital at the same time. The winners plan for all three together.",
        "questions": [
            ("How do we improve operational and commercial performance?", "Loss reduction, metering, billing and collection for utilities; productivity and cost for producers."),
            ("Which transition investments make sense for us?", "Portfolio strategy for renewables, distributed generation and storage, tested against realistic demand and tariffs."),
            ("How do we deliver capital projects on time?", "Project assurance, contracting strategy and governance for large investments."),
            ("How do we protect critical infrastructure?", "Operational technology security, resilience and incident readiness for grids and plants."),
            ("How do we earn our licence to operate?", "Community, regulatory and investor engagement grounded in transparent reporting."),
        ],
    },
    {
        "slug": "financial-services",
        "name": "Financial Services",
        "hero": "bank-portico", "hero_alt": "The columned portico of a stone banking hall",
        "purpose": "Growth with the controls that customers and regulators depend on.",
        "lede": "We work with banks, insurers, asset managers, payments companies and their regulators to grow, modernise their systems and serve customers better, while strengthening the controls that protect them.",
        "statement": "Customers rarely think about their bank until something goes wrong. Our work is to make that moment rare, and to ensure the institution is ready when it comes.",
        "questions": [
            ("Where should we grow, and what should we stop?", "Portfolio strategy, product economics and the operating model to serve chosen segments profitably."),
            ("How do we replace core systems safely?", "Core platform selection, migration planning and delivery assurance."),
            ("Are we ready for a cyber incident?", "Readiness against supervisory expectations, incident simulation and third-party risk."),
            ("How do we meet new regulation efficiently?", "Regulatory change programmes that leave durable capabilities behind once the deadline has passed."),
            ("How do we serve customers better on every channel?", "Service design for branches, apps and contact centres, built from customer evidence."),
            ("How do we explain results, deals and setbacks?", "Investor, regulatory and public communication around results, transactions and incidents."),
        ],
        "spot": ("Risk and compliance designed into products", "We bring risk, security and compliance specialists into product teams from the first design, so that new products launch with their controls in place.", "practices/cybersecurity/", "Cybersecurity and Digital Risk", "blue-facade", "A building facade in saturated blue"),
    },
    {
        "slug": "healthcare",
        "name": "Healthcare and Life Sciences",
        "hero": "ward", "hero_alt": "A clean, well-lit hospital ward",
        "purpose": "Better care, delivered more reliably to more people.",
        "lede": "We work with hospitals, health systems, insurers, pharmaceutical companies and public health agencies on strategy, operations, digital health and the patient experience.",
        "statement": "In healthcare, service design is a matter of safety. Small improvements in flow, records and communication change outcomes for patients.",
        "questions": [
            ("How do we improve access and patient flow?", "Capacity planning, scheduling and pathway redesign across clinics, wards and theatres."),
            ("How do we digitise safely?", "Electronic records, telemedicine and data platforms chosen and delivered with clinicians."),
            ("How do we protect patient data?", "Security and privacy programmes for organisations that hold the most sensitive records."),
            ("How do we build a sustainable health business?", "Growth strategy, payer partnerships and operating models for providers and insurers."),
        ],
    },
    {
        "slug": "hospitality",
        "name": "Hospitality and Travel",
        "hero": "ind-hospitality", "hero_alt": "A hotel lobby with designer furniture and wood-panelled walls",
        "purpose": "Experiences guests return to, run at a profit.",
        "lede": "We work with hotel groups, airlines, tourism boards and destinations on brand, guest experience, distribution and the design of the places where guests are welcomed.",
        "statement": "Guests remember how a stay or a journey made them feel, and they share it. Consistent experience, designed and measured, is the most valuable asset in the sector.",
        "questions": [
            ("How do we position our brand and destination?", "Brand strategy, identity and the story that sets a property or place apart."),
            ("How do we design the guest experience?", "Journeys mapped from booking to departure, and the spaces, services and staff training that deliver them."),
            ("How do we grow direct bookings?", "Digital products, loyalty and distribution strategy that reduce dependence on intermediaries."),
            ("How do we develop a new property or destination?", "Feasibility, concept, spatial planning and the operating model, from first sketch to opening."),
        ],
    },
    {
        "slug": "manufacturing",
        "name": "Manufacturing and Industrials",
        "hero": "ind-manufacturing", "hero_alt": "Engineers at work in an automotive factory",
        "purpose": "Productive, safe and resilient operations.",
        "lede": "We work with manufacturers and industrial groups on operational performance, supply-chain resilience, digital manufacturing and the security of the systems that run their plants.",
        "statement": "Competitiveness in manufacturing is decided on the shop floor and in the supply chain. Data that reaches the people running the line is where improvement begins.",
        "questions": [
            ("How do we raise productivity?", "Operational diagnostics, lean improvement and the routines that sustain gains."),
            ("How resilient is our supply chain?", "Supplier risk, sourcing strategy and inventory policy tested against realistic disruptions."),
            ("Where do digital tools pay back?", "Use cases for automation, analytics and AI selected for value and implemented with operators."),
            ("How do we secure our operational technology?", "Security for plant systems, where an incident stops production as well as data."),
        ],
    },
    {
        "slug": "private-capital",
        "name": "Private Capital",
        "hero": "ind-capital", "hero_alt": "A financial candlestick chart on a dark screen",
        "purpose": "Better investment decisions, and value created after the deal.",
        "lede": "We work with private equity, venture and infrastructure investors from diligence to exit: assessing targets, planning integration and leading the value-creation work in portfolio companies.",
        "statement": "Returns increasingly depend on what investors do after the deal closes. Operational, technology and reputational diligence before signing makes that work faster.",
        "questions": [
            ("Is this the right target?", "Commercial, technology and cyber diligence completed to transaction timetables."),
            ("What is the value-creation plan?", "The first hundred days and the initiatives that drive growth and margin."),
            ("How do we strengthen portfolio companies?", "Leadership, operating model, systems and reporting fit for the next stage."),
            ("How do we prepare for exit?", "Equity story, data room readiness and stakeholder communication."),
        ],
    },
    {
        "slug": "public-sector",
        "name": "Public Sector and Government",
        "hero": "civic-hall", "hero_alt": "A stone civic building facing an empty square",
        "purpose": "Public services that deliver for citizens, and reforms that last.",
        "lede": "We work with ministries, agencies, regulators and state enterprises to design reforms that can be delivered, modernise services and build institutions that sustain them through changes of leadership.",
        "statement": "Most of the work of reform happens after the announcement: in procurement, systems, people and the persistence to see it through.",
        "questions": [
            ("How do we turn priorities into a delivery plan?", "Programmes with owners, budgets and measures that a delivery unit can track week by week."),
            ("Which services should go digital first?", "Services chosen by volume and need, redesigned around citizens, and built on infrastructure the state controls."),
            ("How do we buy technology well?", "Procurement strategies, specifications and contracts that keep the state in control of its systems and data."),
            ("How do we protect citizens' data?", "Data protection programmes and security readiness for agencies that hold sensitive records."),
            ("How do we explain a difficult reform?", "Public engagement and communication that prepares citizens for change before it reaches them."),
            ("How do we make reform last?", "Institutions, rules and capabilities designed to continue after the people who launched them have moved on."),
        ],
        "spot": ("Building delivery units", "We help governments establish small, senior delivery units that track commitments against evidence, escalate problems early and publish progress that citizens can check.", "practices/strategy/", "Strategy and Transformation", "towers", "Office towers rising into a blue sky"),
    },
    {
        "slug": "real-estate",
        "name": "Real Estate and Infrastructure",
        "hero": "lekki-bridge-wide", "hero_alt": "A cable-stayed bridge crossing open water",
        "purpose": "Places and networks that are planned, financed and delivered well.",
        "lede": "We work with developers, investors and public owners on strategy, project delivery, the design of places and the technology and services that bring them to life.",
        "statement": "A building or network is judged for decades by how well it serves the people who use it. Those decisions are made in the first months of planning.",
        "questions": [
            ("What should we build, and where?", "Market assessment, feasibility and portfolio strategy for development and investment."),
            ("How do we deliver major projects?", "Project assurance, procurement and governance that keep cost and schedule under control."),
            ("How do we design places people value?", "Masterplanning, spatial design and the services that make a development work."),
            ("How do we make our assets smarter and safer?", "Building technology, data and security for connected assets."),
        ],
    },
    {
        "slug": "tmt",
        "name": "Telecoms, Media and Technology",
        "hero": "ind-tmt", "hero_alt": "Telecommunication towers silhouetted at sunset",
        "purpose": "Networks, platforms and products that win customers and keep their trust.",
        "lede": "We work with operators, technology companies, broadcasters and publishers on growth strategy, product development, customer experience and the security and regulation of digital services.",
        "statement": "The companies that shape public life online are held to rising standards of security, privacy and conduct. Meeting them well is a source of advantage.",
        "questions": [
            ("Where are our next sources of growth?", "Strategy for new services, markets and partnerships, tested against customer evidence."),
            ("How do we build products customers choose?", "Product strategy, design and delivery for digital services."),
            ("How do we manage regulation and public scrutiny?", "Policy engagement, compliance and the communication that sustains trust."),
            ("How do we protect our networks and customers?", "Security, resilience and incident readiness at the scale of national infrastructure."),
        ],
    },
    {
        "slug": "transport",
        "name": "Transport and Logistics",
        "hero": "port", "hero_alt": "Container cranes at a busy port",
        "purpose": "Goods and people moved reliably, efficiently and safely.",
        "lede": "We work with ports, airlines, rail and road operators and logistics companies on network strategy, operational performance, digital systems and the customer experience.",
        "statement": "Reliability is the product in transport and logistics. It depends on assets, systems and people working to the same timetable.",
        "questions": [
            ("How do we improve reliability and throughput?", "Operational diagnostics, scheduling and capacity planning across networks and terminals."),
            ("Where should we invest?", "Network and asset strategy, business cases and partnership models."),
            ("How do we digitise operations?", "Tracking, booking and planning systems selected and delivered with operators."),
            ("How do we serve customers better?", "Service design for passengers and shippers, from booking to delivery."),
        ],
    },
    {
        "slug": "consumer",
        "name": "Consumer and Retail",
        "hero": "ind-consumer", "hero_alt": "Shoppers in a brightly lit supermarket aisle",
        "purpose": "Brands and retailers that customers trust and return to.",
        "lede": "We work with consumer brands, retailers and distributors on growth strategy, brand, the shopping experience across channels and the operations that keep shelves full.",
        "statement": "Consumers reward brands that are easy to find, easy to buy and consistent in what they promise. Each depends on decisions far from the shelf.",
        "questions": [
            ("Where should we grow?", "Category, channel and market strategy grounded in consumer and sales data."),
            ("How do we strengthen our brand?", "Brand positioning, identity and campaigns that build preference over time."),
            ("How do we sell across channels?", "Commerce, distribution and the in-store and online experience."),
            ("How do we run a leaner supply chain?", "Planning, sourcing and logistics that improve availability and cost."),
        ],
    },
]

ORDER = sorted(INDUSTRIES, key=lambda d: d["name"])
BY_SLUG = {d["slug"]: d for d in INDUSTRIES}


def tile(r: dict, attrs: str = "") -> str:
    return (
        f'<a class="ad-tile ad-tile--shade" href="{{{{root}}}}industries/{r["slug"]}/"{attrs} data-reveal>'
        f'<div class="ad-tile__media">{img(r["hero"], "", "(max-width: 900px) 100vw, 33vw")}</div>'
        f'<p class="ad-tile__type">Industry</p><h3>{r["name"]}</h3><p>{r["purpose"]}</p></a>'
    )


def page(d: dict) -> str:
    qs = "".join(f'<div class="ad-card"><h3>{q}</h3><p>{a}</p></div>' for q, a in d["questions"])
    pills = "".join(f'<li><a href="{{{{root}}}}{h}">{n}</a></li>' for n, h in PRACTICE_LINKS)
    spot = ""
    if d.get("spot"):
        title, text, link, link_label, image, alt = d["spot"]
        label = link_label if link_label.startswith("Read") else f"{link_label} practice"
        spot = f"""
<section class="ad-sec ad-dark" id="work" aria-labelledby="spot-title">
  <div class="ad-wrap ad-split ad-split--flip">
    <div class="ad-split__media" data-reveal>{img(image, alt)}</div>
    <div data-reveal>
      <p class="ad-eyebrow">Our work</p>
      <h2 id="spot-title" class="ad-h2">{title}</h2>
      <p class="ad-lede">{text}</p>
      <a class="ad-link" href="{{{{root}}}}{link}">{label} {{{{arrow}}}}</a>
    </div>
  </div>
</section>
"""
    i = ORDER.index(d)
    related = "".join(tile(ORDER[(i + k) % len(ORDER)]) for k in (1, 2, 3))
    tabs = [("help", "How we help clients"), ("perspective", "Our perspective")]
    if spot:
        tabs.append(("work", "Our work"))
    tabs += [("practices", "Capabilities"), ("contact", "Contact")]
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
{subnav(d['name'], tabs)}
<section class="ad-sec ad-mist" id="help" aria-labelledby="q-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">How we help clients</p><h2 id="q-title" class="ad-h2">Questions we help leaders answer</h2></div><p>Most draw on more than one of our practices.</p></div>
    <div class="ad-cards">{qs}</div>
  </div>
</section>

<section class="ad-sec ad-statement ad-on-light" id="perspective" aria-label="Our perspective">
  <div class="ad-wrap"><p class="ad-eyebrow">Our perspective</p><p class="ad-lit" data-light>{d['statement']}</p></div>
</section>
{spot}
<section class="ad-sec ad-on-light" id="practices" aria-labelledby="pr-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Capabilities</p><h2 id="pr-title" class="ad-h2">Our practices in {d['name']}</h2></div></div>
    <ul class="ad-pills">{pills}</ul>
    <p class="ad-eyebrow ad-mt">Related industries</p>
    <div class="ad-depth">{related}</div>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" id="contact" aria-labelledby="close-title">
  <div class="ad-wrap">
    <p class="ad-eyebrow" style="justify-content:center">{d['name']}</p>
    <h2 id="close-title" class="ad-h2 ad-mt-s">Connect with our {d['name']} team</h2>
    <p class="ad-lede">Tell us about the challenge in front of you. A partner will reply in confidence.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/?topic={d['name'].replace(' ', '%20')}">Contact us {{{{arrow}}}}</a></div>
  </div>
</section>
"""


def index() -> str:
    tiles = "".join(tile(d, f' id="{d["slug"]}"') for d in ORDER)
    return f"""<!--
title: Industries
description: Aldier serves organisations across fifteen industries, bringing strategy, technology, cybersecurity, design and communications to the issues that define each one.
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
    <p class="ad-lede">We serve organisations across fifteen industries, combining knowledge of each sector with the capabilities of our five practices.</p>
  </div>
</section>

<section class="ad-sec ad-on-light" aria-labelledby="all-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Our industries</p><h2 id="all-title" class="ad-h2">Explore our industries</h2></div><p>Each page sets out the questions we help leaders answer, our perspective on the sector and how to reach us.</p></div>
    <div class="ad-depth" style="margin-top:0">{tiles}</div>
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
    for d in INDUSTRIES:
        out = SRC / d["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(d), encoding="utf-8")
    print(f"industries written: {len(INDUSTRIES)}")


if __name__ == "__main__":
    main()
