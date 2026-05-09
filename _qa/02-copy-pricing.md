# Copy / Pricing QA — benjisaiempire.com

Date: 2026-05-10
Scope: Homepage tier copy + all linked sub-pages (read-only).
Source-of-truth tier copy:
- $0 FREE = ONLY sales call videos (Tues Cold Call Live + Thurs Build Day Live + archive). Nothing else.
- $10/mo INSIDER = 4 courses, every prompt/script, Starter Kit, both 30-Day challenges, GHL reseller @ $0.04/min, community.
- $49/mo WHOLESALE GHL = was $99, first 100 seats only, locked for life, JUST GHL @ $0.015/min, NO courses.

Note: Could not WebFetch live URLs (permission denied). Sub-page liveness was not verified by HTTP — the audit reads the local source-of-truth HTML committed to `C:\Users\HP\benjisaiempire-site\`. If the live site differs from this repo it would only get worse, since these files are what gets shipped to Coolify.

---

## Critical copy errors

### Sub-pages are still on the OLD pricing model (Founder $99 / first 50 / $149 retail)
The homepage was updated to the new $49 / 100-seats / was-$99 wholesale framing, but every sub-page still sells "Empire Builder Founder — $99/mo locked for life — first 50 only, then $149." This is the single biggest QA failure on the site. The homepage and every other page contradict each other.

Specific files (all under `C:\Users\HP\benjisaiempire-site\`):

- **`founders\index.html`** — entire page is the OLD offer.
  - L8 `<title>`: `Empire Builder — $99/mo Locked For Life. First 50 Founders Only`
  - L9 meta description: `The first 50 founder spots lock $99/month for life. After 50, the price moves to $149/month for everyone.`
  - L24,31,32 OG/Twitter titles all say `$99/mo Locked For Life` / `First 50 founders only. After that, $149/mo for everyone.`
  - L208–214 sticky bar: `38 OF 50 SPOTS LEFT — $99/MO LOCKED FOR LIFE` / `FOUNDER DOORS CLOSED — BUILDER IS NOW $149/MO RETAIL`
  - L247 eyebrow: `Founders · First 50 Only · $99/mo Locked For Life`
  - L249 H1: `The first 50 get in for life at $99/month.`
  - L260–269 counter: `12 of 50 founder spots claimed`, `38 founder spots remaining at $99/mo`
  - L274 primary CTA: `Claim My Founder Spot — $99/mo`
  - L279 reassurance: `$99/mo locked for life`
  - L296 doors-closed H2: `All 50 founder spots are gone.`
  - L300 retail price: `Builder retail at $149/month`
  - L301 mention `$99 lock for life` and "founder badge" framing
  - L362–364 founder pitch references "first 50"
  - L378 H2: `As a founding Builder ($99/mo locked for life), you get:`
  - L484–485: `FOUNDER PRICE: $99/month, locked for life. AFTER 50 FOUNDERS: $149/month for everyone.`
  - L506–508 upgrade promise: "if you upgrade before all 50 founder spots fill, you still lock the $99 price"
  - L568 form title: `Claim my founder spot — $99/mo locked for life.`
  - L577–585 GHL embed code references `Empire Builder Founder ($99/mo)` and `/checkout/empire-founder-99` for $99/mo
  - L612–625 FAQ: $99 / $149 / $199 / $297 grandfather framing
  - **Correct version:** Page should be the $49/mo wholesale GHL offer — was $99, first 100 seats, $0.015/min, NO courses, locked for life.

- **`insider\index.html`** — comparison table and copy reference the dead $99 founder tier.
  - L237 "Builder-only at $99/mo — that's the upgrade trigger."
  - L285 H2: `Free Starter Kit. Insider $10/mo. Builder $99/mo founder.`
  - L293 compare card: `Free Starter Kit — $0 / one-time` listing "30-Day AI Empire Challenge (email drip)" and "Free seat at the live launch event" — **violates new rule that ONLY sales call videos are free.**
  - L298–299 list items inside the "Free" comparison column are wrong (Starter Kit and Empire Challenge moved to $10).
  - L307 CTA `Get The Free Kit` linking to `/starter-kit` — Starter Kit is no longer free.
  - L332–347 `Empire Builder (Founder) — $99 / month locked for life` comparison column and CTA `See Founder Page`
  - L353–354 promise: "If 50 founder spots are still open when you upgrade, you lock the $99 founder rate too."
  - L366 H2: `What you DON'T get at $10 — and when to upgrade.` with old comparison
  - L389–394 phone-math arguments comparing Insider $0.04 vs Builder $0.015 reference $99/$149.
  - L401–405 "Until 50 Builders fill, Insiders get a bonus." + counter `38 of 50 Builders.`
  - L432 bottom CTA "$97–$297/mo. As an Insider..." (this one is a pricing-context line for GHL retail, OK in isolation but contextually muddled)
  - L483–485 H2: `$10. Same inbox, more access. Cancel anytime in one click.` "The entry tier exists because not everyone is ready for $99 on day one." — references dead $99 tier.
  - L532 footer FAQ: "If 50 founder spots are still open when you upgrade, you lock the $99 founder rate too."
  - **Correct version:** Replace all "$99 / 50 / $149 / Builder Founder" copy with "$49 / 100 / was-$99 / Wholesale GHL." Also: $10 Insider should be described as the EVERYTHING tier (all 4 courses, all prompts, Starter Kit, both 30-day challenges, community, GHL @ $0.04). Wholesale GHL is software-only, NO courses.

- **`courses\cold-calling\index.html`** (and same pattern in `brand-builder`, `marketing-engine`, `empire-os`)
  - L373–374 (cold-calling): "is included in Empire Builder ($99/mo Founder)"
  - L473–486 (cold-calling): compare-card titled `Empire Builder — Founder` at `$99/mo · locked for life`, with line "After 50: $149/mo for new joiners" and CTA "Skip — Get This Free With Builder ($99/mo)"
  - L551,585,588 (cold-calling) repeat $99 / $297 / $149 framing
  - `brand-builder\index.html` L186 references "Founders/Founding-Member offer ... deployed via Netlify" — also flags the **Netlify** mention, which violates the Coolify-only rule (and is wrong context anyway since this is supposed to be a course curriculum description). L251 same "Founders / Founding-Member offer" copy. L415–445, 546–549 same $99 / $149 / Founder compare card.
  - `empire-os\index.html` L67 schema.org `"name": "Empire Builder Founder"`; L247 crown badge `Empire Founder Material`; L377–382 explains a now-invalid three-tier model **"The Two-Tier Stack (Insider / Builder / Founder)"** — note the heading says "Two-Tier" but lists three tiers, and this entire mental model is no longer correct.  L380 `Builder $99/$149`. L595, 627, 635, 648–665, 674 all reference $497 one-time + $99/mo Builder Founder.
  - **Correct version:** Either remove the comparison cards entirely on course pages, or replace the right-hand "Builder Founder $99" column with "Insider $10/mo — get this course + 3 others." Wholesale GHL ($49) does NOT include courses, so it should NOT appear as the "get the course free" upsell on any course page. The $10 Insider is the upsell.

- **`partners\index.html`**
  - L317 `Join Insider To Unlock Codes` — wording OK, but page L344 says `Builders ($99/mo founder rate, $149 retail) see the deeper member-only deals`
  - L422, L573, L809 partner cards have CTA `Become A Builder →` linking to `/founders`
  - L481 "Insiders dial at $0.04/min, Builders at $0.015/min" — should be "Wholesale dials at $0.015/min."
  - L501 reference list: `$10 / $99 / $149 / course one-time checkouts` — $99 and $149 are dead.
  - L851–866 founder counter callout: `Founder rate is $99/mo locked for life, capped at the first 50` + counter `38 of 50 founder spots remaining` + CTA `Lock Founder Pricing — $99/mo`
  - L915 "Same $10 / $99 doors as everything else in the Empire."
  - **Correct version:** Replace Builder/Founder language with Wholesale GHL ($49 was $99, first 100 seats). Note the per-minute pricing is preserved correctly ($0.04 vs $0.015) but bound to the wrong tier names.

- **`challenge\index.html`** (30-Day Empire Challenge)
  - L382 "Members who complete BOTH ... join the Empire Insider tier ($10/mo) for the community" — OK, but
  - L442–443 FAQ: `mention the Empire Insider tier ($10/mo) or the founder rate (Empire Builder, $99/mo locked for life for the first 50).` — references dead pricing.
  - L546 footer link: `Empire Builder — Founder Rate` linking to `/founders`
  - **Correct version:** Replace Empire Builder Founder $99 references with Wholesale GHL $49 (was $99, first 100). Also: the homepage now says the 30-Day Empire Challenge is **Insider-only ($10)**, but the Challenge page itself markets the program as free email signup. **This is a direct contradiction with the homepage tier copy** (homepage tier-02 list at L2888 says "30-Day Empire Challenge (email sequence)" is included in the $10 Insider — implying it's not free). Decide which is canonical and reconcile.

- **`cold-call-30\index.html`** (30-Day Cold Calling Challenge)
  - L521–522 FAQ: `Day 30 graduation includes a 24-hour Builder upgrade window at the founder rate ($99/mo locked for life).`
  - L638 footer: `Empire Builder — Founder Rate`
  - Same homepage-vs-page contradiction: homepage tier-02 lists "30-Day Cold Calling Challenge (email sequence)" as Insider-only ($10), this page sells it as free.

- **`starter-kit\index.html`**
  - This entire page is selling the Starter Kit as a FREE 4-tool lead magnet (cold call script, Claude Code design prompts, 30-Day Empire Challenge, free seat at live launch event).
  - **Direct contradiction with homepage**: the homepage Tier-02 list (L2887) explicitly says "The Starter Kit (PDF + cold-call scripts)" is INSIDER ($10). The current Starter Kit page L290–308 has CTAs `Get The Starter Kit` opting users into a free email form.
  - L432 footer: `Empire Builder — Founder Rate`
  - L348 emails will mention "the Insider tier or founder rate" — references dead founder tier.
  - **Correct version per source-of-truth:** Either the Starter Kit IS still free as a lead magnet (then update homepage Tier-02 to remove it), OR the Starter Kit is paywalled inside Insider $10 (then this entire page needs to be rewritten as a $10 paywall page). The brief says "no Starter Kit free — those moved to $10," so this page should become an Insider sales page, not a free opt-in.

### Homepage FREE-tier CTA points to a free-Starter-Kit opt-in page
- `index.html` L2859 — Tier 01 / FREE CTA: `<a class="tier-cta" href="/starter-kit/">` with text "Watch the videos."
  - The destination page is the Starter Kit opt-in (4 free tools), not a sales-call video library. Per source-of-truth, the only thing free is the videos — the FREE CTA should point to the YouTube channel(s), not to a Starter Kit form. And per the new rule, the Starter Kit is NOT free anyway.
- `index.html` L2712 — hero ghost CTA: `<a class="btn btn-ghost" href="/starter-kit/">` with text "Get free video access."
  - Same problem — destination is a free Starter Kit opt-in form, not the sales-call video archive. Wrong destination for the labeled intent.

### Homepage course tile "Enroll free" CTAs contradict the $10 paywall
- `index.html` L3088 (`/challenge/`) and L3110 (`/cold-call-30/`) — tile CTA reads `Enroll free`. But the pricing block immediately above says these challenges are INCLUDED IN $10 INSIDER. "Enroll free" + "Included with $10 Insider" eyebrow (L2961) = mixed message. Either it's free or it's $10. Recommend changing the tile CTA from "Enroll free" → "Open in Insider →" (or similar) once the Starter Kit / challenges paywall is committed.

---

## Sub-pages that need updates

| URL | Current pitch | Correct pitch (per source-of-truth) |
|-----|---------------|-------------------------------------|
| `/founders/` | Empire Builder Founder $99/mo, first 50, after-50 = $149 retail, full vault + Friday Q&A + courses + GHL @ $0.015 | Wholesale GHL $49/mo, was $99, first 100 seats, $0.015/min, JUST software, NO courses, locked for life |
| `/insider/` | $10/mo with foundation courses only; positions full courses (Brand Builder, Marketing Engine, Empire OS) as Builder-only at $99 | $10/mo includes ALL 4 courses, all prompts/scripts, Starter Kit, both 30-Day challenges, community, GHL @ $0.04. Wholesale GHL $49 is software-only, NO course access. |
| `/starter-kit/` | Free 4-tool lead magnet | Either rewrite as $10 Insider paywall page (per source-of-truth "no Starter Kit free"), or update homepage tier-02 list to remove Starter Kit as a $10 perk. Decision needed. |
| `/challenge/` | Free email opt-in for 30-Day Empire Challenge; references $99 Founder rate | Per source-of-truth, this is included in $10 Insider — paywall it. Remove $99 founder mentions. |
| `/cold-call-30/` | Free email opt-in for 30-Day Cold Calling Challenge; references $99 Founder rate at Day-30 graduation | Per source-of-truth, included in $10 Insider — paywall it. Remove $99 founder mentions. |
| `/courses/cold-calling/` | $297 one-time OR $99/mo Builder; comparison card pushes Builder Founder | Replace Builder Founder card with Insider $10/mo (or remove the upsell card entirely). Course is included in Insider. |
| `/courses/brand-builder/` | $497 one-time OR $99/mo Builder Founder; references "Netlify" deployment in module description (L186) | Same as above. Also: remove the Netlify mention (Coolify-only). |
| `/courses/marketing-engine/` | (assumed same pattern as cold-calling and brand-builder; verified $99/$149 references via grep) | Same fix. |
| `/courses/empire-os/` | $497 OR $99 Builder Founder; explains a "Two-Tier Stack" that lists three tiers including Founder; schema.org name = "Empire Builder Founder" | Same fix; rewrite the "Two-Tier Stack" module description to match the new $0/$10/$49 model; update schema.org. |
| `/partners/` | Builder = $99 founder / $149 retail; CTAs `Become A Builder` → /founders | Replace with Wholesale GHL $49 (or split: keep the $10 Insider upsell for general partner perks; route software-perks copy to $49 wholesale). |

---

## CTA destination issues

| File · line | Button text | Current href | Should be |
|---|---|---|---|
| `index.html` · 2712 | Get free video access | `/starter-kit/` | A YouTube/video page (or anchor linking to the live-stream archive). The Starter Kit is no longer the "free video access" destination. |
| `index.html` · 2859 | Watch the videos (FREE tier CTA) | `/starter-kit/` | YouTube channel or sales-call video archive |
| `index.html` · 3088 | Enroll free (30-Day Empire Challenge tile) | `/challenge/` | OK destination, but copy should not say "free" — it's $10 Insider per the new rule |
| `index.html` · 3110 | Enroll free (30-Day Cold Calling Challenge tile) | `/cold-call-30/` | Same — destination OK, copy wrong |
| `index.html` · 2939 | Lock my $49 seat (Wholesale tier CTA) | `/founders/` | Destination page is currently the OLD $99 Founder offer — page contents must be rewritten to the $49 wholesale offer. (Slug `/founders/` is itself misleading; consider `/wholesale/` or `/wholesale-ghl/`.) |
| `founders/index.html` · 274 | Claim My Founder Spot — $99/mo | `#checkout` | Whole page needs rewrite to $49 wholesale. CTA copy and the on-page hosted-checkout button at L584 (`/checkout/empire-founder-99`) are pointing at the dead $99/mo product. |
| `founders/index.html` · 275 | Or start as Insider for $10/mo | `/insider` | OK link, but contextually fine only after the rewrite. |
| `insider/index.html` · 347 | See Founder Page | `/founders` | After rewrite, this card's whole concept (Builder Founder $99) must change to "Wholesale GHL $49 — software-only" with NO course-comparison framing. |
| `partners/index.html` · 422, 573, 809 | Become A Builder → | `/founders` | Should read "Lock $49 Wholesale Seat →" → /founders (after page rewrite). |
| `partners/index.html` · 863 | Lock Founder Pricing — $99/mo | `/founders` | Same — copy and price both wrong. |

---

## Per-minute rate audit

Both rates appear correctly bound on the **homepage** (`$0.04/min` on Insider tier L2877; `$0.015/min` on Wholesale tier L2917). However, on sub-pages the rates are correctly bound but to the wrong **tier names**:
- Sub-pages say `$0.04/min` for Insider — correct rate, correct tier.
- Sub-pages say `$0.015/min` for Builder Founder — correct rate, but Builder Founder is the dead tier. After the rewrite, `$0.015/min` must be bound to **Wholesale GHL $49**, NOT to a course-bundle tier. There is no rate swap, but the tier-naming will need a clean find/replace.

---

## Typos / minor

- `index.html` L2868 — Tier 02 eyebrow reads `TIER 02 / EVERYTHING` but the tier nav pills (L2657, footer L3327, etc.) and ribbon copy (L2730 "Bucket $10/mo") use "Insider." Just an inconsistency between EVERYTHING and INSIDER eyebrow language.
- `index.html` L2961 — "Included with $10 Insider" eyebrow above tile cards that say "Enroll free" — see contradiction note above.
- `cold-call-30/index.html` L358, L373 — placeholder text in production HTML: `[Cold Caller Badge graphic placeholder — gold badge on navy, 800×800]` and `[Hardcore Badge graphic placeholder — gold + red double-badge, 800×800]`. These are visible to users. **Replace with real images or remove.**
- `starter-kit/thank-you.html` L119, L123 — visible text `VIDEO EMBED PLACEHOLDER` and instruction copy `replace this .video-frame…`. Visible to anyone who lands on the thank-you page. **Replace with real embed.**
- `founders/index.html` L577–581, `insider/index.html` L458–463, `challenge/index.html` L344–352, `cold-call-30/index.html` L415–417, `courses/empire-os/index.html` L648–659, etc. — every form/checkout block contains a literal `<strong>GHL FORM EMBED #N · ...</strong>` placeholder block visible to users (with copy like "Open `GoHighLevel > Sites > Forms > Starter Kit Opt-In`. Paste embed code here..."). These are essentially "FORM_ID_HERE"-style placeholder blocks rendered to the live page. **Critical**: replace every one with the real GHL iframe before launch. (README.md L40 acknowledges this is a known TODO.)
- `courses/brand-builder/index.html` L186 — "deployed via Netlify or GHL custom HTML." **Coolify-only** rule violation — and also incorrect copy.
- `courses/empire-os/index.html` L377 — heading says "The Two-Tier Stack (Insider / Builder / Founder)" — a literal "two-tier stack" with three tiers listed. Bug + outdated tier model.
- `courses/empire-os/index.html` L67 — schema.org `"name": "Empire Builder Founder"` — outdated tier name will surface in Google rich-results.
- `index.html` L2722 — `8<em>—figure</em>` (should be readable as "8-figure") — encoded as `8â€"figure` in source (mojibake). Same UTF-8 → CP-1252 corruption affects MANY em-dashes, en-dashes, middle dots, and arrows across the codebase (`â†’`, `â€”`, `Â·`, `&mdash;`-as-text, etc.). When the file is served as UTF-8 the rendered output is garbled. **Confirm the deployed nginx Content-Type is `text/html; charset=utf-8` and the file is actually saved as UTF-8.** If the file on disk is CP-1252, the `&mdash;` HTML entities are rendered correctly but the bare `—` characters in the file will mojibake. Run `file index.html` / save-as-UTF-8 across the repo.
- `partners/index.html` L501 — "$10 / $99 / $149 / course one-time" — strikes through nothing; just lists dead prices.
- `index.html` L2655–2659 nav pills — "Free / Insider $10 / Wholesale $49" — correct.

---

## What's correct

- Homepage `<title>` (L6) and meta description (L7, L14) are on-message: `Sales Calls Free · Everything Else $10 · Wholesale GHL $49` and "first 100 operators." Open Graph descriptions at L14 are correct.
- Homepage top nav pricing pills (L2655–2659) correctly show Free / Insider $10 / Wholesale $49.
- Homepage Tier 01 FREE block (L2840–2864) lists ONLY sales-call videos:
  - "Full library of my sales call videos"
  - "Tuesday Cold Call Live (YouTube)"
  - "Thursday Build Day Live (YouTube)"
  - The old free-tier items (Starter Kit, Empire Challenge) are **gone from the list** — confirmed.
- Homepage Tier 02 INSIDER block (L2867–2901) correctly enumerates: 4 courses (Cold Calling 2.0, AI Brand Builder, AI Marketing Engine, Empire OS), every prompt, every script/template/SOP, Starter Kit, 30-Day Empire Challenge, 30-Day Cold Calling Challenge, GHL reseller, private community, cancel anytime. GHL rate `$0.04/min` correctly bound here (L2877).
- Homepage Tier 03 WHOLESALE block (L2903–2945) correctly shows:
  - Ribbon: `FIRST 100 SEATS · WAS $99` (L2905)
  - Strikethrough $99 next to $49 (L2911–2913)
  - "$49/mo locked for life" (L2932)
  - Scarcity: `87 of 100 left` (L2924)
  - GHL rate `$0.015/min` correctly bound (L2917)
  - "Pure software access — NO courses, NO prompts" (L2933)
  - "Only 100 seats. Then it goes back to $99 forever." (L2935)
  - CTA: `Lock my $49 seat` → `/founders/` (L2939–2940)
- `$99` only appears on the homepage as either the strikethrough was-price (L2911) or in the ribbon (L2905) and the after-100 footnote (L2935). **No homepage standalone $99 violations found.**
- Per-minute rates on the homepage are bound to the correct tiers (no $0.04 / $0.015 swap on the homepage).
- Pricing lede subhead (L2832–2834): "Free is just the videos. Ten gets you the playbook. Forty-nine is wholesale software for the first hundred operators who want it." — perfectly on-message.
- Footer pricing links (L3327–3328) correctly show Insider $10/mo and Wholesale GHL $49/mo.
- Hero headline (L2693–2698) "the videos free" correctly anchors the FREE tier to videos.
- Robots.txt and sitemap.xml exist; Dockerfile + nginx.conf exist (Coolify deploy target consistent).

---

## Severity summary

1. **P0 / blocker** — Sub-pages still sell the dead $99 Founder / 50-seats / $149-retail offer. The tier the user clicks into from the homepage's "$49 wholesale" CTA goes to a page selling them $99 with the wrong feature list. Ship-blocker.
2. **P0** — Visible placeholder strings on production: `GHL FORM EMBED #N · ...`, `VIDEO EMBED PLACEHOLDER`, `[Cold Caller Badge graphic placeholder]`. Replace before launch.
3. **P1** — Starter Kit / 30-Day challenge pages contradict homepage paywall rule. Need a single source-of-truth decision: are these free lead magnets or $10 paywalled?
4. **P1** — Mojibake on em-dashes / arrows across nearly every file. Verify charset.
5. **P2** — Course pages still pitch "$99 Builder Founder" as the upsell against $497 one-time. Replace upsell with $10 Insider.
6. **P2** — Netlify reference in `courses/brand-builder/index.html` L186 (Coolify-only rule violation).
7. **P3** — Nav-eyebrow inconsistency `EVERYTHING` vs `INSIDER`; "Enroll free" tile CTAs paired with "$10 Insider" eyebrow.
