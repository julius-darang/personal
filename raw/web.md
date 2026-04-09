---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --blue: #2563eb;
    --blue-light: #eff6ff;
    --blue-mid: #bfdbfe;
    --text: #111827;
    --muted: #6b7280;
    --border: #e5e7eb;
    --white: #ffffff;
    --off-white: #f9fafb;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.6;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 0.4em;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 28px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 2px solid var(--blue);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--blue);
    margin-bottom: 8px;
  }

  p {
    color: var(--text);
    margin: 0.4em 0;
  }

  ul {
    padding-left: 1.4em;
  }

  li {
    margin-bottom: 10px;
    color: var(--text);
  }

  strong {
    color: var(--blue);
    font-weight: 600;
  }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--blue-light);
    color: var(--blue);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  blockquote {
    border-left: 4px solid var(--blue);
    background: var(--blue-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #1e40af;
    line-height: 1.6;
  }

  blockquote p {
    color: #1e40af;
    margin: 0;
  }

  .tag {
    display: inline-block;
    background: var(--blue-light);
    color: var(--blue);
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    padding: 4px 12px;
    border-radius: 999px;
    margin: 4px;
  }

  /* Cover slide */
  section.cover {
    background: var(--text);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover h1 {
    color: var(--white);
    font-size: 46px;
  }

  section.cover p {
    color: #9ca3af;
  }

  section.cover strong {
    color: #60a5fa;
  }

  section.cover code {
    background: #1e3a5f;
    color: #93c5fd;
  }

  /* Step slides */
  section.step {
    background: var(--off-white);
  }

  /* Highlight box */
  .highlight {
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  /* Tool card grid */
  .tools {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .tool-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .tool-card .icon {
    font-size: 24px;
    margin-bottom: 6px;
  }

  .tool-card .name {
    font-weight: 600;
    font-size: 15px;
    color: var(--text);
  }

  .tool-card .desc {
    font-size: 13px;
    color: var(--muted);
    margin-top: 2px;
  }

  /* Step badge */
  .step-badge {
    display: inline-block;
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
  }

  /* URL display */
  .url-box {
    background: #111827;
    border-radius: 8px;
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 15px;
    color: #60a5fa;
    margin: 16px 0;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  /* Final slide */
  section.final {
    background: var(--blue);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 {
    color: white;
    font-size: 40px;
  }

  section.final p {
    color: #bfdbfe;
    font-size: 18px;
  }
---

<!-- _class: cover -->

# Build a Website for Free
## No Coding Experience Required

&nbsp;

**A step-by-step guide** using AI + GitHub Pages

`html` · `css` · `github pages` · `free`

---

## What You'll Need

<div class="tools">
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">Claude or ChatGPT</div>
    <div class="desc">Free account · sign in with Google</div>
  </div>
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">A Web Browser</div>
    <div class="desc">Any browser works</div>
  </div>
  <div class="tool-card">
    <div class="icon">💻</div>
    <div class="name">VS Code <em style="font-weight:400;color:#9ca3af">optional</em></div>
    <div class="desc">For direct edits to colors & content</div>
  </div>
  <div class="tool-card">
    <div class="icon">🐙</div>
    <div class="name">GitHub Account</div>
    <div class="desc">Free · sign in with Google</div>
  </div>
</div>

&nbsp;

> No paid tools. No subscriptions. Nothing else.

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Generate Your Website with AI

Open Claude or ChatGPT and use this prompt:

> Create a personal website using only HTML and CSS deployable to GitHub Pages.
> Name: [your name] · Career: [your field] · Motto: [optional]
> Interests: [list] · Skills: [list] · Work history: [brief or paste resume]
> Color scheme: [describe or leave blank]
> Keep the design clean and professional. No JavaScript or frameworks.

&nbsp;

Download the generated **HTML file**, then **double-click** it to preview in your browser.

✅ You now have a working website — running locally on your computer.

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Refine It with AI

Not happy with something? Just ask. Be specific — the more detail, the better result.

**Example prompt:**

> The header feels cramped. Increase spacing between sections, set the header background to dark navy (#0a192f) with white text, and bump the base font size to 16px.

&nbsp;

- Want to edit directly? Open the file in **VS Code** or **Notepad**
- Colors, text, and layout are straightforward to adjust once you see the code
- Keep iterating until you're happy

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Deploy to GitHub Pages

1. Go to **github.com** → create a free account (use Google sign-in)
2. Choose your **username carefully** — it appears in your URL
3. Click **+** → **New repository** → set to **Public**
4. Name it `website` or `personal-website`
5. **Upload your HTML file**
6. Go to **Settings → Pages**
7. Source: **Deploy from branch → main → / (root)** → Save

⏳ Wait 1–3 minutes for GitHub to build your site.

---

## Your Website is Live 🎉

<div class="url-box">
  🔗 &nbsp; https://yourusername.github.io/website
</div>

&nbsp;

Shareable with anyone, anywhere in the world — **completely free**.

<div class="highlight">

**What you used:**
&nbsp;&nbsp;✦ AI to generate the code &nbsp;&nbsp;✦ GitHub to host it for free
&nbsp;&nbsp;✦ Zero dollars spent &nbsp;&nbsp;✦ Zero lines of code written

</div>

---

<!-- _class: final -->

# That's It.

&nbsp;

This is only a fraction of what AI can do.

Share this with a friend who's been putting off building their site.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*