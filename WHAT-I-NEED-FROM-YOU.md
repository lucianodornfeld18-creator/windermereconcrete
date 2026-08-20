# WHAT I NEED FROM YOU — windermereconcrete.com
Every unknown is a clearly-labeled placeholder in the built site. Supply these and
re-run `py build_all.py` after editing _data.py (placeholders live there + _gen.py GA4_ID).

## P0 — site is not launchable without these
1. **{{PHONE}} / {{PHONE_E164}}** — tracking or business number, display + E.164
   (e.g. "(407) 555-0134" / "+14075550134"). Update BUSINESS["phone*"] in _data.py.
   WhatsApp link also derives from it ({{PHONE_DIGITS}} in _data.py WA_LINK).
2. **{{EMAIL}}** — e.g. hello@windermereconcrete.com (create the mailbox).
3. **{{FORM_ENDPOINT}}** — form handler URL (Formspree/Basin/HighLevel webhook).
   In _build_pages.py contact form. Set redirect/thank-you to /thanks/.

## P1 — before/at launch
4. **{{GOOGLE_PROFILE_URL}} / {{GOOGLE_REVIEW_URL}}** — create the GBP
   (Service-Area Business, hide address, category "Concrete contractor", service area =
   the 24 cities), then paste both URLs.
5. **{{FACEBOOK_URL}} / {{INSTAGRAM_URL}}** — create profiles, paste URLs.
6. **Images** — per images/IMAGE-MANIFEST.md (16 files, exact names). Licensed stock OK initially.
7. **{{GA4_ID}}** — GA4 measurement ID (G-XXXXXXX) in _gen.py; tag emits only when real.
8. **IndexNow key** — generate any 32-hex key, save as [key].txt in site root
   (optional but recommended for Bing/AI-engine indexing pings).

## P2 — as they become real (NEVER invent these)
9. **{{YEAR}}** — year founded (enables foundingDate in schema).
10. **{{RATING}} / {{REVIEW_COUNT}}** — only after ≥5 real Google reviews;
    then set BUSINESS["has_reviews"]=True and add real REVIEWS entries in _data.py.
11. **{{UNIQUE_STAT}}** — one true, verifiable brand stat (e.g. "300+ pallets of
    travertine set in 2026") to strengthen the AEO citable line.
12. **{{FINANCING_DETAILS}}** — actual lender/terms sentence for /financing/.

## Deploy checklist (Cloudflare Pages or equivalent)
- Connect repo/folder; custom domain windermereconcrete.com (non-www canonical).
- _headers and _redirects are ready; verify 404 handling picks up /404.html.
- Search Console + Bing Webmaster: verify, submit sitemap.xml.
- GBP website field → https://windermereconcrete.com ; UTM if desired.
- After phone/email are real: update _data.py, rebuild, redeploy.
