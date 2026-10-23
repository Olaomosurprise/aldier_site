"""The firm's published insights, in one list, so every page that shows
"Our latest insights" draws the same cards in the same form."""

ITEMS = [
    {"url": "insights/the-joins/", "img": "team-laptops", "cat": "Strategy and Transformation", "practices": ["strategy", "technology", "design"],
     "title": "Where transformations fail: the gaps between disciplines",
     "dek": "The hard problems sit between the contracts. Nobody is paid to notice them, so nobody does.", "type": "Perspective", "meta": "6 min read"},
    {"url": "insights/before-the-breach/", "img": "server-engineer", "cat": "Cybersecurity and Digital Risk", "practices": ["cybersecurity", "technology", "communications"],
     "title": "Before the breach: seven questions a board can ask this quarter",
     "dek": "The decisions of the first hours are made long before the attack. Directors can test them now.", "type": "Board briefing", "meta": "7 min read"},
    {"url": "insights/the-handover/", "img": "careers-team", "cat": "Strategy and Transformation", "practices": ["strategy", "communications"],
     "title": "The handover: building institutions that outlast their founders",
     "dek": "An institution is tested on the day its founders leave. The best ones plan for that day first.", "type": "Perspective", "meta": "6 min read"},
    {"url": "work/genivy/", "img": "auditorium", "cat": "Education", "practices": ["strategy", "technology", "cybersecurity", "design", "communications"],
     "title": "GENIVY: founding an international guild of students",
     "dek": "How Aldier designed an institution owned by its members, from its constitution to its campus.", "type": "Case study", "meta": "Client story"},
    {"url": "podcast/", "img": "microphones", "cat": "The Aldier Podcast", "practices": ["communications"],
     "title": "The Aldier Podcast: conversations with the people who build institutions",
     "dek": "Season one follows four decisions that build, or break, an institution.", "type": "Podcast", "meta": "Coming soon"},
]


def card(item: dict) -> str:
    return (
        f'<li data-type="{item["type"]}"><a class="ad-feed__a" href="{{{{root}}}}{item["url"]}">'
        f'<div class="ad-feed__media"><img src="{{{{root}}}}assets/photos/{item["img"]}-800.webp" alt="" loading="lazy"></div>'
        f'<p class="ad-feed__cat">{item["cat"]}</p><h3 class="ad-feed__title">{item["title"]}</h3>'
        f'<p class="ad-feed__dek">{item["dek"]}</p><p class="ad-feed__meta">{item["type"]} <span>{item["meta"]}</span></p></a></li>'
    )


def latest(practice: str | None = None, count: int = 3, heading_id: str = "latest-title") -> str:
    items = [i for i in ITEMS if practice is None or practice in i["practices"]][:count]
    cards = "".join(card(i) for i in items)
    return f"""<div class="ad-rulehead"><h2 id="{heading_id}" class="ad-h2">Our latest insights</h2></div>
    <ul class="ad-feed">{cards}</ul>
    <p class="ad-center ad-mt"><a class="ad-btn ad-btn--ghost ad-btn--dark" href="{{{{root}}}}insights/">See all insights</a></p>"""
