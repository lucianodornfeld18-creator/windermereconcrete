#!/usr/bin/env python3
"""Windermere Concrete — city hub pages (/[city]/) for all 24 Tier-1 + Tier-2 cities."""
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, TIER1, TIER2, TEL_LINK, clip_desc)
from _gen import (SITE, head, header, breadcrumbs, write_page, og_url, OG_DEFAULT,
                  answer_block, keyfact, CITABLE_LINE, contact_band, final_cta,
                  craft_code_section, faq_section, reviews_invite, credo_bar,
                  neighborhoods_section, schema_local_business, schema_breadcrumb,
                  schema_faqpage, schema_webpage)
from _build_services import page_hero, clip_title

DRIVE = SERVICES["concrete-driveways"]
PAVER = SERVICES["paver-driveways"]
TRAV = SERVICES["travertine-pool-decks"]


def city_services_grid(city):
    """Tier-1 cities link to /svc/city/; Tier-2 to the hubs."""
    is_t1 = city["slug"] in TIER1
    cards = ""
    for s in SERVICE_ORDER:
        svc = SERVICES[s]
        href = f"/{s}/{city['slug']}/" if is_t1 else f"/{s}/"
        cards += f'''<article class="svc-card">
      <div class="svc-num">No. {svc["numeral"]}</div>
      <h3><a href="{href}">{svc["name"]}</a></h3>
      <p>{clip_desc(svc["intro_lead"].replace("&mdash;", "—"), 130)}</p>
      <a class="tlink" href="{href}">{"In " + city["name"] if is_t1 else "Explore the service"}</a>
    </article>'''
    return f'''<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap-wide">
    <div class="sect-head"><span class="eyebrow">Full Catalog · {city["name"]}</span>
    <h2>Every service we bring to <em>{city["name"]}</em></h2></div>
    <div class="svc-grid">{cards}</div>
  </div>
</section>'''


def city_faqs(city):
    name = city["name"]
    return [
        (f'Which concrete and paver services do {name} homeowners request most?',
         f'{city["demand_note"]}. Those patterns follow the housing stock: {city["profile_short"]} Whatever the project, it runs through the same 48-checkpoint Windermere Craft Code &mdash; probe, base, build, hose-test, warranty.'),
        (f'What do driveways and patios cost in {name}?',
         f'At 2026 rates in {name}: broom-finish concrete driveways run {DRIVE["pricing_rows"][0][1]} installed and paver driveways {PAVER["pricing_rows"][0][1]}; concrete patios start around {SERVICES["concrete-patios"]["pricing_rows"][0][1]}, and travertine pool decks run {TRAV["pricing_rows"][0][1]}. Every service page on this site publishes its full investment table, and your written proposal pins the exact number line by line.'),
        (f'Is {name} really inside your service area?',
         f'Yes &mdash; {name} sits well inside the 50-mile radius we serve from our Windermere, FL 34786 base. {city["distinction"]}. We reply the same day, walk the site within days, and deliver a written proposal within one business day of the visit.'),
        (f'What should I know about {name}&rsquo;s soil and drainage before building?',
         f'{city["terrain_note"]} It is the first thing we check, not the last: the Craft Code&rsquo;s Ground Truth phase probes the subgrade and maps the fall lines before anything is priced, so the proposal reflects your lot &mdash; not a template.'),
        (f'Do I need permits or HOA approval for hardscape work in {name}?',
         f'{city["review_note"]} We prepare the submittal documentation as part of every proposal and sequence the work approvals-first. It is the difference between a smooth project and a stop-work letter, and it costs you nothing extra.'),
        (f'Why hire a Windermere-based contractor for a {name} project?',
         f'Because proximity plus standard beats either alone. We are minutes away, not a metro-wide franchise routing you to whichever crew is free &mdash; and every project, in every city we serve, is verified against the same 48 checkpoints, documented with photos, and closed with a written workmanship warranty and a post-rain follow-up.'),
    ]


def related_cities_rail(city):
    order = TIER1 + TIER2
    idx = order.index(city["slug"])
    near = [order[(idx + k) % len(order)] for k in range(1, 7)]
    links = "".join(f'<li><a href="/{c}/">Concrete &amp; pavers in {CITIES[c]["name"]}, FL</a></li>' for c in near)
    is_t1 = city["slug"] in TIER1
    svc_links = "".join(
        f'<li><a href="/{s}/{city["slug"] + "/" if is_t1 else ""}">{SERVICES[s]["short"]}{" in " + city["name"] if is_t1 else ""}</a></li>'
        for s in ["concrete-driveways", "paver-driveways", "travertine-pool-decks", "concrete-pool-decks", "stamped-concrete"])
    guides = ('<li><a href="/blog/pavers-vs-concrete-florida/">Pavers vs. concrete in Florida</a></li>'
              '<li><a href="/blog/best-pool-deck-material-florida/">Best pool deck material for Florida heat</a></li>'
              '<li><a href="/blog/hoa-arc-approval-hardscape-windermere/">Clearing ARC review the first time</a></li>'
              '<li><a href="/blog/paver-cleaning-sealing-schedule-florida/">The real Florida paver sealing schedule</a></li>')
    return f'''<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap-wide">
    <div class="sect-head"><span class="eyebrow">Keep Exploring</span><h2>Nearby cities &amp; useful reading</h2></div>
    <div class="rail-grid">
      <div class="rail-box"><span class="rb-tag">Top services here</span><ul>{svc_links}</ul></div>
      <div class="rail-box"><span class="rb-tag">Nearby service areas</span><ul>{links}</ul></div>
      <div class="rail-box"><span class="rb-tag">From the Insights desk</span><ul>{guides}</ul></div>
    </div>
  </div>
</section>'''


def build_city(slug):
    city = CITIES[slug]
    canonical = f"{SITE}/{slug}/"
    title = clip_title(f'Concrete & Pavers {city["name"]} FL | Windermere Concrete')
    desc = clip_desc(f'Concrete, paver & travertine contractor in {city["name"]}, FL — driveways, pool decks, patios '
                     f'& hardscape built under a 48-checkpoint standard. Free estimates, written proposals, fully insured.')
    faqs = city_faqs(city)
    schemas = [
        schema_local_business(canonical, f'Concrete & Pavers in {city["name"]}', city=city["name"]),
        schema_breadcrumb([("Home", SITE + "/"), ("Service Areas", f"{SITE}/windermere/"), (f'{city["name"]}, FL', canonical)]),
        schema_faqpage(faqs),
        schema_webpage(canonical, title, desc),
    ]
    crumbs = [("Home", "/"), ("Service Areas", "/windermere/"), (f'{city["name"]}, FL', None)]
    ans = (f'Windermere Concrete installs concrete driveways, paver systems, travertine pool decks, patios, and '
           f'walkways throughout <strong>{city["name"]}, FL ({", ".join(city["zips"])})</strong>. '
           f'{city["distinction"]}. Typical work here: {city["demand_note"].lower()}. Free estimates &mdash; '
           f'written proposal within one business day.')
    hero = page_hero(f'Service Area · {city["county"]}',
                     f'Concrete, Pavers &amp; Travertine in <em>{city["name"]}, FL</em>',
                     city["profile_short"],
                     facts=["Fully Insured", "Free Estimates", f'{city["population"]}', "48-Checkpoint Craft Code"])
    body = f'''{hero}
{credo_bar()}
<section class="snug">
  <div class="wrap">
    {answer_block(ans, tag=f"Serving {city['name']} — The Short Version")}
    <div class="prose dropcap">
      <p>{city["profile"]}</p>
      <p><strong>The ground rules here:</strong> {city["terrain_note"]} And the paperwork rules: {city["review_note"]} Both are handled inside our process &mdash; probing and drainage mapping in the Craft Code&rsquo;s Ground Truth phase, and submittal documentation prepared with every proposal.</p>
    </div>
    {keyfact(CITABLE_LINE)}
    {contact_band(title=f'Planning a project in {city["name"]}?')}
  </div>
</section>
{city_services_grid(city)}
{craft_code_section(context=f'{city["name"]}')}
{neighborhoods_section(city)}
{faq_section(faqs, headline=f'{city["name"]} homeowners ask us')}
{reviews_invite()}
{related_cities_rail(city)}
{final_cta(headline=f'{city["name"]}, let&rsquo;s build something that <em>outlasts the mortgage</em>.')}'''
    write_page(f"{slug}/index.html",
               head(title, desc, canonical, og_image=f"{SITE}{OG_DEFAULT}", json_ld=schemas),
               header(active="areas"), body,
               breadcrumbs_html=breadcrumbs(crumbs))


def build_all():
    for slug in TIER1 + TIER2:
        build_city(slug)
    print(f"[cities] wrote {len(TIER1) + len(TIER2)} city pages")


if __name__ == "__main__":
    build_all()
