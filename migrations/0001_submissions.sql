-- Every form submission, kept so the team can read and export them.
-- Apply once to the Aldier database: Cloudflare dashboard > Storage & databases > D1 > aldier > Console,
-- paste this file and run it (or: npx wrangler d1 execute aldier --remote --file migrations/0001_submissions.sql).
CREATE TABLE IF NOT EXISTS submissions (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  form       TEXT    NOT NULL,
  created_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
  name       TEXT,
  email      TEXT,
  fields     TEXT    NOT NULL,          -- every field, as JSON
  emailed    INTEGER NOT NULL DEFAULT 0 -- 1 once the team's email was sent
);
CREATE INDEX IF NOT EXISTS submissions_form_created ON submissions (form, created_at);
