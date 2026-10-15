/* Aldier: header, menu, hero films, statement, practices, reveals. */
(() => {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const saveData = navigator.connection && navigator.connection.saveData;
  document.documentElement.classList.add("ad-js");

  /* Header turns solid after the hero and steps aside while reading down. */
  const header = document.querySelector(".ad-header");
  if (header) {
    let last = window.scrollY;
    const onScroll = () => {
      const y = window.scrollY;
      header.classList.toggle("is-solid", y > 40);
      header.classList.toggle("is-hidden", y > 600 && y > last && !document.querySelector(".ad-nav.is-open"));
      last = y;
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Phone menu */
  const menu = document.querySelector(".ad-menu");
  const nav = document.querySelector(".ad-nav");
  if (menu && nav) {
    const set = (open) => {
      nav.classList.toggle("is-open", open);
      menu.setAttribute("aria-expanded", String(open));
      menu.querySelector("span").textContent = open ? "Close" : "Menu";
      document.body.style.overflow = open ? "hidden" : "";
    };
    menu.addEventListener("click", () => set(!nav.classList.contains("is-open")));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        set(false);
        menu.focus();
      }
    });
  }

  /* Hero: five films, one per practice, each with its own progress bar. */
  const hero = document.querySelector("[data-films]");
  if (hero) {
    const films = [...hero.querySelectorAll(".ad-hero__film")];
    const buttons = [...document.querySelectorAll(".ad-chapters button")];
    const toggle = document.querySelector(".ad-film-toggle");
    const DURATION = 7000;
    let index = 0;
    let timer = null;
    let paused = reduce || saveData;
    const load = (film) => {
      const v = film.querySelector("video");
      if (v && !v.dataset.loaded) {
        v.querySelectorAll("source[data-src]").forEach((s) => (s.src = s.dataset.src));
        v.load();
        v.dataset.loaded = "1";
      }
      return v;
    };
    const show = (i) => {
      index = (i + films.length) % films.length;
      films.forEach((f, k) => {
        const on = k === index;
        f.classList.toggle("is-on", on);
        const v = f.querySelector("video");
        if (v) {
          if (on && !paused) {
            load(f);
            v.currentTime = 0;
            v.play().catch(() => {});
          } else if (!on) {
            v.pause();
          }
        }
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
      // Load the next film quietly so it is ready in time.
      if (!paused) load(films[(index + 1) % films.length]);
      window.clearTimeout(timer);
      if (!paused) timer = window.setTimeout(() => show(index + 1), DURATION);
    };
    buttons.forEach((b, k) => b.addEventListener("click", () => show(k)));
    if (toggle) {
      const label = () => {
        toggle.setAttribute("aria-label", paused ? "Play the films" : "Pause the films");
        toggle.innerHTML = paused
          ? '<svg width="12" height="14" viewBox="0 0 12 14" aria-hidden="true"><path d="M0 0L12 7L0 14Z" fill="currentColor"/></svg>'
          : '<svg width="12" height="14" viewBox="0 0 12 14" aria-hidden="true"><rect width="4" height="14" fill="currentColor"/><rect x="8" width="4" height="14" fill="currentColor"/></svg>';
      };
      toggle.addEventListener("click", () => {
        paused = !paused;
        label();
        show(index);
      });
      label();
    }
    show(0);
  }

  /* Statement: each word lights as it crosses the middle of the screen. */
  document.querySelectorAll("[data-light]").forEach((p) => {
    const words = [];
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part.trim()) {
              frag.appendChild(document.createTextNode(part));
              return;
            }
            const s = document.createElement("span");
            s.className = "w" + (node.classList && node.classList.contains("ad-serif") ? " ad-serif" : "");
            s.textContent = part;
            frag.appendChild(s);
            words.push(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) {
          walk(n);
        }
      });
    };
    walk(p);
    if (reduce) {
      words.forEach((w) => w.classList.add("is-lit"));
      return;
    }
    const update = () => {
      const r = p.getBoundingClientRect();
      const vh = window.innerHeight;
      const progress = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      const lit = Math.round(progress * words.length);
      words.forEach((w, i) => w.classList.toggle("is-lit", i < lit));
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
  });

  /* Practices: hover, focus or tap opens a panel and plays its film. */
  document.querySelectorAll(".ad-acc").forEach((acc) => {
    const items = [...acc.querySelectorAll(".ad-acc__item")];
    const open = (item) => {
      items.forEach((it) => {
        const on = it === item;
        it.classList.toggle("is-open", on);
        const v = it.querySelector("video");
        if (v) {
          if (on && !reduce && !saveData) {
            v.querySelectorAll("source[data-src]").forEach((s) => {
              if (!s.src) s.src = s.dataset.src;
            });
            if (!v.dataset.loaded) {
              v.load();
              v.dataset.loaded = "1";
            }
            v.play().catch(() => {});
          } else {
            v.pause();
          }
        }
      });
    };
    items.forEach((it) => {
      it.addEventListener("mouseenter", () => open(it));
      it.addEventListener("focus", () => open(it));
      it.addEventListener("click", (e) => {
        if (!it.classList.contains("is-open")) {
          e.preventDefault();
          open(it);
        }
      });
    });
  });

  /* Sections lift into place the first time they arrive. */
  if (!reduce && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) =>
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.remove("is-waiting");
            io.unobserve(e.target);
          }
        }),
      { rootMargin: "0px 0px -10% 0px" },
    );
    document.querySelectorAll("[data-reveal]").forEach((el, i) => {
      if (el.getBoundingClientRect().top > window.innerHeight) {
        el.classList.add("is-waiting");
        el.style.transitionDelay = `${(i % 4) * 90}ms`;
        io.observe(el);
      }
    });
  }
})();
