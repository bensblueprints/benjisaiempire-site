# benjisaiempire.com

Static marketing site for Benji's AI Empire. Hosted on Coolify (Contabo VPS 2, `212.28.184.24`) behind Traefik.

## Stack
- Plain HTML/CSS — no build step
- nginx:alpine in Docker
- Traefik (Coolify) handles TLS via Let's Encrypt

## Local preview
```bash
docker compose up --build
# then visit http://localhost (after temporarily exposing port 80)
```

## Deploy
```bash
# from this folder
git add -A && git commit -m "update" && git push

# rebuild on server
ssh -i ~/.ssh/id_server212 root@212.28.184.24 \
  "cd /opt/benjisaiempire-site && git pull && docker compose up -d --build"
```

## Site structure
- `/` — home (door picker)
- `/starter-kit/` — free lead magnet funnel (index, thank-you, insider-offer, welcome)
- `/insider/` — $10/mo Insider funnel
- `/founders/` — $99/mo Founder funnel (50 seats)
- `/challenge/` — 30-Day AI Empire Challenge
- `/cold-call-30/` — 30-Day Cold Calling Challenge
- `/partners/` — software partner showcase
- `/courses/cold-calling/` — Cold Calling 2.0 + AI
- `/courses/brand-builder/` — AI Brand Builder
- `/courses/marketing-engine/` — AI Marketing Engine
- `/courses/empire-os/` — Empire OS

## GHL integration
Form embeds, hosted-checkout buttons, and the founder counter still hold placeholder IDs. Wire real GHL form/product IDs by editing the HTML and redeploying. Full spec: `INTEGRATION_SPEC.md` in the source project folder.
