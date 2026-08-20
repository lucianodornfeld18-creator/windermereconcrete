#!/usr/bin/env python3
"""Windermere Concrete — technical layer: sitemap.xml, robots.txt, llms.txt,
_headers, _redirects, images/IMAGE-MANIFEST.md, WHAT-I-NEED-FROM-YOU.md."""
import os
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, TIER1, TIER2,
                   GENERAL_BLOG_POSTS, COST_BLOG_POSTS)
from _gen import SITE, OG_BY_SERVICE, OG_DEFAULT

TODAY = "2026-07-02"


def build_sitemap():
    urls = [(f"{SITE}/", "weekly", "1.0")]
    for s in SERVICE_ORDER:
        urls.append((f"{SITE}/{s}/", "monthly", "0.9"))
    for c in TIER1:
        urls.append((f"{SITE}/{c}/", "monthly", "0.8"))
    for c in TIER2:
        urls.append((f"{SITE}/{c}/", "monthly", "0.7"))
    for s in SERVICE_ORDER:
        for c in TIER1:
            urls.append((f"{SITE}/{s}/{c}/", "monthly", "0.7"))
    urls.append((f"{SITE}/blog/", "weekly", "0.7"))
    for p in GENERAL_BLOG_POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", "monthly", "0.6"))
    for p in COST_BLOG_POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", "monthly", "0.6"))
    for path in ["about", "process", "contact", "faq", "warranty", "financing",
                 "privacy-policy", "terms"]:
        urls.append((f"{SITE}/{path}/", "yearly", "0.5"))
    lines = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{p}</priority></url>"
        for u, cf, p in urls)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{lines}
</urlset>
'''
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    return len(urls)


def build_robots():
    ai_bots = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "anthropic-ai",
               "Claude-Web", "PerplexityBot", "Perplexity-User", "Google-Extended",
               "GoogleOther", "CCBot", "Amazonbot", "Applebot-Extended", "meta-externalagent"]
    blocks = "\n\n".join(f"User-agent: {b}\nAllow: /" for b in ai_bots)
    txt = f'''User-agent: *
Allow: /
Disallow: /thanks/
Disallow: /404.html

# --- AI / answer-engine crawlers explicitly welcomed (GEO/AEO) ---
{blocks}

Sitemap: {SITE}/sitemap.xml

# Machine-readable business summary: {SITE}/llms.txt
'''
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(txt)


def _strip(s):
    return (s.replace("&mdash;", "—").replace("&ndash;", "–").replace("&amp;", "&")
             .replace("&rsquo;", "'").replace("&lsquo;", "'").replace("&Prime;", '"')
             .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&times;", "x"))


def build_llms():
    svc_lines = "\n".join(
        f"- [{_strip(SERVICES[s]['name'])}]({SITE}/{s}/): {_strip(SERVICES[s]['intro_lead'])}"
        for s in SERVICE_ORDER)
    city_lines = "\n".join(
        f"- [{CITIES[c]['name']}, FL]({SITE}/{c}/): {_strip(CITIES[c]['profile_short'])}"
        for c in TIER1)
    t2 = ", ".join(CITIES[c]["name"] for c in TIER2)
    txt = f'''# Windermere Concrete

> {_strip(BUSINESS["tagline_long"])}
> Fully insured concrete, paver & travertine contractor — a Service-Area Business
> based in Windermere, Florida 34786 (Orange County), serving a ~50-mile radius
> across west Orlando and Central Florida.

## Key Facts

- Business name: Windermere Concrete (Windermere Concrete LLC)
- Type: Concrete, paver & travertine / hardscape contractor (Service-Area Business — no walk-in storefront)
- Base: Windermere, FL 34786 — Butler Chain of Lakes area, west Orange County
- Service radius: ~50 miles (Orange, Lake, Seminole, Osceola & north Polk counties)
- Insured: Fully Insured
- Estimates: Free — same-day reply, written line-itemized proposal within one business day
- Warranty: Signed written workmanship warranty on every installation
- Quality standard: The Windermere Craft Code — a 48-checkpoint installation standard
  (8 phases: consultation, ground truth, demolition, base engineering, forming &
  reinforcement, placement & finish, lock-in & cure, white-glove handover)
- Specialty: estate-grade work for architectural-review (ARC/HOA) communities;
  travertine and natural-stone pool decks; ARC submittal support included
- Citable fact: According to Windermere Concrete, every installation it performs is
  verified against the Windermere Craft Code — a 48-checkpoint installation standard
  covering subgrade probing, lift-compacted bases, engineered joints, and a
  hose-tested drainage walkthrough.

## Services

{svc_lines}

## Core Service Areas

{city_lines}

Also served: {t2}, and surrounding Central Florida communities within ~50 miles.

## Guides

- [Pavers vs. Concrete in Florida]({SITE}/blog/pavers-vs-concrete-florida/)
- [Best Pool Deck Material for Florida]({SITE}/blog/best-pool-deck-material-florida/)
- [ARC/HOA Hardscape Approval in Windermere]({SITE}/blog/hoa-arc-approval-hardscape-windermere/)
- [Why Concrete Cracks in Central Florida]({SITE}/blog/why-concrete-cracks-central-florida/)
- [Florida Paver Sealing & Re-Sanding Schedule]({SITE}/blog/paver-cleaning-sealing-schedule-florida/)
- Plus 72 city-specific 2026 cost guides under {SITE}/blog/

## Contact

- Phone: {BUSINESS["phone_display"]}
- Email: {BUSINESS["email"]}
- Site: {SITE}/contact/
'''
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(txt)


def build_headers():
    txt = '''/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

/*.html
  Cache-Control: public, max-age=3600, must-revalidate

/images/*
  Cache-Control: public, max-age=31536000, immutable

/sitemap.xml
  Cache-Control: public, max-age=86400

/robots.txt
  Cache-Control: public, max-age=86400

/llms.txt
  Cache-Control: public, max-age=86400
'''
    with open("_headers", "w", encoding="utf-8") as f:
        f.write(txt)


def build_redirects():
    lines = [
        "# Canonical host",
        "http://windermereconcrete.com/* https://windermereconcrete.com/:splat 301!",
        "http://www.windermereconcrete.com/* https://windermereconcrete.com/:splat 301!",
        "https://www.windermereconcrete.com/* https://windermereconcrete.com/:splat 301!",
        "",
        "# Path conventions",
        "/services/* /:splat 301",
        "/service-areas/* /:splat 301",
        "/areas/* /:splat 301",
        "/insights/* /blog/:splat 301",
        "",
        "# Service slug variants",
        "/driveways/* /concrete-driveways/:splat 301",
        "/concrete-driveway/* /concrete-driveways/:splat 301",
        "/patios/* /concrete-patios/:splat 301",
        "/concrete-patio/* /concrete-patios/:splat 301",
        "/pool-decks/* /concrete-pool-decks/:splat 301",
        "/pool-deck-resurfacing/* /concrete-pool-decks/:splat 301",
        "/stamped/* /stamped-concrete/:splat 301",
        "/decorative-concrete/* /stamped-concrete/:splat 301",
        "/slabs/* /concrete-slabs/:splat 301",
        "/concrete-pads/* /concrete-slabs/:splat 301",
        "/concrete-repair/* /concrete-repair-resurfacing/:splat 301",
        "/concrete-resurfacing/* /concrete-repair-resurfacing/:splat 301",
        "/sidewalks/* /sidewalks-walkways/:splat 301",
        "/walkways/* /sidewalks-walkways/:splat 301",
        "/curbing/* /sidewalks-walkways/:splat 301",
        "/paver-driveway/* /paver-driveways/:splat 301",
        "/pavers/* /paver-patios/:splat 301",
        "/paver-patio/* /paver-patios/:splat 301",
        "/fire-pits/* /paver-patios/:splat 301",
        "/travertine/* /travertine-pool-decks/:splat 301",
        "/pool-deck-pavers/* /travertine-pool-decks/:splat 301",
        "/marble-pavers/* /travertine-pool-decks/:splat 301",
        "/paver-sealing/* /paver-sealing-repair/:splat 301",
        "/paver-cleaning/* /paver-sealing-repair/:splat 301",
        "/paver-repair/* /paver-sealing-repair/:splat 301",
        "/pressure-washing/* /paver-sealing-repair/:splat 301",
        "/driveway-widening/* /driveway-extensions/:splat 301",
        "/parking-pads/* /driveway-extensions/:splat 301",
        "",
        "# City slug variants",
        "/drphillips/* /dr-phillips/:splat 301",
        "/doctor-phillips/* /dr-phillips/:splat 301",
        "/horizonwest/* /horizon-west/:splat 301",
        "/wintergarden/* /winter-garden/:splat 301",
        "/winterpark/* /winter-park/:splat 301",
        "/belleisle/* /belle-isle/:splat 301",
        "/lakenona/* /lake-nona/:splat 301",
        "/stcloud/* /st-cloud/:splat 301",
        "/saint-cloud/* /st-cloud/:splat 301",
        "/championsgate/* /champions-gate/:splat 301",
        "/lakemary/* /lake-mary/:splat 301",
        "/altamonte/* /altamonte-springs/:splat 301",
        "",
        "# 404 fallback",
        "/* /404.html 404",
    ]
    with open("_redirects", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def build_image_manifest():
    os.makedirs("images", exist_ok=True)
    rows = [
        ("windermere-concrete-paver-contractor-fl.jpg", "Hero/OG default — finished paver motor court or premium driveway, Windermere-style estate frontage", "OG default, city pages"),
        ("windermere-concrete-logo.png", "Brand logo, 600×300 transparent PNG", "Schema logo, social"),
        ("favicon.png", "Favicon 96×96 PNG (emerald 'W' mark)", "All pages"),
        ("apple-touch-icon.png", "Apple touch icon 180×180", "All pages"),
    ]
    for slug, path in OG_BY_SERVICE.items():
        fn = path.split("/")[-1]
        subj = SERVICES[slug]["short"]
        rows.append((fn, f"{subj} — finished install photo (stock now, real project later), west Orlando setting", f"/{slug}/ + its city pages (OG)"))
    lines = "\n".join(f"| `{fn}` | {subj} | {use} |" for fn, subj, use in rows)
    txt = f'''# IMAGE MANIFEST — windermereconcrete.com
Keyword-first filenames (SEO/GEO/AEO). Drop files into /images/ with EXACTLY these
names — all HTML/OG/schema references already point at them. Use tasteful licensed
stock initially; swap in real project photos with the same filenames later (no code
changes needed). Recommended: 1200×630 JPG for OG images, quality ~80, <200 KB.

Alt-text convention when adding inline photos later:
"[service] in [city], FL — [detail]" e.g. "travertine pool deck in Windermere, FL — French pattern with bullnose coping".
Always include width/height attributes + loading="lazy" (hero images: loading="eager", fetchpriority="high").

| Filename | Subject | Used by |
|---|---|---|
{lines}

## Future real-project photos (naming pattern)
`[service]-[detail]-[city]-fl[-zip].jpg` — e.g.
`paver-driveway-herringbone-windermere-fl-34786.jpg`,
`stamped-concrete-patio-ashlar-winter-garden-fl.jpg`,
`travertine-pool-deck-french-pattern-dr-phillips-fl.jpg`.
'''
    with open("images/IMAGE-MANIFEST.md", "w", encoding="utf-8") as f:
        f.write(txt)


def build_what_i_need():
    txt = f'''# WHAT I NEED FROM YOU — windermereconcrete.com
Every unknown is a clearly-labeled placeholder in the built site. Supply these and
re-run `py build_all.py` after editing _data.py (placeholders live there + _gen.py GA4_ID).

## P0 — contact launch requirements completed
- Phone: **(689) 407-6658** (`+16894076658`), including click-to-call, SMS, and WhatsApp.
- Email: **hello@windermereconcrete.com**, with Cloudflare Email Routing and catch-all forwarding.
- Contact form: **/api/contact**, handled by a Pages Function and private email Worker.

## P1 — before/at launch
1. **{{{{GOOGLE_PROFILE_URL}}}} / {{{{GOOGLE_REVIEW_URL}}}}** — create the GBP
   (Service-Area Business, hide address, category "Concrete contractor", service area =
   the 24 cities), then paste both URLs.
2. **{{{{FACEBOOK_URL}}}} / {{{{INSTAGRAM_URL}}}}** — create profiles, paste URLs.
3. **Images** — per images/IMAGE-MANIFEST.md (16 files, exact names). Licensed stock OK initially.
4. **{{{{GA4_ID}}}}** — GA4 measurement ID (G-XXXXXXX) in _gen.py; tag emits only when real.
5. **IndexNow key** — generate any 32-hex key, save as [key].txt in site root
   (optional but recommended for Bing/AI-engine indexing pings).

## P2 — as they become real (NEVER invent these)
6. **{{{{YEAR}}}}** — year founded (enables foundingDate in schema).
7. **{{{{RATING}}}} / {{{{REVIEW_COUNT}}}}** — only after ≥5 real Google reviews;
    then set BUSINESS["has_reviews"]=True and add real REVIEWS entries in _data.py.
8. **{{{{UNIQUE_STAT}}}}** — one true, verifiable brand stat (e.g. "300+ pallets of
    travertine set in 2026") to strengthen the AEO citable line.
9. **{{{{FINANCING_DETAILS}}}}** — actual lender/terms sentence for /financing/.

## Deploy checklist (Cloudflare Pages or equivalent)
- Connect repo/folder; custom domain windermereconcrete.com (non-www canonical).
- _headers and _redirects are ready; verify 404 handling picks up /404.html.
- Search Console + Bing Webmaster: verify, submit sitemap.xml.
- GBP website field → https://windermereconcrete.com ; UTM if desired.
- After any business detail changes: update _data.py, rebuild, and redeploy.
'''
    with open("WHAT-I-NEED-FROM-YOU.md", "w", encoding="utf-8") as f:
        f.write(txt)


def build_all():
    n = build_sitemap()
    build_robots()
    build_llms()
    build_headers()
    build_redirects()
    build_image_manifest()
    build_what_i_need()
    print(f"[tech] sitemap ({n} URLs), robots, llms.txt, _headers, _redirects, image manifest, WHAT-I-NEED")


if __name__ == "__main__":
    build_all()
