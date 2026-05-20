# Deploy benjisaiempire-site to Netlify

Static HTML (insider landing, legacy course shells, assets). **Production marketing domain should use the Next.js app** (`benjisaiempire-app`) on apex `benjisaiempire.com`.

## Recommended use

- **Preview / staging** Netlify site, or
- **`www.benjisaiempire.com`** with Cloudflare redirect of apex `@` → app, **or**
- Cloudflare Page Rule: redirect `www` → apex after both are configured

This repo’s `netlify.toml` already proxies `/courses` and `/landing` to `https://benjisaiempire.com` when the static site is hit directly.

## Build

- Publish directory: `.` (repo root)
- No build command

## Netlify UI

No runtime secrets required for static files. Optional: none unless you add serverless functions later.

## Custom domain

If you attach a hostname here, use **`www.benjisaiempire.com`** only, not apex (apex = app site).

## GitHub Actions

Optional mirror of app: add `.github/workflows/deploy-netlify.yml` with repo secrets `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` for **this** static site (separate site ID from the app).

## Do not link to goaiempire site

Site ID `6ce082c1-3ac9-4af1-a439-a5da380cc85d` belongs to **benjis-ai-empire** / goaiempire.advancedmarketing.co — create a new Netlify site for this static repo.
