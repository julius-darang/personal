# visayasgrid Case-Study Page — Design

**Date:** 2026-06-04
**Status:** Approved — ready to build

## Goal

Add a concise case-study page for the visayasgrid project to the personal site,
to serve as the portfolio's flagship depth piece (roadmap step 1). Audience:
international remote / AI roles that judge technical depth but also skim.

## File & linking

- New page: `proj/visayasgrid.html`, reusing the existing nav, footer, and
  `assets/main.css` design system.
- `pages/projects.html`: visayasgrid card gets a **"Case study →"** link added,
  alongside the existing Live demo + GitHub links.
- `index.html`: the visayasgrid card (currently → live demo) repoints to the case
  study, which itself links out to the live demo.

## Page structure (concise — each section 2–4 sentences)

1. **Header** — back link, title "Visayas Grid", one-line tagline, `Live` status,
   primary links (Live demo · GitHub).
2. **Screenshot** — hero image captured from the live app, saved to `assets/`.
3. **Key facts strip** — `54 buses · 60 lines · 115 generators · AC load flow ·
   No backend · Vercel`.
4. **The problem** — NGCP transmission data isn't readily public; the "serious"
   v2 architecture was 10–11 weeks of PostGIS/FastAPI/Docker infra — too heavy
   for a prototype.
5. **The approach** — compute everything offline in a Python pipeline (pandapower
   AC Newton-Raphson load flow), pre-bake results to static GeoJSON, serve from a
   React/Leaflet frontend on Vercel. *No backend at runtime* is the core decision.
6. **What it does** — voltage + line-loading color encoding, click-to-inspect
   bus/line panel, island + voltage filters, demand/generation stats, provenance
   footer.
7. **The result** — live, unit-tested (Vitest), honest modeling (documented
   constants, IEC 60840 submarine-cable values, flagged load estimates). One line
   on what's next (swapping in fuller real data).
8. **Tech stack** — Python · pandapower · React · react-leaflet · Vite · Tailwind
   · Vercel.
9. Footer (reused).

## CSS

Add a small `/* ── CASE STUDY ── */` block to `main.css` reusing existing CSS
variables. New classes limited to: case-study header, figure/screenshot, and the
key-facts strip.

## Honesty guardrail

Every claim must match the visayasgrid repo. The prototype uses hand-tuned /
estimated loads and flagged gap-fills; present this transparently — visible
data-provenance judgment is a strength for this audience.

## Screenshot

Capture `https://visayasgrid.vercel.app` with a headless browser and save to
`assets/`. If no headless browser is available locally, fall back to a placeholder
image reference and flag it for the user to supply.

## Out of scope

- No deep technical dive (concise overview only — user's choice).
- No powergrid case-study page yet (later roadmap item).
- No framework / build tooling (site stays static HTML).

## Success criteria

- `proj/visayasgrid.html` renders with the site's existing styling.
- All links resolve (Live demo, GitHub, internal back link).
- Project cards on `index.html` and `pages/projects.html` link to the case study.
- Every factual claim matches the visayasgrid repo.
