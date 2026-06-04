# Personal Website — Content Cleanup Design

**Date:** 2026-06-04
**Author:** Julius Darang (with Claude)
**Status:** Approved design — ready for implementation plan

## Goal

Remove all fictional projects and writings from the personal website and replace
them with the user's real work. Every project, link, status badge, and feed entry
on the site must correspond to something that actually exists. No invented content.

## Background

The site (static HTML, no build, no framework) currently advertises ~7 fictional
projects (PVsyst studies, ETAP arc flash, DIgSILENT model, wind resource
assessment, content automation pipeline, power flow web interface) and 5 fictional
blog posts. Only two blog posts actually exist, and the real project work is
`powergrid` and `visayasgrid` in the `polymath/Projects/` folder.

Scope decisions (from brainstorming):
- Feature **only** `powergrid` and `visayasgrid` for now.
- List **only** the two real blog posts.
- Both repos are public on GitHub (`github.com/julius-darang`); `visayasgrid` has a
  live deploy at `https://visayasgrid.vercel.app` (both verified HTTP 200).

## Real content

### Projects

**powergrid — Philippine Power Grid Visualization**
- Desc: Web app visualizing the Philippine grid — Visayas transmission backbone
  (69/138/230 kV) plus per-province distribution — with a pandapower load-flow
  model underneath. Combines OSM, hand-curated NGCP substation data, and flagged
  synthetic infill. Phase 1 (data foundation) done: 2,960 buses, 2,967 lines;
  Visayas peak load within 4% of published figures.
- Stack: Python · pandapower · PostGIS · FastAPI · OSMnx
- Status: **In progress**
- Link: GitHub → https://github.com/julius-darang/powergrid

**visayasgrid — Visayas Grid (live prototype)**
- Desc: Lightweight Vercel-only prototype modeling the Visayas transmission grid
  (69/138/230 kV + 350 kV HVDC) from real public NGCP data. Precomputed JSON +
  Leaflet map with voltage/loading color encoding, click-to-inspect, and
  island/voltage filters; pandapower load-flow snapshot with a topology-validation
  gate. No backend.
- Stack: Python · pandapower · Leaflet · JavaScript · Vercel
- Status: **Live**
- Links: Live demo → https://visayasgrid.vercel.app · GitHub →
  https://github.com/julius-darang/visayasgrid

### Writings (both Apr 2026)

- **How to Build the Life You Actually Want** →
  `blogs/how to build the life you want.html` — category: Psychology & Philosophy
- **How I Created and Deployed a Website From Scratch** →
  `blogs/how to create a website.html` — category: AI & Software

## Changes by file

1. **index.html**
   - Projects section: replace 4 dummy cards with the 2 real project items.
   - Writing section: replace 5 dummy posts with the 2 real posts, linking to the
     correct blog files (not the dummy `blogs/blogs.html`).

2. **pages/projects.html**
   - Replace 7 dummy `.project-card` blocks with the 2 real ones (real links +
     truthful status badges).
   - Remove the filter bar markup and its `filter()` `<script>`.

3. **pages/writings.html**
   - Reduce to the 2 real posts (the two real cards already present at the bottom
     become the only cards). Remove all dummy cards.
   - Remove the filter bar markup and its `filter()` `<script>`.

4. **feed.xml**
   - Replace the 5 fictional `<item>` entries with the 2 real posts: correct
     titles, real blog URLs, and `pubDate` from git (both Apr 2026).
   - Update `lastBuildDate`.

5. **sitemap.xml**
   - Replace the single `blogs/blogs.html` entry with the two real blog post URLs.

6. **blogs/blogs.html**
   - **Keep as an unlinked draft.** Do not delete. Remove all site references to it
     (homepage links and sitemap entry) so it is orphaned but preserved on disk.

## Out of scope

- No framework / build tooling (intentional; site stays static HTML).
- No redesign of layout, hero, or About section.
- Other real work (Ritual PWA, TUTORIALS, Conquer Self, automations) is
  deliberately excluded for now.
- Re-adding filter bars later when content grows.

## Success criteria

- No fictional project or post text remains anywhere in the site or SEO files.
- Every external link resolves (GitHub repos + Vercel live URL).
- Every internal writing link points to a real blog file.
- `feed.xml` and `sitemap.xml` reflect only real content.
- Pages render correctly with the filter bars and their JS removed.
