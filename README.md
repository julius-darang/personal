# juliusdarang.com

Personal website of Julius Darang — built with vanilla HTML/CSS, zero JavaScript, hosted on GitHub Pages.

## Stack

- Pure static HTML (no framework, no build step)
- Vanilla CSS with custom properties, single stylesheet (`assets/main.css`)
- Zero JavaScript (CSS-only hamburger nav via checkbox hack)
- Google Fonts: DM Sans
- GitHub Pages deployment

## Structure

```
├── index.html              Homepage
├── assets/
│   ├── main.css            Single stylesheet
│   ├── favicon.svg         SVG favicon
│   └── prof-img.JPG        Profile image
├── pages/
│   ├── projects.html       Project portfolio
│   ├── writings.html       Writing index with filterable cards
├── proj/
│   └── visayasgrid.html    Case study
├── blogs/
│   ├── modelling-the-philippine-grid.html
│   ├── how to build the life you want.html
│   └── how to create a website.html
├── feed.xml                RSS feed
├── sitemap.xml
└── robots.txt
```

## Key Notes

- All pages share the same nav component (manually synced — no templating)
- Mobile nav collapses into a hamburger at 560px breakpoint
- Filter tabs on writings page are CSS-only (active class via static HTML)
- The site is a deliberate zero-JS showcase
