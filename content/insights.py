"""Writes the insights index and essays into src/insights/.

Run from the project root: python3 content/insights.py
"""

from pathlib import Path

from practices import img

SRC = Path(__file__).resolve().parent.parent / "src" / "insights"

ESSAYS = [
    {
        "slug": "the-joins",
        "type": "Perspective",
        "title": "Institutions rarely fail inside one discipline. They fail at the joins.",
        "dek": "Strategy, systems, security, service and reputation are bought separately and fail together. The remedy is organisational before it is technical.",
        "practice": "Strategy and Transformation",
        "date": "October 2026",
        "minutes": 6,
        "image": "team-laptops",
        "image_alt": "Colleagues working together at a table with laptops",
        "body": """
<p>Consider how a large institution typically changes itself. A strategy firm produces the plan. A systems integrator, chosen by a separate procurement, builds the platform. A security consultancy is engaged after the design is fixed. A design agency is asked to make the result pleasant to use. A communications firm is retained when the launch date nears, or when something goes wrong. Each adviser is competent. Each delivers what its contract describes. And the programme fails anyway.</p>
<p>It fails because the hard problems sit between the contracts. The strategy assumed a capability the system cannot provide. The system was designed without the controls the regulator expects. The service was redesigned around a process the strategy had already abolished. The announcement promised a date the delivery team never agreed. Nobody was paid to notice, so nobody did.</p>
<h2>Where accountability goes missing</h2>
<p>The pattern is familiar to anyone who has sat through a programme review. Every workstream reports green. The whole is plainly red. The reason is structural. When advice is divided among firms, accountability is divided with it, and the gaps between the pieces belong to no one. The client is left to integrate work it hired experts to do, often without the staff to do it.</p>
<p class="ad-pull">When advice is divided among firms, accountability is divided with it. The gaps between the pieces belong to no one.</p>
<p>Procurement rules make the problem worse. Breaking a large engagement into separate lots can look like prudence: more competition, lower prices, less dependence on a single supplier. But each lot is scoped in isolation, and the joins between lots are rarely written into anyone's terms of reference. The institution saves on fees and pays in failure.</p>
<h2>What integration actually requires</h2>
<p>Hiring one large firm for everything is a tempting answer, and a flawed one. Scale brings its own risks, including conflicts of interest when the same adviser designs a system and then audits it. What matters is that one person is accountable for the whole problem, that the team includes every discipline the problem needs from the start, and that someone outside that team checks the work before it reaches the client.</p>
<p>In practice this means three habits. First, the decision and its delivery are planned together: no strategy is final until the people who must build it have tested its assumptions. Second, security, design and communication enter at the beginning, when they are cheap to accommodate, rather than at the end, when they are expensive to retrofit. Third, the engagement is organised around the outcomes the institution cares about, and judged by them.</p>
<h2>Questions for leaders</h2>
<p>Leaders who suspect their programmes are failing at the joins can test the suspicion with a few questions. Who, by name, is accountable for the whole programme, and do they have authority over every adviser? When the strategy changed last, how long did it take the system design to follow? Was the security team consulted before or after the architecture was fixed? Has the launch announcement been agreed with the people who must deliver it?</p>
<p>If the answers are uncertain, the risk lies in the spaces between the workstreams, and that is where attention should go first.</p>
""",
    },
    {
        "slug": "before-the-breach",
        "type": "Board briefing",
        "title": "Before the breach: seven questions a board can ask this quarter",
        "dek": "Serious cyber incidents are now a question of when. Directors cannot become engineers, but they can ask the questions that reveal whether their institution is ready.",
        "practice": "Cybersecurity and Digital Risk",
        "date": "October 2026",
        "minutes": 7,
        "image": "data-hall",
        "image_alt": "A long corridor of server cabinets behind glass in a data hall",
        "body": """
<p>Boards are accountable for cyber risk whether or not they understand it. Regulators increasingly expect directors to show that they oversee it actively, and courts and shareholders tend to judge them by what they asked before an incident far more than by what they said after it. Effective oversight rests on the right questions, asked regularly, and a willingness to press when the answers are vague.</p>
<p>What follows are seven questions any board can put to management this quarter. None needs specialist knowledge to ask. All of them reveal a great deal from the way they are answered.</p>
<h2>1. What are the few things we cannot afford to lose?</h2>
<p>Some systems matter far more than others. Management should be able to name the handful of services and data sets whose loss or exposure would do the most harm to customers, citizens or the institution itself, and explain how each is protected. A long list suggests the work of prioritising has not been done.</p>
<h2>2. How quickly would we know?</h2>
<p>Many breaches are discovered months after they begin, often by outsiders. Ask how an intrusion would be detected, by whom, and how quickly the chief executive and the board would be told. If nobody can describe the path from alert to boardroom, it probably does not exist.</p>
<h2>3. Who decides, at three in the morning?</h2>
<p>Serious incidents force fast decisions: whether to shut down a service, whether to pay a ransom, whether to notify a regulator. Ask who has authority to make each one, and whether they know it. Ambiguity costs hours that cannot be recovered.</p>
<p class="ad-pull">A board that has rehearsed an incident recovers faster than one that meets it for the first time.</p>
<h2>4. What do we owe, and to whom, and when?</h2>
<p>Data protection law and sector rules often set strict deadlines for notifying regulators and the people affected. Ask management to set out those obligations, and to show the drafts that would be used. Writing them during the incident is too late.</p>
<h2>5. Which suppliers could hurt us?</h2>
<p>Many incidents begin at a supplier: a payroll provider, a software vendor, a cloud host. Ask which third parties hold sensitive data or run critical systems, what the contracts require of them, and how their security is checked.</p>
<h2>6. Can we restore, and have we tried?</h2>
<p>A backup that has never been restored is only a hope. Ask when the institution last recovered a critical service from backup under realistic conditions, how long it took, and what went wrong.</p>
<h2>7. When did we last rehearse?</h2>
<p>The most reliable predictor of a good response is practice. Ask when the board last took part in an incident exercise alongside management and the communications team, and what changed as a result. If the answer is never, that is the first thing to fix.</p>
<h2>A note on answers</h2>
<p>The value of these questions lies as much in how they are answered as in what is said. Precise, candid answers that acknowledge gaps are a good sign. Reassurance without evidence is a warning. Directors should feel entitled to ask for the evidence, and to return to the same questions until the answers improve.</p>
""",
    },
    {
        "slug": "the-handover",
        "type": "Perspective",
        "title": "The handover: an institution is finished only when it can run without its founder",
        "dek": "Institutions are built to outlast the people who start them. Designing for succession from the first day is harder, and more important, than it sounds.",
        "practice": "Strategy and Transformation",
        "date": "October 2026",
        "minutes": 6,
        "image": "white-curves",
        "image_alt": "Curving white balconies of a high-rise against blue sky",
        "body": """
<p>Every founder faces the same temptation. In the early days, it is faster to decide everything personally, to hold the relationships, to keep the important knowledge in one's head. The institution grows around that person like a vine around a post. Then, one day, the post is removed, by retirement, appointment elsewhere or simple exhaustion, and the vine falls over.</p>
<p>The pattern is common in public programmes launched by a single minister, in universities shaped by a long-serving vice-chancellor, in companies built by a founder who never quite let go. The work was real. The results were real. But the institution was never finished, because it could not stand without its builder.</p>
<h2>Designing to be replaced</h2>
<p>The alternative is to design the institution, from the beginning, to be handed over. That means writing down what is usually left unwritten: how decisions are made, by whom, under what rules, and how those rules can be changed. It means building governance that can say no to the founder. It means training successors early and giving them real authority to match their titles.</p>
<p class="ad-pull">An institution is finished only when it can carry on without the person who built it.</p>
<p>It also means accepting a loss of control, which is the part most founders resist. An institution that can outlive its builder is, by definition, one its builder cannot fully command. The trade is worth making. Influence that rests on rules and relationships lasts longer than influence that rests on presence.</p>
<h2>A test case</h2>
<p>Aldier faced this question directly as Founding Partner to GENIVY, an international guild of students. From the outset, the firm committed in writing to hand every function, from finance to communications, to the students who run the guild. Its role was designed to shrink as theirs grows. That made some early decisions slower. It also meant that the institution's legitimacy rested with its members from the start.</p>
<h2>Questions for builders</h2>
<p>Anyone building an institution can test its readiness for handover with a few questions. If you left tomorrow, who would decide what you decide today? Are the rules that govern the institution written, public and changeable by someone other than you? Who among the next generation has already exercised real authority, and been allowed to get things wrong? What would your successor need to know that only you know now?</p>
<p>The answers are uncomfortable for most founders. That is precisely why they are worth asking early, while there is still time to act on them.</p>
""",
    },
]


def essay(e: dict) -> str:
    others = [o for o in ESSAYS if o["slug"] != e["slug"]]
    more = "".join(
        f'<a class="ad-card" href="{{{{root}}}}insights/{o["slug"]}/"><div class="ad-card__img">{img(o["image"], "", "(max-width: 900px) 100vw, 33vw")}</div><span class="ad-tile__type" style="color:var(--blue)">{o["type"]}</span><h3>{o["title"]}</h3></a>'
        for o in others
    )
    return f"""<!--
title: {e['title']}
description: {e['dek']}
header: light
slug: essay
image: assets/photos/{e['image']}-1600.webp
-->
<article>
<header class="ad-rhero">
  <div class="ad-wrap">
    <p class="ad-eyebrow">{e['type']}</p>
    <h1 id="page-title" class="ad-h2" style="max-width:22ch">{e['title']}</h1>
    <p class="ad-lede">{e['dek']}</p>
    <div class="ad-byline"><span>From the <b>{e['practice']}</b> practice</span><span>{e['date']}</span><span>{e['minutes']} minute read</span></div>
  </div>
</header>
<div class="ad-wrap"><figure class="ad-figure">{img(e['image'], e['image_alt'], '100vw').replace(' loading="lazy"', ' fetchpriority="high"')}</figure></div>
<div class="ad-sec ad-sec--tight">
  <div class="ad-wrap ad-article">
    <aside class="ad-article__aside" aria-label="About this piece">
      <div><b>Practice</b><a class="ad-link" href="{{{{root}}}}practices/">{e['practice']}</a></div>
      <div><b>Review</b>Checked by a reviewer outside the authors' team before publication.</div>
      <div><b>Share</b><a class="ad-link" href="mailto:?subject={e['title'].replace(' ', '%20')}">By email</a></div>
    </aside>
    <div class="ad-prose">{e['body']}</div>
  </div>
</div>
</article>

<section class="ad-sec ad-mist" aria-labelledby="more-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Continue reading</p><h2 id="more-title" class="ad-h2">More <em>perspectives.</em></h2></div></div>
    <div class="ad-cards">{more}
      <a class="ad-card" style="background:var(--ink);color:#fff;border-color:transparent" href="{{{{root}}}}review/"><span class="ad-tile__type" style="color:var(--sky)">The Aldier Review</span><h3>A journal of how institutions actually work. Issue one in preparation.</h3><span class="ad-link" style="color:var(--sky)">About the Review {{{{arrow}}}}</span></a>
    </div>
  </div>
</section>
"""


def index() -> str:
    lead = ESSAYS[0]
    rest = "".join(
        f'<li><a href="{{{{root}}}}insights/{e["slug"]}/" style="display:grid;grid-template-columns:1fr 120px;gap:20px;text-decoration:none;align-items:center"><div><span class="ad-tile__type" style="color:var(--blue)">{e["type"]}</span><h3 style="font:400 1.35rem/1.2 var(--serif);margin-top:8px">{e["title"]}</h3><p class="ad-note" style="margin-top:6px">{e["minutes"]} minute read</p></div><div style="aspect-ratio:1;border-radius:12px;overflow:hidden">{img(e["image"], "", "120px").replace("width:", "")}</div></a></li>'
        for e in ESSAYS[1:]
    )
    return f"""<!--
title: Insights
description: Perspectives, briefings and research from Aldier on how institutions decide, build, protect, design and explain.
header: light
slug: insights
image: assets/photos/working-table-1600.webp
-->
<section class="ad-rhero">
  <div class="ad-wrap">
    <p class="ad-eyebrow">Insights</p>
    <h1 id="page-title" class="ad-h1">What we are <em>learning.</em></h1>
    <p class="ad-lede">Perspectives, board briefings and research from across the firm, signed by the people who wrote them and checked by someone who did not.</p>
  </div>
</section>

<section class="ad-sec ad-sec--tight" aria-labelledby="lead-title">
  <div class="ad-wrap ad-split" style="align-items:start">
    <a class="ad-tile ad-tile--shade" style="min-height:560px" href="{{{{root}}}}insights/{lead['slug']}/" data-reveal>
      <div class="ad-tile__media">{img(lead['image'], '', '(max-width: 900px) 100vw, 50vw')}</div>
      <p class="ad-tile__type">Lead perspective</p>
      <h2 id="lead-title" class="ad-h3" style="color:#fff">{lead['title']}</h2>
      <p>{lead['dek']}</p>
    </a>
    <div data-reveal>
      <p class="ad-eyebrow">Latest</p>
      <ul class="ad-latest ad-mt-s">{rest}</ul>
      <div class="ad-soon ad-mt"><span class="ad-tag ad-tag--soon">Coming soon</span><p>The Institute's first working papers and the first issue of the Aldier Review are in preparation.</p></div>
    </div>
  </div>
</section>

<section class="ad-sec ad-on-light" aria-labelledby="prog-title">
  <div class="ad-wrap">
    <div class="ad-head"><div><p class="ad-eyebrow">Programmes</p><h2 id="prog-title" class="ad-h2">Research, a journal <em>and a film series.</em></h2></div></div>
    <div class="ad-bento" style="grid-auto-rows:220px">
      <a class="ad-tile ad-tile--shade ad-bento__a" href="{{{{root}}}}institute/"><div class="ad-tile__media">{img('render-waves', '', '(max-width: 960px) 100vw, 50vw')}</div><p class="ad-tile__type">Research</p><h3>The Aldier Institute</h3><p>Independent research on institutional performance, public trust and digital resilience.</p></a>
      <a class="ad-tile ad-tile--royal ad-bento__b" href="{{{{root}}}}review/"><span class="ad-tag ad-tag--soon">In preparation</span><p class="ad-tile__type">Journal</p><h3>The Aldier Review</h3></a>
      <a class="ad-tile ad-tile--shade" href="{{{{root}}}}conversations/"><div class="ad-tile__media"><img src="{{{{root}}}}assets/film/meeting.jpg" alt="" loading="lazy"></div><p class="ad-tile__type">Film series</p><h3>Aldier Conversations</h3></a>
      <a class="ad-tile ad-tile--light" href="{{{{root}}}}board-programme/"><p class="ad-tile__type" style="color:var(--blue)">For directors</p><h3>The Board Programme</h3></a>
    </div>
  </div>
</section>

<section class="ad-sec ad-dark" id="briefing" aria-labelledby="brief-title">
  <div class="ad-wrap ad-split">
    <div>
      <p class="ad-eyebrow">The Aldier Briefing</p>
      <h2 id="brief-title" class="ad-h2">One considered note, <em>once a month.</em></h2>
      <p class="ad-lede">New perspectives, research and programme news, with a short reading list from beyond the firm. Unsubscribe at any time by replying to any issue.</p>
    </div>
    <form class="ad-sub" action="{{{{root}}}}api/enquiry" method="post" data-enquiry>
      <input type="hidden" name="form" value="briefing">
      <label class="ad-vh" for="ins-email">Email address</label>
      <input id="ins-email" name="email" type="email" autocomplete="email" placeholder="Your email address" required>
      <input class="ad-hp" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="ad-btn ad-btn--light" type="submit">Subscribe</button>
      <p class="ad-sub__note" role="status">See the <a href="{{{{root}}}}privacy/">privacy notice</a>.</p>
    </form>
  </div>
</section>
"""


def main() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    idx = index().replace("header: light\nslug: insights", "header: light\nslug: insights\nbrief: no")
    (SRC / "index.html").write_text(idx, encoding="utf-8")
    for e in ESSAYS:
        out = SRC / e["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(essay(e), encoding="utf-8")
    print("insights written")


if __name__ == "__main__":
    main()
