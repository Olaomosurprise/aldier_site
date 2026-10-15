# Aldier website

The institutional website of Aldier, built as static pages with one Cloudflare Pages Function for forms.

## Structure

- `src/` holds each page as an HTML fragment with a short settings block at the top.
- `content/` holds Python scripts that write the repeated page families (practices, industries, insights) into `src/`. Edit the script, then run it.
- `assets/` holds the stylesheet, script, fonts, films and photographs.
- `build.py` wraps every page in the shared header, menus and footer and writes the finished site to `dist/`.
- `functions/api/enquiry.js` receives every form on the site.
- `migrations/` holds the database table definition.

## Build locally

```
cd content && python3 practices.py && python3 industries.py && python3 insights.py && cd ..
python3 build.py
```

Then open `dist/index.html`, or serve `dist/` with any static server.

## Hosting on Cloudflare Pages

- Project: `aldier-site` (aldier-site.pages.dev)
- Build command: `python3 build.py`
- Output directory: `dist`
- Production branch: `main`
- Binding: `DB` to the D1 database `aldier`, created from `migrations/0001_submissions.sql`

Variables for email (set in the Pages project, never in this repository):

- `ENQUIRY_TO`: the inbox that receives submissions
- `ENQUIRY_FROM`: a sender on a domain verified with Resend
- `RESEND_API_KEY`: secret

Without the email variables, submissions are still saved to the database.
