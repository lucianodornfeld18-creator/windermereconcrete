#!/usr/bin/env python3
"""
Windermere Concrete — Shared Page Generator
"Lakeside Estate" design system: estate emerald + lake navy + linen + sage mist.
Serif display (Fraunces) + humanist body (Figtree). Near-square corners,
hairline rules, small-caps eyebrows, ledger tables, quiet-luxury voice.
100% distinct from ocoeeconcrete.com (orange/Outfit+Lato) and
lakewoodranchconcretefl.com (gold-cream/Outfit+Inter, editorial ticker).
Used by every _build_*.py script.
"""
import json, os
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, SERVICE_GROUPS, TIER1, TIER2,
                   CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, SMS_LINK, WHY_US_POINTS,
                   PROCESS_STEPS, HERO_TRUST_BADGES, EXCLUSIONS, GENERAL_BLOG_POSTS,
                   COST_BLOG_POSTS, AREASERVED_ONLY, clip_desc)

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"
GA4_ID = "{{GA4_ID}}"   # emitted only when the owner supplies a real ID

# ============================================================================
# OG IMAGES — keyword-first filenames (see images/IMAGE-MANIFEST.md)
# ============================================================================
OG_DEFAULT = "/images/windermere-concrete-paver-contractor-fl.jpg"
OG_BY_SERVICE = {
    "concrete-driveways":         "/images/concrete-driveway-windermere-fl.jpg",
    "concrete-patios":            "/images/concrete-patio-windermere-fl.jpg",
    "concrete-pool-decks":        "/images/concrete-pool-deck-windermere-fl.jpg",
    "stamped-concrete":           "/images/stamped-concrete-patio-windermere-fl.jpg",
    "concrete-slabs":             "/images/concrete-slab-pad-windermere-fl.jpg",
    "concrete-repair-resurfacing":"/images/concrete-repair-resurfacing-windermere-fl.jpg",
    "sidewalks-walkways":         "/images/concrete-walkway-steps-windermere-fl.jpg",
    "paver-driveways":            "/images/paver-driveway-windermere-fl.jpg",
    "paver-patios":               "/images/paver-patio-windermere-fl.jpg",
    "travertine-pool-decks":      "/images/travertine-pool-deck-windermere-fl-34786.jpg",
    "paver-sealing-repair":       "/images/paver-sealing-cleaning-windermere-fl.jpg",
    "driveway-extensions":        "/images/driveway-extension-widening-windermere-fl.jpg",
}
def og_url(service_slug=None, path=None):
    if path:
        return f"{SITE}{path}"
    return f"{SITE}{OG_BY_SERVICE.get(service_slug, OG_DEFAULT)}"

# ============================================================================
# CSS — Lakeside Estate design system
# ============================================================================
CSS = r"""
:root{
  --pine:#1E5D48;           /* estate emerald — primary accent */
  --pine-deep:#14432F;      /* hover/active emerald */
  --pine-wash:#E8EFE7;      /* sage mist — tinted sections */
  --lake:#10293A;           /* lake navy — dark sections, headings */
  --lake-soft:#1B3B52;      /* navy hover */
  --linen:#F7F8F3;          /* page base */
  --card:#FFFFFF;
  --hairline:#D8DED3;       /* rules & borders */
  --ink:#1E2A26;            /* body text */
  --ink-soft:#5C6B62;       /* secondary text */
  --brass:#8A6D3B;          /* restrained metallic detail — small accents only */
  --ok:#2E7D32;
  --shadow-1:0 1px 3px rgba(16,41,58,.08);
  --shadow-2:0 8px 28px rgba(16,41,58,.12);
  --r:5px;
  --disp:'Fraunces',Georgia,serif;
  --body:'Figtree','Segoe UI',system-ui,sans-serif;
  --wrap:1140px;
  --wrap-wide:1320px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;scroll-padding-top:88px}
body{font-family:var(--body);font-size:16.5px;line-height:1.7;color:var(--ink);background:var(--linen)}
img{max-width:100%;height:auto;display:block}
a{color:var(--pine);text-decoration:none;transition:color .18s}
a:hover{color:var(--pine-deep)}
h1,h2,h3,h4{font-family:var(--disp);font-weight:600;line-height:1.12;color:var(--lake);letter-spacing:-.01em}
h1{font-size:clamp(2.1rem,4.6vw,3.3rem)}
h2{font-size:clamp(1.55rem,3.2vw,2.3rem)}
h3{font-size:clamp(1.12rem,1.9vw,1.4rem)}
p{margin:0 0 1rem}
ul,ol{margin:0;padding:0}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 22px}
.wrap-wide{max-width:var(--wrap-wide);margin:0 auto;padding:0 22px}
section{padding:76px 0}
section.snug{padding:46px 0}

/* EYEBROW — small caps + dot, replaces sister sites' numbered headers */
.eyebrow{display:flex;align-items:center;gap:10px;font-size:.74rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--pine);margin-bottom:14px}
.eyebrow::after{content:"";flex:0 0 34px;height:1px;background:var(--hairline)}
.eyebrow.on-dark{color:#9FC3B2}
.eyebrow.on-dark::after{background:rgba(255,255,255,.25)}
.eyebrow.center{justify-content:center}
.eyebrow.center::after{display:none}
.sect-head{max-width:760px;margin-bottom:2.6rem}
.sect-head h2 em{font-style:italic;color:var(--pine)}
.sect-head .lede{color:var(--ink-soft);font-size:1.02rem;margin-top:.7rem}
.sect-head.center{margin-left:auto;margin-right:auto;text-align:center}

/* BUTTONS — rectangular, hairline, quiet luxury */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:15px 30px;font-family:var(--body);font-weight:700;font-size:.9rem;letter-spacing:.05em;text-transform:uppercase;border-radius:var(--r);border:1.5px solid transparent;cursor:pointer;transition:all .2s;white-space:nowrap}
.btn-pine{background:var(--pine);color:#fff;border-color:var(--pine)}
.btn-pine:hover{background:var(--pine-deep);border-color:var(--pine-deep);color:#fff;box-shadow:var(--shadow-2)}
.btn-lake{background:var(--lake);color:#fff;border-color:var(--lake)}
.btn-lake:hover{background:var(--lake-soft);color:#fff}
.btn-ghost{background:transparent;color:var(--lake);border-color:var(--lake)}
.btn-ghost:hover{background:var(--lake);color:#fff}
.btn-ghost-light{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}
.btn-ghost-light:hover{background:#fff;color:var(--lake);border-color:#fff}
.tlink{font-weight:700;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;color:var(--pine);display:inline-flex;align-items:center;gap:8px}
.tlink::after{content:"›";font-size:1.15rem;line-height:1;transition:transform .18s}
.tlink:hover::after{transform:translateX(4px)}

/* TOPLINE + HEADER */
.topline{background:var(--lake);color:rgba(255,255,255,.82);font-size:.78rem;letter-spacing:.04em;padding:8px 0}
.topline .wrap-wide{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap}
.topline a{color:#fff;font-weight:600}
.topline a:hover{color:#9FC3B2}
.masthead{position:sticky;top:0;z-index:1000;background:rgba(247,248,243,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--hairline)}
.mast-in{max-width:var(--wrap-wide);margin:0 auto;padding:14px 22px;display:flex;align-items:center;justify-content:space-between;gap:1.4rem}
.wordmark{display:flex;flex-direction:column;line-height:1.05;text-decoration:none}
.wordmark .wm-name{font-family:var(--disp);font-weight:700;font-size:1.32rem;color:var(--lake);letter-spacing:.01em}
.wordmark .wm-name em{font-style:italic;color:var(--pine)}
.wordmark .wm-sub{font-size:.62rem;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--brass);margin-top:4px}
.navlist{display:flex;align-items:center;gap:1.7rem;list-style:none}
.navlist>li{position:relative}
.navlist>li>a{font-weight:600;font-size:.94rem;color:var(--ink);padding:10px 0;border-bottom:2px solid transparent}
.navlist>li:hover>a,.navlist>li.on>a{color:var(--pine);border-bottom-color:var(--pine)}
.drop{position:absolute;top:calc(100% + 8px);left:-14px;background:#fff;border:1px solid var(--hairline);border-radius:var(--r);box-shadow:var(--shadow-2);min-width:280px;padding:10px 0;opacity:0;visibility:hidden;transform:translateY(-5px);transition:all .18s;z-index:60;max-height:70vh;overflow-y:auto}
.navlist li:hover .drop{opacity:1;visibility:visible;transform:none}
.drop a{display:block;padding:9px 20px;font-size:.9rem;color:var(--ink)}
.drop a:hover{background:var(--pine-wash);color:var(--pine-deep)}
.drop .grp{padding:9px 20px 4px;font-size:.68rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--brass)}
.mast-cta{display:flex;align-items:center;gap:14px}
.mast-tel{display:flex;align-items:center;gap:8px;font-weight:700;color:var(--lake);font-size:.95rem}
.mast-tel svg{width:15px;height:15px;color:var(--pine)}
.mast-tel:hover{color:var(--pine)}
.burger{display:none;background:none;border:none;cursor:pointer;color:var(--lake);padding:4px}
.burger svg{width:27px;height:27px}

/* CRUMBS */
.crumbs{border-bottom:1px solid var(--hairline);background:#fff;padding:11px 0}
.crumbs ol{display:flex;flex-wrap:wrap;gap:5px;list-style:none;font-size:.8rem;color:var(--ink-soft)}
.crumbs li+li::before{content:"·";margin:0 7px;color:var(--hairline)}
.crumbs a{color:var(--pine)}
.crumbs li:last-child{color:var(--lake);font-weight:600}

/* HERO — split: serif statement left, estimate card right (no photo dependency) */
.hero{background:linear-gradient(160deg,var(--lake) 0%,#0B1E2C 70%),var(--lake);color:#fff;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(820px 400px at 85% 15%,rgba(30,93,72,.35),transparent 65%)}
.hero::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:linear-gradient(90deg,transparent,rgba(159,195,178,.5),transparent)}
.hero-in{position:relative;z-index:1;max-width:var(--wrap-wide);margin:0 auto;padding:86px 22px 78px;display:grid;grid-template-columns:1.25fr .85fr;gap:56px;align-items:center}
.hero h1{color:#fff;font-size:clamp(2.3rem,5vw,3.7rem);font-weight:600;margin-bottom:1.3rem}
.hero h1 em{font-style:italic;color:#9FC3B2}
.hero-kicker{display:inline-flex;align-items:center;gap:12px;font-size:.72rem;font-weight:700;letter-spacing:.26em;text-transform:uppercase;color:#9FC3B2;margin-bottom:20px}
.hero-kicker::before{content:"";width:30px;height:1px;background:#9FC3B2}
.hero-sub{font-size:1.08rem;line-height:1.65;color:rgba(255,255,255,.82);max-width:560px;margin-bottom:1.9rem}
.hero-ctas{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:2rem}
.hero-badges{display:flex;flex-wrap:wrap;gap:9px}
.hero-badges span{font-size:.74rem;font-weight:600;letter-spacing:.05em;color:rgba(255,255,255,.85);border:1px solid rgba(255,255,255,.22);border-radius:30px;padding:6px 14px;display:inline-flex;align-items:center;gap:7px}
.hero-badges span::before{content:"✦";color:#9FC3B2;font-size:.6rem}
/* estimate card */
.quote-card{background:#fff;border-radius:8px;box-shadow:0 24px 60px rgba(0,0,0,.35);padding:30px 28px;color:var(--ink)}
.quote-card h2{font-size:1.35rem;margin-bottom:.4rem}
.quote-card .qc-sub{font-size:.86rem;color:var(--ink-soft);margin-bottom:1.2rem}
.quote-card ul{list-style:none;margin-bottom:1.3rem}
.quote-card li{padding:8px 0;border-bottom:1px dashed var(--hairline);font-size:.9rem;display:flex;gap:10px;align-items:baseline}
.quote-card li::before{content:"✓";color:var(--pine);font-weight:800;flex:0 0 auto}
.quote-card li:last-child{border-bottom:none}
.quote-card .btn{width:100%}
.quote-card .qc-alt{text-align:center;font-size:.8rem;color:var(--ink-soft);margin-top:.8rem}
.quote-card .qc-alt a{font-weight:700}

/* CREDO BAR — static strip (deliberately not an animated ticker) */
.credo{background:var(--pine);color:#fff;padding:16px 0}
.credo .wrap-wide{display:flex;justify-content:center;flex-wrap:wrap;gap:10px 38px;font-size:.78rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase}
.credo span{display:inline-flex;align-items:center;gap:10px}
.credo span::before{content:"—";color:rgba(255,255,255,.5)}
.credo span:first-child::before{display:none}

/* ANSWER BLOCK — AEO direct answer, opens money pages */
.answer-block{background:#fff;border:1px solid var(--hairline);border-left:4px solid var(--pine);border-radius:var(--r);padding:22px 26px;margin:0 0 2.2rem;box-shadow:var(--shadow-1)}
.answer-block .ab-tag{font-size:.68rem;font-weight:800;letter-spacing:.24em;text-transform:uppercase;color:var(--brass);display:block;margin-bottom:8px}
.answer-block p{font-size:1.04rem;line-height:1.65;margin:0;color:var(--ink)}

/* PAGE HERO (inner pages) */
.page-hero{background:var(--lake);color:#fff;padding:64px 0 56px;position:relative;overflow:hidden}
.page-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(640px 300px at 90% 0%,rgba(30,93,72,.4),transparent 60%)}
.page-hero .wrap{position:relative;z-index:1}
.page-hero h1{color:#fff;margin-bottom:.9rem}
.page-hero h1 em{font-style:italic;color:#9FC3B2}
.page-hero .ph-sub{color:rgba(255,255,255,.8);font-size:1.05rem;max-width:720px;margin-bottom:1.5rem}
.page-hero .ph-facts{display:flex;flex-wrap:wrap;gap:8px 26px;border-top:1px solid rgba(255,255,255,.16);padding-top:1.2rem;font-size:.82rem;color:rgba(255,255,255,.78)}
.page-hero .ph-facts span{display:inline-flex;gap:7px;align-items:center}
.page-hero .ph-facts span::before{content:"✦";color:#9FC3B2;font-size:.62rem}

/* SERVICE CARDS — ledger rows on desktop-friendly grid */
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.svc-card{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);padding:28px 26px;display:flex;flex-direction:column;min-height:250px;transition:all .22s;position:relative;overflow:hidden}
.svc-card::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:transparent;transition:background .22s}
.svc-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-2);border-color:var(--pine)}
.svc-card:hover::before{background:var(--pine)}
.svc-num{font-family:var(--disp);font-style:italic;font-size:.95rem;color:var(--brass);margin-bottom:10px}
.svc-card h3{margin-bottom:.65rem}
.svc-card h3 a{color:var(--lake)}
.svc-card h3 a:hover{color:var(--pine)}
.svc-card p{font-size:.92rem;color:var(--ink-soft);line-height:1.6;flex:1;margin-bottom:1.1rem}
.svc-card .tlink{margin-top:auto}

/* WHY — single column ledger with roman numerals */
.why-ledger{border-top:1px solid var(--hairline)}
.why-row{display:grid;grid-template-columns:88px 1fr;gap:26px;padding:30px 0;border-bottom:1px solid var(--hairline);align-items:start}
.why-roman{font-family:var(--disp);font-style:italic;font-size:2rem;color:var(--pine);line-height:1;padding-top:4px}
.why-row h3{margin-bottom:.55rem}
.why-row p{color:var(--ink-soft);font-size:.97rem;margin:0}

/* AREAS — light section (sister sites use dark), tier-grouped */
.areas-section{background:var(--pine-wash)}
.tier-label{font-size:.7rem;font-weight:800;letter-spacing:.24em;text-transform:uppercase;color:var(--brass);margin:1.8rem 0 .9rem}
.area-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.area-tile{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);padding:18px 18px 15px;transition:all .2s;display:flex;flex-direction:column;gap:4px}
.area-tile:hover{border-color:var(--pine);box-shadow:var(--shadow-1);transform:translateY(-2px)}
.area-tile .at-name{font-family:var(--disp);font-weight:600;font-size:1.06rem;color:var(--lake)}
.area-tile .at-meta{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-soft)}

/* PROCESS — horizontal rule steps */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:2px solid var(--lake)}
.step{padding:26px 22px 8px;border-right:1px solid var(--hairline);position:relative}
.step:last-child{border-right:none}
.step::before{content:attr(data-n);position:absolute;top:-15px;left:22px;background:var(--linen);padding:0 10px;font-family:var(--disp);font-style:italic;font-size:1.15rem;color:var(--pine);font-weight:700}
.step h3{font-size:1.1rem;margin-bottom:.5rem}
.step p{font-size:.9rem;color:var(--ink-soft)}

/* CRAFT CODE — 8-phase ledger, roman numerals */
.code-section{background:var(--lake);color:#fff}
.code-section h2{color:#fff}
.code-section h2 em{color:#9FC3B2;font-style:italic}
.code-section .sect-head .lede{color:rgba(255,255,255,.7)}
.code-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.code-card{background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.13);border-radius:var(--r);padding:20px 20px 16px}
.code-card .cc-roman{font-family:var(--disp);font-style:italic;font-size:1.5rem;color:#9FC3B2;display:block;margin-bottom:6px}
.code-card h3{color:#fff;font-size:1.02rem;margin-bottom:.7rem}
.code-card ul{list-style:none}
.code-card li{font-size:.82rem;color:rgba(255,255,255,.72);padding:5px 0 5px 16px;position:relative;line-height:1.45}
.code-card li::before{content:"·";position:absolute;left:2px;color:#9FC3B2;font-weight:800}
.code-tally{margin-top:2rem;text-align:center;font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:#9FC3B2}

/* NEIGHBORHOODS + ZIPs */
.hood-flow{display:flex;flex-wrap:wrap;gap:9px;margin:1.1rem 0 1.6rem}
.hood{background:#fff;border:1px solid var(--hairline);border-radius:30px;padding:8px 17px;font-size:.88rem;color:var(--ink);display:inline-flex;align-items:center;gap:8px}
.hood::before{content:"";width:5px;height:5px;border-radius:50%;background:var(--pine)}
.zip-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px;border-top:1px solid var(--hairline);padding-top:1.2rem}
.zip-row .zr-label{font-size:.7rem;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--brass);margin-right:6px}
.zip-chip{background:var(--lake);color:#fff;border-radius:var(--r);padding:4px 11px;font-size:.8rem;font-weight:700;letter-spacing:.04em}

/* LEDGER TABLES — investment guide & options */
.ledger-wrap{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);overflow:hidden;box-shadow:var(--shadow-1)}
.ledger-cap{display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;padding:16px 22px;border-bottom:2px solid var(--lake)}
.ledger-cap h3{font-size:1.2rem;margin:0}
.ledger-cap h3 em{font-style:italic;color:var(--pine)}
.ledger-cap .lc-note{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft)}
table.ledger{width:100%;border-collapse:collapse}
.ledger th{text-align:left;padding:11px 22px;font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-soft);border-bottom:1px solid var(--hairline);background:var(--linen)}
.ledger td{padding:13px 22px;border-bottom:1px solid var(--hairline);font-size:.94rem;vertical-align:top}
.ledger tr:last-child td{border-bottom:none}
.ledger td:first-child{font-weight:600;color:var(--lake)}
.ledger .amount{font-family:var(--disp);font-weight:700;color:var(--pine);white-space:nowrap}
.ledger tr:hover td{background:var(--pine-wash)}
.ledger-foot{padding:12px 22px;font-size:.8rem;color:var(--ink-soft);background:var(--linen);border-top:1px solid var(--hairline)}
.ledger-foot a{font-weight:700}

/* SCOPE LIST — two-column checklist */
.scope-cols{columns:2;column-gap:44px;max-width:900px}
.scope-cols li{list-style:none;break-inside:avoid;padding:9px 0 9px 28px;position:relative;font-size:.96rem;border-bottom:1px dashed var(--hairline)}
.scope-cols li::before{content:"✓";position:absolute;left:2px;color:var(--pine);font-weight:800}

/* PROSE */
.prose{max-width:820px}
.prose p{font-size:1.04rem;line-height:1.75;margin-bottom:1.15rem}
.prose strong{color:var(--lake)}
.prose h2{margin:2.1rem 0 .9rem}
.prose h3{margin:1.6rem 0 .7rem}
.prose ul,.prose ol{padding-left:1.35rem;margin-bottom:1.2rem}
.prose li{margin-bottom:.5rem;line-height:1.65}
.prose li::marker{color:var(--pine);font-weight:700}
.prose blockquote{border-left:3px solid var(--pine);padding:.4rem 0 .4rem 1.3rem;font-family:var(--disp);font-style:italic;font-size:1.18rem;color:var(--lake);margin:1.7rem 0}
.dropcap p:first-of-type::first-letter{font-family:var(--disp);font-size:3.6rem;float:left;line-height:.85;padding:6px 10px 0 0;color:var(--pine);font-weight:700}

/* KEY FACT — AEO citable stat callout */
.keyfact{background:var(--pine-wash);border:1px solid var(--hairline);border-radius:var(--r);padding:20px 24px;margin:1.8rem 0;display:flex;gap:18px;align-items:center}
.keyfact .kf-mark{font-family:var(--disp);font-style:italic;font-size:2.3rem;color:var(--pine);line-height:1;flex:0 0 auto}
.keyfact p{margin:0;font-size:.98rem}
.keyfact strong{color:var(--lake)}

/* EXCLUSIONS NOTE */
.honest-note{border:1px dashed var(--brass);border-radius:var(--r);padding:18px 22px;margin:1.8rem 0;font-size:.92rem;color:var(--ink-soft);background:#fff}
.honest-note strong{color:var(--brass);display:block;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;margin-bottom:6px}

/* FAQ */
.faq-rail{max-width:820px;border-top:1px solid var(--hairline)}
.faq-rail details{border-bottom:1px solid var(--hairline)}
.faq-rail summary{list-style:none;cursor:pointer;padding:20px 34px 20px 0;font-family:var(--disp);font-weight:600;font-size:1.08rem;color:var(--lake);position:relative;line-height:1.35}
.faq-rail summary::-webkit-details-marker{display:none}
.faq-rail summary::after{content:"+";position:absolute;right:4px;top:50%;transform:translateY(-50%);font-family:var(--body);font-weight:400;font-size:1.5rem;color:var(--pine)}
.faq-rail details[open] summary::after{content:"–"}
.faq-rail details[open] summary{color:var(--pine-deep)}
.faq-rail .faq-a{padding:0 0 20px;color:var(--ink-soft);font-size:.98rem;line-height:1.7;max-width:740px}

/* REVIEWS INVITE (new business — no fabricated reviews) */
.invite{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);padding:30px;display:grid;grid-template-columns:1fr auto;gap:22px;align-items:center;box-shadow:var(--shadow-1)}
.invite h3{margin-bottom:.4rem}
.invite p{margin:0;color:var(--ink-soft);font-size:.95rem;max-width:640px}
.invite .iv-ctas{display:flex;gap:10px;flex-wrap:wrap}

/* RELATED RAILS */
.rail-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.rail-box{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);padding:22px}
.rail-box .rb-tag{font-size:.68rem;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--brass);display:block;margin-bottom:10px}
.rail-box ul{list-style:none}
.rail-box li{border-bottom:1px dashed var(--hairline)}
.rail-box li:last-child{border-bottom:none}
.rail-box a{display:block;padding:8px 0;font-size:.92rem;color:var(--ink)}
.rail-box a:hover{color:var(--pine);padding-left:4px}

/* CONTACT BAND */
.band{background:var(--lake);border-radius:8px;color:#fff;padding:30px 34px;margin:2.4rem 0;display:grid;grid-template-columns:1fr auto;gap:22px;align-items:center;position:relative;overflow:hidden}
.band::before{content:"";position:absolute;inset:0;background:radial-gradient(400px 200px at 95% 10%,rgba(30,93,72,.5),transparent 65%)}
.band>*{position:relative}
.band strong{font-family:var(--disp);font-size:1.35rem;display:block;margin-bottom:4px}
.band span{font-size:.82rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.65)}
.band .bd-ctas{display:flex;gap:10px;flex-wrap:wrap}

/* FINAL CTA — emerald gradient (sisters end orange / gold) */
.finale{background:linear-gradient(150deg,var(--pine-deep),var(--pine));color:#fff;text-align:center;padding:86px 0}
.finale h2{color:#fff;max-width:740px;margin:0 auto 1rem}
.finale h2 em{font-style:italic;color:#CFE5D8}
.finale .fin-sub{color:rgba(255,255,255,.85);max-width:560px;margin:0 auto 1.9rem;font-size:1.04rem}
.finale .fin-tel{font-family:var(--disp);font-weight:700;font-size:clamp(1.7rem,4vw,2.5rem);color:#fff;display:inline-block;margin-bottom:1.5rem;border-bottom:2px solid rgba(255,255,255,.5);padding-bottom:4px}
.finale .fin-tel:hover{border-bottom-color:#fff;color:#fff}
.finale .fin-ctas{display:flex;justify-content:center;gap:12px;flex-wrap:wrap}

/* BLOG CARDS */
.post-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.post-card{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);padding:26px;display:flex;flex-direction:column;min-height:220px;transition:all .2s}
.post-card:hover{border-color:var(--pine);box-shadow:var(--shadow-2);transform:translateY(-3px)}
.post-card .pc-meta{font-size:.7rem;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--brass);margin-bottom:.8rem;display:flex;justify-content:space-between;gap:1rem}
.post-card h3{font-size:1.12rem;line-height:1.3;flex:1;margin-bottom:.9rem}
.post-card h3 a{color:var(--lake)}
.post-card h3 a:hover{color:var(--pine)}

/* ARTICLE */
.article{max-width:740px;margin:0 auto;padding:56px 0}
.article .art-meta{font-size:.74rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-soft);display:flex;gap:18px;flex-wrap:wrap;margin-bottom:1.2rem}
.article .art-meta .cat{color:var(--pine);font-weight:800}
.article h1{margin-bottom:1.1rem}
.article .standfirst{font-family:var(--disp);font-style:italic;font-size:1.22rem;line-height:1.5;color:var(--ink-soft);border-bottom:1px solid var(--hairline);padding-bottom:1.6rem;margin-bottom:1.8rem}
.article h2{margin:2.3rem 0 .9rem;padding-top:1.6rem;border-top:1px solid var(--hairline)}
.article h3{margin:1.7rem 0 .7rem}
.article p{font-size:1.05rem;line-height:1.75;margin-bottom:1.15rem}
.article ul,.article ol{padding-left:1.35rem;margin-bottom:1.25rem}
.article li{margin-bottom:.5rem;font-size:1.01rem;line-height:1.65}
.article li::marker{color:var(--pine);font-weight:700}
.article table{width:100%;border-collapse:collapse;margin:1.8rem 0;font-size:.92rem;background:#fff;border:1px solid var(--hairline)}
.article th{background:var(--lake);color:#fff;text-align:left;padding:10px 15px;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase}
.article td{padding:10px 15px;border-bottom:1px solid var(--hairline)}
.article tr:nth-child(even) td{background:var(--linen)}
.byline{display:flex;align-items:center;gap:14px;border-top:1px solid var(--hairline);margin-top:2.4rem;padding-top:1.6rem}
.byline .by-mark{width:48px;height:48px;border-radius:50%;background:var(--pine);color:#fff;display:grid;place-items:center;font-family:var(--disp);font-style:italic;font-weight:700;font-size:1.2rem;flex:0 0 auto}
.byline strong{display:block;color:var(--lake);font-size:.95rem}
.byline span{font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft)}

/* FORM */
.formcard{background:#fff;border:1px solid var(--hairline);border-radius:var(--r);padding:30px;box-shadow:var(--shadow-1)}
.formcard .fgrid{display:grid;grid-template-columns:1fr 1fr;gap:15px}
.formcard label{display:flex;flex-direction:column;gap:6px;font-size:.74rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--lake)}
.formcard label.full{grid-column:span 2}
.formcard input,.formcard select,.formcard textarea{font-family:var(--body);font-size:.96rem;padding:12px 14px;border:1.5px solid var(--hairline);border-radius:var(--r);background:var(--linen);color:var(--ink);transition:all .18s}
.formcard input:focus,.formcard select:focus,.formcard textarea:focus{outline:none;border-color:var(--pine);background:#fff;box-shadow:0 0 0 3px rgba(30,93,72,.12)}
.formcard textarea{min-height:120px;resize:vertical}
.formcard .fsubmit{grid-column:span 2;justify-self:start}

/* FOOTER */
footer{background:var(--lake);color:rgba(255,255,255,.72);padding:64px 0 0;font-size:.92rem}
.foot-grid{max-width:var(--wrap-wide);margin:0 auto;padding:0 22px;display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:40px;padding-bottom:2.6rem}
.foot-grid .ft-h{font-size:.7rem;font-weight:800;letter-spacing:.24em;text-transform:uppercase;color:#9FC3B2;margin-bottom:1rem}
.foot-brand .fb-name{font-family:var(--disp);font-weight:700;font-size:1.4rem;color:#fff}
.foot-brand .fb-name em{font-style:italic;color:#9FC3B2}
.foot-brand .fb-sub{font-size:.62rem;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--brass);margin:4px 0 1rem}
.foot-brand p{color:rgba(255,255,255,.55);line-height:1.65;margin-bottom:.8rem}
.foot-grid ul{list-style:none}
.foot-grid li{margin-bottom:.45rem}
.foot-grid a{color:rgba(255,255,255,.68);font-size:.88rem}
.foot-grid a:hover{color:#9FC3B2}
.foot-contact div{display:flex;gap:10px;margin-bottom:.55rem;align-items:flex-start}
.foot-contact svg{width:14px;height:14px;color:#9FC3B2;flex:0 0 auto;margin-top:4px}
.foot-hours{font-size:.78rem;color:rgba(255,255,255,.45);line-height:1.8;margin-top:.8rem}
.foot-rule{border-top:1px solid rgba(255,255,255,.12);max-width:var(--wrap-wide);margin:0 auto;padding:1.3rem 22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.7rem;font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.4)}
.foot-rule a{color:rgba(255,255,255,.5)}
.foot-rule a:hover{color:#9FC3B2}

/* FLOATS — desktop side rail; mobile bottom bar */
.side-float{position:fixed;right:20px;bottom:20px;z-index:900;display:flex;flex-direction:column;gap:9px}
.side-float a{display:inline-flex;align-items:center;gap:8px;background:var(--pine);color:#fff;font-weight:700;font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;padding:12px 17px;border-radius:var(--r);box-shadow:var(--shadow-2);transition:all .2s}
.side-float a:hover{background:var(--pine-deep);color:#fff;transform:translateY(-2px)}
.side-float a.alt{background:var(--lake)}
.side-float a.alt:hover{background:var(--lake-soft)}
.side-float svg{width:15px;height:15px}
.callbar{display:none}

@media(max-width:1080px){
  .hero-in{grid-template-columns:1fr;gap:40px;padding:66px 22px 60px}
  .svc-grid,.post-grid,.rail-grid{grid-template-columns:repeat(2,1fr)}
  .area-grid{grid-template-columns:repeat(3,1fr)}
  .code-grid{grid-template-columns:repeat(2,1fr)}
  .steps{grid-template-columns:repeat(2,1fr);border-top:none}
  .step{border-top:2px solid var(--lake);margin-top:16px}
  .foot-grid{grid-template-columns:1fr 1fr;gap:30px}
}
@media(max-width:760px){
  .navlist{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;flex-direction:column;align-items:stretch;gap:0;border-bottom:1px solid var(--hairline);box-shadow:var(--shadow-2);max-height:calc(100vh - 80px);overflow-y:auto;z-index:1200}
  .navlist.open{display:flex}
  .navlist>li{border-top:1px solid var(--hairline)}
  .navlist>li>a{display:block;padding:15px 22px;border-bottom:none}
  .drop{position:static;opacity:0;visibility:hidden;max-height:0;overflow:hidden;transform:none;box-shadow:none;border:none;border-radius:0;background:var(--pine-wash);padding:0;transition:max-height .25s}
  .navlist>li.m-open .drop{opacity:1;visibility:visible;max-height:75vh;padding:6px 0}
  .drop a{padding:10px 36px}
  .navlist>li.has-drop>a::after{content:"+";float:right;color:var(--pine);font-size:1.2rem}
  .navlist>li.has-drop.m-open>a::after{content:"–"}
  .burger{display:block}
  .mast-tel span{display:none}
  .mast-cta .btn{display:none}
  .topline .tl-edition{display:none}
  section{padding:52px 0}
  .svc-grid,.post-grid,.rail-grid,.code-grid{grid-template-columns:1fr}
  .area-grid{grid-template-columns:1fr 1fr}
  .steps{grid-template-columns:1fr}
  .why-row{grid-template-columns:54px 1fr;gap:16px}
  .scope-cols{columns:1}
  .invite,.band{grid-template-columns:1fr}
  .foot-grid{grid-template-columns:1fr}
  .formcard .fgrid{grid-template-columns:1fr}
  .formcard label.full,.formcard .fsubmit{grid-column:span 1}
  .hero-in{padding:54px 18px 48px}
  .quote-card{padding:24px 20px}
  .side-float{display:none}
  .callbar{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:1100}
  .callbar a{padding:15px 0;text-align:center;font-weight:800;font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;color:#fff}
  .callbar a.cb-call{background:var(--pine)}
  .callbar a.cb-quote{background:var(--lake)}
  body{padding-bottom:52px}
}
@media(max-width:460px){
  .wrap,.wrap-wide{padding:0 15px}
  .area-grid{grid-template-columns:1fr}
  .ledger{display:block;overflow-x:auto}
}
"""

# ============================================================================
# HEAD
# ============================================================================
def head(title, desc, canonical, og_image=None, og_type="website", indexable=True, json_ld=None, extra_meta=""):
    og_image = og_image or f"{SITE}{OG_DEFAULT}"
    robots = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" if indexable else "noindex, nofollow"
    schemas_html = ""
    if json_ld:
        items = json_ld if isinstance(json_ld, list) else [json_ld]
        for s in items:
            schemas_html += f'<script type="application/ld+json">{json.dumps(s, separators=(",",":"))}</script>\n'
    ga = ""
    if "{{" not in GA4_ID:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>\n'
              f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}"
              f"gtag('js',new Date());gtag('config','{GA4_ID}');</script>\n")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
{ga}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="author" content="{BUSINESS["name"]}">
<meta name="geo.region" content="US-{BUSINESS["state"]}">
<meta name="geo.placename" content="{BUSINESS["city"]}, {BUSINESS["state_long"]}">
<meta name="geo.position" content="{BUSINESS["lat"]};{BUSINESS["lng"]}">
<meta name="ICBM" content="{BUSINESS["lat"]}, {BUSINESS["lng"]}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BUSINESS["name"]} — concrete, paver &amp; travertine contractor, Windermere FL">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{BUSINESS["name"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" type="image/png" sizes="96x96" href="/images/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Figtree:wght@400;600;700;800&display=swap" rel="stylesheet">
{extra_meta}<style>{CSS}</style>
{schemas_html}</head>
'''

# ============================================================================
# HEADER / NAV
# ============================================================================
def header(active=""):
    svc_links = ""
    for grp_name, slugs in SERVICE_GROUPS:
        svc_links += f'<span class="grp">{grp_name}</span>'
        svc_links += "".join(f'<a href="/{s}/">{SERVICES[s]["name"]}</a>' for s in slugs)
    t1 = "".join(f'<a href="/{s}/">{CITIES[s]["name"]}, FL</a>' for s in TIER1)
    area_links = ('<span class="grp">Core Service Area</span>' + t1 +
                  f'<a href="/windermere/" style="font-weight:700;color:var(--pine)">All {len(CITIES)} cities we serve ›</a>')
    def on(k): return ' class="on"' if active == k else ""
    def on_drop(k): return ' class="has-drop on"' if active == k else ' class="has-drop"'
    return f'''<div class="topline">
  <div class="wrap-wide">
    <span class="tl-edition">Concrete · Pavers · Travertine — Windermere &amp; West Orlando, FL</span>
    <span>Fully Insured · Free Estimates · <a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a></span>
  </div>
</div>
<header class="masthead">
  <nav class="mast-in" aria-label="Main">
    <a class="wordmark" href="/" aria-label="{BUSINESS["name"]} — home">
      <span class="wm-name">Windermere <em>Concrete</em></span>
      <span class="wm-sub">Estate-Grade Hardscape</span>
    </a>
    <ul class="navlist" id="navList">
      <li{on("home")}><a href="/">Home</a></li>
      <li{on_drop("services")}><a href="/concrete-driveways/">Services</a><div class="drop">{svc_links}</div></li>
      <li{on_drop("areas")}><a href="/windermere/">Service Areas</a><div class="drop">{area_links}</div></li>
      <li{on("process")}><a href="/process/">Our Craft Code</a></li>
      <li{on("blog")}><a href="/blog/">Insights</a></li>
      <li{on("about")}><a href="/about/">About</a></li>
      <li{on("contact")}><a href="/contact/">Contact</a></li>
    </ul>
    <div class="mast-cta">
      <a class="mast-tel" href="{TEL_LINK}" aria-label="Call {BUSINESS["name"]}">
        <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        <span>{BUSINESS["phone_display"]}</span>
      </a>
      <a class="btn btn-pine" href="/contact/#proposal">Request Proposal</a>
      <button class="burger" id="navBurger" aria-label="Menu" aria-expanded="false">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="17" x2="21" y2="17"/></svg>
      </button>
    </div>
  </nav>
</header>'''

# ============================================================================
# BREADCRUMBS
# ============================================================================
def breadcrumbs(items):
    lis = ""
    for label, href in items:
        lis += f'<li><a href="{href}">{label}</a></li>' if href else f'<li>{label}</li>'
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{lis}</ol></div></nav>'

# ============================================================================
# FOOTER
# ============================================================================
def footer():
    svc_links = "".join(f'<li><a href="/{s}/">{SERVICES[s]["name"]}</a></li>' for s in SERVICE_ORDER)
    area_links = "".join(f'<li><a href="/{s}/">{CITIES[s]["name"]}, FL</a></li>' for s in TIER1)
    area_links += "".join(f'<li><a href="/{s}/">{CITIES[s]["name"]}, FL</a></li>' for s in TIER2[:6])
    hours_html = "<br>".join(f'{d[:3].upper()} &nbsp;{o}&ndash;{c}' if o != "Closed" else f'{d[:3].upper()} &nbsp;Closed'
                             for d, o, c in BUSINESS["hours"])
    socials = ""
    for name, url in [("Facebook", BUSINESS["facebook"]), ("Instagram", BUSINESS["instagram"])]:
        if url and "{{" not in url:
            socials += f'<a href="{url}" target="_blank" rel="noopener">{name}</a> &nbsp;·&nbsp; '
    return f'''<footer>
  <div class="foot-grid">
    <div class="foot-brand">
      <div class="fb-name">Windermere <em>Concrete</em></div>
      <div class="fb-sub">Estate-Grade Hardscape</div>
      <p>{BUSINESS["tagline_long"]}</p>
      <p style="font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:#9FC3B2">{BUSINESS["checklist_name"]} · 48 Checkpoints · Fully Insured</p>
    </div>
    <div>
      <div class="ft-h">Services</div>
      <ul>{svc_links}</ul>
    </div>
    <div>
      <div class="ft-h">Where We Work</div>
      <ul>{area_links}</ul>
    </div>
    <div class="foot-contact">
      <div class="ft-h">Reach Us</div>
      <div><svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg><a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a></div>
      <div><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a></div>
      <div><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg><span>{BUSINESS["city"]}, {BUSINESS["state"]} {BUSINESS["zip"]} — serving a 50-mile radius</span></div>
      <p class="foot-hours">{hours_html}</p>
    </div>
  </div>
  <div class="foot-rule">
    <span>© 2026 {BUSINESS["legal_name"]} · Fully Insured · Windermere, FL</span>
    <span>{socials}<a href="/process/">Craft Code</a> &nbsp;·&nbsp; <a href="/warranty/">Warranty</a> &nbsp;·&nbsp; <a href="/faq/">FAQ</a> &nbsp;·&nbsp; <a href="/privacy-policy/">Privacy</a> &nbsp;·&nbsp; <a href="/terms/">Terms</a></span>
  </div>
</footer>'''

# ============================================================================
# FLOATS + MENU JS
# ============================================================================
FLOAT_CONTACT = f'''<div class="side-float">
  <a href="{TEL_LINK}" aria-label="Call {BUSINESS["name"]}">
    <svg fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
    Call
  </a>
  <a href="/contact/#proposal" class="alt" aria-label="Request a written proposal">
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
    Proposal
  </a>
</div>
<div class="callbar">
  <a class="cb-call" href="{TEL_LINK}">Call Now</a>
  <a class="cb-quote" href="/contact/#proposal">Free Proposal</a>
</div>'''

MENU_JS = '''<script>
(function(){
  var b=document.getElementById("navBurger"),m=document.getElementById("navList");
  if(!b||!m)return;
  b.addEventListener("click",function(){
    var o=m.classList.toggle("open");
    b.setAttribute("aria-expanded",o);
    if(!o)m.querySelectorAll("li.m-open").forEach(function(li){li.classList.remove("m-open");});
  });
  m.querySelectorAll("li").forEach(function(li){
    var d=li.querySelector(".drop");if(!d)return;
    li.classList.add("has-drop");
    var a=li.querySelector(":scope > a");if(!a)return;
    a.addEventListener("click",function(e){
      if(window.innerWidth<=760){
        e.preventDefault();
        li.parentNode.querySelectorAll("li.m-open").forEach(function(s){if(s!==li)s.classList.remove("m-open");});
        li.classList.toggle("m-open");
      }
    });
  });
})();
</script>'''

# ============================================================================
# SHARED SECTIONS
# ============================================================================
def credo_bar():
    items = ["Fully Insured", "Free Estimates", "Written Warranty",
             "ARC / HOA Submittal Support", "48-Checkpoint Craft Code"]
    return '<div class="credo"><div class="wrap-wide">' + "".join(f"<span>{x}</span>" for x in items) + "</div></div>"

def answer_block(html_text, tag="The Short Answer"):
    return f'<div class="answer-block"><span class="ab-tag">{tag}</span><p>{html_text}</p></div>'

def keyfact(text_html):
    return f'<aside class="keyfact"><span class="kf-mark">48</span><p>{text_html}</p></aside>'

CITABLE_LINE = ("According to <strong>Windermere Concrete</strong>, every driveway, patio, pool deck, and paver "
                "installation it performs is verified against <strong>the Windermere Craft Code &mdash; a 48-checkpoint "
                "installation standard</strong> covering subgrade probing, lift-compacted bases, engineered joints, "
                "and a hose-tested drainage walkthrough.")

def contact_band(title=None, sub=None):
    title = title or "Same-day reply. Written proposal within one business day."
    sub = sub or "Fully insured · free estimates · ARC submittal support included"
    return f'''<aside class="band">
  <div><strong>{title}</strong><span>{sub}</span></div>
  <div class="bd-ctas">
    <a class="btn btn-pine" href="{TEL_LINK}">Call {BUSINESS["phone_display"]}</a>
    <a class="btn btn-ghost-light" href="/contact/#proposal">Request Proposal</a>
  </div>
</aside>'''

def final_cta(headline=None, sub=None):
    headline = headline or "Your property deserves a surface built to <em>estate standard</em>."
    sub = sub or "Walk the project with us. Get a written, line-itemized proposal within one business day — no pressure, no theater."
    return f'''<section class="finale">
  <div class="wrap">
    <span class="eyebrow on-dark center">Free Estimate · Fully Insured</span>
    <h2>{headline}</h2>
    <p class="fin-sub">{sub}</p>
    <a class="fin-tel" href="{TEL_LINK}">{BUSINESS["phone_display"]}</a>
    <div class="fin-ctas">
      <a class="btn btn-lake" href="/contact/#proposal">Request a Proposal</a>
      <a class="btn btn-ghost-light" href="{SMS_LINK}">Text Us</a>
    </div>
  </div>
</section>'''

def craft_code_section(context=None):
    ctx = f" — applied in full on every {context} project" if context else ""
    cards = ""
    for p in CHECKLIST["phases"]:
        items = "".join(f"<li>{i}</li>" for i in p["items"])
        cards += f'''<article class="code-card"><span class="cc-roman">{p["roman"]}</span><h3>{p["title"]}</h3><ul>{items}</ul></article>'''
    return f'''<section class="code-section">
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow on-dark">The Standard</span>
      <h2>The Windermere <em>Craft Code</em></h2>
      <p class="lede">Eight phases, forty-eight checkpoints{ctx}. The base is photographed before it disappears, the drainage is hose-tested in front of you, and the warranty arrives in writing.</p>
    </div>
    <div class="code-grid">{cards}</div>
    <p class="code-tally">48 checkpoints · every project · no exceptions</p>
  </div>
</section>'''

def neighborhoods_section(city):
    pills = "".join(f'<div class="hood">{n}</div>' for n in city["neighborhoods"])
    zips = "".join(f'<span class="zip-chip">{z}</span>' for z in city["zips"])
    return f'''<section>
  <div class="wrap">
    <div class="sect-head">
      <span class="eyebrow">Local Coverage · {city["county"]}</span>
      <h2>Neighborhoods we serve in <em>{city["name"]}</em></h2>
      <p class="lede">From the communities below to the streets between them &mdash; if you&rsquo;re in or around {city["name"]}, you&rsquo;re inside our service area. Don&rsquo;t see your community? Call anyway; we quote the address, not the list.</p>
    </div>
    <div class="hood-flow">{pills}</div>
    <div class="zip-row"><span class="zr-label">ZIP codes</span>{zips}</div>
  </div>
</section>'''

def faq_section(faqs, headline=None, label="Questions, answered plainly"):
    headline = headline or "What homeowners ask us"
    items = "".join(f'<details><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q, a in faqs)
    return f'''<section>
  <div class="wrap">
    <div class="sect-head">
      <span class="eyebrow">{label}</span>
      <h2>{headline}</h2>
    </div>
    <div class="faq-rail">{items}</div>
  </div>
</section>'''

def reviews_invite():
    gp = BUSINESS.get("google_review_url") or ""
    btn = (f'<a class="btn btn-pine" href="{gp}" target="_blank" rel="noopener">Review us on Google</a>'
           if gp and "{{" not in gp else "")
    return f'''<section class="snug">
  <div class="wrap">
    <div class="invite">
      <div>
        <h3>Our reputation is being built one project at a time.</h3>
        <p>We&rsquo;re an owner-run local company and we don&rsquo;t publish testimonials we can&rsquo;t stand behind &mdash; so you won&rsquo;t find invented five-star quotes here. What you will find is a written warranty, published pricing, and a crew that answers the phone. If we&rsquo;ve built for you, your honest review is the most valuable thing you can leave behind.</p>
      </div>
      <div class="iv-ctas">{btn}<a class="btn btn-ghost" href="/contact/">Get an estimate</a></div>
    </div>
  </div>
</section>'''

def pricing_table(svc, city_name=None):
    where = f" in {city_name}" if city_name else " — Windermere &amp; West Orlando"
    rows = "".join(
        f'<tr><td>{item}</td><td class="amount">{amt}</td><td>{note}</td></tr>'
        for item, amt, note in svc["pricing_rows"])
    return f'''<div class="ledger-wrap">
  <div class="ledger-cap">
    <h3>Investment guide — <em>{svc["short"]}</em>{where}</h3>
    <span class="lc-note">Honest 2026 ranges · exact number in your written proposal</span>
  </div>
  <table class="ledger">
    <thead><tr><th scope="col">Scope</th><th scope="col">Typical range</th><th scope="col">What&rsquo;s included</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <div class="ledger-foot">Ranges reflect typical site conditions in our service area. Access, demolition findings, and material selections move the number &mdash; the <a href="/contact/">written proposal</a> pins it, line by line.</div>
</div>'''

def options_table(svc):
    rows = "".join(
        f'<tr><td>{opt}</td><td>{best}</td><td>{note}</td></tr>'
        for opt, best, note in svc["options_rows"])
    return f'''<div class="ledger-wrap" style="margin-top:22px">
  <div class="ledger-cap">
    <h3>Choosing the right <em>system</em></h3>
    <span class="lc-note">Comparison, not upsell</span>
  </div>
  <table class="ledger">
    <thead><tr><th scope="col">Option</th><th scope="col">Best for</th><th scope="col">Why</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>'''

def scope_section(svc, city_name=None):
    where = f" in {city_name}" if city_name else ""
    items = "".join(f"<li>{i}</li>" for i in svc["scope_items"])
    return f'''<section class="snug">
  <div class="wrap">
    <div class="sect-head">
      <span class="eyebrow">Full Scope</span>
      <h2>Everything this service covers{where}</h2>
    </div>
    <ul class="scope-cols">{items}</ul>
  </div>
</section>'''

def honest_note(svc):
    return f'''<div class="honest-note"><strong>What we don&rsquo;t do</strong>{svc["not_included"]}</div>'''

def why_us_section():
    rows = "".join(f'''<div class="why-row"><div class="why-roman">{w["num"]}.</div><div><h3>{w["title"]}</h3><p>{w["body"]}</p></div></div>'''
                   for w in WHY_US_POINTS)
    return f'''<section>
  <div class="wrap">
    <div class="sect-head">
      <span class="eyebrow">Why Windermere Concrete</span>
      <h2>Six reasons this market <em>keeps our number</em></h2>
    </div>
    <div class="why-ledger">{rows}</div>
  </div>
</section>'''

def process_section():
    steps = "".join(f'''<div class="step" data-n="{s["num"]}"><h3>{s["title"]}</h3><p>{s["body"]}</p></div>'''
                    for s in PROCESS_STEPS)
    return f'''<section class="snug">
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow">How Every Project Runs</span>
      <h2>Consultation to <em>white-glove handover</em></h2>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>'''

def exclusions_block():
    lis = "".join(f"<li>{e}</li>" for e in EXCLUSIONS)
    return f'''<div class="honest-note"><strong>Deliberately outside our scope</strong>
We stay in our lane, and we&rsquo;re direct about where the lane ends:<ul style="padding-left:1.2rem;margin-top:.5rem">{lis}</ul></div>'''

# ============================================================================
# JSON-LD SCHEMA BUILDERS
# ============================================================================
def _clean_sameas():
    return [x for x in [BUSINESS["google_profile"], BUSINESS["facebook"], BUSINESS["instagram"],
                        BUSINESS["yelp"], BUSINESS["thumbtack"], BUSINESS["angi"],
                        BUSINESS["houzz"], BUSINESS["bbb"]] if x and "{{" not in x]

def _areas_served():
    areas = [{"@type": "City", "name": c["name"]} for c in CITIES.values()]
    areas += [{"@type": "City", "name": n} for n in AREASERVED_ONLY]
    return areas

def schema_organization():
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": BUSINESS["name"],
        "alternateName": BUSINESS["legal_name"],
        "url": SITE,
        "logo": {"@type": "ImageObject", "url": f"{SITE}/images/windermere-concrete-logo.png", "width": 600, "height": 300},
        "image": f"{SITE}{OG_DEFAULT}",
        "email": BUSINESS["email"],
        "address": {"@type": "PostalAddress", "addressLocality": BUSINESS["city"],
                    "addressRegion": BUSINESS["state"], "postalCode": BUSINESS["zip"],
                    "addressCountry": BUSINESS["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": BUSINESS["lat"], "longitude": BUSINESS["lng"]},
        "areaServed": _areas_served(),
        "sameAs": _clean_sameas(),
        "slogan": "Finished to estate standard.",
        "description": "Concrete, paver, and travertine contractor serving Windermere, FL and a 50-mile radius of west Orlando — estate-grade driveways, pool decks, patios, and hardscape installed under the 48-checkpoint Windermere Craft Code.",
        "knowsAbout": ["concrete driveways", "paver driveways", "travertine pool decks", "stamped concrete",
                       "concrete patios", "pool deck resurfacing", "paver sealing", "driveway widening",
                       "HOA architectural review hardscape"],
    }
    if "{{" not in str(BUSINESS["phone"]):
        org["telephone"] = BUSINESS["phone"]
    if "{{" not in str(BUSINESS["year_founded"]):
        org["foundingDate"] = str(BUSINESS["year_founded"])
    return org

def schema_local_business(page_url, page_name, city=None, service=None, image=None, desc=None):
    if not desc:
        if service and city:
            desc = f"{service} in {city}, FL by Windermere Concrete — estate-grade installation under the 48-checkpoint Windermere Craft Code. Fully insured, free estimates."
        elif service:
            desc = f"{service} across Windermere and west Orlando by Windermere Concrete — installed under the 48-checkpoint Windermere Craft Code. Fully insured, free estimates."
        elif city:
            desc = f"Concrete, paver & travertine contractor serving {city}, FL — Windermere Concrete installs driveways, pool decks, and patios under a 48-checkpoint standard."
        else:
            desc = page_name
    sch = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": page_url + "#business",
        "name": BUSINESS["name"],
        "url": page_url,
        "email": BUSINESS["email"],
        "image": image or f"{SITE}{OG_DEFAULT}",
        "description": desc,
        "address": {"@type": "PostalAddress", "addressLocality": BUSINESS["city"],
                    "addressRegion": BUSINESS["state"], "postalCode": BUSINESS["zip"],
                    "addressCountry": BUSINESS["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": BUSINESS["lat"], "longitude": BUSINESS["lng"]},
        "areaServed": {"@type": "City", "name": city} if city else _areas_served(),
        "priceRange": "$$-$$$",
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c}
            for d, o, c in BUSINESS["hours"] if o != "Closed"
        ],
        "parentOrganization": {"@id": f"{SITE}/#organization"},
    }
    if "{{" not in str(BUSINESS["phone"]):
        sch["telephone"] = BUSINESS["phone"]
    if BUSINESS.get("has_reviews") and REVIEWS and "{{" not in str(BUSINESS["rating"]):
        sch["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": BUSINESS["rating"],
                                  "reviewCount": str(BUSINESS["review_count"]), "bestRating": "5"}
    return sch

def schema_breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(items)]}

def schema_faqpage(faqs):
    import re as _re
    def strip(t): return _re.sub(r"<[^>]+>", "", t)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q),
                            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}

def schema_article(post, canonical, image=None):
    return {"@context": "https://schema.org", "@type": "Article",
            "headline": post["title"].replace("&rsquo;", "'").replace("&amp;", "&").replace("&mdash;", "—"),
            "description": post["meta_desc"],
            "image": image or f"{SITE}{OG_DEFAULT}",
            "datePublished": post["date_published"], "dateModified": post["date_modified"],
            "author": {"@type": "Organization", "name": BUSINESS["name"], "url": SITE},
            "publisher": {"@type": "Organization", "name": BUSINESS["name"],
                          "logo": {"@type": "ImageObject", "url": f"{SITE}/images/windermere-concrete-logo.png"}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
            "articleSection": post.get("category", "Concrete & Pavers")}

def schema_webpage(canonical, name, desc):
    return {"@context": "https://schema.org", "@type": "WebPage", "@id": canonical, "url": canonical,
            "name": name, "description": desc, "isPartOf": {"@id": f"{SITE}/#website"},
            "inLanguage": "en-US"}

def schema_website():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{SITE}/#website",
            "url": SITE, "name": BUSINESS["name"],
            "publisher": {"@id": f"{SITE}/#organization"}, "inLanguage": "en-US"}

def schema_service(service, city=None, canonical=None):
    name = f'{service["name"]} in {city}, FL' if city else service["name"]
    return {"@context": "https://schema.org", "@type": "Service",
            "serviceType": service["name"].replace("&amp;", "&"),
            "name": name.replace("&amp;", "&"),
            "description": service["intro_lead"].replace("&mdash;", "—").replace("&amp;", "&").replace("&rsquo;", "'"),
            "provider": {"@id": f"{SITE}/#organization"},
            "areaServed": {"@type": "City", "name": city} if city else _areas_served(),
            "url": canonical or SITE}

# ============================================================================
# PAGE WRAPPER
# ============================================================================
def wrap_page(head_html, header_html, body_html, footer_html=None, breadcrumbs_html="", float_html=None):
    footer_html = footer_html if footer_html is not None else footer()
    float_html = float_html if float_html is not None else FLOAT_CONTACT
    return f'''{head_html}<body>
{header_html}
{breadcrumbs_html}
<main>
{body_html}
</main>
{footer_html}
{float_html}
{MENU_JS}
</body>
</html>'''

def write_page(filepath, head_html, header_html, body_html, footer_html=None, breadcrumbs_html="", float_html=None):
    html = wrap_page(head_html, header_html, body_html, footer_html=footer_html,
                     breadcrumbs_html=breadcrumbs_html, float_html=float_html)
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath
