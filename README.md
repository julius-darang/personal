# juliusdarang.com

Personal website of Julius Darang — built with vanilla HTML/CSS and a small vanilla-JS theme toggle, hosted on GitHub Pages.

## Stack

- Pure static HTML (no framework)
- Vanilla CSS with custom properties, single stylesheet (`assets/main.css`)
- Small vanilla-JS theme preference (`assets/theme.js`); CSS-only hamburger nav
- Google Fonts: DM Sans
- GitHub Pages deployment

## Structure

```
├── index.html              Homepage
├── assets/
│   ├── main.css            Single stylesheet
│   ├── theme.js            Persistent dark/light theme toggle
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

- All pages share the same nav component, synced with `python3 sync.py`
- Mobile nav collapses into a hamburger at 560px breakpoint
- The theme preference is stored locally in the browser; dark mode remains the default
- Filter tabs on writings page are CSS-only (active class via static HTML)
- The site remains framework-free and intentionally lightweight.
