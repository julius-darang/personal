# Personal Website — Improvement Roadmap

**Last updated:** 2026-06-04

## Positioning (the north star)

**Primary audience:** international remote / AI roles — companies hiring engineers
who blend power-systems domain knowledge with AI tooling.

**Secondary goals (reinforced by the same work):** engineering credibility, and
growing the `@juliusdarang` brand → Substack + Gumroad funnel.

**The unfair advantage:** a rare intersection —
**deep power-systems domain knowledge × AI-native building × clear writing.**
Almost nobody has all three. Every change on this site should make that combo
legible fast. Stop presenting as "engineer who also writes"; present as
"engineer who ships AI software in a domain most devs can't touch."

**Operating principle:** Go *deep*, not wide. The raw material for a standout
portfolio already exists in two projects. The work is **extraction and
presentation**, not more building. Avoid spreading thin across half-built projects.

---

## Projects

### Tier 1 — flagship (deepen now)
- [x] **visayasgrid** — strongest asset: live, deployed, domain + software. Has a
      concise **case-study page** at `proj/visayasgrid.html` (2026-06-04). Tells
      the story:
      - The problem: NGCP topology isn't public.
      - The judgment call: killed an 11-week v2 architecture, shipped in ~2 weeks.
      - The engineering: topology-validation gate before load flow; static JSON +
        Leaflet; pandapower snapshot.
      - What's live + a link to https://visayasgrid.vercel.app

### Tier 2 — supporting evidence
- [ ] **powergrid** — frame as the "serious R&D" sibling. Credibility hook: data
      rigor (validated within 4% of published peak load). Keep second to
      visayasgrid until it has a deployed URL (deployed > impressive-but-hidden).
      Add its own case-study page once portfolio matures.
- [ ] **Ritual PWA** (habit tracker) — add later. A shipped, tested vanilla-JS
      product proves polished frontend ability, not just simulations.
- [ ] **This website + daily-email automation** — small but concrete "AI-native
      builder" proof. Worth a one-line mention.

### Drop from the site
- RTS_pygame, simulation — dilute the narrative. At most, a tiny "experiments"
  footnote.

---

## Blogs — write at the intersection

Priority order. Note 1–3 all mine the *same two projects* — more to say without
more to build.

- [x] **1. "I built a live model of the Philippine grid. The code was the easy
      part."** — published 2026-06-04 at `blogs/modelling-the-philippine-grid.html`.
      Leads with the AI-workflow-honestly angle (where domain judgment was
      irreplaceable: slack bus, mixed-voltage transformers, plausible-but-wrong
      DC answer). Domain × AI × software × shipping, with a live link.
- [ ] **2. "Why I killed my own 11-week architecture and shipped in 2 weeks"**
      — the visayasgrid v2→v3 decision. Senior judgment (YAGNI, deploy-target-driven
      design). International hiring loves this story.
- [ ] **3. "Modeling a grid nobody will give you the data for"**
      — OSM + hand-curated + *flagged* synthetic infill, validated within 4%.
      Pure domain credibility + honest data engineering. Almost nobody can write it.
- [ ] **4. "The AI-native engineering workflow I actually use"**
      — Claude Code, agents, how you really build. Feeds courses/brand and signals
      you're ahead of the curve. Personal-voice version of the TUTORIALS material.
- [ ] **5. One identity/career post** in the existing "build the life you want"
      lane to feed Substack/brand — but keep it the minority, not the majority.

Existing posts to keep: "How I created and deployed a website" (AI-builder proof),
"How to build the life you want" (brand/identity lane).

---

## Structural changes

- [x] **Sharpen the hero.** Eyebrow line now reads "Power-Systems Engineer ·
      AI-Native Builder"; sub-headline mentions building software with AI agents.
      "Think in systems. Build what matters." kept as brand flavor (2026-06-04).
- [ ] **Add case-study pages** (visayasgrid first, powergrid later). Highest-leverage
      structural change — depth separates a portfolio from a link list.
- [ ] **Make GitHub prominent**; ensure pinned repos shine. Give visayasgrid's README
      the same quality as powergrid's.
- [ ] **Add a short "What I do" / "Now" section** stating the bridge explicitly.

---

## Suggested sequence

1. **visayasgrid case-study page + Blog #1** (the AI-agents build story) — do
   together; they share material. Biggest single jump in perception.
2. Sharpen the hero positioning line.
3. **Blog #2** (architecture-killing judgment post).
4. Later: add Ritual PWA + powergrid case-study page as the portfolio matures.

---

## Done

- [x] Removed all fictional projects/writings; site now reflects real work only
      (powergrid + visayasgrid, 2 real blog posts). See
      `docs/superpowers/specs/2026-06-04-website-content-cleanup-design.md`.
