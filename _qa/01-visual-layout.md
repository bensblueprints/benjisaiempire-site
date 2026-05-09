# Visual / Layout QA — benjisaiempire.com

Live URL: https://benjisaiempire.com/  
Source: `C:\Users\HP\benjisaiempire-site\index.html`  
Reviewed: 2026-05-10

## Top issues (ranked)

1. **[critical]** — Mojibake (UTF-8 → Win-1252 → UTF-8 corruption) is splattered across visible copy and CSS comments — the regex extract/concat step did the round-trip. Examples:
   - `â„– 01` should be `№ 01` (hero issue tag, line 2743)
   - `â‰ˆ18.5h` should be `≈18.5h` (courses meta-row, line 2975)
   - `Â·` should be middle-dot `·` (everywhere — topbar brand sub line 2651, marquee separators 2773–2793 are entered as literal `Â·`, hero rail "On Air Â· Tuesdays" 2684, ticker "Live calls / wk", "Bucket" footers, proof-section ps-folio "NÂº 04" 3157, ps-stat-label "Â·", footer "Â© 2026", footer "Operator's Playbook &nbsp;Â·&nbsp; Built In Public" 3305, etc.)
   - `â€"` should be em-dash `—` (hero "06 â€" The Empire" 2680, hero CTAs 2714, proof bio "â€" so I could write" 3176, marquee items 2788, 2814, etc.)
   - `â€œ` / `â€` (smart quotes) in tile taglines 2996, 3018, 3040, 3062, 3084, 3106 and footer brand-tagline 3307
   - `â†'` `â†—` `â†"` (arrows) inside `<span class="arrow">`/`<span class="ps-arrow">` in 14+ CTAs (2710, 2714, 2861, 2898, 2941, 3110, etc.) — every CTA arrow renders as garbage
   - `â”€` (box-drawing) in CSS section comments (cosmetic only)
   - **Fix**: re-save `index.html` as UTF-8 (no BOM is fine, it has one) AND fix the actual byte sequences. The CSS comments are harmless; but every visible `Â·`, `â€"`, `â„–`, `â‰ˆ`, `â†'`, `â€œ`, `â€` must be replaced with the real Unicode char or HTML entity. Confirm `Content-Type: text/html; charset=utf-8` is sent (currently nginx returns just `text/html` — meta charset saves it, but only because BOM is present).

2. **[high]** — Pull quote does NOT dominate. The brief said "should DOMINATE; if it looks small/lost, flag it." `.proof-section .ps-quote-body` is `font-size:clamp(28px,3.6vw,56px)` AND `max-width:24ch` AND `margin-inline:auto` AND `text-align:left`. Combined with the `.ps-quote-marker` (a 220px italic open-quote that sits absolutely positioned top-left), the quote body is squeezed into a narrow center column flanked by mostly empty space. On a 1440px viewport the body caps at ~56px which is smaller than `.ps-headline` (168px) and the `.ps-stat-num` (108px). It reads as a sidebar, not a spread. **Fix**: either bump `font-size` to clamp(40px, 5.5vw, 88px), widen `max-width` to 36–40ch, or remove the centered narrow column treatment and let it span the full 1180px masthead width.

3. **[high]** — Scarcity meter contradicts itself on the featured pricing card. HTML says "**87** of 100 left" (line 2924) but `.scarcity-bar::before { width: 87%; }` (line 1083) plus the gradient `gold→rust` paints the bar 87% full — implying 87 sold / 13 left. They should agree. **Fix**: change the bar fill to `width:13%` (13 sold, 87 left) — or change the copy if 87 is sold. File: `index.html` line 1083 vs 2924.

4. **[high]** — Footer "Entry Points" links go to anchors that don't exist on the page: `#starter-kit`, `#empire-challenge`, `#cold-calling-challenge`, `#software-partners` (lines 3316–3319). Clicking them does nothing (or jumps to top). The actual sections are `#pricing`, `#the-bucket`, `#proof`. The pages they probably mean (`/starter-kit/`, `/challenge/`, `/cold-call-30/`, `/partners/`) DO exist as folders. **Fix**: change to absolute paths `/starter-kit/`, `/challenge/`, `/cold-call-30/`, `/partners/`.

5. **[high]** — Hero polaroid is positioned `left:42%; top:54%; transform:translate(-58%,-50%)` and crosses the seam between the 42% ink panel and 58% photo panel. On viewports between 860–1100px, the breakpoint shifts the grid to `48%/52%` and the polaroid jumps to `left:48%`, but its width doesn't shrink proportionally, so it can overlap the headline `h1` (which extends right under the polaroid). The headline `clamp(46px,6.6vw,108px)` at 1000px viewport is ~66px — the last word of "the videos free." can collide with the polaroid's left edge.

6. **[high]** — Tile-03 and tile-06 numerals (`clamp(160px,22vw,320px)` and `clamp(180px,26vw,380px)`) sit at `top:-64px` and `top:-88px` respectively. The page section `.courses-section` has `overflow:hidden` (line 1133) — these huge stroked numerals will be clipped at the section's top edge, not floated freely. On wide viewports the 320–380px font sizes mean ~250–300px tall numerals, but only the bottom ~190–290px is visible. Either drop the negative `top` offsets, or remove `overflow:hidden`, or accept that the numerals will look chopped.

7. **[high]** — Tile-02, tile-04, tile-05 use `transform:translateY(64px / 40px / -32px)` AFTER the IntersectionObserver adds `.is-in`. The base `.tile { transform: translateY(28px); }` plus the per-tile post-in translate creates a vertical waterfall that, combined with the 12-col asymmetric grid, will cause tile-02 to dip noticeably below tile-01's footer and tile-05 to push up into tile-04's footer area. Tile-04's right edge ends at column 5 and tile-05 starts at column 7 — column 6 is an empty gutter. With tile-05 translated `-32px` (up) and tile-04 translated `+40px` (down) the two captions can sit at very different heights — visually choppy, not editorial.

8. **[high]** — Tile-03 `.tile-03 .tile__copy { display:grid; grid-template-columns: 5fr 4fr 3fr; gap:56px; }` (line 1485). The kicker has inline `style="grid-column:1/-1"` (line 3034), but `.tile__title`, `.tile__tagline`, `.tile__body` are placed in cols 1/2/3 of the SAME grid row, forcing them onto one line. With `clamp(40px,5vw,84px)` title and `clamp(18px,1.5vw,24px)` tagline and 15px body, the body column is ~22% of available width — at 1280px container that's ~280px, fine, but the `.tile__title` "AI Marketing Engine" plus tagline column "One Tuesday Live → 14 pieces of content." may wrap weirdly. Worth a screenshot at 1280/1440. (Same applies to tile-06.)

9. **[medium]** — `.tier--featured` at desktop has `transform:translateY(-12px); margin-top:-12px;` to lift it above the other two cards (line 962). But the tier-ribbon is `position:absolute; top:0` and overflows above the card border — combined with the `-12px` lift, the ribbon overlaps the `.pricing-masthead` bottom margin (which is `clamp(48px,6vw,88px)`). At narrow desktop widths (~900–1000px) this can feel cramped. Verify ribbon doesn't kiss the lede paragraph.

10. **[medium]** — Hero `::after` decorative seam is a 1px vertical line at `left:42%` (line 90). On the 1100px breakpoint the grid switches to `48%/52%` (line 527) and the `::after` correctly moves to `left:48%`. BUT the polaroid `transform:translate(-58%,-50%)` is keyed to a 42% seam — at the 48% breakpoint the polaroid's translate origin doesn't update, so polaroid sits visually offset from the new seam. Subtle but a designer would notice.

11. **[medium]** — `.hero-section` has `overflow:hidden` — the polaroid uses `box-shadow: 0 30px 60px -20px rgba(0,0,0,.7)` and may have its bottom shadow clipped if it sits near the bottom of the hero. Same for the bracket `1.5px` decorative borders.

12. **[medium]** — `.tile-03 .tile__photo { aspect-ratio: 21/9 }` (cinematic) plus `tile-03 .tile__numeral { font-size: clamp(160px,22vw,320px); top:-64px }`. At 1480px courses-grid container width (line 1151), the tile-03 photo is ~1410px × 605px. The 320px numeral floats top-left. Looks fine on widescreen. But at the 1000px breakpoint where the 12-col layout activates, tile-03 photo is ~960px × 411px, and the numeral is ~210px — proportional to width but not to height — feels chunky vs cinematic. Editorial-intentional, but flag.

13. **[medium]** — Marquee: `.shell-marquee__track { animation: shell-marquee-scroll 30s linear infinite; }` translates `0 → -50%`. This works ONLY if both `.shell-marquee__group` divs have IDENTICAL widths AND together fill `width:max-content`. They do (group 1 = group 2 byte-for-byte). At a 30s duration with ~12 items per group at 26px+content padding, total scroll length is roughly 1500–1800px per group, so scroll speed ≈ 50–60px/s — reasonable. No clipping bug. But `.shell-marquee__fade` is 80px wide; on viewports < 480px that fade eats ~33% of the visible content. **Fix**: shrink fade to 32–40px on mobile.

14. **[medium]** — Pricing `.tier--featured::before` is a 1px gold gradient line `top:-1px`, but `.tier-ribbon` is `position:absolute; top:0; left:0; right:0` and covers it entirely. The decorative gold hairline rule (designed as a top-of-card register mark) is hidden on the only card it really matters for. **Fix**: move ribbon down by 4px or set `.tier--featured::before { top:-1px; z-index:2 }` above the ribbon top edge.

15. **[medium]** — Featured tier shimmer (`.tier--featured::after` lines 974–999) uses CSS mask-composite trick — works on Chromium/Safari, but `mask-composite: exclude` is unsupported pre-2023 Firefox; not a break, just a no-op. Acceptable.

16. **[medium]** — Hero `.polaroid::after` content is hardcoded "BENJI / 2026" with `position:absolute; top:-22px; left:14px; background:var(--ink); border:1px solid var(--line)` — this is a separate 9px monospace tab. On the 860px breakpoint where the polaroid is moved to `right:22px; bottom:-46px`, this tab still renders at top-left of the polaroid and may collide with the photo above it (the hero-right is 62vh and the polaroid hangs off the bottom edge by 46px, so the tab appears against the next section).

17. **[medium]** — Pricing `.scarcity-bar` is `flex:1` inside a flex row that includes a fixed-width pulse and a counter `.scarcity-count`. It compresses on narrow cards. At < 380px card width, the bar can be < 80px which is unreadable as a progress indicator.

18. **[low]** — `.tile__cta::after { content: "â†'" }` (line 1467) uses literal mojibake instead of `→`. Same in `.shell-topbar__cta::after { content: "â†'" }` (line 2340). All CTA arrows are broken text in CSS-generated content. (Listed separately because it's CSS-only — issue #1 is HTML body content.)

19. **[low]** — `.proof-section .ps-tile.t1 .ps-frame{ aspect-ratio:auto; }` and `t2{ aspect-ratio:auto }` (lines 2079–2080). The tiles use `grid-row:span 5` and `grid-row:span 3` with `grid-auto-rows:84px` and `gap:14–22px`. So t1 frame is ~5*84+4*gap = ~510px tall, width is `span 7` of 12 cols = ~58% of 1320px = ~770px. The shopify screenshot is roughly 16:10 — it'll be cropped to 770×510 (3:2). The "VERIFIED · SHOPIFY EXPORT" badge has `Â·` mojibake (line 2092).

20. **[low]** — Topbar `height:80px` collapses to `64px` on `.is-scrolled` (line 2205), but no JS in the document adds the `.is-scrolled` class. The animation is wired but never triggers. Either add a scroll listener or delete the unused styles.

21. **[low]** — Hero stat ticker: `.stat .v em { font-family:'Fraunces',serif; font-style:italic; color:var(--gold); }` — but the HTML uses `<em>â€"figure</em>`, `<em>+</em>`, `<em>/mo</em>` (lines 2722, 2726, 2730). The em-dash is mojibake — but more importantly, `8â€"figure` becomes `8—figure` should render as `8 — figure` with the em-dash gilded/italic. The dash by itself with no space looks tight against the `8`.

22. **[low]** — `.courses-display .outline { -webkit-text-stroke: 1.5px var(--cream) }` — text-stroke needs `text-stroke` shorthand for non-webkit, but the rule includes `text-stroke: 1.5px var(--cream)` (lines 1208–1209) which is not a valid CSS shorthand (only `-webkit-text-stroke` exists). Harmless, just dead.

23. **[low]** — `.proof-section .ps-quote-marker { font-size:clamp(120px,16vw,220px); top:clamp(-8px,-1vw,-4px); }` — the `clamp(-8px,-1vw,-4px)` is fine, but the marker sits absolute over `.ps-quote-body` (which has `padding-left: 0` from masthead but body itself has `padding:clamp(36px,5vw,72px) clamp(24px,4vw,56px)`). The 220px italic glyph will overlap the first line of the quote text — intentional editorial overlay, but at narrow widths the glyph swallows the first 4–5 words.

24. **[low]** — `.tier-price-strike { transform:translateY(-6px) }` (line 793). Combined with `align-self:center` on a baseline-aligned flex row, the $99 strikethrough sits visually higher than the $49 currency sign, which is fine — but at the smallest breakpoint (`.tier-price{ font-size: 56px }` line 1117) the gap between $99 and $49 baselines can become awkward.

25. **[low]** — `<meta property="og:url">` is hard-coded `benjisaiempire.com/` and there's no `<html lang>` issue, but `<meta property="og:image">` references `/images/hero-empire.jpg` which is a 16:9 photograph likely cropped poorly for OG (1200×630). Not visual on the page itself, but social previews will look bad.

## What's working

- All 22 image references return HTTP 200. No broken `<img>` srcs.
- Live HTML matches the local `index.html` byte-for-byte (server is correctly publishing the build).
- CSS is well-namespaced — every section uses scoped class prefixes (`.hero-section`, `.pricing-section`, `.tier-…`, `.tile`, `.proof-section .ps-…`, `.shell-topbar`, `.shell-marquee`, `.shell-footer`). I did NOT find any cross-section selector bleed (e.g. no global `h2` rules, no `.tier h2` accidentally hitting `.proof-section h2`). The mechanical concat preserved isolation cleanly.
- Single source of truth for tokens — every section consumes `var(--ink)`, `var(--cream)`, `var(--gold)`, etc. Pricing section additionally aliases them under `--ps-*` for safety. No literal `#0b0b0c` or `#d4af37` appearing in section CSS bodies (literal hex only in `:root`, in `tier--featured` background `#1a1916` line 951 — one drift, see below).
- Type stack is consistent: Anton (display), Fraunces (italic editorial), Manrope (body), JetBrains Mono (kicker/labels). Every section uses these in the same roles. No font drift.
- Color palette holds across sections: ink/cream/gold/rust register the same in topbar, hero, pricing, courses, proof, footer.
- Shell-topbar is `z-index:80` and properly stacks above all content sections (which have `z-index:1` or unset). No sticky-overlap issues.
- `body { overflow-x:hidden }` (line 38) prevents horizontal scrollbars from any of the off-screen polaroid/numeral/marquee elements.
- Marquee duplicates groups 1+2 byte-identical so the 0→-50% loop is seamless.
- Reduced-motion media queries are present in hero, pricing, courses, proof — accessibility solid.
- Pricing tier card heights line up via `min-height:100%` + `display:flex` + `tier-foot { margin-top:auto }`. CTAs anchor at the bottom of every card. Good.
- Pricing 3-card asymmetry (1fr 1fr 1.18fr) plus `--featured` lift creates visible hierarchy without breaking grid.
- All anchor `id`s used by topbar nav `#pricing` exist (line 2823). `#the-bucket` (line 2956) and `#proof` (line 3148) exist.

## Notes / further investigation

- **Render the page in a real browser at 1440×900, 1280×800, 1024×768, 768×1024, 390×844** and screenshot the hero seam, pricing trio, courses grid (especially the asymmetric `translateY` offsets on tiles 02/04/05), proof pull quote, and footer. Static analysis can't catch float/translate collisions perfectly. Per CLAUDE.md, the next step is the Playwright design analyst pass.
- **Encoding fix is the #1 priority and likely a one-shot find/replace** — the corruption is consistent: every `—` became `â€"`, every `·` became `Â·`, every `→` became `â†'`, etc. A scripted fix can repair the file in one pass.
- **Featured pricing tier `background: linear-gradient(180deg, #1a1916 0%, var(--ps-ink-2) 65%)`** — the literal `#1a1916` is the only hex color leak in section CSS. It's a deliberate slightly-warmer ink for the featured card. Either token-ize as `--ink-warm` in `:root` for consistency, or leave as a local accent.
- **Topbar is sticky** with `position:sticky; top:0; z-index:80` and the marquee that follows is `position:relative` — when the topbar sits over content, the marquee's gold hairline `::before` (top:0) sits flush under the topbar's gold hairline `::after` (bottom:-1px) — they overlap at the seam between topbar and marquee on first paint (before any scroll). Worth a screenshot.
- **Courses tile-06's ENORMOUS numeral `clamp(180px,26vw,380px)`** at full 1480px viewport renders ~380px tall. Tile-06 photo is `aspect-ratio:21/9` and `grid-column:1/-1` so ~1410×604px. The numeral sits `top:-88px; left:2%`, so it floats above the photo but `overflow:hidden` on `.courses-section` will clip ~88px off the top of the "06" stroke. Intentional design choice (peek-numeral) but verify it doesn't read as bug.
- **Polaroid::after pseudo "BENJI / 2026" tab** — clever, but if any user has a system where the photographic image fails to load, the polaroid div becomes a blank cream rectangle with a tiny gold tab and the "yeah, you." caption hanging — looks broken. Not critical.
- The page is 113.9 KB of HTML+inline CSS. With 5 sections concatenated this is reasonable. No external CSS file is loaded — everything is inline `<style>`. That means no caching for CSS but also no FOUC.
- Worth running `lighthouse` to confirm CLS — the hero `heroLineUp` keyframe animates `translateY(102%)→0` on first paint and the polaroid `heroPolaroid` shifts position. Likely CLS > 0.1. The `prefers-reduced-motion` query mitigates.
