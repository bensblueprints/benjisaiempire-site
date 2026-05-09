# 04 — Image / Asset Audit

**Site:** https://benjisaiempire.com/
**Source:** `C:\Users\HP\benjisaiempire-site\images\`
**Library:** `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\`
**Date:** 2026-05-10

All 20 image URLs return **HTTP 200**. Live `Content-Length` matches local file size for every image **except `course-marketing-engine.jpg`** (local 308,241 B, live 9,321 B — see Missing/broken).

---

## Photo usage map

| section | filename | role | size | verdict |
|---|---|---|---|---|
| `<head>` favicon | `favicon.png` | favicon | 27 KB | OK |
| `<head>` OG image | `hero-empire.jpg` | social share preview | 559 KB | OK |
| `<head>` preload | `hero-empire.jpg` | hero preload | 559 KB | OK |
| Hero (CSS bg, full-bleed) | `hero-empire.jpg` | landing hero | 559 KB | OK — high-res |
| Hero foreground figure | `headshot-pointing.jpg` | hero portrait | 442 KB | OK |
| Course tile 1 | `course-cold-calling.jpg` | Cold Calling 2.0 + AI | **11 KB** | FLAG — likely FB-thumbnail-tier; will smear on retina |
| Course tile 2 | `course-brand-builder.jpg` | AI Brand Builder | **11 KB** | FLAG — same |
| Course tile 3 | `course-marketing-engine.jpg` | AI Marketing Engine | local 301 KB / **live 9 KB** | FLAG — live CDN serving an old 9 KB version (deploy mismatch) |
| Course tile 4 | `course-empire-os.jpg` | Empire OS | **12 KB** | FLAG — low-res |
| Course tile 5 | `streaming-rig.jpg` | 30-Day AI Empire Challenge | 301 KB | OK (note: identical bytes to local `course-dev-rig.jpg` — duplicate file) |
| Course tile 6 | `broll-bangkok.jpg` | 30-Day Cold Calling Challenge | 720 KB | OK — but topical mismatch (Bangkok b-roll for "cold calling challenge"?) |
| About headshot | `headshot-mural.jpg` | About Ben portrait | 527 KB | OK |
| Proof gallery 1 | `proof-shopify-2-8m.jpg` | $2.8M dashboard | 618 KB | OK — strongest money-proof |
| Proof gallery 2 | `proof-grant-cardone.jpg` | Grant Cardone selfie | 89 KB | OK (acceptable for thumbnail; not hero) |
| Proof gallery 3 | `proof-meta-ads.jpg` | Meta Ads dashboard | 197 KB | OK |
| Proof gallery 4 | `hero-petronas.jpg` | Petronas Towers | 553 KB | OK |
| Proof gallery 5 | `headshot-mural.jpg` (re-used) | Bangkok mural | 527 KB | FLAG — same image appears twice (About + proof) |
| Proof gallery 6 | `course-dev-rig.jpg` | Live cold-call rig | 196 KB | OK |
| Unused (in folder) | `hero-throne.jpg` | — | **10 KB** | UNUSED + low-res; safe to delete |
| Unused (in folder) | `lifestyle-mclaren.jpg` | — | **10 KB** | UNUSED + low-res; delete |
| Unused (in folder) | `headshot-bookshelf.jpg` | — | **10 KB** | UNUSED + low-res; delete |
| Unused (in folder) | `headshot-leaves.jpg` | — | 413 KB | UNUSED, but high-res — candidate for swap-in |
| Unused (in folder) | `hero-mclaren.jpg` | — | 627 KB | UNUSED, high-res — candidate |
| Unused (in folder) | `hero-petronas-2.jpg` | — | 524 KB | UNUSED, high-res — candidate |

**Summary of low-res problems:** 4 of 6 course tiles are 9–12 KB. Even displayed at ~400 px tile width on retina they will look soft / JPEG-blocky. These are the worst remaining offenders from the FB-thumbnail era the user complained about.

---

## Recommended swaps

| current photo (role) | recommended replacement (full path) | why |
|---|---|---|
| `course-cold-calling.jpg` (11 KB) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\01-Cold-Calling\ben-cold-calling-tee-trio.jpg` | Manifest's #5 primary pick — literal "Cold Calling" tee, zero-ambiguity course thumbnail |
| `course-brand-builder.jpg` (11 KB) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\02-AI-Brand-Builder\ben-book-lose-million-dollars-364-days.jpg` | Manifest's #10 pick — Ben's published book is the single best Brand-Builder authority artifact |
| `course-marketing-engine.jpg` (live 9 KB / mismatched) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\03-AI-Marketing-Engine\ben-claude-code-tshirt-rgb-desk.jpg` | Manifest's #4 pick — RGB rig + Claude Code shirt = on-the-nose "AI Marketing Engine" |
| `course-empire-os.jpg` (12 KB) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\04-Empire-OS\ben-cinematic-banyan-tree-stussy-tee.jpg` | Manifest's #6 pick — quiet operator energy, exactly the Empire OS brand archetype |
| `streaming-rig.jpg` (used for "30-Day AI Empire Challenge") | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\03-AI-Marketing-Engine\ben-prada-cap-shure-mic-vsp-monitor-streaming.jpg` | The current file is a duplicate of `course-dev-rig.jpg`. Use the actual streaming/mic shot for variety |
| `broll-bangkok.jpg` (720 KB but topical mismatch for "Cold Calling Challenge") | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\03-AI-Marketing-Engine\meta-ads-benji-boyce-4-active-campaigns.jpg` (or a phone-headset shot) | Bangkok b-roll has nothing to do with cold calling. Replace with on-topic asset |
| `hero-empire.jpg` (currently full-bleed hero) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\06-Hero-Landing\ben-gold-throne-givenchy-chains.jpg` | Manifest #1 — single strongest brand-archetype shot. Keep current as fallback if throne shot reads too over-the-top for AI/marketing audience |
| `headshot-pointing.jpg` (hero figure) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\08-Instructor-Headshots\ben-bookshelf-white-tee-headshot.jpg` | Manifest's #2 "best About Ben headshot" — use on About section instead; keep pointing shot in hero |
| `headshot-mural.jpg` re-used in proof gallery | swap proof-gallery slot to `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\09-Social-Proof\ben-with-the-game-rapper-fendi-gold-chains.jpg` or `…\cameo-celebrities-the-game-tommy-chong-cassidy.jpg` | Stops same headshot appearing twice; adds A-list social proof (The Game, Tommy Chong, Cassidy) |
| `proof-grant-cardone.jpg` (89 KB) | `C:\Users\HP\Desktop\Benji-AI-Empire-Photos\09-Social-Proof\ben-with-grant-cardone-lambo-cap.jpg` (full-res original) | Same shot, full-resolution from library — replaces the 89 KB compressed copy |

Optional new heroes available unused in `/images/`: `hero-mclaren.jpg` (627 KB), `hero-petronas-2.jpg` (524 KB), `headshot-leaves.jpg` (413 KB) — already deployed but referenced nowhere.

---

## Compliance flags

- **No Risky-Internal-Only photos detected on the site** — verified all 22 files in `/images/` against the 37 filenames in `Benji-AI-Empire-Photos/14-Risky-Internal-Only/`. Zero matches. No partner photos, no PII screenshots, no fake mugshot, no Root Access account-rental graphic, no `nomadicben420@gmail.com` leaks, no Airbnb guest names, no GTA copyright tee. **PASS.**
- **No cannabis-brand imagery currently on the site.** None of `Hempire`, `Kandy Boy`, `DOPE Thailand`, `Buy Delta 8`, `Herban`, `Texas Cannabis` filenames are in `/images/`. The `proof-shopify-2-8m.jpg` is the master-dashboard composite — manifest notes Hempire/Buy-Delta-8 store names DO appear in that screenshot. Per CLAUDE.md / manifest: cannabis branding is OK on owned property (this site) but flagged as Meta/Google ad-rejection risk. **Acceptable on this site, do not lift into paid ads.**
- **Identifiable third parties without consent:** Grant Cardone (`proof-grant-cardone.jpg`) appears publicly. He's a public figure photographed in a selfie context — generally low-risk but no written release on file. Manifest treats it as primary social-proof asset; flagging here for awareness only.
- **No partner photos visible** (manifest tracks ~6 photos in folder 14 — none on site).

---

## Missing / broken

- **`course-marketing-engine.jpg` deploy/CDN mismatch:** local file is 301 KB but the live CDN at `https://benjisaiempire.com/images/course-marketing-engine.jpg` returns only 9,321 B (HTTP 200 but stale low-res copy). Either purge Coolify/Cloudflare cache or force a redeploy; otherwise the current "fixed" version isn't reaching users.
- **Three unused 9–12 KB files in `/images/`:** `hero-throne.jpg` (10 KB), `lifestyle-mclaren.jpg` (10 KB), `headshot-bookshelf.jpg` (10 KB). Not referenced in `index.html`. Delete to prevent accidental future use of FB-thumbnail-tier files. Their high-quality replacements live in the photo library.
- **`streaming-rig.jpg` and `course-dev-rig.jpg` are byte-identical duplicates** (both 308,241 B, identical mtime). Two different sections render the same image. Replace one (see swaps).
- **`headshot-mural.jpg` used twice** (About headshot + proof gallery slot 5). Visual repetition. See swaps.
- **`broll-bangkok.jpg` topical mismatch** — used as the "30-Day Cold Calling Challenge" thumbnail; image content is unrelated to cold calling. See swaps.
- **No broken/404 image references found.** All 16 distinct `<img>` / `background-image` URLs resolve 200.
