#!/usr/bin/env python3
"""Windermere Concrete — homepage."""
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, TIER1, TIER2, TEL_LINK,
                   GENERAL_BLOG_POSTS, clip_desc)
from _gen import (SITE, head, header, breadcrumbs, write_page, OG_DEFAULT,
                  answer_block, keyfact, CITABLE_LINE, contact_band, final_cta,
                  craft_code_section, faq_section, reviews_invite, credo_bar,
                  why_us_section, process_section, exclusions_block,
                  schema_organization, schema_website, schema_local_business,
                  schema_breadcrumb, schema_faqpage, schema_webpage)

HOME_FAQS = [
    ("What does Windermere Concrete actually do?",
     "We design and install exterior concrete, paver, and natural-stone surfaces: driveways (poured, paver, and clay brick), pool decks (concrete, resurfaced, and travertine), patios and outdoor rooms, walkways and steps, utility slabs and pads, driveway extensions, and the sealing, cleaning, and repair that keeps all of it looking installed-yesterday. Every project runs under the Windermere Craft Code — our 48-checkpoint installation standard — and closes with a written workmanship warranty."),
    ("Which areas do you serve?",
     "Our base is Windermere, FL 34786, and we serve a 50-mile radius across west Orlando and Central Florida — Windermere, Dr. Phillips, Horizon West, Winter Garden, Gotha, Oakland, Montverde, Clermont, Winter Park, Maitland, Belle Isle, and Orlando as core markets, plus Lake Nona, Celebration, Kissimmee, St. Cloud, and the wider Lake, Seminole, Osceola, and north Polk corridors."),
    ("How fast can I get an estimate?",
     "Same-day reply to every inquiry, a site walk usually within a few days, and a written, line-itemized proposal within one business day of that visit. The proposal lists thickness, reinforcement, base spec, and finish — so you can compare it line-for-line against any other bid and see exactly what each number buys."),
    ("Are you insured, and is the work guaranteed?",
     "Fully insured, yes — documentation available on request for your HOA or property manager. Every installation leaves with a signed workmanship warranty, a care guide, and a cure calendar; and we come back after the first heavy rain to watch your drainage perform, because that promise should be tested by the sky, not just the hose."),
    ("Can you handle my HOA or ARC approval?",
     "It is built into our proposals. The communities we serve — from Keene's Pointe to the Horizon West villages to Celebration — review hardscape materials, colors, and drainage before approving anything. We prepare the sample boards, spec sheets, and drawings your committee asks for, and we schedule work only after the approval clears."),
    ("Pavers, concrete, or travertine — how do I choose?",
     "That decision is most of our first conversation, and we install all three, so the advice is criteria rather than sales: concrete wins on budget and seamlessness, pavers on repairability and ARC-friendly looks, travertine on barefoot temperature and estate presence. Our Insights guides compare them honestly, and the consultation maps the trade-offs onto your actual lot, budget, and community rules."),
]


def build_home():
    canonical = f"{SITE}/"
    title = "Concrete Contractor Windermere FL | Pavers & Travertine"
    desc = clip_desc("Windermere Concrete — estate-grade concrete driveways, paver systems & travertine pool decks "
                     "in Windermere, FL & west Orlando. 48-checkpoint standard, free estimates, fully insured.")
    schemas = [
        schema_organization(), schema_website(),
        schema_local_business(canonical, "Windermere Concrete",
                              desc="Concrete, paver & travertine contractor in Windermere, FL serving west Orlando within a 50-mile radius — driveways, pool decks, patios, and hardscape under the 48-checkpoint Windermere Craft Code."),
        schema_breadcrumb([("Home", canonical)]),
        schema_faqpage(HOME_FAQS),
        schema_webpage(canonical, title, desc),
    ]
    badges = "".join(f"<span>{b}</span>" for b in
                     ["Fully Insured", "Free Estimates", "Written Warranty", "ARC / HOA Submittal Support"])
    svc_opts = "".join(f'<option value="{SERVICES[s]["name"]}">{SERVICES[s]["name"]}</option>'
                       for s in SERVICE_ORDER)
    hero = f'''<div class="hero">
  <div class="hero-in">
    <div>
      <span class="hero-kicker">Windermere · Dr. Phillips · Horizon West · Winter Garden</span>
      <h1>Concrete, pavers &amp; travertine — <em>finished to estate standard.</em></h1>
      <p class="hero-sub">Driveways, pool decks, patios, and hardscape for the Butler Chain communities and greater west Orlando &mdash; every project verified against the 48-checkpoint Windermere Craft Code, priced in writing, and warrantied on paper.</p>
      <div class="hero-ctas">
        <a class="btn btn-pine" href="{TEL_LINK}">Call {BUSINESS["phone_display"]}</a>
        <a class="btn btn-ghost-light" href="/contact/#proposal">Request a Proposal</a>
      </div>
      <div class="hero-badges">{badges}</div>
    </div>
    <div class="quote-card" id="estimate">
      <h2>Get your written proposal</h2>
      <p class="qc-sub">Free · line-itemized · tell us what you are planning</p>
      <form class="hero-form" method="POST" action="/api/contact">
        <label aria-hidden="true" class="hero-hp">Company<input type="text" name="company" tabindex="-1" autocomplete="off"></label>
        <div class="hero-form-grid">
          <label class="full">Name<input type="text" name="name" required autocomplete="name" placeholder="Your name"></label>
          <label>Phone<input type="tel" name="phone" required autocomplete="tel" placeholder="{BUSINESS["phone_display"]}"></label>
          <label>Email<input type="email" name="email" required autocomplete="email" placeholder="you@email.com"></label>
          <label class="full">Service<select name="service"><option value="">Select a service</option>{svc_opts}<option>Something else / not sure</option></select></label>
          <label class="full">Project details<textarea name="message" placeholder="Approximate size, current surface, timeline…"></textarea></label>
          <button class="btn btn-pine full" type="submit">Request My Proposal</button>
        </div>
      </form>
      <p class="qc-alt">Prefer to talk? <a href="{TEL_LINK}">{BUSINESS["phone_display"]}</a></p>
    </div>
  </div>
</div>'''
    svc_cards = ""
    for s in SERVICE_ORDER:
        svc = SERVICES[s]
        svc_cards += f'''<article class="svc-card">
      <div class="svc-num">No. {svc["numeral"]}</div>
      <h3><a href="/{s}/">{svc["name"]}</a></h3>
      <p>{clip_desc(svc["intro_lead"].replace("&mdash;", "—"), 135)}</p>
      <a class="tlink" href="/{s}/">Explore the service</a>
    </article>'''
    t1_tiles = "".join(f'''<a class="area-tile" href="/{c}/"><span class="at-name">{CITIES[c]["name"]}, FL</span><span class="at-meta">{CITIES[c]["county"]} · {" · ".join(CITIES[c]["zips"][:2])}</span></a>''' for c in TIER1)
    t2_tiles = "".join(f'''<a class="area-tile" href="/{c}/"><span class="at-name">{CITIES[c]["name"]}, FL</span><span class="at-meta">{CITIES[c]["county"]}</span></a>''' for c in TIER2)
    posts = ""
    for p in GENERAL_BLOG_POSTS[:3]:
        posts += f'''<article class="post-card">
      <div class="pc-meta"><span>{p["category"]}</span><span>{p["date_modified"][:7]}</span></div>
      <h3><a href="/blog/{p["slug"]}/">{p["title"]}</a></h3>
      <a class="tlink" href="/blog/{p["slug"]}/">Read the guide</a>
    </article>'''
    body = f'''{hero}
{credo_bar()}
<section>
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow">The Catalog</span>
      <h2>Twelve services. One <em>standard</em>.</h2>
      <p class="lede">Concrete, pavers, and natural stone — installed by one crew, under one 48-checkpoint code, with pricing published before you ever call.</p>
    </div>
    <div class="svc-grid">{svc_cards}</div>
  </div>
</section>
{why_us_section()}
{craft_code_section()}
<section class="areas-section">
  <div class="wrap-wide">
    <div class="sect-head">
      <span class="eyebrow">Service Area · 50-Mile Radius</span>
      <h2>Based in Windermere. Building across <em>west Orlando &amp; beyond</em>.</h2>
    </div>
    <div class="tier-label">Core Markets</div>
    <div class="area-grid">{t1_tiles}</div>
    <div class="tier-label">Extended Service Area</div>
    <div class="area-grid">{t2_tiles}</div>
  </div>
</section>
{process_section()}
<section class="snug">
  <div class="wrap">
    {keyfact(CITABLE_LINE)}
    {exclusions_block()}
    {contact_band()}
  </div>
</section>
{faq_section(HOME_FAQS, headline="Before you call — the essentials")}
{reviews_invite()}
<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap-wide">
    <div class="sect-head"><span class="eyebrow">Insights</span><h2>Guides written by the crew, <em>not a content farm</em></h2></div>
    <div class="post-grid">{posts}</div>
    <p style="margin-top:1.6rem"><a class="tlink" href="/blog/">All guides &amp; cost breakdowns</a></p>
  </div>
</section>
{final_cta()}'''
    write_page("index.html",
               head(title, desc, canonical, og_image=f"{SITE}{OG_DEFAULT}", json_ld=schemas,
                    extra_meta='<link rel="preload" as="image" href="/images/concrete-crew-working-hero-v3.webp" fetchpriority="high">\n'),
               header(active="home"), body)
    print("[home] wrote index.html")


if __name__ == "__main__":
    build_home()
