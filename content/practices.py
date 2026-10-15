"""Writes the five practice pages and the practices index into src/.

Run from the project root: python3 content/practices.py
"""

from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src" / "practices"

PRACTICES = [
    {
        "slug": "strategy",
        "no": "01",
        "verb": "Decide",
        "name": "Strategy and Transformation",
        "film": "decide",
        "title_html": "Decide what matters, <em>and make it happen.</em>",
        "lede": "Strategy is only as good as the institution's ability to carry it out. We set direction with leadership teams, then stay to build the office, the measures and the habits that turn a plan into results.",
        "question": "Leaders rarely lack a plan. What they lack is a plan the organisation can execute, a way of knowing whether it is working, and the discipline to stop what is not.",
        "services": [
            ("Corporate and public strategy", "Where to compete or serve, what to stop, and the few choices that decide the rest. Written for the board and readable by everyone who must act on it."),
            ("Operating model and organisation", "Structures, decision rights and governance that let people act without waiting for permission they should not need."),
            ("Mergers, partnerships and restructuring", "Diligence, integration planning and separation, with the first hundred days designed before the announcement."),
            ("Transformation office", "The engine room of change: a small team that tracks every commitment, surfaces problems early and keeps leadership honest about progress."),
            ("Performance and cost", "Costs reduced where they do not serve the mission, and capacity redirected to where it does."),
            ("Growth and new ventures", "New services, markets and businesses tested quickly and cheaply before they are funded properly."),
        ],
        "feature": "phases",
        "joins": ["technology", "communications"],
        "insight": ("the-joins", "Institutions rarely fail inside one discipline. They fail at the joins."),
        "image": "team-room",
    },
    {
        "slug": "technology",
        "no": "02",
        "verb": "Build",
        "name": "Technology and Data",
        "film": "build",
        "title_html": "Systems that work, <em>and data you can trust.</em>",
        "lede": "We sit on the client's side of the table: deciding what to build or buy, contracting for it, overseeing delivery and staying through the first months of live operation, when most programmes quietly fail.",
        "question": "Most technology programmes fail before a line of code is written: in a requirement nobody tested, a contract that rewards the wrong thing, or a launch date chosen for a speech.",
        "services": [
            ("Technology strategy and architecture", "A target architecture tied to what the institution must do, with a sequence it can afford and staff."),
            ("Selection and procurement advisory", "Requirements, market testing, evaluation and contract terms written to protect the buyer."),
            ("Delivery assurance", "Independent oversight of programmes in flight: early warning, honest status and the authority to call a halt."),
            ("Data and analytics", "Data governance, platforms and the reporting leaders actually use to decide, with definitions everyone shares."),
            ("Applied AI", "Use cases chosen for value and risk, governed from the start, and measured against the work they replace."),
            ("Cloud and infrastructure", "Hosting, resilience and cost decisions taken on evidence, with an exit route designed in."),
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
        "title_html": "Protected before, ready during, <em>trusted after.</em>",
        "lede": "Every institution will face a serious incident. The difference between a bad week and a lost decade is preparation: knowing what you hold, who can reach it, how fast you would know, and what the board will say on the first morning.",
        "question": "A breach is a technical event for an hour and a governance event for a year. Boards that have rehearsed it recover; boards that have not are still explaining it long after the systems are restored.",
        "services": [
            ("Cyber strategy and governance", "Risk appetite, accountability and reporting set at board level, in language directors can act on."),
            ("Readiness assessment", "A frank review against recognised frameworks such as ISO/IEC 27001 and the NIST Cybersecurity Framework, prioritised by consequence."),
            ("Data protection and privacy", "Records of processing, impact assessments and controls that meet the data protection law that applies to you."),
            ("Incident response and rehearsal", "Playbooks, decision rights and a live exercise in which the board, the technical team and the spokesperson work one realistic incident together."),
            ("Third-party and supply-chain risk", "Contracts, assurance and monitoring for the suppliers who hold your data or run your systems."),
            ("Resilience and continuity", "The services that must survive, how long they can be down, and the plan that keeps them running."),
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
        "title_html": "Brands, products and places <em>people choose to use.</em>",
        "lede": "Design is how an institution's decisions reach people: the service they queue for, the screen they tap, the building they enter, the film that tells them why it matters. The practice makes all of it, in Aldier Studio.",
        "question": "People judge an institution by the last service it gave them. The strategy may be sound; if the form is confusing, the queue is long and the app fails, the strategy is invisible.",
        "services": [
            ("Brand and identity", "Name, voice, visual identity and the guidelines that keep them consistent across every touchpoint."),
            ("Service design", "Journeys mapped from observation, redesigned around the people who use them, and specified so they can be built."),
            ("Digital products", "Websites, applications and platforms designed and built to accessibility standards, and measured once live."),
            ("Film and motion", "Documentary, campaign and explainer films that carry an institution's story further than any report."),
            ("Spatial and environmental design", "Branches, campuses, offices and public spaces planned around the service they house."),
            ("Research and testing", "Interviews, observation and usability testing that replace opinion with evidence."),
        ],
        "feature": "studio",
        "joins": ["technology", "communications"],
        "insight": ("the-handover", "The handover: an institution is finished only when it can run without its founder"),
        "image": "wireframe",
    },
    {
        "slug": "communications",
        "no": "05",
        "verb": "Explain",
        "name": "Communications and Public Affairs",
        "film": "communicate",
        "title_html": "Trust with the people who <em>decide your future.</em>",
        "lede": "Regulators, investors, staff, partners and the public each decide something about you. We help institutions give an honest, consistent account of themselves, and prepare for the days when that account is tested.",
        "question": "Reputation is earned in practice and lost in public. Communication cannot rescue a decision that was wrong, but it can make sure a right decision is understood.",
        "services": [
            ("Corporate reputation", "A clear account of what the institution stands for, built from what it does and tested with the people it must persuade."),
            ("Crisis and issues", "Preparation, round-the-clock counsel and the statements that matter in the first hours of a crisis."),
            ("Government relations and public affairs", "Policy analysis, engagement with officials and legislators, and coalitions built on shared interest, conducted openly and lawfully."),
            ("Investor and financial communications", "Results, transactions and capital markets disclosure written to be read as well as filed."),
            ("Internal and change communications", "Leaders who explain change before it happens, and staff who hear it from them first."),
            ("Executive positioning", "Speeches, interviews and op-eds for leaders who have something worth saying."),
        ],
        "feature": "quote",
        "joins": ["strategy", "cybersecurity"],
        "insight": ("the-joins", "Institutions rarely fail inside one discipline. They fail at the joins."),
        "image": "microphones",
    },
]

BY_SLUG = {p["slug"]: p for p in PRACTICES}


def video(name: str, cls: str = "", ambient: bool = False) -> str:
    amb = " data-ambient" if ambient else ""
    autoplay = "" if ambient else " autoplay loop"
    return (
        f'<video class="{cls}" muted playsinline{autoplay} preload="metadata" poster="{{{{root}}}}assets/film/{name}.jpg"{amb} aria-hidden="true">'
        f'<source src="{{{{root}}}}assets/film/{name}.webm" type="video/webm"><source src="{{{{root}}}}assets/film/{name}.mp4" type="video/mp4"></video>'
    )


def img(key: str, alt: str = "", sizes: str = "(max-width: 900px) 100vw, 50vw", style: str = "") -> str:
    st = f' style="{style}"' if style else ""
    return (
        f'<img src="{{{{root}}}}assets/photos/{key}-1600.webp" srcset="{{{{root}}}}assets/photos/{key}-800.webp 800w, {{{{root}}}}assets/photos/{key}-1600.webp 1600w, {{{{root}}}}assets/photos/{key}-2400.webp 2400w" '
        f'sizes="{sizes}" alt="{alt}" loading="lazy"{st}>'
    )


def feature(p: dict) -> str:
    kind = p["feature"]
    if kind == "phases":
        return """<section class="ad-sec ad-dark" aria-labelledby="how-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">How an engagement runs</p><h2 id="how-title" class="ad-h2">Four stages, <em>one team throughout.</em></h2></div><p>The people who diagnose the problem stay to deliver the answer. Nobody hands a plan to strangers and leaves.</p></div>
    <ol class="ad-steps">
      <li><h3>Diagnose</h3><p>Six to eight weeks to establish the facts: the economics, the constraints, the people and the history of what has been tried before.</p></li>
      <li><h3>Decide</h3><p>A small number of choices, set out with their costs and risks, for leadership to take and own. We recommend; you decide.</p></li>
      <li><h3>Deliver</h3><p>A transformation office that tracks each commitment against named owners and dates, and reports progress without varnish.</p></li>
      <li><h3>Hand over</h3><p>Capabilities transferred to your people, with the measures, routines and documentation to carry on without us.</p></li>
    </ol>
  </div>
</section>"""
    if kind == "split":
        return f"""<section class="ad-sec ad-ice" aria-labelledby="side-title">
  <div class="ad-wrap ad-split">
    <div class="ad-split__media ad-split__media--frame" data-reveal>{img(p['image'], 'A long corridor of server cabinets in a data hall')}</div>
    <div data-reveal>
      <p class="ad-eyebrow">On your side of the table</p>
      <h2 id="side-title" class="ad-h2">We never sell the systems <em>we help you choose.</em></h2>
      <p class="ad-lede">Aldier takes no commission, referral fee or reseller margin from any vendor. When we evaluate bidders, the only party paying us is you, and the evaluation file is yours to keep.</p>
      <dl class="ad-facts ad-mt"><div><dt>Vendor fees</dt><dd>None</dd></div><div><dt>Evaluation file</dt><dd>Yours</dd></div><div><dt>Live support</dt><dd>First months</dd></div></dl>
    </div>
  </div>
</section>"""
    if kind == "timeline":
        return """<section class="ad-sec ad-night" aria-labelledby="day-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">The rehearsal</p><h2 id="day-title" class="ad-h2">The first morning, <em>practised in advance.</em></h2></div><p>Our incident exercise runs a realistic scenario in real time. Directors, technical leads and the spokesperson each face the decisions that will fall to them.</p></div>
    <ol class="ad-steps">
      <li><h3>Detection</h3><p>An alert that might be nothing. Who decides whether it is an incident, and how quickly does the chief executive hear?</p></li>
      <li><h3>Containment</h3><p>Systems isolated, evidence preserved, and a choice between keeping services running and stopping the spread.</p></li>
      <li><h3>Notification</h3><p>Regulators, customers and partners told what they must be told, within the time the law allows, in words agreed in advance.</p></li>
      <li><h3>Recovery and review</h3><p>Services restored in the right order, and an honest account of what failed, published to those who need it.</p></li>
    </ol>
  </div>
</section>"""
    if kind == "studio":
        return f"""<section class="ad-sec ad-on-light" aria-labelledby="studio-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Aldier Studio</p><h2 id="studio-title" class="ad-h2">Where the practice <em>makes things.</em></h2></div><p>Designers, film-makers, architects and engineers working in one room, on the same brief as the strategists who shaped it.</p></div>
    <div class="ad-mosaic">
      <div class="ad-tile ad-tile--shade ad-span-6 ad-row-2 ad-wide-m" data-reveal><div class="ad-tile__media">{img('tablet-studio', 'A designer working on a tablet in a studio', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Digital products</p><h3>Designed to accessibility standards, and measured once live.</h3></div>
      <div class="ad-tile ad-tile--shade ad-span-6" data-reveal><div class="ad-tile__media">{img('drafting', 'An architect drawing a plan by hand', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Spatial design</p><h3>Branches, campuses and offices planned around the service they house.</h3></div>
      <div class="ad-tile ad-tile--shade ad-span-6" data-reveal><div class="ad-tile__media">{img('loupe', 'A printer’s loupe on colour proofs', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Identity</p><h3>Every colour, typeface and mark specified so it survives a thousand hands.</h3></div>
    </div>
    <p class="ad-mt"><a class="ad-link" href="{{{{root}}}}studio/">Visit Aldier Studio {{{{arrow}}}}</a></p>
  </div>
</section>"""
    if kind == "quote":
        return f"""<section class="ad-sec ad-dark" aria-labelledby="principle-title">
  <div class="ad-wrap ad-split">
    <div data-reveal>
      <p class="ad-eyebrow">Our principle</p>
      <h2 id="principle-title" class="ad-vh">Our principle</h2>
      <p class="ad-quote">We will help an institution explain a decision. We will not help it disguise one.</p>
      <p class="ad-quote-by">The standard every engagement in the practice is held to.</p>
    </div>
    <div class="ad-split__media ad-split__media--wide" data-reveal>{img(p['image'], 'Four microphones lined up at a podium')}</div>
  </div>
</section>"""
    return ""


def page(p: dict) -> str:
    services = "".join(f"<li><h3>{h}</h3><p>{t}</p></li>" for h, t in p["services"])
    joins = "".join(
        f'<a class="ad-card" href="{{{{root}}}}practices/{BY_SLUG[s]["slug"]}/"><span class="ad-tile__type" style="color:var(--blue)">{BY_SLUG[s]["no"]} · {BY_SLUG[s]["verb"]}</span><h3>{BY_SLUG[s]["name"]}</h3><p>{BY_SLUG[s]["lede"].split(". ")[0]}.</p><span class="ad-link">Explore {{{{arrow}}}}</span></a>'
        for s in p["joins"]
    )
    slug, title = p["insight"]
    return f"""<!--
title: {p['name']}
description: {p['lede'].split('. ')[0]}.
header: dark
slug: practice-{p['slug']}
image: assets/film/{p['film']}.jpg
preload: assets/film/{p['film']}.jpg
-->
<section class="ad-phero" aria-labelledby="page-title">
  <div class="ad-phero__media">{video(p['film'])}</div>
  <div class="ad-wrap ad-phero__body">
    <p class="ad-phero__crumb"><a href="{{{{root}}}}practices/">Practices</a> / {p['name']}</p>
    <p class="ad-eyebrow">{p['no']} · {p['verb']}</p>
    <h1 id="page-title" class="ad-h1">{p['title_html']}</h1>
    <p class="ad-lede">{p['lede']}</p>
  </div>
</section>

<section class="ad-sec ad-statement ad-on-light" aria-label="The problem">
  <div class="ad-wrap">
    <p class="ad-eyebrow">The problem we solve</p>
    <p class="ad-lit" data-light>{p['question']}</p>
  </div>
</section>

<section class="ad-sec ad-mist" aria-labelledby="services-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">What we do</p><h2 id="services-title" class="ad-h2">Six capabilities, <em>one standard.</em></h2></div><p>Each capability can be engaged on its own. Most clients find the work goes further when two or three are combined under one partner.</p></div>
    <ol class="ad-steps">{services}</ol>
  </div>
</section>

{feature(p)}

<section class="ad-sec ad-on-light" aria-labelledby="joins-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Where the practice joins others</p><h2 id="joins-title" class="ad-h2">Rarely engaged <em>alone.</em></h2></div><p>The practice works most often with these two. One partner leads, so the joins between them are nobody's blind spot.</p></div>
    <div class="ad-cards">
      {joins}
      <a class="ad-card" style="background:var(--ink);color:#fff;border-color:transparent" href="{{{{root}}}}insights/{slug}/"><span class="ad-tile__type" style="color:var(--sky)">Related perspective</span><h3>{title}</h3><span class="ad-link" style="color:var(--sky)">Read {{{{arrow}}}}</span></a>
    </div>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" aria-labelledby="close-title">
  <div class="ad-wrap">
    <p class="ad-eyebrow" style="justify-content:center">{p['name']}</p>
    <h2 id="close-title" class="ad-h2 ad-mt-s">Start with one conversation <em>with a partner.</em></h2>
    <p class="ad-lede">Tell us what is at stake. We reply personally, in confidence, usually within two working days.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/?topic={p['name'].replace(' ', '%20')}">Contact the practice {{{{arrow}}}}</a></div>
  </div>
</section>
"""


def index() -> str:
    rows = "".join(
        f"""<a class="ad-acc__item{' is-open' if i == 0 else ''}" href="{{{{root}}}}practices/{p['slug']}/">
        <video muted loop playsinline preload="none" poster="{{{{root}}}}assets/film/{p['film']}.jpg" aria-hidden="true"><source data-src="{{{{root}}}}assets/film/{p['film']}.webm" type="video/webm"><source data-src="{{{{root}}}}assets/film/{p['film']}.mp4" type="video/mp4"></video>
        <div class="ad-acc__body"><span class="ad-acc__no">{p['no']} · {p['verb'].upper()}</span><span class="ad-acc__name">{p['name']}</span><div class="ad-acc__more"><div><p>{p['lede'].split('. ')[0]}.</p><span class="ad-link">Explore the practice {{{{arrow}}}}</span></div></div></div>
      </a>"""
        for i, p in enumerate(PRACTICES)
    )
    detail = "".join(
        f"""<li id="{p['slug']}"><h3><a href="{{{{root}}}}practices/{p['slug']}/" style="text-decoration:none">{p['name']}</a></h3><p>{'; '.join(h for h, _ in p['services'])}.</p></li>"""
        for p in PRACTICES
    )
    return f"""<!--
title: Practices
description: Five practices in one firm: strategy, technology, cybersecurity, design and communications, led by one accountable partner.
header: dark
slug: practices
image: assets/film/civic.jpg
preload: assets/film/civic.jpg
-->
<section class="ad-phero" aria-labelledby="page-title">
  <div class="ad-phero__media">{video('civic')}</div>
  <div class="ad-wrap ad-phero__body">
    <p class="ad-eyebrow">Practices</p>
    <h1 id="page-title" class="ad-h1">Five disciplines. <em>One answerable team.</em></h1>
    <p class="ad-lede">Institutions face problems that cross every boundary in an organisation chart. Aldier is organised so that the people solving them do not have to stop at those boundaries.</p>
  </div>
</section>

<section class="ad-sec ad-dark" aria-labelledby="five-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">The practices</p><h2 id="five-title" class="ad-h2">Decide, build, protect, design, <em>explain.</em></h2></div><p>Choose a practice to see what it does, how it works and where it joins the others.</p></div>
    <div class="ad-acc">{rows}</div>
  </div>
</section>

<section class="ad-sec ad-on-light" aria-labelledby="all-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Capabilities</p><h2 id="all-title" class="ad-h2">Thirty capabilities, <em>at a glance.</em></h2></div><p>Every capability below can be engaged on its own or combined with others under one partner.</p></div>
    <ul class="ad-ilist" style="grid-template-columns:1fr">{detail}</ul>
  </div>
</section>

<section class="ad-sec ad-mist" aria-labelledby="model-title">
  <div class="ad-wrap ad-split">
    <div class="ad-split__media" data-reveal>{img('team-laptops', 'Colleagues working together at a table with laptops')}</div>
    <div data-reveal>
      <p class="ad-eyebrow">The model</p>
      <h2 id="model-title" class="ad-h2">One partner. One team. <em>No hand-offs.</em></h2>
      <p class="ad-lede">A lead partner is named for each engagement and answers for all of it. The team is drawn from whichever practices the problem needs, and every deliverable is reviewed by someone outside that team before it reaches you.</p>
      <a class="ad-link" href="{{{{root}}}}about/#how-we-work">How we work {{{{arrow}}}}</a>
    </div>
  </div>
</section>

<section class="ad-sec ad-royal ad-close" aria-labelledby="close-title">
  <div class="ad-wrap">
    <h2 id="close-title" class="ad-h2">Not sure which practice <em>you need?</em></h2>
    <p class="ad-lede">Most clients are not. Describe the problem and a partner will tell you honestly who should be in the room.</p>
    <div class="ad-actions"><a class="ad-btn ad-btn--light" href="{{{{root}}}}contact/">Describe the problem {{{{arrow}}}}</a><a class="ad-btn ad-btn--ghost" href="{{{{root}}}}#where-to-start">Try the two questions</a></div>
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
