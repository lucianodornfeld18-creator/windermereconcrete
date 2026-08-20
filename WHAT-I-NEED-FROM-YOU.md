# WHAT I NEED FROM YOU — windermereconcrete.com
Every unknown is a clearly-labeled placeholder in the built site. Supply these and
re-run `py build_all.py` after editing _data.py (placeholders live there + _gen.py GA4_ID).

## P0 — contact launch requirements completed
- Phone: **(689) 407-6658** (`+16894076658`), including click-to-call, SMS, and WhatsApp.
- Email: **hello@windermereconcrete.com**, with Cloudflare Email Routing and catch-all forwarding.
- Contact form: **/api/contact**, handled by a Pages Function and private email Worker.

## P1 — before/at launch
1. **{{GOOGLE_PROFILE_URL}} / {{GOOGLE_REVIEW_URL}}** — create the GBP
   (Service-Area Business, hide address, category "Concrete contractor", service area =
   the 24 cities), then paste both URLs.
2. **{{FACEBOOK_URL}} / {{INSTAGRAM_URL}}** — create profiles, paste URLs.
3. **Images** — per images/IMAGE-MANIFEST.md (16 files, exact names). Licensed stock OK initially.
4. **{{GA4_ID}}** — GA4 measurement ID (G-XXXXXXX) in _gen.py; tag emits only when real.
5. **IndexNow key** — generate any 32-hex key, save as [key].txt in site root
   (optional but recommended for Bing/AI-engine indexing pings).

## P2 — as they become real (NEVER invent these)
6. **{{YEAR}}** — year founded (enables foundingDate in schema).
7. **{{RATING}} / {{REVIEW_COUNT}}** — only after ≥5 real Google reviews;
    then set BUSINESS["has_reviews"]=True and add real REVIEWS entries in _data.py.
8. **{{UNIQUE_STAT}}** — one true, verifiable brand stat (e.g. "300+ pallets of
    travertine set in 2026") to strengthen the AEO citable line.
9. **{{FINANCING_DETAILS}}** — actual lender/terms sentence for /financing/.

## Deploy checklist (Cloudflare Pages or equivalent)
- Connect repo/folder; custom domain windermereconcrete.com (non-www canonical).
- _headers and _redirects are ready; verify 404 handling picks up /404.html.
- Search Console + Bing Webmaster: verify, submit sitemap.xml.
- GBP website field → https://windermereconcrete.com ; UTM if desired.
- After any business detail changes: update _data.py, rebuild, and redeploy.
