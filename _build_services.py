#!/usr/bin/env python3
"""Windermere Concrete — service hub pages (/[service]/) + service-city pages (/[service]/[city]/, Tier 1)."""
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, TIER1, TEL_LINK, SMS_LINK,
                   COST_PRIORITY_SERVICES, clip_desc)
from _gen import (SITE, head, header, footer, breadcrumbs, write_page, og_url,
                  answer_block, keyfact, CITABLE_LINE, contact_band, final_cta,
                  craft_code_section, faq_section, reviews_invite, pricing_table,
                  options_table, scope_section, honest_note, credo_bar,
                  schema_organization, schema_website, schema_local_business,
                  schema_breadcrumb, schema_faqpage, schema_service, schema_webpage)

PHONE = BUSINESS["phone_display"]


def clip_title(s, n=60):
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0].rstrip(" |,-")


def page_hero(kicker, h1_html, sub_html, facts=None):
    facts = facts or ["Fully Insured", "Free Estimates", "Written Warranty", "ARC / HOA Submittal Support"]
    facts_html = "".join(f"<span>{f}</span>" for f in facts)
    return f'''<div class="page-hero">
  <div class="wrap">
    <span class="eyebrow on-dark">{kicker}</span>
    <h1>{h1_html}</h1>
    <p class="ph-sub">{sub_html}</p>
    <div class="ph-facts">{facts_html}</div>
  </div>
</div>'''


def related_rails(svc_slug=None, city_slug=None):
    """Three rail boxes: other services (here), same service elsewhere, guides."""
    boxes = ""
    if city_slug:
        city = CITIES[city_slug]
        others = [s for s in SERVICE_ORDER if s != svc_slug][:8]
        links = "".join(f'<li><a href="/{s}/{city_slug}/">{SERVICES[s]["short"]} in {city["name"]}</a></li>' for s in others)
        boxes += f'<div class="rail-box"><span class="rb-tag">More in {city["name"]}</span><ul>{links}</ul></div>'
    if svc_slug:
        svc = SERVICES[svc_slug]
        cities = [c for c in TIER1 if c != city_slug][:8]
        links = "".join(f'<li><a href="/{svc_slug}/{c}/">{svc["short"]} in {CITIES[c]["name"]}</a></li>' for c in cities)
        boxes += f'<div class="rail-box"><span class="rb-tag">{svc["short"]} nearby</span><ul>{links}</ul></div>'
    guide_links = ['<li><a href="/blog/pavers-vs-concrete-florida/">Pavers vs. concrete in Florida</a></li>',
                   '<li><a href="/blog/best-pool-deck-material-florida/">Best pool deck material for Florida</a></li>',
                   '<li><a href="/blog/hoa-arc-approval-hardscape-windermere/">Clearing ARC review, first submittal</a></li>',
                   '<li><a href="/blog/why-concrete-cracks-central-florida/">Why Central Florida concrete cracks</a></li>']
    if svc_slug in COST_PRIORITY_SERVICES and city_slug:
        guide_links.insert(0, f'<li><a href="/blog/{svc_slug}-cost-in-{city_slug}-fl-2026/">{SERVICES[svc_slug]["short"]} cost in {CITIES[city_slug]["name"]} (2026)</a></li>')
    boxes += f'<div class="rail-box"><span class="rb-tag">From the Insights desk</span><ul>{"".join(guide_links[:5])}</ul></div>'
    return f'''<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap-wide">
    <div class="sect-head"><span class="eyebrow">Keep Exploring</span><h2>Related pages worth a look</h2></div>
    <div class="rail-grid">{boxes}</div>
  </div>
</section>'''


# ============================================================================
# SERVICE HUB
# ============================================================================
def build_service_hub(slug):
    svc = SERVICES[slug]
    canonical = f"{SITE}/{slug}/"
    plain = svc["short"]
    title = clip_title(f'{plain} Windermere FL | Windermere Concrete')
    desc = clip_desc(svc["intro_lead"].replace("&mdash;", "—").replace("&amp;", "&").replace("&rsquo;", "'") +
                     f" Serving Windermere & west Orlando. Free estimates.")
    crumb_items = [("Home", "/"), ("Services", "/concrete-driveways/"), (svc["name"], None)]
    schemas = [
        schema_organization(), schema_website(),
        schema_local_business(canonical, plain, service=plain, image=og_url(slug)),
        schema_service(svc, canonical=canonical),
        schema_breadcrumb([("Home", SITE + "/"), (plain, canonical)]),
        schema_faqpage(svc["faqs"]),
        schema_webpage(canonical, title, desc),
    ]
    hero = page_hero(f"Service · Windermere &amp; West Orlando", f'{svc["h1_phrase"]} in <em>Windermere, FL</em> &amp; West Orlando',
                     svc["intro_lead"])
    cities_links = " · ".join(f'<a href="/{slug}/{c}/">{CITIES[c]["name"]}</a>' for c in TIER1)
    body = f'''{hero}
{credo_bar()}
<section class="snug">
  <div class="wrap">
    {answer_block(svc["answer_block"])}
    <div class="prose dropcap">
      <p>{svc["craft_p1"]}</p>
      <p>{svc["craft_p2"]}</p>
    </div>
    {keyfact(CITABLE_LINE)}
    {options_table(svc)}
    {contact_band()}
  </div>
</section>
<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap">
    <div class="sect-head"><span class="eyebrow">Transparent Pricing</span><h2>What {plain.lower()} cost in <em>our market</em></h2></div>
    {pricing_table(svc)}
  </div>
</section>
{scope_section(svc)}
{craft_code_section(context=plain.lower())}
<section class="snug">
  <div class="wrap">
    {honest_note(svc)}
  </div>
</section>
{faq_section(svc["faqs"], headline=f"{plain} — the questions we hear")}
{reviews_invite()}
<section class="snug">
  <div class="wrap">
    <div class="sect-head"><span class="eyebrow">City Pages</span><h2>{plain} by <em>city</em></h2>
    <p class="lede">Local pages with neighborhood coverage, terrain notes, and city-specific answers:</p></div>
    <p style="line-height:2.2">{cities_links}</p>
  </div>
</section>
{related_rails(svc_slug=slug)}
{final_cta()}'''
    write_page(f"{slug}/index.html",
               head(title, desc, canonical, og_image=og_url(slug), json_ld=schemas),
               header(active="services"), body,
               breadcrumbs_html=breadcrumbs(crumb_items))


# ============================================================================
# SERVICE-CITY PAGES (Tier 1)
# ============================================================================
def city_answer(svc, city):
    kw = svc["short"].lower()
    main_range = svc["pricing_rows"][0][1]
    return (f'In {city["name"]}, FL, {kw} typically run <strong>{main_range} installed</strong> at 2026 rates. '
            f'{city["terrain_note"]} Windermere Concrete serves {city["name"]} from its Windermere base &mdash; '
            f'same-day reply, written proposal within one business day, fully insured.')


def city_fit_prose(svc, city):
    kw = svc["short"].lower()
    return f'''<div class="prose dropcap">
      <p><strong>{city["name"]}</strong> &mdash; {city["profile"]}</p>
      <p>For {kw} specifically, that local picture translates into how we build. {city["terrain_note"]} Our answer is the same one we give every {city["county"]} property: probe first, base in compacted lifts, engineer the falls, and document the work &mdash; all forty-eight checkpoints of the Windermere Craft Code, applied to your address. Typical demand we see here: {city["demand_note"].lower()}.</p>
      <p>One more local reality worth naming: {city["review_note"]} We prepare the submittal documentation with your proposal, and we schedule work only after the approvals clear &mdash; the sequence that keeps projects friendly with the neighbors and the board.</p>
    </div>'''


def city_svc_faqs(svc, city):
    kw = svc["short"].lower()
    return [
        (f'Do you actually work in {city["name"]}, or just list it?',
         f'{city["profile_short"]} We serve it as a core market from our Windermere base &mdash; close enough for the site visit this week, the written proposal within one business day, and the crew on schedule. Landmarks our trucks know well: {city["landmarks"]}.'),
        (f'How does the ground in {city["name"]} affect {kw}?',
         f'{city["terrain_note"]} That is exactly the class of condition the Craft Code&rsquo;s Ground Truth phase exists for: we probe the subgrade before pricing, correct what we find, compact the base in measured lifts, and photograph it before it disappears under the finished surface.'),
        (f'Will I need a permit or HOA approval in {city["name"]}?',
         f'{city["review_note"]} We flag what your specific project needs during the consultation and prepare the documentation with the proposal &mdash; approvals first, demolition second, always.'),
    ]


def build_service_city(svc_slug, city_slug):
    svc = SERVICES[svc_slug]
    city = CITIES[city_slug]
    canonical = f"{SITE}/{svc_slug}/{city_slug}/"
    plain = svc["short"]
    # "in {city}," differentiates from the hub title ({plain} Windermere FL) — no
    # hub/city title collision, esp. for the Windermere city page itself.
    title = clip_title(f'{plain} in {city["name"]}, FL | Windermere Concrete')
    desc = clip_desc(f'{plain} in {city["name"]}, FL — installed under the 48-checkpoint Windermere Craft Code. '
                     f'{city["profile_short"].replace("&mdash;", "—").replace("&rsquo;", chr(8217))} Free estimates, written proposals.')
    faqs = svc["faqs"][:4] + city_svc_faqs(svc, city)
    schemas = [
        schema_local_business(canonical, f'{plain} in {city["name"]}', city=city["name"], service=plain, image=og_url(svc_slug)),
        schema_service(svc, city=city["name"], canonical=canonical),
        schema_breadcrumb([("Home", SITE + "/"), (plain, f"{SITE}/{svc_slug}/"), (city["name"], canonical)]),
        schema_faqpage(faqs),
        schema_webpage(canonical, title, desc),
    ]
    crumb_items = [("Home", "/"), (svc["name"], f"/{svc_slug}/"), (f'{city["name"]}, FL', None)]
    hero = page_hero(f'{svc["name"]} · {city["county"]}',
                     f'{svc["h1_phrase"]} in <em>{city["name"]}, FL</em>',
                     f'{city["distinction"]}. {svc["intro_lead"]}',
                     facts=["Fully Insured", "Free Estimates", f'Serving all of {city["name"]}', "Written proposal in one business day"])
    body = f'''{hero}
{credo_bar()}
<section class="snug">
  <div class="wrap">
    {answer_block(city_answer(svc, city), tag=f"The Short Answer — {city['name']}")}
    {city_fit_prose(svc, city)}
    {keyfact(CITABLE_LINE)}
    {contact_band(title=f'Ready to look at your {city["name"]} project?')}
  </div>
</section>
<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap">
    <div class="sect-head"><span class="eyebrow">Transparent Pricing</span><h2>{plain} pricing in <em>{city["name"]}</em></h2></div>
    {pricing_table(svc, city_name=city["name"])}
    {options_table(svc)}
  </div>
</section>
{scope_section(svc, city_name=city["name"])}
{craft_code_section(context=f'{city["name"]} {plain.lower()}')}
<section class="snug">
  <div class="wrap">
    {honest_note(svc)}
  </div>
</section>
<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap">
    <div class="sect-head"><span class="eyebrow">Local Coverage</span><h2>Where we work in <em>{city["name"]}</em></h2></div>
    <div class="hood-flow">{"".join(f'<div class="hood">{n}</div>' for n in city["neighborhoods"])}</div>
    <div class="zip-row"><span class="zr-label">ZIPs</span>{"".join(f'<span class="zip-chip">{z}</span>' for z in city["zips"])}</div>
  </div>
</section>
{faq_section(faqs, headline=f'{plain} in {city["name"]} — asked &amp; answered')}
{related_rails(svc_slug=svc_slug, city_slug=city_slug)}
{final_cta(headline=f'Let&rsquo;s walk your {city["name"]} project <em>this week</em>.')}'''
    write_page(f"{svc_slug}/{city_slug}/index.html",
               head(title, desc, canonical, og_image=og_url(svc_slug), json_ld=schemas),
               header(active="services"), body,
               breadcrumbs_html=breadcrumbs(crumb_items))


def build_all():
    n = 0
    for slug in SERVICE_ORDER:
        build_service_hub(slug); n += 1
        for c in TIER1:
            build_service_city(slug, c); n += 1
    print(f"[services] wrote {n} pages ({len(SERVICE_ORDER)} hubs + {len(SERVICE_ORDER) * len(TIER1)} service-city)")


if __name__ == "__main__":
    build_all()
