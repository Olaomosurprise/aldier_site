/**
 * POST /api/enquiry
 * Receives every form on the site: the contact form, the Aldier Briefing
 * subscription, Board Programme registrations and careers registrations.
 *
 * Each submission is saved to the database when one is bound, and emailed to
 * Aldier when the email service is configured. If neither is set up, the
 * visitor is told the service is not yet available, so nothing is lost silently.
 *
 * Environment (set in Cloudflare Pages, never in this repository):
 *   RESEND_API_KEY  API key for the email delivery service (secret)
 *   ENQUIRY_TO      the inbox that receives submissions
 *   ENQUIRY_FROM    a sender on a domain verified with the email service
 * Optional bindings:
 *   DB              a D1 database with the table in migrations/0001_submissions.sql
 *   RATE            a KV namespace; when bound, each connection may send five messages an hour
 */

const FORMS = {
  contact: { required: ["name", "email", "message"], consent: true, subject: "Enquiry" },
  briefing: { required: ["email"], consent: false, subject: "Briefing subscription" },
  podcast: { required: ["email"], consent: false, subject: "Podcast launch list" },
  "board-programme": { required: ["name", "email", "organisation", "role"], consent: true, subject: "Board Programme registration" },
  careers: { required: ["name", "email", "discipline"], consent: true, subject: "Careers registration" },
};
const FIELDS = { name: 120, email: 200, organisation: 160, role: 120, topic: 120, format: 80, discipline: 120, link: 300, message: 5000 };
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const LABELS = { name: "your name", email: "an email address we can reply to", organisation: "your organisation", role: "your role", discipline: "your discipline", message: "a short description" };

const reply = (status, message, extra = {}) =>
  new Response(JSON.stringify({ message, ...extra }), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });

const clean = (value, max) =>
  String(value ?? "")
    .replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, "")
    .trim()
    .slice(0, max);

const escapeHtml = (s) =>
  s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

export async function onRequestPost({ request, env }) {
  let data;
  try {
    data = await request.json();
  } catch {
    return reply(400, "The form could not be read. Please try again.", { error: "The form could not be read. Please try again." });
  }

  const kind = clean(data.form, 40);
  const rules = FORMS[kind];
  if (!rules) return reply(422, "Unknown form.", { error: "Unknown form." });

  // Automated submissions fill the hidden field; accept them quietly and drop them.
  if (clean(data.company_website, 200)) return reply(200, "Thank you. It has reached us.");

  const fields = {};
  for (const [key, max] of Object.entries(FIELDS)) {
    const value = clean(data[key], max);
    if (value) fields[key] = value;
  }
  for (const key of rules.required) {
    if (!fields[key]) {
      const msg = `Please give ${LABELS[key] || key}.`;
      return reply(422, msg, { error: msg });
    }
  }
  if (!EMAIL.test(fields.email || "")) {
    const msg = "Please give an email address we can reply to.";
    return reply(422, msg, { error: msg });
  }
  if (rules.consent && data.consent !== "yes" && data.consent !== "on" && data.consent !== true) {
    const msg = "Please confirm that Aldier may use these details to reply to you.";
    return reply(422, msg, { error: msg });
  }

  if (env.RATE) {
    const ip = request.headers.get("CF-Connecting-IP") || "unknown";
    const key = `enquiry:${ip}:${new Date().toISOString().slice(0, 13)}`;
    const count = Number((await env.RATE.get(key)) || 0);
    if (count >= 5) {
      const msg = "Too many messages from this connection. Please try again in an hour.";
      return reply(429, msg, { error: msg });
    }
    await env.RATE.put(key, String(count + 1), { expirationTtl: 3700 });
  }

  const emailReady = env.RESEND_API_KEY && env.ENQUIRY_TO && env.ENQUIRY_FROM;
  if (!env.DB && !emailReady) {
    const msg = "This form is not yet switched on. Please try again soon.";
    return reply(503, msg, { error: msg });
  }

  let saved = false;
  if (env.DB) {
    try {
      await env.DB.prepare("INSERT INTO submissions (form, created_at, name, email, fields, emailed) VALUES (?, ?, ?, ?, ?, 0)")
        .bind(kind, new Date().toISOString(), fields.name || "", fields.email, JSON.stringify(fields))
        .run();
      saved = true;
    } catch (err) {
      console.log("[enquiry] database write failed", String(err));
    }
  }

  let sent = false;
  if (emailReady) {
    const rows = Object.entries(fields)
      .map(([k, v]) => `<tr><th align="left" valign="top">${k}</th><td>${escapeHtml(v).replace(/\n/g, "<br>")}</td></tr>`)
      .join("");
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: env.ENQUIRY_FROM,
        to: [env.ENQUIRY_TO],
        reply_to: fields.email,
        subject: `[Aldier] ${rules.subject}: ${fields.name || fields.email}${fields.organisation ? `, ${fields.organisation}` : ""}`,
        html: `<table cellpadding="6" style="font-family:Arial,sans-serif;font-size:14px">${rows}</table>`,
        text: Object.entries(fields).map(([k, v]) => `${k}: ${v}`).join("\n"),
      }),
    });
    sent = res.ok;
    if (!res.ok) console.log("[enquiry] email failed", res.status, await res.text());
  }

  if (!saved && !sent) {
    const msg = "Your message could not be delivered just now. Please try again in a few minutes.";
    return reply(502, msg, { error: msg });
  }
  const thanks = {
    contact: "Thank you. Your message has reached Aldier, and a partner will reply.",
    briefing: "Thank you. You will receive the next Aldier Briefing.",
    podcast: "Thank you. We will send you the first episode on the day it is released.",
    "board-programme": "Thank you. A partner will be in touch about the Board Programme.",
    careers: "Thank you. We will write to you when applications open.",
  };
  return reply(200, thanks[kind]);
}

export function onRequest() {
  return new Response(null, { status: 405, headers: { Allow: "POST" } });
}
