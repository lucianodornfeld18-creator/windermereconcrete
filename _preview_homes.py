#!/usr/bin/env python3
"""Windermere Concrete — 5 homepage design variants for owner review.
Writes preview-homes/v1..v5/index.html (noindex, NOT in sitemap).
V1 = current production home. V2-V5 = alternative hero/section treatments,
all inside the Lakeside Estate brand system (emerald/navy/linen, Fraunces/Figtree)
so every option stays 100% divergent from the sister sites."""
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, TIER1, TIER2, TEL_LINK,
                   GENERAL_BLOG_POSTS, clip_desc)
from _gen import (SITE, head, header, write_page, OG_DEFAULT, keyfact, CITABLE_LINE,
                  contact_band, final_cta, craft_code_section, faq_section,
                  reviews_invite, credo_bar, why_us_section, process_section,
                  exclusions_block)
from _build_home import HOME_FAQS

B = BUSINESS
BADGES = "".join(f"<span>{b}</span>" for b in
                 ["Fully Insured", "Free Estimates", "Written Warranty", "ARC / HOA Submittal Support"])

QUOTE_CARD = f'''<div class="quote-card" id="estimate">
  <h2>Get your written proposal</h2>
  <p class="qc-sub">Free · line-itemized · delivered within one business day of the site walk</p>
  <ul>
    <li>Same-day reply to every inquiry</li>
    <li>Published pricing &mdash; compare us line by line</li>
    <li>ARC / HOA submittal package included</li>
    <li>Base work photographed before it&rsquo;s covered</li>
    <li>Signed workmanship warranty at handover</li>
  </ul>
  <a class="btn btn-pine" href="/contact/#proposal">Start My Proposal</a>
  <p class="qc-alt">Prefer to talk? <a href="{TEL_LINK}">{B["phone_display"]}</a></p>
</div>'''


def svc_cards():
    out = ""
    for s in SERVICE_ORDER:
        svc = SERVICES[s]
        out += f'''<article class="svc-card">
      <div class="svc-num">No. {svc["numeral"]}</div>
      <h3><a href="/{s}/">{svc["name"]}</a></h3>
      <p>{clip_desc(svc["intro_lead"].replace("&mdash;", "—"), 135)}</p>
      <a class="tlink" href="/{s}/">Explore the service</a>
    </article>'''
    return out


def services_section():
    return f'''<section>
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow">The Catalog</span>
      <h2>Twelve services. One <em>standard</em>.</h2>
      <p class="lede">Concrete, pavers, and natural stone — installed by one crew, under one 48-checkpoint code, with pricing published before you ever call.</p>
    </div>
    <div class="svc-grid">{svc_cards()}</div>
  </div>
</section>'''


def svc_ledger_section():
    """Alt services presentation: numbered ledger rows instead of cards (V2/V4)."""
    rows = ""
    for s in SERVICE_ORDER:
        svc = SERVICES[s]
        rows += f'''<a class="ledger-row" href="/{s}/">
      <span class="lr-num">No. {svc["numeral"]}</span>
      <span class="lr-name">{svc["name"]}</span>
      <span class="lr-desc">{clip_desc(svc["intro_lead"].replace("&mdash;", "—"), 92)}</span>
      <span class="lr-go">›</span>
    </a>'''
    return f'''<section>
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow">The Catalog</span>
      <h2>Twelve services, <em>indexed</em>.</h2>
    </div>
    <div class="svc-ledger">{rows}</div>
  </div>
</section>'''


def areas_section():
    t1 = "".join(f'''<a class="area-tile" href="/{c}/"><span class="at-name">{CITIES[c]["name"]}, FL</span><span class="at-meta">{CITIES[c]["county"]} · {" · ".join(CITIES[c]["zips"][:2])}</span></a>''' for c in TIER1)
    t2 = "".join(f'''<a class="area-tile" href="/{c}/"><span class="at-name">{CITIES[c]["name"]}, FL</span><span class="at-meta">{CITIES[c]["county"]}</span></a>''' for c in TIER2)
    return f'''<section class="areas-section">
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow">Service Area · 50-Mile Radius</span>
      <h2>Based in Windermere. Building across <em>west Orlando &amp; beyond</em>.</h2>
    </div>
    <div class="tier-label">Core Markets</div>
    <div class="area-grid">{t1}</div>
    <div class="tier-label">Extended Service Area</div>
    <div class="area-grid">{t2}</div>
  </div>
</section>'''


def insights_section():
    posts = ""
    for p in GENERAL_BLOG_POSTS[:3]:
        posts += f'''<article class="post-card">
      <div class="pc-meta"><span>{p["category"]}</span><span>{p["date_modified"][:7]}</span></div>
      <h3><a href="/blog/{p["slug"]}/">{p["title"]}</a></h3>
      <a class="tlink" href="/blog/{p["slug"]}/">Read the guide</a>
    </article>'''
    return f'''<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap-wide">
    <div class="sect-head"><span class="eyebrow">Insights</span><h2>Guides written by the crew, <em>not a content farm</em></h2></div>
    <div class="post-grid">{posts}</div>
    <p style="margin-top:1.6rem"><a class="tlink" href="/blog/">All guides &amp; cost breakdowns</a></p>
  </div>
</section>'''


def trust_section():
    return f'''<section class="snug">
  <div class="wrap">
    {keyfact(CITABLE_LINE)}
    {exclusions_block()}
    {contact_band()}
  </div>
</section>'''


# ============================================================================
# HEROES
# ============================================================================
HERO_V1 = f'''<div class="hero">
  <div class="hero-in">
    <div>
      <span class="hero-kicker">Windermere · Dr. Phillips · Horizon West · Winter Garden</span>
      <h1>Concrete, pavers &amp; travertine — <em>finished to estate standard.</em></h1>
      <p class="hero-sub">Driveways, pool decks, patios, and hardscape for the Butler Chain communities and greater west Orlando &mdash; every project verified against the 48-checkpoint Windermere Craft Code, priced in writing, and warrantied on paper.</p>
      <div class="hero-ctas">
        <a class="btn btn-pine" href="{TEL_LINK}">Call {B["phone_display"]}</a>
        <a class="btn btn-ghost-light" href="/contact/#proposal">Request a Proposal</a>
      </div>
      <div class="hero-badges">{BADGES}</div>
    </div>
    {QUOTE_CARD}
  </div>
</div>'''

HERO_V2 = f'''<div class="hero-lt">
  <div class="wrap">
    <span class="eyebrow">Windermere · Dr. Phillips · Horizon West · Winter Garden · Winter Park</span>
    <h1>The driveway is part of<br>the <em>architecture.</em></h1>
    <p class="hero-lt-sub">Estate-grade concrete, pavers &amp; travertine for west Orlando &mdash; built under the 48-checkpoint Windermere Craft Code, priced in writing, warrantied on paper.</p>
    <div class="hero-ctas">
      <a class="btn btn-pine" href="/contact/#proposal">Request a Written Proposal</a>
      <a class="btn btn-ghost" href="{TEL_LINK}">Call {B["phone_display"]}</a>
    </div>
    <div class="hero-lt-stats">
      <div><strong>48</strong><span>Craft Code checkpoints</span></div>
      <div><strong>1 day</strong><span>To your written proposal</span></div>
      <div><strong>24</strong><span>Cities served, 50-mi radius</span></div>
      <div><strong>100%</strong><span>Projects warrantied in writing</span></div>
    </div>
  </div>
</div>'''

CSS_V2 = '''
.hero-lt{background:linear-gradient(180deg,#FFFFFF 0%,var(--linen) 100%);padding:104px 0 78px;border-bottom:1px solid var(--hairline);position:relative;overflow:hidden}
.hero-lt::after{content:"";position:absolute;right:-140px;top:-140px;width:460px;height:460px;border:1px solid var(--hairline);border-radius:50%}
.hero-lt::before{content:"";position:absolute;right:-60px;top:-60px;width:460px;height:460px;border:1px solid var(--pine-wash);border-radius:50%}
.hero-lt h1{font-size:clamp(2.6rem,6vw,4.6rem);font-weight:600;margin:14px 0 1.4rem;color:var(--lake)}
.hero-lt h1 em{font-style:italic;color:var(--pine)}
.hero-lt-sub{font-size:1.12rem;color:var(--ink-soft);max-width:620px;margin-bottom:2rem}
.hero-lt-stats{display:flex;flex-wrap:wrap;gap:0;margin-top:3rem;border-top:2px solid var(--lake)}
.hero-lt-stats div{flex:1 1 150px;padding:18px 26px 0 0;border-right:1px solid var(--hairline);margin-right:26px}
.hero-lt-stats div:last-child{border-right:none}
.hero-lt-stats strong{font-family:var(--disp);font-size:2.1rem;color:var(--pine);display:block;line-height:1.1}
.hero-lt-stats span{font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft)}
.svc-ledger{border-top:2px solid var(--lake)}
.ledger-row{display:grid;grid-template-columns:90px 300px 1fr 40px;gap:22px;align-items:center;padding:19px 4px;border-bottom:1px solid var(--hairline);color:var(--ink);transition:all .18s}
.ledger-row:hover{background:#fff;padding-left:14px}
.lr-num{font-family:var(--disp);font-style:italic;color:var(--brass);font-size:.95rem}
.lr-name{font-family:var(--disp);font-weight:600;font-size:1.15rem;color:var(--lake)}
.ledger-row:hover .lr-name{color:var(--pine)}
.lr-desc{font-size:.88rem;color:var(--ink-soft)}
.lr-go{font-size:1.5rem;color:var(--pine);text-align:right}
@media(max-width:900px){.ledger-row{grid-template-columns:64px 1fr 30px}.lr-desc{display:none}}
'''

HERO_V3 = f'''<div class="hero hero-emerald">
  <div class="hero-in">
    <div>
      <span class="hero-kicker">Estate-Grade Hardscape · West Orlando</span>
      <h1>Quiet luxury,<br><em>poured &amp; laid.</em></h1>
      <p class="hero-sub">Windermere&rsquo;s concrete, paver &amp; travertine specialists. Forty-eight checkpoints on every install, a written proposal in one business day, and a crew that comes back after the first rain to watch the water behave.</p>
      <div class="hero-ctas">
        <a class="btn btn-lake" href="{TEL_LINK}">Call {B["phone_display"]}</a>
        <a class="btn btn-ghost-light" href="/contact/#proposal">Request a Proposal</a>
      </div>
      <div class="hero-badges">{BADGES}</div>
    </div>
    {QUOTE_CARD}
  </div>
</div>'''

CSS_V3 = '''
.hero-emerald{background:linear-gradient(155deg,#0E3325 0%,#1E5D48 78%) !important}
.hero-emerald::before{background:radial-gradient(820px 400px at 88% 12%,rgba(16,41,58,.55),transparent 65%) !important}
.hero-emerald .hero-kicker{color:#D9C9A3}
.hero-emerald .hero-kicker::before{background:#D9C9A3}
.hero-emerald h1 em{color:#CFE5D8}
.hero-emerald .hero-badges span::before{color:#D9C9A3}
.credo{background:var(--lake)}
.finale{background:linear-gradient(150deg,#0B1E2C,var(--lake))}
'''

HERO_V4 = f'''<div class="hero-split">
  <div class="hs-left">
    <span class="hero-kicker">Windermere Concrete · Est. Windermere FL 34786</span>
    <h1>Twelve crafts.<br>Forty-eight checkpoints.<br><em>One standard.</em></h1>
    <p class="hero-sub">Concrete, pavers &amp; travertine for the Butler Chain communities and greater west Orlando.</p>
    <div class="hero-ctas">
      <a class="btn btn-pine" href="/contact/#proposal">Request a Proposal</a>
      <a class="btn btn-ghost-light" href="{TEL_LINK}">{B["phone_display"]}</a>
    </div>
    <div class="hero-badges">{BADGES}</div>
  </div>
  <div class="hs-right">
    <span class="hs-index-cap">The Catalog · No. 01&ndash;12</span>
    {"".join(f'<a href="/{s}/"><i>No. {SERVICES[s]["numeral"]}</i>{SERVICES[s]["name"]}<b>›</b></a>' for s in SERVICE_ORDER)}
  </div>
</div>'''

CSS_V4 = '''
.hero-split{display:grid;grid-template-columns:1.15fr .85fr;min-height:620px}
.hs-left{background:linear-gradient(160deg,var(--lake) 0%,#0B1E2C 80%);color:#fff;padding:96px 60px 70px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
.hs-left::before{content:"";position:absolute;inset:0;background:radial-gradient(600px 320px at 85% 10%,rgba(30,93,72,.4),transparent 60%)}
.hs-left>*{position:relative}
.hs-left h1{color:#fff;font-size:clamp(2.2rem,4.2vw,3.6rem);margin:16px 0 1.2rem;line-height:1.1}
.hs-left h1 em{font-style:italic;color:#9FC3B2}
.hs-left .hero-sub{color:rgba(255,255,255,.82)}
.hs-right{background:var(--linen);border-left:4px solid var(--pine);padding:56px 48px;display:flex;flex-direction:column;justify-content:center}
.hs-index-cap{font-size:.68rem;font-weight:800;letter-spacing:.26em;text-transform:uppercase;color:var(--brass);margin-bottom:14px}
.hs-right a{display:flex;align-items:center;gap:14px;padding:11px 2px;border-bottom:1px solid var(--hairline);font-family:var(--disp);font-weight:600;font-size:1.02rem;color:var(--lake);transition:all .16s}
.hs-right a:hover{color:var(--pine);padding-left:10px}
.hs-right a i{font-style:italic;font-size:.78rem;color:var(--brass);min-width:52px}
.hs-right a b{margin-left:auto;color:var(--pine);font-weight:400;font-size:1.2rem}
@media(max-width:1000px){.hero-split{grid-template-columns:1fr}.hs-left{padding:70px 24px 54px}.hs-right{padding:40px 24px}}
'''

HERO_V5 = f'''<div class="hero hero-center">
  <div class="wrap" style="position:relative;z-index:1;text-align:center;padding:96px 22px 84px">
    <span class="hero-kicker" style="justify-content:center">Windermere · FL 34786 · Serving a 50-Mile Radius</span>
    <h1 style="max-width:860px;margin:0 auto 1.3rem">West Orlando&rsquo;s <em>estate-grade</em> concrete, paver &amp; travertine crew.</h1>
    <p class="hero-sub" style="margin:0 auto 2rem;max-width:640px">Every driveway, pool deck, and terrace verified against the 48-checkpoint Windermere Craft Code &mdash; with published pricing and a signed written warranty.</p>
    <div class="hero-ctas" style="justify-content:center">
      <a class="btn btn-pine" href="{TEL_LINK}">Call {B["phone_display"]}</a>
      <a class="btn btn-ghost-light" href="/contact/#proposal">Request a Proposal</a>
    </div>
    <div class="hero-badges" style="justify-content:center">{BADGES}</div>
  </div>
</div>
<div class="pillar-strip">
  <div class="wrap-wide pillar-in">
    <div><i>I.</i><strong>Ground Truth First</strong><span>Subgrade probed &amp; bases photographed before they disappear</span></div>
    <div><i>II.</i><strong>Priced in Writing</strong><span>Line-itemized proposal within one business day</span></div>
    <div><i>III.</i><strong>ARC-Ready</strong><span>HOA submittal package included with every estimate</span></div>
    <div><i>IV.</i><strong>Back After the Rain</strong><span>Drainage hose-tested &mdash; then re-checked after the first storm</span></div>
  </div>
</div>'''

CSS_V5 = '''
.hero-center .hero-kicker::before{display:none}
.pillar-strip{background:#fff;border-bottom:1px solid var(--hairline)}
.pillar-in{display:grid;grid-template-columns:repeat(4,1fr);gap:0}
.pillar-in div{padding:26px 24px;border-right:1px solid var(--hairline);display:flex;flex-direction:column;gap:4px}
.pillar-in div:first-child{border-left:1px solid var(--hairline)}
.pillar-in i{font-family:var(--disp);font-style:italic;color:var(--brass);font-size:1.05rem}
.pillar-in strong{font-family:var(--disp);color:var(--lake);font-size:1.08rem}
.pillar-in span{font-size:.82rem;color:var(--ink-soft);line-height:1.5}
@media(max-width:900px){.pillar-in{grid-template-columns:1fr 1fr}}
@media(max-width:540px){.pillar-in{grid-template-columns:1fr}}
'''

# ============================================================================
# VARIANT DEFINITIONS
# ============================================================================
def variant_sections(order_key):
    common_tail = [faq_section(HOME_FAQS, headline="Before you call — the essentials"),
                   reviews_invite(), insights_section(), final_cta()]
    if order_key == "classic":       # V1/V3: services → why → code → areas → process → trust
        return [credo_bar(), services_section(), why_us_section(), craft_code_section(),
                areas_section(), process_section(), trust_section()] + common_tail
    if order_key == "editorial":     # V2: why first, ledger services, code, areas
        return [credo_bar(), why_us_section(), svc_ledger_section(), craft_code_section(),
                process_section(), areas_section(), trust_section()] + common_tail
    if order_key == "code-first":    # V4: code right after hero, then cards
        return [credo_bar(), craft_code_section(), services_section(), why_us_section(),
                areas_section(), process_section(), trust_section()] + common_tail
    if order_key == "trust-first":   # V5: pillars done in hero; process, services, why
        return [process_section(), services_section(), why_us_section(), craft_code_section(),
                areas_section(), trust_section()] + common_tail
    raise ValueError(order_key)


VARIANTS = [
    ("v1", "Option 1 — Navy Split + Proposal Card (current)", HERO_V1, "", "classic"),
    ("v2", "Option 2 — Editorial Light (airy, serif-forward)", HERO_V2, CSS_V2, "editorial"),
    ("v3", "Option 3 — Deep Emerald (dramatic, lush)", HERO_V3, CSS_V3, "classic"),
    ("v4", "Option 4 — Split Panel + Service Index", HERO_V4, CSS_V4, "code-first"),
    ("v5", "Option 5 — Centered Classic + Pillar Strip", HERO_V5, CSS_V5, "trust-first"),
]


def build_variant(slug, label, hero, css_override, order_key):
    canonical = f"{SITE}/preview-homes/{slug}/"
    banner = f'''<div style="background:#8A6D3B;color:#fff;text-align:center;font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;padding:8px 12px;position:relative;z-index:2000">PREVIEW · {label}</div>'''
    extra_css = f"<style>{css_override}</style>" if css_override else ""
    body = banner + hero + "\n" + "\n".join(variant_sections(order_key)) + extra_css
    write_page(f"preview-homes/{slug}/index.html",
               head(f"PREVIEW {label} | Windermere Concrete",
                    "Internal design preview — not for indexing.",
                    canonical, indexable=False),
               header(active="home"), body)


if __name__ == "__main__":
    for slug, label, hero, css, order_key in VARIANTS:
        build_variant(slug, label, hero, css, order_key)
    print(f"[preview] wrote {len(VARIANTS)} home variants under /preview-homes/")
