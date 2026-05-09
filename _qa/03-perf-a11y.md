# Benji's AI Empire — Performance + Accessibility + SEO Audit

Audit date: 2026-05-10
Live URL: https://benjisaiempire.com/

---

## Performance — Critical

- **Hero image is huge AND render-blocking via preload.** `/images/hero-empire.jpg` = **572 KB**, preloaded as image AND used as CSS `background-image`. Compress to ~150 KB and serve a `webp`/`avif` variant. This is on the critical render path — it's literally the LCP.
- **Five images > 500 KB** ship to every visitor on the home page:
  - `broll-bangkok.jpg` — **737 KB** (largest)
  - `proof-shopify-2-8m.jpg` — 633 KB
  - `hero-empire.jpg` — 572 KB (CSS bg, preloaded)
  - `hero-petronas.jpg` — 567 KB
  - `headshot-mural.jpg` — 539 KB
  - Combined that's ~3 MB of just these five. Run `cwebp -q 80` or `squoosh` — should drop to ~600 KB combined.
- **TTFB is 931 ms.** That's slow for static nginx behind Cloudflare. `cf-cache-status: DYNAMIC` on the HTML — Cloudflare is NOT caching the page edge-side. Add a Cache Rule for `benjisaiempire.com/*` HTML (or set `Cache-Control: public, max-age=300, s-maxage=86400` in nginx for `text/html`). Should drop TTFB to <100 ms on cache hits.
- **HTML is 114 KB uncompressed.** Cloudflare is gzipping it on the wire (`Vary: Accept-Encoding` confirmed, gzip request returns ~27 KB), but origin nginx already has gzip on, so this is fine — the issue is just that the file itself is big because all CSS is inlined. Consider extracting `agents-styles` to a cacheable `/styles.css`.

## Performance — Wins to grab

- **Add `loading="lazy"` decoding="async" to ALL non-hero images.** Currently set on most courseware/proof images (good), but consider also `decoding="async"` and explicit `width` / `height` attributes to prevent layout shift.
- **Drop `course-dev-rig.jpg` (201 KB) or use the small placeholder version.** Several other course tiles use ~10 KB placeholder JPGs but `course-dev-rig` and `streaming-rig` (308 KB) and `course-marketing-engine` (9 KB — actually fine) are wildly inconsistent in weight. Pick a target dimension (~800px wide, q80) and re-export every course tile.
- **Google Fonts: 4 families loaded** (Anton, Fraunces, JetBrains Mono, Manrope) with multiple weights/italics. Each adds ~30-50 KB woff2. `display=swap` is set (good), and `preconnect` is in place (good), but consider self-hosting or trimming to 2 families. Fraunces with `opsz` axis is a variable font — that's already efficient.
- **Static asset caching is correctly configured** in nginx (`Cache-Control: public, max-age=2592000, immutable` for jpg/png/css/js/woff2 — 30 days). Verified live.
- **Origin gzip is configured correctly** (`gzip on; gzip_types ... text/css application/javascript image/svg+xml`).
- **HTTP/2 alt-svc h3** is advertised by Cloudflare. Good.

## Accessibility — Must fix

- **Empty alt + `aria-hidden="true"` on the polaroid hero image** (line 2758). The image (`headshot-pointing.jpg`, 453 KB) is the second face shown in the hero with the caption "yeah, you." — it's decorative-by-intent but content-by-impact. If truly decorative, fine. If you want screen readers to announce Ben's polaroid, give it a real alt and remove `aria-hidden` from the figure.
- **No visible focus styles on interactive elements.** Searched `:focus` / `:focus-visible` — only `.skip-to-main:focus` is styled. Every link, button, pricing tier CTA, and nav item has zero visible keyboard focus indicator. Add a global `:focus-visible { outline: 2px solid var(--gold); outline-offset: 2px; }` rule. This is a WCAG 2.4.7 failure.
- **Headline structure is OK but check h2/h3 ordering.** One h1 (hero), then h2 (pricing-headline, courses-display, ps-headline), then h3 (tier names, tile titles, receipts, footer cols). Heading order is valid. The footer brand uses h2 ("Benji's AI Empire") which is fine but semantically debatable — could be `<p>` since the visual logo isn't a section heading.

## Accessibility — Should fix

- **Cream/gold text on photo backgrounds — contrast risk.** The hero uses `--cream:#f4ecd8` text over a dark ink panel (fine, ~13:1) AND over `hero-empire.jpg` photo on the right side. Without a scrim/overlay on the photo side, any text floating over the photo (photo credit, polaroid caption) risks failing 4.5:1. Recommend a `linear-gradient(rgba(11,11,12,.45), transparent)` overlay on photo regions where text overlaps. Same applies to the proof section receipts if any text overlays the photos.
- **`role="marquee"` is non-standard** (line 2765). The `<div role="marquee">` is invalid ARIA — `marquee` is not a real role. Use `role="region" aria-label="Proof ticker"` or just leave it as a plain region. Screen readers will ignore the bogus role.
- **No `aria-current` on nav links** (if the topbar has nav). Minor.
- **Skip link present and functional** (`<a class="skip-to-main" href="#main">` + `<main id="main">` exists at line 2669). Good.
- **`prefers-reduced-motion` is respected** in 6 places across the stylesheet — animations and transitions get neutralized. Good.
- **`<html lang="en">` set.** Good.

## SEO

- **`<title>` present and unique** — "Benji's AI Empire — Sales Calls Free · Everything Else $10 · Wholesale GHL $49"
- **`<meta description>` present** — 173 chars, well-targeted.
- **OG tags complete** — `og:type`, `og:url`, `og:title`, `og:description`, `og:image`, `og:site_name`, `twitter:card=summary_large_image`. Note: no explicit `og:image:width`/`og:image:height` — add them so LinkedIn/Slack render properly without re-fetching.
- **Canonical URL set** — `<link rel="canonical" href="https://benjisaiempire.com/" />`. Good.
- **`sitemap.xml` accessible** — 11 URLs (home + 4 tiers + 2 challenges + 4 courses). Clean.
- **`robots.txt` accessible** — Cloudflare-managed, allows search bots, blocks AI training crawlers (GPTBot, ClaudeBot, CCBot, etc.). Fine.
- **Structured data (JSON-LD) is MISSING.** No `<script type="application/ld+json">` anywhere in the HTML. Add at minimum:
  - `Organization` (name, logo, url, sameAs for socials)
  - `WebSite` with `SearchAction` (optional)
  - `Person` for Ben Boyce (since this is a personal brand) with `image`, `jobTitle`, `sameAs`.
  - For each course page, add `Course` schema. Big SEO win, low effort.

## Numbers (raw)

- **HTML weight:** 114 KB uncompressed / ~27 KB gzipped on the wire
- **Total page weight (HTML + 14 images + logo + favicon + fonts):**
  - HTML gzipped: ~27 KB
  - Images (14 referenced + logo + favicon): ~4.46 MB
  - Google Fonts CSS + woff2 (4 families): est. 200-300 KB
  - **Total: ~4.7-4.8 MB**
- **TTFB:** 931 ms (Cloudflare DYNAMIC, not edge-cached)
- **Total request time (homepage HTML):** 1.66 s
- **Largest image:** `broll-bangkok.jpg` — **737 KB**

### Top-5 image offenders (compress these first)

| File | Size | Used as |
|---|---|---|
| broll-bangkok.jpg | 737 KB | course tile (lazy) |
| proof-shopify-2-8m.jpg | 633 KB | receipts grid (lazy) |
| hero-empire.jpg | 572 KB | hero CSS bg + preloaded |
| hero-petronas.jpg | 567 KB | receipts grid (lazy) |
| headshot-mural.jpg | 539 KB | proof section + receipts (lazy) |
| headshot-pointing.jpg | 453 KB | hero polaroid |

Target: each ≤ 200 KB at q80 webp. Should reclaim ~2.8 MB.

### Verified-good config

- nginx gzip: on (`text/css text/xml application/json application/javascript image/svg+xml` etc.)
- nginx static caching: `public, max-age=2592000, immutable` for jpg/png/css/js/woff2/svg/ico
- Cloudflare is in front (server: cloudflare, cf-ray present)
- gzip confirmed on the wire (`Content-Encoding: gzip` with `Accept-Encoding: gzip`)
- Security headers: `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: geolocation=(), microphone=(), camera=()` — all present.
