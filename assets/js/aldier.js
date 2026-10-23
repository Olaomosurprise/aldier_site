/* Aldier: header and menus, films, scroll effects, the finder and forms. */
(() => {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const saveData = !!(navigator.connection && navigator.connection.saveData);
  const desktop = window.matchMedia("(min-width: 1081px)");
  document.documentElement.classList.add("ad-js");

  /* ---------------- Header ---------------- */
  const header = document.querySelector(".ad-header");
  const nav = document.querySelector(".ad-nav");
  const menuBtn = document.querySelector(".ad-menu");
  const items = [...document.querySelectorAll(".ad-nav__item")];
  let last = window.scrollY;
  const anyOpen = () => items.some((i) => i.classList.contains("is-open")) || (nav && nav.classList.contains("is-open"));
  const onScroll = () => {
    const y = window.scrollY;
    header.classList.toggle("is-solid", y > 24);
    header.classList.toggle("is-hidden", y > 640 && y > last + 2 && !anyOpen());
    if (y < last - 2) header.classList.remove("is-hidden");
    last = y;
  };
  if (header) {
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  const closeAll = (except) => {
    items.forEach((it) => {
      if (it === except) return;
      it.classList.remove("is-open");
      const b = it.querySelector(".ad-nav__top");
      if (b) b.setAttribute("aria-expanded", "false");
    });
    if (!except && header && !(nav && nav.classList.contains("is-open"))) header.classList.remove("is-open");
  };
  const openItem = (it) => {
    closeAll(it);
    it.classList.add("is-open");
    it.querySelector(".ad-nav__top").setAttribute("aria-expanded", "true");
    header.classList.add("is-open");
  };
  items.forEach((it) => {
    const btn = it.querySelector(".ad-nav__top");
    let timer;
    btn.addEventListener("click", () => (it.classList.contains("is-open") ? closeAll() : openItem(it)));
    it.addEventListener("mouseenter", () => {
      if (!desktop.matches) return;
      clearTimeout(timer);
      timer = setTimeout(() => openItem(it), 90);
    });
    it.addEventListener("mouseleave", () => {
      if (!desktop.matches) return;
      clearTimeout(timer);
      timer = setTimeout(() => closeAll(), 160);
    });
  });
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    const open = items.find((i) => i.classList.contains("is-open"));
    if (open) {
      closeAll();
      open.querySelector(".ad-nav__top").focus();
    } else if (nav && nav.classList.contains("is-open")) {
      setDrawer(false);
      menuBtn.focus();
    }
  });
  document.addEventListener("click", (e) => {
    if (desktop.matches && !e.target.closest(".ad-nav__item")) closeAll();
  });
  const setDrawer = (open) => {
    nav.classList.toggle("is-open", open);
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.querySelector(".ad-menu__label").textContent = open ? "Close" : "Menu";
    header.classList.toggle("is-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (!open) closeAll();
  };
  if (menuBtn && nav) menuBtn.addEventListener("click", () => setDrawer(!nav.classList.contains("is-open")));
  desktop.addEventListener("change", () => nav && nav.classList.contains("is-open") && setDrawer(false));

  /* ---------------- Videos load only when needed ---------------- */
  const loadVideo = (v) => {
    if (!v || v.dataset.loaded) return v;
    v.querySelectorAll("source[data-src]").forEach((s) => (s.src = s.dataset.src));
    v.load();
    v.dataset.loaded = "1";
    return v;
  };
  // Ambient films outside the hero play while on screen.
  const ambient = [...document.querySelectorAll("video[data-ambient]")];
  if (ambient.length && "IntersectionObserver" in window && !reduce && !saveData) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const v = e.target;
        if (e.isIntersecting) {
          loadVideo(v);
          v.play().catch(() => {});
        } else if (v.dataset.loaded) v.pause();
      });
    }, { rootMargin: "200px 0px" });
    ambient.forEach((v) => io.observe(v));
  }

  /* ---------------- Home hero films ---------------- */
  const hero = document.querySelector("[data-films]");
  if (hero) {
    const films = [...hero.querySelectorAll(".ad-hero__film")];
    const slides = [...hero.querySelectorAll(".ad-hero__slide")];
    const buttons = [...hero.querySelectorAll(".ad-chapters button")];
    const toggle = hero.querySelector(".ad-film-toggle");
    const DURATION = 7500;
    let index = 0;
    let timer = null;
    let paused = reduce || saveData;
    const show = (i) => {
      index = (i + films.length) % films.length;
      films.forEach((f, k) => {
        const on = k === index;
        f.classList.toggle("is-on", on);
        const v = f.querySelector("video");
        if (!v) return;
        if (on && !paused) {
          loadVideo(v);
          try { v.currentTime = 0; } catch (err) { /* not ready yet */ }
          v.play().catch(() => {});
        } else if (!on) v.pause();
      });
      slides.forEach((s, k) => {
        s.classList.toggle("is-on", k === index);
        s.querySelectorAll("a").forEach((l) => (l.tabIndex = k === index ? 0 : -1));
        s.setAttribute("aria-hidden", String(k !== index));
      });
      buttons.forEach((b, k) => {
        b.setAttribute("aria-current", String(k === index));
        b.classList.toggle("is-done", k < index);
        b.style.setProperty("--dur", `${DURATION}ms`);
        const bar = b.querySelector(".ad-bar i");
        if (bar) {
          bar.style.animation = "none";
          void bar.offsetWidth;
          bar.style.animation = "";
          bar.style.animationPlayState = paused ? "paused" : "running";
        }
      });
      if (!paused) loadVideo(films[(index + 1) % films.length].querySelector("video"));
      clearTimeout(timer);
      if (!paused) timer = setTimeout(() => show(index + 1), DURATION);
    };
    buttons.forEach((b, k) => b.addEventListener("click", () => show(k)));
    const label = () => {
      if (!toggle) return;
      toggle.setAttribute("aria-label", paused ? "Play the films" : "Pause the films");
      toggle.innerHTML = paused
        ? '<svg width="12" height="14" viewBox="0 0 12 14" aria-hidden="true"><path d="M0 0L12 7L0 14Z" fill="currentColor"/></svg>'
        : '<svg width="12" height="14" viewBox="0 0 12 14" aria-hidden="true"><rect width="4" height="14" fill="currentColor"/><rect x="8" width="4" height="14" fill="currentColor"/></svg>';
    };
    if (toggle) toggle.addEventListener("click", () => { paused = !paused; label(); show(index); });
    label();
    show(0);
    document.addEventListener("visibilitychange", () => {
      const v = films[index].querySelector("video");
      if (document.hidden) { clearTimeout(timer); if (v) v.pause(); } else if (!paused) show(index);
    });
  }

  /* ---------------- Statement lit word by word ---------------- */
  document.querySelectorAll("[data-light]").forEach((p) => {
    const words = [];
    const walk = (node, em) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (!part.trim()) { frag.appendChild(document.createTextNode(part)); return; }
            const s = document.createElement("span");
            s.className = "w" + (em ? " is-em" : "");
            s.textContent = part;
            frag.appendChild(s);
            words.push(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) walk(n, em || n.tagName === "EM");
      });
    };
    walk(p, false);
    if (reduce) { words.forEach((w) => w.classList.add("is-lit")); return; }
    let ticking = false;
    const update = () => {
      ticking = false;
      const r = p.getBoundingClientRect();
      const vh = window.innerHeight;
      const progress = Math.min(1, Math.max(0, (vh * 0.8 - r.top) / (r.height + vh * 0.3)));
      const lit = Math.round(progress * words.length);
      words.forEach((w, i) => w.classList.toggle("is-lit", i < lit));
    };
    update();
    window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  });

  /* ---------------- Practices accordion ---------------- */
  document.querySelectorAll(".ad-acc").forEach((acc) => {
    const entries = [...acc.querySelectorAll(".ad-acc__item")];
    const open = (item) => {
      entries.forEach((it) => {
        const on = it === item;
        it.classList.toggle("is-open", on);
        const v = it.querySelector("video");
        if (!v) return;
        if (on && !reduce && !saveData) { loadVideo(v); v.play().catch(() => {}); } else v.pause();
      });
    };
    entries.forEach((it) => {
      it.addEventListener("mouseenter", () => desktop.matches && open(it));
      it.addEventListener("focus", () => open(it));
      it.addEventListener("click", (e) => {
        if (!it.classList.contains("is-open")) { e.preventDefault(); open(it); }
      });
    });
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver((list) => {
        list.forEach((e) => { if (e.isIntersecting) { open(acc.querySelector(".is-open") || entries[0]); io.disconnect(); } });
      }, { threshold: 0.3 });
      io.observe(acc);
    }
  });

  /* ---------------- Where to start ---------------- */
  const finder = document.querySelector("[data-finder]");
  if (finder) {
    const ADVICE = {
      direction: { title: "Setting and delivering strategy", practices: ["Strategy and Transformation", "Communications and Public Affairs"], text: "Begin with a short diagnostic: what the institution must achieve, what it can afford and what it should stop. We then establish the transformation office that carries the plan, and prepare the communication to the people it affects." },
      systems: { title: "Selecting and delivering core systems", practices: ["Technology and Data", "Cybersecurity and Digital Risk"], text: "Begin with what the systems must do and who will run them. We then lead selection and procurement independently, assure delivery and support the first months of live operation, with security designed in from the start." },
      breach: { title: "Cyber readiness", practices: ["Cybersecurity and Digital Risk", "Communications and Public Affairs"], text: "Begin with a readiness review of what you hold, who can reach it and how fast you would know. We then run a simulation in which the board, the technical team and the spokesperson work through a realistic incident together." },
      service: { title: "Service redesign", practices: ["Design and Experience", "Technology and Data"], text: "Begin by watching the service as it is used today. We map where people abandon it, redesign the journey, the product and, where it matters, the physical space, and build what is needed to run it." },
      trust: { title: "Rebuilding trust", practices: ["Communications and Public Affairs", "Strategy and Transformation"], text: "Begin with an assessment of where confidence was lost, and with whom. We set out what must change in practice, then how and when to say so to regulators, investors, staff and the public." },
    };
    const SECTOR = { government: "a public body", university: "an education institution", bank: "a financial institution", company: "your company", investor: "an investor", nonprofit: "your organisation", health: "a health system" };
    let sector = null;
    const step2 = finder.querySelector("[data-step='2']");
    const result = finder.querySelector(".ad-finder__result");
    const press = (group, btn) => group.querySelectorAll(".ad-chip").forEach((c) => c.setAttribute("aria-pressed", String(c === btn)));
    finder.querySelectorAll("[data-step='1'] .ad-chip").forEach((btn) => btn.addEventListener("click", () => {
      press(btn.closest("[data-step]"), btn);
      sector = btn.dataset.value;
      step2.hidden = false;
      step2.querySelector(".ad-chip").focus({ preventScroll: true });
    }));
    finder.querySelectorAll("[data-step='2'] .ad-chip").forEach((btn) => btn.addEventListener("click", () => {
      press(step2, btn);
      const a = ADVICE[btn.dataset.value];
      result.querySelector("h3").textContent = a.title;
      result.querySelector("[data-text]").textContent = `For ${SECTOR[sector] || "you"}, we would ${a.text.charAt(0).toLowerCase()}${a.text.slice(1)}`;
      result.querySelector(".ad-finder__practices").innerHTML = a.practices.map((p) => `<li>${p}</li>`).join("");
      const link = result.querySelector("a");
      link.href = link.dataset.base + "?topic=" + encodeURIComponent(btn.textContent.trim());
      result.hidden = false;
      requestAnimationFrame(() => result.classList.add("is-on"));
    }));
  }

  /* ---------------- Cards drifting over a heading ---------------- */
  const drift = document.querySelector("[data-drift]");
  if (drift && !reduce) {
    const cards = [...drift.querySelectorAll(".ad-drift__card")];
    const speeds = [0.18, -0.12, 0.1, -0.2, 0.14];
    let ticking = false;
    const move = () => {
      ticking = false;
      if (!desktop.matches) { cards.forEach((c) => (c.style.transform = "")); return; }
      const r = drift.getBoundingClientRect();
      const mid = r.top + r.height / 2 - window.innerHeight / 2;
      cards.forEach((c, i) => (c.style.transform = `translate3d(0, ${(mid * speeds[i % speeds.length]).toFixed(1)}px, 0)`));
    };
    move();
    window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(move); } }, { passive: true });
  }

  /* ---------------- Series list follows the screen ---------------- */
  document.querySelectorAll("[data-series]").forEach((s) => {
    const rows = [...s.querySelectorAll(".ad-series__list li")];
    if (!rows.length || reduce) return;
    let i = 0;
    setInterval(() => { rows[i].classList.remove("is-on"); i = (i + 1) % rows.length; rows[i].classList.add("is-on"); }, 4200);
  });

  /* ---------------- Reveal ---------------- */
  if (!reduce && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.remove("is-waiting"); io.unobserve(e.target); }
    }), { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll("[data-reveal]").forEach((el, i) => {
      if (el.getBoundingClientRect().top > window.innerHeight * 0.92) {
        el.classList.add("is-waiting");
        el.style.transitionDelay = `${(i % 3) * 80}ms`;
        io.observe(el);
      }
    });
  }

  /* ---------------- Forms ---------------- */
  const params = new URLSearchParams(location.search);
  const topic = params.get("topic");
  const topicField = document.querySelector("[data-topic]");
  if (topic && topicField) {
    const match = [...topicField.options].find((o) => o.text === topic || o.value === topic);
    if (match) topicField.value = match.value;
    else { const o = new Option(topic, topic, true, true); topicField.add(o); }
  }
  document.querySelectorAll("form[data-enquiry]").forEach((form) => {
    const status = form.querySelector("[role='status']");
    const original = status ? status.innerHTML : "";
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const btn = form.querySelector("button[type='submit']");
      btn.disabled = true;
      const data = Object.fromEntries(new FormData(form).entries());
      try {
        const res = await fetch(form.action, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) });
        const out = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(out.error || "We could not send that.");
        form.reset();
        if (status) { status.className = (status.className.replace(/ ?is-(ok|err)/g, "") + " is-ok").trim(); status.textContent = out.message || "Thank you. It has reached us."; }
      } catch (err) {
        if (status) { status.className = (status.className.replace(/ ?is-(ok|err)/g, "") + " is-err").trim(); status.textContent = err.message === "Failed to fetch" ? "We could not reach the server. Please try again in a moment." : err.message; }
      } finally {
        btn.disabled = false;
        if (status && status.classList.contains("is-ok")) setTimeout(() => { status.className = status.className.replace(/ ?is-ok/, ""); status.innerHTML = original; }, 9000);
      }
    });
  });
})();

/* Tabs */
(() => {
  document.querySelectorAll("[data-tabs]").forEach((box) => {
    const tabs = [...box.querySelectorAll("[role='tab']")];
    const select = (t) => {
      tabs.forEach((x) => {
        const on = x === t;
        x.setAttribute("aria-selected", String(on));
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute("aria-controls")).hidden = !on;
      });
    };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => select(t));
      t.addEventListener("keydown", (e) => {
        if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
        const n = tabs[(i + (e.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length];
        select(n);
        n.focus();
      });
    });
  });
})();

/* In-page navigation, search, article tools and back to top. */
(() => {
  "use strict";
  const root = (document.querySelector(".ad-logo") || {}).getAttribute ? document.querySelector(".ad-logo").getAttribute("href") : "/";

  // Sticky in-page navigation: highlight the section in view.
  const sub = document.querySelector("[data-subnav]");
  if (sub && "IntersectionObserver" in window) {
    const links = [...sub.querySelectorAll("a[href^='#']")];
    const sections = links.map((a) => document.getElementById(a.getAttribute("href").slice(1))).filter(Boolean);
    const set = (id) => links.forEach((a) => a.setAttribute("aria-current", a.getAttribute("href") === "#" + id ? "true" : "false"));
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) set(e.target.id); });
    }, { rootMargin: "-40% 0px -55% 0px" });
    sections.forEach((s) => io.observe(s));
    links.forEach((a) => a.addEventListener("click", () => {
      const item = a.closest("li"); if (item) item.scrollIntoView({ inline: "center", block: "nearest" });
    }));
  }

  // Site search, from a small index built with the site.
  const form = document.querySelector("[data-search]");
  if (form) {
    const input = form.querySelector("input");
    const list = document.querySelector("[data-search-results]");
    const count = document.querySelector("[data-search-count]");
    const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
    let index = null;
    const run = (q) => {
      const terms = q.toLowerCase().split(/\s+/).filter((t) => t.length > 1);
      if (!terms.length) { list.innerHTML = ""; count.textContent = ""; return; }
      const scored = index.map((e) => {
        const t = e.t.toLowerCase(), d = e.d.toLowerCase(), x = e.x.toLowerCase();
        let score = 0;
        for (const term of terms) {
          if (t.includes(term)) score += 10; else if (d.includes(term)) score += 4; else if (x.includes(term)) score += 1; else return null;
        }
        return { e, score };
      }).filter(Boolean).sort((a, b) => b.score - a.score);
      const mark = (s) => { let out = esc(s); terms.forEach((term) => { out = out.replace(new RegExp("(" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi"), "<mark>$1</mark>"); }); return out; };
      count.textContent = scored.length ? `${scored.length} result${scored.length === 1 ? "" : "s"} for “${q}”` : `No results for “${q}”. Try a broader term, or browse the site map.`;
      list.innerHTML = scored.slice(0, 30).map(({ e }) => `<li><a href="${root}${e.u}"><span class="ad-tile__type" style="color:var(--blue)">${esc(e.k)}</span><h2>${mark(e.t)}</h2><p>${mark(e.d)}</p></a></li>`).join("");
    };
    const params = new URLSearchParams(location.search);
    const start = params.get("q") || "";
    input.value = start;
    fetch(root + "search.json").then((r) => r.json()).then((data) => { index = data; if (start) run(start); });
    form.addEventListener("submit", (ev) => {
      ev.preventDefault();
      const q = input.value.trim();
      history.replaceState(null, "", "?q=" + encodeURIComponent(q));
      if (index) run(q);
    });
    let timer;
    input.addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => index && run(input.value.trim()), 180); });
  }

  // Reading progress on articles.
  const bar = document.querySelector(".ad-progress i");
  const article = document.querySelector("article");
  if (bar && article) {
    const tick = () => {
      const r = article.getBoundingClientRect();
      const total = r.height - window.innerHeight;
      bar.style.transform = `scaleX(${Math.min(1, Math.max(0, -r.top / (total > 0 ? total : 1)))})`;
    };
    window.addEventListener("scroll", () => requestAnimationFrame(tick), { passive: true });
    tick();
  }

  // Share links.
  document.querySelectorAll("[data-share]").forEach((box) => {
    const url = location.href.split("#")[0];
    const title = document.title;
    box.querySelectorAll("[data-share-to]").forEach((el) => {
      const to = el.dataset.shareTo;
      if (to === "linkedin") el.href = "https://www.linkedin.com/sharing/share-offsite/?url=" + encodeURIComponent(url);
      if (to === "x") el.href = "https://x.com/intent/post?url=" + encodeURIComponent(url) + "&text=" + encodeURIComponent(title);
      if (to === "email") el.href = "mailto:?subject=" + encodeURIComponent(title) + "&body=" + encodeURIComponent(url);
      if (to === "linkedin" || to === "x") { el.target = "_blank"; el.rel = "noopener"; }
      if (to === "copy") el.addEventListener("click", () => {
        (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(() => { el.textContent = "Link copied"; }, () => { el.textContent = url; });
      });
    });
  });

  // Back to top on long pages.
  if (document.documentElement.scrollHeight > window.innerHeight * 3) {
    const btn = document.createElement("button");
    btn.type = "button"; btn.className = "ad-top"; btn.setAttribute("aria-label", "Back to top");
    btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 13V3M4 7l4-4 4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>';
    btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }));
    document.body.appendChild(btn);
    window.addEventListener("scroll", () => btn.classList.toggle("is-on", window.scrollY > window.innerHeight * 1.5), { passive: true });
  }
})();

/* Filter a list of insights by format */
(() => {
  document.querySelectorAll("[data-filterable]").forEach((box) => {
    const chips = [...box.querySelectorAll("[data-filter]")];
    const items = [...box.querySelectorAll(".ad-feed > li")];
    const empty = box.querySelector(".ad-filter-empty");
    chips.forEach((chip) => chip.addEventListener("click", () => {
      const f = chip.dataset.filter;
      chips.forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
      let shown = 0;
      items.forEach((li) => { const on = !f || li.dataset.type === f; li.hidden = !on; if (on) shown += 1; });
      if (empty) empty.hidden = shown > 0;
    }));
  });
})();
