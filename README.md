# Liam Graham — Actor Portfolio

A static portfolio site for **Liam Graham**, a Scottish‑born Australian screen actor. The site showcases credits, character range, awards, news, and contact details — designed as a refined, editorial single‑purpose marketing site.

| | |
|---|---|
| **Live site** | _Coming soon at a custom domain_ → `https://YOUR-DOMAIN.com` *(placeholder — domain pending)* |
| **Vercel project** | https://vercel.com/thedalycreative/liam-graham-actor |
| **Source** | https://github.com/thedalycreative/liam-graham-actor |
| **Status** | Active — pre‑launch (waiting on production domain) |

---

## Visuals

### Hero — black‑and‑white event portrait
![Liam Graham — hero portrait](images/hero-section-1.png)
<!-- TODO: replace with hero slideshow GIF once recorded -->

### Headshot
![Liam Graham — primary headshot](images/headshot-primary.jpg)

### Featured project — *Burning Kiss* (2018)
![Burning Kiss — official poster](images/project-burning-kiss-poster.png)
<!-- TODO: replace with credits-page scroll GIF -->

### Behind the scenes
![Liam Graham — behind the scenes](images/behind-the-scenes.png)

---

## Description

This is a **plain HTML, CSS, and vanilla JavaScript** site — no build step, no framework. Pages are written by hand, share a single design system in `css/style.css`, and rely on a small amount of scroll/reveal JS in `js/main.js`. The site is deployed on Vercel as static files.

It serves three audiences:

- **Casting directors and producers** — credits, characters, IMDb link
- **Agents and managers** — awards and contact details
- **Journalists and fans** — news and editorial coverage

### Pages

| Page | Purpose |
|---|---|
| `index.html` | Home — hero, featured credits, showreel teaser |
| `credits.html` | Full filmography with posters and stills |
| `characters.html` | Character range gallery |
| `awards.html` | Wins, nominations, and laurels |
| `news.html` | Press coverage and editorial |
| `contact.html` | Casting / representation enquiries |

---

## Installation

Clone the repo:

```bash
git clone https://github.com/thedalycreative/liam-graham-actor.git
cd liam-graham-actor
```

There is nothing to install for the site itself — it's plain HTML/CSS/JS. The only dev dependency is `serve` (pulled via `npx`, no `npm install` required).

## Usage

### Run locally

```bash
npm run dev
```

This serves the site at `http://localhost:3000`. Open any page (`/`, `/credits.html`, `/contact.html`, …) in the browser.

### Edit content

- **Copy / text** — edit the relevant `*.html` file directly. Sections are commented (`<!-- HERO -->`, `<!-- CREDITS -->`, etc.).
- **Styles** — all design tokens (colors, fonts, easings, timings) live at the top of `css/style.css` under `:root`.
- **Images** — drop new files into `/images/` and reference them as `<img src="images/<filename>">`. Keep filenames descriptive (`project-*.png`, `headshot-*.jpg`, `portrait-*.png`).

### Deploy

Pushes to the default branch deploy automatically via the Vercel project linked above. No build command is needed; Vercel serves files straight from the repo root. Anything under `archive/` (see below) is excluded from the deploy via `.vercelignore`.

---

## Project structure

```
liam-graham-actor/
├── index.html          # Home
├── credits.html        # Filmography
├── characters.html     # Character range
├── awards.html         # Awards & nominations
├── news.html           # Press
├── contact.html        # Contact
├── css/
│   └── style.css       # Design system + all styles
├── js/
│   └── main.js         # Scroll reveals, nav, slideshow
├── images/             # All images referenced by the live site (40 files)
├── archive/            # NOT deployed — raw source assets
│   ├── loose-images/         # Original unprocessed shoots & posters
│   ├── headshots-stock/      # Bulk character/headshot studies
│   ├── unreferenced-images/  # Site image variants not currently in use
│   └── convert_light.py      # One‑off image processing script
├── package.json        # Dev server only (`npm run dev`)
├── .vercelignore       # Excludes archive/ and *.zip from deploys
└── README.md           # You are here
```

The `archive/` folder is intentional: it preserves the original asset library (raw shoots, alternate cuts, unused poster comps) without bloating the deployed site. Vercel ignores it. If you need an image that isn't in `/images/`, look there first.

---

## Support

For issues with the site itself, open an issue on the [GitHub repo](https://github.com/thedalycreative/liam-graham-actor/issues).

For **casting, representation, and professional enquiries**, use the [contact page](contact.html) or message [@liamansellgraham](https://www.instagram.com/liamansellgraham/) on Instagram.

---

## Roadmap

- [ ] Purchase and connect production domain
- [ ] Add showreel video to home page
- [ ] Record short GIFs for the README visuals (hero slideshow, credits scroll)
- [ ] Add Open Graph preview images per page
- [ ] Optional: migrate to a static site generator if the page count grows

---

## Contributing

This is a personal portfolio site and is **not accepting external contributions**. If you spot a bug or have a suggestion, an issue is welcome.

---

## Authors and acknowledgment

- **Subject** — Liam Graham · [IMDb](https://www.imdb.com/name/nm4223899/) · [@liamansellgraham](https://www.instagram.com/liamansellgraham/)
- **Design and build** — [The Daly Creative](https://thedalycreative.com)

---

## License

© Liam Graham. **All rights reserved.** All images, copy, and brand assets in this repository are the property of Liam Graham and may not be reused without written permission.
