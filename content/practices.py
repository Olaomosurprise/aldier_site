"""Writes the five practice pages and the practices index into src/.

Run from the project root: python3 content/practices.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from feed import latest  # noqa: E402

SRC = Path(__file__).resolve().parent.parent / "src" / "practices"

PRACTICES = [
    {
        "slug": "strategy",
        "no": "01",
        "verb": "Decide",
        "name": "Strategy and Transformation",
        "film": "decide",
        "purpose": "Setting direction, and delivering it across the whole institution.",
        "lede": "We work with boards and leadership teams on the choices that define an institution, then build the programmes, measures and routines that carry those choices through to results.",
        "question": "Most strategies falter in execution. The institutions that succeed choose fewer priorities, fund them fully, measure them honestly and stop what is failing early.",
        "services": [
            ("Corporate and public strategy", "Clear choices on where to compete or serve, and what to stop."),
            ("Operating model and organisation", "Structures, decision rights and governance matched to the strategy."),
            ("Mergers, partnerships and restructuring", "Diligence, integration and separation, planned before the announcement."),
            ("Transformation office", "Programme leadership that tracks every commitment through to delivery."),
            ("Performance and cost", "Costs reduced where they add little, and capacity moved to priorities."),
            ("Growth and new ventures", "New services, markets and businesses tested before they are scaled."),
        ],
        "feature": "phases",
        "joins": ["technology", "communications"],
        "insight": ("the-joins", "Where transformations fail: the gaps between disciplines"),
        "image": "team-room",
    },
    {
        "slug": "technology",
        "no": "02",
        "verb": "Build",
        "name": "Technology and Data",
        "film": "build",
        "purpose": "Systems and data that institutions can rely on.",
        "lede": "We advise on what to build or buy, run the market on our clients' behalf, assure delivery and support the first months of live operation, when large programmes are most exposed.",
        "question": "The fate of a large technology programme is usually settled before any code is written: in its requirements, its contract and its timetable. That is where we concentrate our effort.",
        "services": [
            ('Technology strategy and architecture', "A target architecture tied to the institution's priorities, sequenced for its budget and people."),
            ("Selection and procurement advisory", "Requirements, market testing, evaluation and contracts that protect the buyer."),
            ("Delivery assurance", "Independent oversight of major programmes, with early warning and clear reporting."),
            ("Data and analytics", "Governance, platforms and reporting that leaders use to decide."),
            ("Applied AI", "Use cases selected for value and risk, governed from the outset and measured in operation."),
            ("Cloud and infrastructure", "Hosting, resilience and cost decisions based on evidence, with exit routes designed in."),
        ],
        "feature": "split",
        "joins": ["cybersecurity", "design"],
        "insight": ("before-the-breach", "Before the breach: seven questions a board can ask this quarter"),
        "image": "data-hall",
    },
    {
        "slug": "cybersecurity",
        "no": "03",
        "verb": "Protect",
        "name": "Cybersecurity and Digital Risk",
        "film": "guard",
        "purpose": "Preparing institutions for the incidents they will face.",
        "lede": "We help boards and executives understand their exposure, strengthen their defences and rehearse their response, so that a serious incident is contained, reported and recovered from with confidence.",
        "question": "A serious breach is a technical event for hours and a governance event for months. Boards that have rehearsed their response recover faster, and keep the confidence of customers and regulators.",
        "services": [
            ("Cyber strategy and governance", "Risk appetite, accountability and reporting set at board level."),
            ("Readiness assessment", "Assessment against ISO/IEC 27001 and the NIST Cybersecurity Framework, prioritised by consequence."),
            ("Data protection and privacy", "Compliance programmes for the data protection laws that apply to each client."),
            ("Incident response and simulation", "Playbooks, decision rights and live exercises for boards, technical teams and spokespeople."),
            ("Third-party and supply-chain risk", "Contracts, assurance and monitoring for the suppliers that hold data or run systems."),
            ("Resilience and continuity", "Critical services identified, recovery targets set and continuity plans tested."),
        ],
        "feature": "timeline",
        "joins": ["technology", "communications"],
        "insight": ("before-the-breach", "Before the breach: seven questions a board can ask this quarter"),
        "image": "server-engineer",
    },
    {
        "slug": "design",
        "no": "04",
        "verb": "Design",
        "name": "Design and Experience",
        "film": "design",
        "purpose": "Brands, services, products and places people choose to use.",
        "lede": "Working through Aldier Studio, the practice designs and builds the points at which an institution meets the people it serves: its identity, its services, its digital products, its films and its spaces.",
        "question": "People judge an institution by the last service it gave them. Design turns sound decisions into experiences people can understand, use and trust.",
        "services": [
            ("Brand and identity", "Names, voice and visual identity, with guidelines that hold across every channel."),
            ("Service design", "Services redesigned around the people who use them, and specified for delivery."),
            ("Digital products", "Websites, applications and platforms built to accessibility standards and measured in use."),
            ('Film and motion', "Documentary, campaign and explainer films that carry an institution's story."),
            ("Spatial and environmental design", "Branches, campuses, offices and public spaces planned around the services they house."),
            ("Research and testing", "Interviews, observation and usability testing that ground decisions in evidence."),
        ],
        "feature": "studio",
        "joins": ["technology", "communications"],
        "insight": ("the-handover", "The handover: building institutions that outlast their founders"),
        "image": "wireframe",
    },
    {
        "slug": "communications",
        "no": "05",
        "verb": "Explain",
        "name": "Communications and Public Affairs",
        "film": "communicate",
        "purpose": "Earning the trust of the people who decide an institution's future.",
        "lede": "We help institutions build their reputation, engage government and investors, and prepare for the moments when their account of themselves is tested in public.",
        "question": "Reputation follows conduct. Communication earns its value when the decision behind it is sound, and the account given of it is clear, consistent and timely.",
        "services": [
            ('Corporate reputation', "A clear account of the institution's purpose and record, tested with the audiences that matter."),
            ("Crisis and issues management", "Preparation, counsel and statements for the first hours of a crisis and the weeks that follow."),
            ("Government relations and public affairs", "Policy analysis, engagement with officials and legislators, and coalitions, conducted openly and lawfully."),
            ("Investor and financial communications", "Results, transactions and disclosures written for clarity as well as compliance."),
            ("Internal and change communications", "Leaders equipped to explain change to their people before it happens."),
            ('Executive positioning', "Speeches, interviews and articles that set out leaders' views on the issues they own."),
        ],
        "feature": "quote",
        "joins": ["strategy", "cybersecurity"],
        "insight": ("the-joins", "Where transformations fail: the gaps between disciplines"),
        "image": "microphones",
    },
]

BY_SLUG = {p["slug"]: p for p in PRACTICES}
APPROACH = {"phases": "Our approach", "split": "Independence", "timeline": "Incident simulation", "studio": "Aldier Studio", "quote": "Our standard"}


def video(name: str, cls: str = "", ambient: bool = False) -> str:
    amb = " data-ambient" if ambient else ""
    autoplay = "" if ambient else " autoplay loop"
    return (
        f'<video class="{cls}" muted playsinline{autoplay} preload="metadata" poster="{{{{root}}}}assets/film/{name}.webp"{amb} aria-hidden="true">'
        f'<source src="{{{{root}}}}assets/film/{name}.webm" type="video/webm"><source src="{{{{root}}}}assets/film/{name}.mp4" type="video/mp4"></video>'
    )


def img(key: str, alt: str = "", sizes: str = "(max-width: 900px) 100vw, 50vw", style: str = "") -> str:
    st = f' style="{style}"' if style else ""
    return (
        f'<img src="{{{{root}}}}assets/photos/{key}-1600.webp" srcset="{{{{root}}}}assets/photos/{key}-800.webp 800w, {{{{root}}}}assets/photos/{key}-1600.webp 1600w, {{{{root}}}}assets/photos/{key}-2400.webp 2400w" '
        f'sizes="{sizes}" alt="{alt}" loading="lazy"{st}>'
    )


def subnav(title: str, tabs: list) -> str:
    """A sticky in-page navigation bar, as on the practice and industry pages of the leading firms."""
    links = "".join(f'<li><a href="#{i}">{label}</a></li>' for i, label in tabs)
    return f'<nav class="ad-subnav" aria-label="On this page" data-subnav><div class="ad-wrap"><span class="ad-subnav__title">{title}</span><ul>{links}</ul></div></nav>'


def feature(p: dict) -> str:
    kind = p["feature"]
    if kind == "phases":
        return """<section class="ad-sec ad-dark" id="approach" aria-labelledby="how-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Our approach</p><h2 id="how-title" class="ad-h2">From diagnosis to delivery</h2></div><p>The team that diagnoses the problem stays to deliver the answer, and hands over only when the client's own people are ready to lead.</p></div>
    <ol class="ad-steps">
      <li><h3>Diagnose</h3><p>Six to eight weeks establishing the facts: the economics, the constraints, the people and the record of past efforts.</p></li>
      <li><h3>Decide</h3><p>A small set of choices, each with its costs and risks, for leadership to take and own.</p></li>
      <li><h3>Deliver</h3><p>A transformation office that tracks each commitment against named owners and dates, and reports progress accurately.</p></li>
      <li><h3>Hand over</h3><p>Capabilities, measures and documentation transferred to the client's own teams.</p></li>
    </ol>
  </div>
</section>"""
    if kind == "split":
        return f"""<section class="ad-sec ad-ice" id="approach" aria-labelledby="side-title">
  <div class="ad-wrap ad-split">
    <div class="ad-split__media ad-split__media--frame" data-reveal>{img('pr-technology', 'A team working together on laptops')}</div>
    <div data-reveal>
      <p class="ad-eyebrow">Independence</p>
      <h2 id="side-title" class="ad-h2">Independent of every vendor</h2>
      <p class="ad-lede">Aldier accepts no commission, referral fee or reseller margin from any technology supplier. Our clients are the only party paying for our advice, and every evaluation file belongs to them.</p>
      <dl class="ad-facts ad-mt"><div><dt>Vendor fees</dt><dd>None</dd></div><div><dt>Evaluation file</dt><dd>Yours</dd></div><div><dt>Live support</dt><dd>First months</dd></div></dl>
    </div>
  </div>
</section>"""
    if kind == "timeline":
        return """<section class="ad-sec ad-night" id="approach" aria-labelledby="day-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Incident simulation</p><h2 id="day-title" class="ad-h2">Rehearsing the first hours of a breach</h2></div><p>Our simulation runs a realistic incident in real time, with directors, technical leads and spokespeople taking the decisions that would fall to them.</p></div>
    <ol class="ad-steps">
      <li><h3>Detection</h3><p>An ambiguous alert. Who declares an incident, and how quickly does the chief executive hear?</p></li>
      <li><h3>Containment</h3><p>Systems isolated, evidence preserved, and a choice between keeping services running and stopping the spread.</p></li>
      <li><h3>Notification</h3><p>Regulators, customers and partners told what they must be told, within the time the law allows, in words agreed in advance.</p></li>
      <li><h3>Recovery and review</h3><p>Services restored in the right order, and an honest account of what failed, published to those who need it.</p></li>
    </ol>
  </div>
</section>"""
    if kind == "studio":
        return f"""<section class="ad-sec ad-on-light" id="approach" aria-labelledby="studio-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Aldier Studio</p><h2 id="studio-title" class="ad-h2">Design and production under one roof</h2></div><p>Designers, film-makers, architects and engineers work alongside the strategists who shaped the brief.</p></div>
    <div class="ad-mosaic">
      <div class="ad-tile ad-tile--shade ad-span-6 ad-row-2 ad-wide-m" data-reveal><div class="ad-tile__media">{img('pr-design', 'A designer working on a drawing tablet beside colour swatches', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Digital products</p><h3>Designed to accessibility standards, and measured once live.</h3></div>
      <div class="ad-tile ad-tile--shade ad-span-6" data-reveal><div class="ad-tile__media">{img('abuja-arcade', 'A brick arcade framed by apartment blocks', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Spatial design</p><h3>Branches, campuses and offices planned around the service they house.</h3></div>
      <div class="ad-tile ad-tile--shade ad-span-6" data-reveal><div class="ad-tile__media">{img('render-lines', '', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Identity</p><h3>Every colour, typeface and mark specified for consistent use at scale.</h3></div>
    </div>
    <p class="ad-mt"><a class="ad-link" href="{{{{root}}}}studio/">Visit Aldier Studio {{{{arrow}}}}</a></p>
  </div>
</section>"""
    if kind == "quote":
        return f"""<section class="ad-sec ad-dark" id="approach" aria-labelledby="principle-title">
  <div class="ad-wrap ad-split">
    <div data-reveal>
      <p class="ad-eyebrow">Our standard</p>
      <h2 id="principle-title" class="ad-vh">Our standard</h2>
      <p class="ad-quote">Every statement we help a client make must be accurate, complete and able to withstand scrutiny.</p>
      <p class="ad-quote-by">The standard applied to every engagement in the practice.</p>
    </div>
    <div class="ad-split__media ad-split__media--wide" data-reveal>{img(p['image'], 'Four microphones lined up at a podium')}</div>
  </div>
</section>"""
    return ""


def page(p: dict) -> str:
    services = "".join(f"<li><h3>{h}</h3><p>{t}</p></li>" for h, t in p["services"])
    joins = "".join(
        f'<a class="ad-card" href="{{{{root}}}}practices/{BY_SLUG[s]["slug"]}/"><span class="ad-tile__type" style="color:var(--blue)">Practice</span><h3>{BY_SLUG[s]["name"]}</h3><p>{BY_SLUG[s]["purpose"]}</p><span class="ad-link">Explore {{{{arrow}}}}</span></a>'
        for s in p["joins"]
    )
    slug, title = p["insight"]
    return f"""<!--
title: {p['name']}
description: {p['purpose']} How Aldier's {p['name']} practice helps clients.
header: dark
slug: practice-{p['slug']}
image: assets/film/{p['film']}.jpg
preload: assets/film/{p['film']}.webp
-->
<section class="ad-phero" aria-labelledby="page-title">
  <div class="ad-phero__media">{video(p['film'])}</div>
  <div class="ad-wrap ad-phero__body">
    <p class="ad-phero__crumb"><a href="{{{{root}}}}practices/">Practices</a> / {p['name']}</p>
    <p class="ad-eyebrow">Practice</p>
    <h1 id="page-title" class="ad-h1">{p['name']}</h1>
    <p class="ad-lede"><b>{p['purpose']}</b> {p['lede']}</p>
  </div>
</section>
{subnav(p["name"], [("help", "How we help clients"), ("perspective", "Our perspective"), ("approach", APPROACH[p["feature"]]), ("related", "Insights"), ("contact", "Contact")])}
<section class="ad-sec ad-mist" id="help" aria-labelledby="services-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Capabilities</p><h2 id="services-title" class="ad-h2">How we help clients</h2></div><p>Clients engage these capabilities individually or in combination with other practices.</p></div>
    <ol class="ad-steps">{services}</ol>
  </div>
</section>

<section class="ad-sec ad-statement ad-on-light" id="perspective" aria-label="Our perspective">
  <div class="ad-wrap">
    <p class="ad-eyebrow">Our perspective</p>
    <p class="ad-lit" data-light>{p['question']}</p>
  </div>
</section>

{feature(p)}

<section class="ad-sec ad-on-light" id="related" aria-labelledby="latest-title">
  <div class="ad-wrap">
    {latest(p["slug"])}
  </div>
</section>

<section class="ad-sec ad-sec--tight ad-mist" aria-labelledby="joins-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Explore further</p><h2 id="joins-title" class="ad-h2">Related practices</h2></div></div>
    <div class="ad-cards">
      {joins}
      <a class="ad-card" style="background:var(--ink);color:#fff;border-color:transparent" href="{{{{root}}}}podcast/"><span class="ad-tile__type" style="color:var(--sky)">Podcast</span><h3>The Aldier Podcast</h3><p style="color:rgba(255,255,255,.75)">Conversations with the people who build institutions. Season one coming soon.</p><span class="ad-link" style="color:var(--sky)">Listen {{{{arrow}}}}</span></a>
    </div>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" id="contact" aria-labelledby="close-title">
  <div class="ad-wrap">
    <p class="ad-eyebrow" style="justify-content:center">{p['name']}</p>
    <h2 id="close-title" class="ad-h2 ad-mt-s">Connect with our {p['name']} practice</h2>
    <p class="ad-lede">Tell us about the challenge in front of you. A partner will reply in confidence.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/?topic={p['name'].replace(' ', '%20')}">Contact us {{{{arrow}}}}</a></div>
  </div>
</section>
"""


def index() -> str:
    rows = "".join(
        f"""<a class="ad-acc__item{' is-open' if i == 0 else ''}" href="{{{{root}}}}practices/{p['slug']}/">
        <video muted loop playsinline preload="none" poster="{{{{root}}}}assets/film/{p['film']}.webp" aria-hidden="true"><source data-src="{{{{root}}}}assets/film/{p['film']}.webm" type="video/webm"><source data-src="{{{{root}}}}assets/film/{p['film']}.mp4" type="video/mp4"></video>
        <div class="ad-acc__body"><span class="ad-acc__no">{p['no']}</span><span class="ad-acc__name">{p['name']}</span><div class="ad-acc__more"><div><p>{p['purpose']}</p><span class="ad-link">Explore the practice {{{{arrow}}}}</span></div></div></div>
      </a>"""
        for i, p in enumerate(PRACTICES)
    )
    detail = "".join(
        f"""<li id="{p['slug']}"><h3><a href="{{{{root}}}}practices/{p['slug']}/" style="text-decoration:none">{p['name']}</a></h3><p>{'; '.join(h for h, _ in p['services'])}.</p></li>"""
        for p in PRACTICES
    )
    return f"""<!--
title: Practices
description: Aldier's five practices: strategy, technology and data, cybersecurity, design and experience, and communications and public affairs.
header: dark
slug: practices
image: assets/film/civic.jpg
preload: assets/film/civic.webp
-->
<section class="ad-phero" aria-labelledby="page-title">
  <div class="ad-phero__media">{video('civic')}</div>
  <div class="ad-wrap ad-phero__body">
    <p class="ad-eyebrow">Capabilities</p>
    <h1 id="page-title" class="ad-h1">Our practices</h1>
    <p class="ad-lede">Aldier advises clients through five practices. Clients engage one, or bring several together on a single engagement.</p>
  </div>
</section>

<section class="ad-sec ad-dark" aria-labelledby="five-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Practices</p><h2 id="five-title" class="ad-h2">Explore our practices</h2></div><p>Each practice page sets out how we help clients, our approach and the people to contact.</p></div>
    <div class="ad-acc">{rows}</div>
  </div>
</section>

<section class="ad-sec ad-on-light" aria-labelledby="all-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Capabilities</p><h2 id="all-title" class="ad-h2">All capabilities</h2></div><p>Thirty capabilities across the five practices, available individually or in combination.</p></div>
    <ul class="ad-ilist" style="grid-template-columns:1fr">{detail}</ul>
  </div>
</section>

<section class="ad-sec ad-mist" aria-labelledby="model-title">
  <div class="ad-wrap ad-split">
    <div class="ad-split__media" data-reveal>{img('working-table', 'Colleagues working through papers at a table')}</div>
    <div data-reveal>
      <p class="ad-eyebrow">How we work</p>
      <h2 id="model-title" class="ad-h2">Integrated teams, led by one partner</h2>
      <p class="ad-lede">Each engagement is led by a named partner who is accountable for the whole of it. Teams are drawn from the practices the work requires, and every deliverable is reviewed by a colleague outside the team before it reaches the client.</p>
      <a class="ad-link" href="{{{{root}}}}about/#how-we-work">How we work {{{{arrow}}}}</a>
    </div>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" aria-labelledby="close-title">
  <div class="ad-wrap">
    <h2 id="close-title" class="ad-h2">Where to start</h2>
    <p class="ad-lede">Answer two questions and we will suggest where to begin, or describe the challenge to a partner directly.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/">Contact us {{{{arrow}}}}</a><a class="ad-btn ad-btn--ghost" href="{{{{root}}}}#where-to-start">Answer two questions</a></div>
  </div>
</section>
"""


def main() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    (SRC / "index.html").write_text(index(), encoding="utf-8")
    for p in PRACTICES:
        out = SRC / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(p), encoding="utf-8")
    print("practices written")


if __name__ == "__main__":
    main()
