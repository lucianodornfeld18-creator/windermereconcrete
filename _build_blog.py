#!/usr/bin/env python3
"""Windermere Concrete — blog: index, 5 flagship guides, 72 per-city cost guides.
Anti-cannibalization: posts target informational cost/comparison intent only and
always link UP to the money pages; they never target a money page's primary keyword."""
from _data import (BUSINESS, CITIES, SERVICES, TIER1, TEL_LINK,
                   GENERAL_BLOG_POSTS, COST_BLOG_POSTS, COST_PRIORITY_SERVICES, clip_desc)
from _gen import (SITE, head, header, breadcrumbs, write_page, og_url, OG_DEFAULT,
                  answer_block, keyfact, CITABLE_LINE, contact_band, final_cta,
                  faq_section, credo_bar, schema_article, schema_breadcrumb,
                  schema_faqpage, schema_webpage)
from _build_services import clip_title

BRAND = BUSINESS["name"]

BYLINE = f'''<div class="byline">
  <div class="by-mark">W</div>
  <div><strong>The {BRAND} Crew</strong><span>Concrete · Pavers · Travertine — Windermere, FL</span></div>
</div>'''


def art_head_meta(post):
    return f'''<div class="art-meta">
    <span class="cat">{post["category"]}</span>
    <span>Published {post["date_published"]}</span>
    <span>Updated {post["date_modified"]}</span>
  </div>'''


def write_post(post, standfirst, body_html, faqs=None, og=None):
    canonical = f'{SITE}/blog/{post["slug"]}/'
    title = clip_title(post["title"].replace("&rsquo;", "'").replace("&amp;", "&").replace("&mdash;", "—"), 62)
    desc = clip_desc(post["meta_desc"])
    schemas = [schema_article(post, canonical, image=og),
               schema_breadcrumb([("Home", SITE + "/"), ("Insights", f"{SITE}/blog/"),
                                  (title, canonical)]),
               schema_webpage(canonical, title, desc)]
    if faqs:
        schemas.append(schema_faqpage(faqs))
    faq_html = ""
    if faqs:
        items = "".join(f'<details><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q, a in faqs)
        faq_html = f'<h2>Questions we hear on this topic</h2><div class="faq-rail">{items}</div>'
    body = f'''<article class="article">
  {art_head_meta(post)}
  <h1>{post["title"]}</h1>
  <p class="standfirst">{standfirst}</p>
  {body_html}
  {faq_html}
  {BYLINE}
  {contact_band()}
</article>'''
    write_page(f'blog/{post["slug"]}/index.html',
               head(title, desc, canonical, og_image=og or f"{SITE}{OG_DEFAULT}",
                    og_type="article", json_ld=schemas),
               header(active="blog"), body,
               breadcrumbs_html="")


# ============================================================================
# COST GUIDES — composed per (service, city); unique via city data + svc angle
# ============================================================================
SVC_COST_ANGLE = {
    "concrete-driveways": {
        "example": ("a typical 600 sq ft two-car driveway", "$5,400&ndash;$8,400 broom-finish; $7,200&ndash;$10,200 as a tear-out-and-replace"),
        "levers": "Demolition findings matter most: what is under the old slab (roots, buried debris, soft fill) decides whether the base line item stays quoted or grows. Finish is the second lever — broom is the budget anchor; exposed aggregate and stamped work carry premiums that buy real curb presence.",
        "redflag": "A driveway quote without slab thickness, PSI, reinforcement type, and joint spacing in writing is not a quote — it is a guess you will be arguing about later.",
    },
    "paver-driveways": {
        "example": ("a typical 600 sq ft paver conversion", "$9,600&ndash;$15,600 including demolition of the builder slab"),
        "levers": "The product tier (standard blends vs. large-format or clay brick) and the base depth do the moving. Vehicle-rated installs need 8&ndash;10 inches of compacted rock — the difference between quotes is usually hiding in that number, not the pavers.",
        "redflag": "If a paver bid doesn&rsquo;t name the base depth, the edge restraint, and the joint sand, the low price is the base you&rsquo;re not getting.",
    },
    "concrete-patios": {
        "example": ("a 300 sq ft entertaining patio", "$2,400&ndash;$3,900 broom-finish; $4,500&ndash;$7,200 stamped"),
        "levers": "Access is the quiet lever: a backyard a truck can reach prices differently from one that needs pumping or wheelbarrow runs. Finish is the loud one — stamped and colored work roughly doubles the broom number and transforms the result.",
        "redflag": "Beware the patio bid with no slope plan. Flat-poured patios pond against the house — and fixing drainage after the pour costs more than the patio did.",
    },
    "concrete-pool-decks": {
        "example": ("a 700 sq ft pool surround", "$4,200&ndash;$7,000 resurfaced; $6,300&ndash;$9,800 rebuilt"),
        "levers": "The resurface-or-replace fork is the whole budget conversation: a structurally sound deck takes a cool-coat system for roughly half the rebuild price. Isolation detailing around the shell and cage adds line items that cheap bids simply omit — until the coping cracks.",
        "redflag": "Any pool-deck quote that doesn&rsquo;t mention isolation joints at the shell and cage track was written by someone who plans to skip them.",
    },
    "travertine-pool-decks": {
        "example": ("an 800 sq ft travertine surround", "$17,500&ndash;$28,000 installed, coping included"),
        "levers": "Stone grade and thickness, sand-set vs. mud-set system, and coping length move the number. Remodels over existing concrete (mud-set) save demolition but demand a sound slab — the inspection decides which system your deck qualifies for.",
        "redflag": "Travertine sealed with a film-forming product clouds and traps moisture. If the bid&rsquo;s sealer line doesn&rsquo;t say &lsquo;breathable&rsquo; or &lsquo;penetrating,&rsquo; ask why.",
    },
    "stamped-concrete": {
        "example": ("a 400 sq ft stamped patio", "$6,000&ndash;$9,600 with two-tone color and sealer"),
        "levers": "Pattern complexity and color system set the premium: integral color plus antiquing release is the two-tone standard; single-color shortcuts read flat and price accordingly. Borders and bands add labor but finish the composition.",
        "redflag": "&lsquo;Stamped&rsquo; bids that skip integral color — planning to paint the surface after — are how gray concrete ends up wearing a costume that peels.",
    },
}


def build_cost_post(post):
    svc = SERVICES[post["service_slug"]]
    city = CITIES[post["city_slug"]]
    angle = SVC_COST_ANGLE[post["service_slug"]]
    kw = post["keyword"]
    rows = "".join(f"<tr><td>{i}</td><td><strong>{a}</strong></td><td>{n}</td></tr>" for i, a, n in svc["pricing_rows"])
    standfirst = (f'What {kw} actually cost in {city["name"]} in 2026 — installed ranges by scope, '
                  f'the local factors that move them, and how to read competing bids like a contractor.')
    ans = (f'In {city["name"]}, FL, {kw} run <strong>{svc["pricing_rows"][0][1]} installed</strong> at 2026 rates, '
           f'with {angle["example"][0]} landing around <strong>{angle["example"][1]}</strong>. '
           f'The ranges below are the same ones published on our service pages — no bait numbers.')
    faqs = [
        (f'Why do {kw} quotes vary so much in {city["name"]}?',
         f'Because the visible surface is identical on every bid and the invisible system is not. {angle["levers"]} When two numbers sit far apart, the difference almost always lives underground — in base depth, compaction, and what happens when demolition finds a surprise.'),
        (f'Does {city["name"]} itself change the price?',
         f'Locally, yes, in two ways. First, ground: {city["terrain_note"]} Second, process: {city["review_note"]} Neither has to inflate your budget — but a bid that ignores both is planning to discover them as change orders.'),
        (f'How do I budget confidently before the site visit?',
         f'Measure your footprint (length &times; width), multiply by the range that matches your scope in the table above, and treat the result as your planning window. Then get the written proposal: ours arrives within one business day of the walk, line-itemized, so the final number is a decision you make — not a surprise you absorb.'),
    ]
    body = f'''{answer_block(ans, tag=f"2026 Cost Snapshot — {city['name']}")}
<h2>The 2026 rate table for {city["name"]}</h2>
<p>These are the working ranges we quote against across {city["county"]} — printed on our <a href="/{post["service_slug"]}/{post["city_slug"]}/">{svc["short"]} in {city["name"]}</a> page as well, because a price you can&rsquo;t see before calling is a negotiation, not a price.</p>
<table>
  <thead><tr><th>Scope</th><th>2026 installed range</th><th>Notes</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
<h2>What moves the number in {city["name"]} specifically</h2>
<p>{city["profile_short"]}</p>
<p>Two local realities shape budgets here more than any brochure factor. The first is the ground itself: {city["terrain_note"]} The second is process: {city["review_note"]} Both get resolved before our proposals are priced — probing during the site walk, submittal documentation with the paperwork — so the number you sign is the number you pay.</p>
<p>{angle["levers"]}</p>
<h2>A worked example</h2>
<p>Take {angle["example"][0]} — the most common request we price in {city["name"]}. At 2026 rates it lands around <strong>{angle["example"][1]}</strong>. Your footprint scales that window directly: measure, multiply, and you have an honest planning budget before anyone visits.</p>
{keyfact(CITABLE_LINE)}
<h2>How to read competing bids</h2>
<p>{angle["redflag"]}</p>
<p>Our advice, even if you never call us: require every bidder to put the system in writing — base depth and compaction method, reinforcement or edge restraint, joint plan, drainage slope, and cure or set protection. The cheapest bid that specifies all five is a real competitor. The cheapest bid that specifies none of them is the most expensive surface you can buy; you just pay the second half later.</p>
<h2>Where to go from here</h2>
<ul>
  <li>Ready for a real number? <a href="/{post["service_slug"]}/{post["city_slug"]}/">{svc["short"]} in {city["name"]}</a> — local page with the full scope, options, and FAQ.</li>
  <li>Comparing systems first? <a href="/blog/pavers-vs-concrete-florida/">Pavers vs. concrete in Florida</a> and <a href="/blog/best-pool-deck-material-florida/">the pool-deck material guide</a>.</li>
  <li>In an HOA community? <a href="/blog/hoa-arc-approval-hardscape-windermere/">How to clear ARC review on the first submittal</a>.</li>
</ul>'''
    write_post(post, standfirst, body, faqs=faqs, og=og_url(post["service_slug"]))


# ============================================================================
# FLAGSHIP GUIDES (5) — original long-form content
# ============================================================================
def guide_pavers_vs_concrete(post):
    standfirst = ("We install both, we warranty both, and we have no margin preference between them — "
                  "which makes this the rare comparison written to be right rather than to sell.")
    faqs = [
        ("Which adds more resale value in Florida — pavers or concrete?",
         "In neighborhoods where pavers are the visual standard (much of Windermere, Dr. Phillips, and the newer master-planned communities), a paver driveway reads as 'correct' to buyers and appraises accordingly; a clean concrete drive is neutral. In neighborhoods where concrete is the norm, a well-finished slab loses nothing. The honest rule: match or exceed your street's standard — exceeding it dramatically rarely returns the premium at sale."),
        ("Can I install pavers over my existing concrete driveway?",
         "Sometimes — thin overlay pavers over a sound slab is a real system — but it is the exception, not the default. Elevation at the garage door and apron usually forces full removal, and a slab that is cracking has already disqualified itself as a base. We assess it honestly during the site walk; most conversions in our market are remove-and-rebuild."),
        ("Which one survives Florida tree roots better?",
         "Pavers, decisively. A root that heaves a slab cracks it permanently; the repair is a saw and a mixer. The same root under pavers lifts a section that can be opened, root-pruned or bridged, and relaid invisibly with the original stones. Under oak canopy — Winter Park, Maitland, College Park — this single factor often decides the whole comparison."),
    ]
    body = f'''{answer_block("For a Florida driveway or patio: <strong>poured concrete wins on installed cost and seamlessness</strong> ($9&ndash;$14/sq ft broom-finish), <strong>pavers win on repairability, looks, and long-run cost of ownership</strong> ($14&ndash;$24/sq ft), and the right answer is usually decided by your neighborhood&rsquo;s standard, your trees, and how long you plan to stay.")}
<h2>The comparison, in one table</h2>
<table>
  <thead><tr><th>Factor</th><th>Poured concrete</th><th>Pavers</th></tr></thead>
  <tbody>
    <tr><td>Installed cost (driveway)</td><td><strong>$9&ndash;$14/sq ft</strong> (broom) · $16&ndash;$26 stamped</td><td>$14&ndash;$24/sq ft · $18&ndash;$30 clay brick</td></tr>
    <tr><td>Repair story</td><td>Patches show; crack repair is visible</td><td><strong>Lift &amp; relay — invisible</strong></td></tr>
    <tr><td>Surface continuity</td><td><strong>Seamless, weed-free</strong></td><td>Joints need sand maintenance</td></tr>
    <tr><td>Root &amp; soil movement</td><td>Cracks when the ground wins</td><td><strong>Flexes; sections re-level</strong></td></tr>
    <tr><td>Maintenance rhythm</td><td>Sealer every ~3 yrs (optional on plain gray)</td><td>Clean-sand-seal every 2&ndash;4 yrs</td></tr>
    <tr><td>HOA/ARC reception</td><td>Approved everywhere; plain in premium areas</td><td><strong>The default standard in most gated communities</strong></td></tr>
    <tr><td>Heat underfoot</td><td>Depends on color; can run hot</td><td>Moderate; travertine runs coolest of all</td></tr>
    <tr><td>Lifespan (built correctly)</td><td>25&ndash;40 years</td><td>30&ndash;50+ years with joint care</td></tr>
  </tbody>
</table>
<h2>Where concrete genuinely wins</h2>
<p><strong>Budget, speed, and seamlessness.</strong> A broom-finish slab is the most surface per dollar in Florida hardscape, full stop. It pours fast, cures predictably, and presents one continuous plane — no joints for weeds, no sand for ants, nothing to re-level. Stamped and colored finishes close most of the aesthetic gap with pavers at a 20&ndash;30% saving. And on rental properties, flip timelines, and budgets that need every square foot, concrete is simply the correct call. We pour it proudly.</p>
<p>Concrete&rsquo;s honest weakness is its repair story. It <em>will</em> crack somewhere, someday — good building controls where (inside a saw-cut joint) rather than whether. When damage goes beyond the joint plan — a root heave, a settled corner, a rogue diagonal — the fix is visible. You live with a patch, or you replace panels.</p>
<h2>Where pavers genuinely win</h2>
<p><strong>Repairability, neighborhood fit, and the long game.</strong> A paver field is hundreds of independent stones on an engineered base: any section that settles, stains, or gets trenched for a utility can be lifted and relaid with the same stones, invisibly. That single property changes the economics over twenty years — a paver driveway is never &lsquo;replaced,&rsquo; only maintained. Around here it also buys belonging: across Windermere, Keene&rsquo;s Pointe, Bay Hill, and the Horizon West villages, pavers are the visual norm and many ARC palettes are written around them.</p>
<p>Pavers&rsquo; honest weakness is the joint system. Sand washes down over years, weeds test the lines, and the field wants a clean-sand-seal cycle every two to four years (<a href="/paver-sealing-repair/">a modest service</a>, but a real one). Skip a decade of it and the &lsquo;maintenance-free&rsquo; myth collects its bill.</p>
<h2>The verdict, by scenario</h2>
<ul>
  <li><strong>Holding the home 10+ years in a paver-standard neighborhood:</strong> pavers — the ownership math and the street agree.</li>
  <li><strong>Budget-first, seamless look, shorter horizon:</strong> broom-finish concrete, sealed, with a real joint plan.</li>
  <li><strong>Design-led patio with stone character at mid budget:</strong> stamped concrete — or split the difference with a paver border on a concrete field.</li>
  <li><strong>Under mature oaks:</strong> pavers, for the root story alone.</li>
  <li><strong>Pool deck:</strong> different contest — <a href="/blog/best-pool-deck-material-florida/">travertine enters and usually wins</a>.</li>
</ul>
{keyfact(CITABLE_LINE)}
<p>Whichever side you land on, the system beneath decides the outcome: probe, base in compacted lifts, engineer the joints or restraints, drain deliberately. Explore the money pages for real scopes and rates: <a href="/concrete-driveways/">concrete driveways</a>, <a href="/paver-driveways/">paver driveways</a>, <a href="/concrete-patios/">concrete patios</a>, <a href="/paver-patios/">paver patios</a>.</p>'''
    write_post(post, standfirst, body, faqs=faqs, og=og_url("paver-driveways"))


def guide_pool_deck_material(post):
    standfirst = ("Barefoot at 3 p.m. in July is the only test that matters. We scored every mainstream "
                  "Florida pool-deck surface against it — plus slip, salt, maintenance, and money.")
    faqs = [
        ("What is genuinely the coolest pool deck surface in Florida?",
         "Travertine, among mainstream options — its porous structure and light mineral color shed heat instead of banking it, and marble runs cooler still. Among budget options, a light-colored cool-coat acrylic over concrete is the surprise performer, engineered specifically to stay walkable. The hottest common choice is dark stamped concrete in full sun; we talk owners out of it weekly."),
        ("Is travertine worth the premium over pavers for a pool deck?",
         "If barefoot temperature, estate aesthetics, or resale positioning in a premium community matter — usually yes; the $6–$10/sq ft premium over concrete pavers buys the coolest surface and the strongest visual. If the deck is shaded, the budget is firm, or the home won't be held long, premium concrete pavers deliver 80% of the result for less. That honest fork is the consultation."),
        ("Can I put travertine or pavers over my existing concrete pool deck?",
         "Often — a mud-set travertine or overlay-paver remodel over a structurally sound slab is one of the most common projects we run in established neighborhoods. Elevations at doors, coping, and cage track decide feasibility, so we measure before we promise. A failing slab disqualifies itself; we tell you which one you own after the straightedge visit."),
    ]
    body = f'''{answer_block("For most Florida pools, <strong>travertine is the best overall deck material</strong> — the coolest mainstream surface underfoot, naturally slip-textured, and the estate standard ($22&ndash;$35/sq ft installed). <strong>Concrete pavers</strong> are the value-premium pick ($15&ndash;$26), and <strong>cool-coat resurfaced concrete</strong> is the budget champion ($6&ndash;$10 over a sound slab).")}
<h2>The scorecard</h2>
<table>
  <thead><tr><th>Surface</th><th>Barefoot heat</th><th>Wet grip</th><th>Salt/chlorine</th><th>Installed cost</th></tr></thead>
  <tbody>
    <tr><td><strong>Travertine</strong></td><td><strong>Coolest mainstream</strong></td><td>Excellent (tumbled)</td><td>Very good, sealed</td><td>$22&ndash;$35/sq ft</td></tr>
    <tr><td>Marble pavers</td><td>Cooler still</td><td>Good (textured grades)</td><td>Good, sealed</td><td>$26&ndash;$38/sq ft</td></tr>
    <tr><td>Shellstone / limestone</td><td>Very cool</td><td>Excellent</td><td>Good, sealed</td><td>$20&ndash;$30/sq ft</td></tr>
    <tr><td>Concrete pavers</td><td>Moderate (color-dependent)</td><td>Very good</td><td>Very good</td><td>$15&ndash;$26/sq ft</td></tr>
    <tr><td>Porcelain pavers</td><td>Moderate</td><td>Grade-dependent</td><td><strong>Immune (zero porosity)</strong></td><td>$18&ndash;$30/sq ft</td></tr>
    <tr><td>Cool-coat acrylic (resurface)</td><td><strong>Best budget performer</strong></td><td>Very good</td><td>Good, renewed</td><td>$6&ndash;$10/sq ft</td></tr>
    <tr><td>Stamped concrete</td><td>Runs hot in dark tones</td><td>Good with grit sealer</td><td>Good, sealed</td><td>$16&ndash;$25/sq ft</td></tr>
  </tbody>
</table>
<h2>Why travertine keeps winning this contest</h2>
<p>The physics are simple and unglamorous: travertine is porous, light-colored stone. The pores interrupt heat transfer and the color reflects solar load, so the surface your feet touch stays dramatically closer to air temperature than dense, dark materials do. Add a tumbled texture that grips wet skin, a French-pattern layout that flatters every architecture from Mediterranean to modern, and a repair story as good as any paver system (lift, relevel, relay), and you have the default surface of Florida&rsquo;s estate pool market. The management cost is a breathable penetrating sealer on a renewal cycle — never a film-former, which clouds the stone. Full scope and rates: <a href="/travertine-pool-decks/">travertine &amp; paver pool decks</a>.</p>
<h2>The value plays</h2>
<p><strong>Concrete pavers</strong> are the strongest cost-to-result ratio for most families: cooler than a slab (in light blends), slip-textured, section-repairable, and available in formats from tumbled cobble to modern plank. <strong>Porcelain</strong> earns its place beside modern architecture and salt systems — zero porosity means chemistry simply doesn&rsquo;t touch it. And for a sound existing deck, <strong>cool-coat acrylic resurfacing</strong> is the honest budget answer: $6&ndash;$10 per square foot for a knock-down texture engineered around barefoot comfort — the classic Florida deck for a reason. Details: <a href="/concrete-pool-decks/">concrete pool decks &amp; resurfacing</a>.</p>
<h2>The two mistakes we keep undoing</h2>
<p><strong>Dark surfaces in full sun.</strong> Charcoal stamped decks photograph beautifully in April and punish feet from June to September. If your deck faces west without shade, weight temperature above aesthetics — or choose a material whose aesthetics don&rsquo;t cost you the afternoon.</p>
<p><strong>Rigid connections to the pool shell.</strong> Whatever the surface, the deck must be isolated from the shell and the cage footer — three structures that move independently. Skip the isolation and the crack arrives at the coping line, the most visible seam on the property. It is checkpoint material in <a href="/process/">our Craft Code</a> because its absence is the most common defect we inherit.</p>
{keyfact(CITABLE_LINE)}
<p>Deciding for your own backyard? Walk it with us — the consultation maps sun, shade, elevations, and budget onto the scorecard above, and the written proposal prices your top two candidates side by side.</p>'''
    write_post(post, standfirst, body, faqs=faqs, og=og_url("travertine-pool-decks"))


def guide_hoa_arc(post):
    standfirst = ("In west Orlando, the committee is part of the job site. Here is how architectural "
                  "review actually works for driveways, pavers, and pool decks — and how to clear it in one pass.")
    faqs = [
        ("How long does ARC approval take for a driveway or paver project?",
         "Plan on two to six weeks in most west Orange communities: committees typically meet monthly, and a complete package submitted just after a meeting waits for the next one. The schedule killer is not the review — it is the incomplete submittal that burns a full cycle on a request for more information. A complete package, first time, is the entire strategy."),
        ("What happens if I build without approval?",
         "The association can require removal or modification at your expense, fine you along the way, and cloud your title with an unresolved violation when you sell. We have seen brand-new paver driveways ordered back to concrete. It is the most expensive shortcut in hardscape — which is why we sequence every project approvals-first, no exceptions."),
        ("Do unincorporated areas like Gotha or Dr. Phillips skip all this?",
         "They skip the HOA layer only where no association exists — county permitting still applies to flatwork in the right-of-way, drainage changes, and accessory pads. Gotha's estate lots are largely HOA-free; most of Dr. Phillips' gated communities are emphatically not. We confirm your address's actual stack — county, city, HOA, or all three — during the consultation."),
    ]
    body = f'''{answer_block("To get hardscape through ARC review in Windermere-area communities: submit a <strong>complete package</strong> — product name and color sample, dimensioned site drawing, drainage note, and contractor insurance certificate — <strong>before any work begins</strong>. Complete first-time submittals routinely clear in one committee cycle (two to six weeks); incomplete ones burn a cycle per missing item.")}
<h2>Why the committee exists (and why it helps your property value)</h2>
<p>Architectural review committees in Isleworth, Keene&rsquo;s Pointe, Bella Collina, Windsong, the Horizon West villages, and Celebration all exist for one reason: the community&rsquo;s visual coherence is a shared asset, priced into every home. The committee&rsquo;s job is to keep your neighbor from expressing himself in orange stamped concrete — and, symmetrically, to make your tasteful upgrade the neighborhood&rsquo;s standard. Treat the ARC as a design partner with a checklist and the process is genuinely smooth. Treat it as an obstacle and it becomes one.</p>
<h2>What committees actually review on hardscape</h2>
<ul>
  <li><strong>Material and color</strong> — many communities publish approved paver blends and finish palettes; the fastest approvals choose from the list.</li>
  <li><strong>Dimensions and coverage</strong> — driveway widening and pads run into lot-coverage and setback rules; the drawing must show them respected.</li>
  <li><strong>Drainage</strong> — increasingly the deciding question: where does the water your new surface sheds actually go? A one-paragraph drainage note answers it before it&rsquo;s asked.</li>
  <li><strong>Visible edges and transitions</strong> — borders, apron tie-ins, and how the new surface meets the street or the neighbor&rsquo;s line.</li>
  <li><strong>Contractor credentials</strong> — proof of insurance, and in gated communities, vendor registration for gate access.</li>
</ul>
<h2>The one-pass submittal package</h2>
<p>This is the package we prepare with every proposal in a reviewed community — the same one that keeps our projects on one-cycle approvals:</p>
<ol>
  <li>Manufacturer product sheet with the exact blend/color named (or a sealed sample tile for stamped and decorative work);</li>
  <li>A dimensioned drawing of the footprint on the lot — existing vs. proposed, setbacks marked;</li>
  <li>Photos of the existing condition;</li>
  <li>The drainage note: slope directions, where runoff discharges, and the statement that flows to neighboring lots are unchanged;</li>
  <li>Contractor insurance certificate and contact block.</li>
</ol>
{keyfact(CITABLE_LINE)}
<h2>Community-flavor notes from the field</h2>
<p><strong>Windermere&rsquo;s estate communities</strong> review at the highest fidelity — expect material samples, and in some cases a site visit. <strong>Horizon West villages</strong> run standardized, portal-based processes with published palettes; fast when the paperwork is exact. <strong>Celebration</strong> is the strictest in Central Florida: the pattern book governs details as fine as apron dimensions, and matching it precisely is the only strategy. <strong>Winter Park&rsquo;s Windsong</strong> and the Vias add the city&rsquo;s tree ordinance on top — root zones shape what can be built at all. We build in all of them, and the sequence never varies: package, approval, then the first saw cut. Related reading: <a href="/blog/pavers-vs-concrete-florida/">choosing the material</a> and <a href="/driveway-extensions/">widening within coverage rules</a>.</p>'''
    write_post(post, standfirst, body, faqs=faqs, og=og_url("paver-driveways"))


def guide_cracks(post):
    standfirst = ("Concrete does not crack because Florida is humid. It cracks because five specific "
                  "shortcuts meet our soil and storms. Here is the failure chain — and where a correct pour breaks it.")
    faqs = [
        ("Is a hairline crack in my new driveway a defect?",
         "Location decides. A hairline inside or along a saw-cut control joint is the system working — the slab shrank, as chemistry requires, and relieved itself exactly where the joint invited it to. A random crack wandering across a panel, a corner dropping, or a joint offsetting vertically is a base or design failure, and on our work it is a warranty conversation, not a shrug."),
        ("Can cracked concrete be repaired, or is replacement inevitable?",
         "Surface-story cracks — stable hairlines, scaling, spalling — repair and resurface well; see our repair service for the honest toolkit. Ground-story cracks — seasonal movers, settled panels, heaves — cannot be fixed from above, because the problem is soil, not slab. The diagnosis visit reads the pattern and tells you which story you own before anyone quotes anything."),
        ("Does fiber mesh or rebar stop cracking?",
         "Neither prevents shrinkage cracking — nothing does; concrete shrinks as it cures. Reinforcement's job is to hold cracks tight and keep panels locked together so hairlines stay hairlines instead of widening into steps and gaps. Joints control where cracks form; reinforcement controls what they become; the base controls whether the ground ever gets a vote. All three, or the warranty is theater."),
    ]
    body = f'''{answer_block("Central Florida concrete cracks for five findable reasons: <strong>uncompacted sandy base, missing or late control joints, slabs poured thin, water trapped at the edges, and cures left to luck</strong>. Every one is preventable at build time — which is why crack prevention is a specification question, not a weather question.")}
<h2>The failure chain, link by link</h2>
<h3>1. The ground moves — and sugar sand forgives nothing</h3>
<p>Our region&rsquo;s deep, fast-draining sands swell and settle with the wet-dry cycle, and any organic pocket under a slab compresses on its own schedule. A slab is only as stable as the prepared base beneath it: subgrade probed, soft zones cut out and rebuilt, crushed rock placed in measured lifts and mechanically compacted, lift by lift. Skip any of that and the ground eventually votes — straight through the surface.</p>
<h3>2. Shrinkage is chemistry — joints are the negotiation</h3>
<p>Curing concrete loses volume; a typical driveway wants to shrink by roughly a joint&rsquo;s width across its length. Control joints are pre-negotiated crack locations: sawed at the right depth, on the right spacing, within the right hours after the pour. Cut them late, shallow, or sparse, and the slab negotiates for itself — diagonally, across the middle, permanently.</p>
<h3>3. Thin slabs and absent steel</h3>
<p>Four inches of reinforced concrete carries cars; the moment the slab thins to 3&Prime; (a classic hidden bid-cut) or the reinforcement drops out, every load becomes a flex test. Fiber, wire, or chaired rebar doesn&rsquo;t prevent cracks — it holds them tight, keeping panels interlocked so hairlines never become steps.</p>
<h3>4. Water at the edges</h3>
<p>An inch-an-hour Florida storm finds every drainage mistake. Slabs pitched wrong pond water against their own edges, softening the base at the perimeter — which is why edge settlement is the most common failure geometry in the metro. Falls must be designed, and then verified: we hose-test drainage at handover, with the owner watching.</p>
<h3>5. The cure nobody supervised</h3>
<p>Concrete gains strength by hydration, not drying. Fresh slabs left to bake lose surface water too fast and craze; slabs rained on too early scar. Curing compound or wet-cure protection, plus a printed traffic calendar, is the cheap insurance most failures skipped.</p>
{keyfact(CITABLE_LINE)}
<h2>What to demand in any bid (including ours)</h2>
<ul>
  <li>Base spec in writing: excavation depth, rock type, lift thickness, compaction method;</li>
  <li>Slab thickness and mix strength (PSI) on the proposal;</li>
  <li>Reinforcement named — fiber, wire, or rebar, and how it&rsquo;s supported;</li>
  <li>Joint plan: spacing, depth, and cut timing;</li>
  <li>Cure method and traffic calendar;</li>
  <li>Drainage slope and a verification step.</li>
</ul>
<p>Six lines. Any contractor unwilling to write them is quoting you a surface, not a system. Ours are printed on every proposal — see <a href="/concrete-driveways/">driveways</a>, <a href="/concrete-patios/">patios</a>, and <a href="/concrete-repair-resurfacing/">repair &amp; resurfacing</a> for the scopes, or <a href="/process/">the Craft Code</a> for all forty-eight checkpoints.</p>'''
    write_post(post, standfirst, body, faqs=faqs, og=og_url("concrete-driveways"))


def guide_sealing_schedule(post):
    standfirst = ("The difference between pavers that age like stone and pavers that age like neglect "
                  "is a calendar. Here is the honest Florida maintenance schedule — dates, costs, and what each step actually does.")
    faqs = [
        ("Can I just pressure-wash my pavers myself?",
         "You can wash the surface — carefully, at moderate pressure, fanning the nozzle — but the rental-washer ritual is how most joint systems die: high pressure blasts the sand out of the lines, and without re-sanding afterward the field loses its interlock, invites weeds, and starts shifting. If you DIY the wash, budget for professional re-sanding behind it. The clean is cosmetic; the joints are structural."),
        ("What's the difference between natural, enhanced, and wet-look sealers?",
         "Protection is similar; the finish is the choice. Natural disappears — the field looks unsealed but sheds stains. Enhanced deepens color like a stone that just got rained on, the most popular pick for faded fields. Wet-look adds gloss on top of the enrichment — dramatic on dark blends, divisive on light ones. We carry samples wet and dry, because the same product reads differently on your pavers than on a brochure."),
        ("My pavers are only two years old. Do I really need to do anything yet?",
         "One thing, and it matters: the first sealing, if it wasn't done at install (after the 60–90 day efflorescence window). Sealing early in a field's life slows UV fade before it starts and hardens the joints from year one — it is the cheapest year of ownership and the highest-leverage one. After that, you inherit the normal two-to-four-year rhythm."),
    ]
    body = f'''{answer_block("In Florida, plan to <strong>clean, re-sand, and seal pavers every 2&ndash;4 years</strong> — toward 2 for full-sun driveways and pool decks, toward 4 for shaded patios. The full professional cycle runs <strong>$1.50&ndash;$3.50 per square foot</strong> and takes one to two days. The tell-tales that you&rsquo;re due: low joint sand, germinating weeds, and rain soaking dark instead of beading.")}
<h2>The Florida paver calendar</h2>
<table>
  <thead><tr><th>Interval</th><th>Task</th><th>Typical cost</th></tr></thead>
  <tbody>
    <tr><td>As needed</td><td>Rinse; spot-treat spills, rust, leaf tannin</td><td>DIY / minimal</td></tr>
    <tr><td>60&ndash;90 days after install</td><td><strong>First sealing</strong> (after efflorescence breathes out)</td><td>$1.50&ndash;$3/sq ft</td></tr>
    <tr><td>Every 2&ndash;4 years</td><td><strong>Full cycle:</strong> deep clean &rarr; re-sand &rarr; seal</td><td>$1.50&ndash;$3.50/sq ft</td></tr>
    <tr><td>When noticed</td><td>Lift &amp; relay settled sections; edge-restraint retrofit</td><td>$8&ndash;$18/sq ft (local)</td></tr>
  </tbody>
</table>
<h2>What each step actually does</h2>
<h3>The clean is chemistry, not just pressure</h3>
<p>Florida grows a black mold-mildew film in shade, drops rust from irrigation and furniture, and stains with oak tannin — three different problems with three different treatments. A correct clean pairs moderate pressure with targeted chemistry, then lets the field dry fully before anything else happens. Aggressive pressure alone whitens the surface by eroding it — and empties the joints, which is the beginning of the end.</p>
<h3>Polymeric sand is the structure</h3>
<p>Joint sand is not cosmetic. Hardened polymeric sand locks hundreds of stones into one load-sharing mat, denies weeds a seedbed, and closes the ant highways. Re-sanding drives fresh sand fully into cleared joints, compacts it, and activates it with a metered wetting — the step where amateur jobs fail in both directions (too dry never sets; too wet hazes the face).</p>
<h3>The sealer is the sunscreen</h3>
<p>UV fades pigment and rain feeds the joints&rsquo; enemies; a quality sealer slows both while making every future cleaning easier. Finish is your only real decision — natural, enhanced, or wet-look — and pool decks get a slip additive blended in, grip without haze. On travertine and natural stone the chemistry changes entirely: pH-neutral cleaners and breathable penetrating sealers only, which is why stone and pavers should never share one quote line.</p>
{keyfact(CITABLE_LINE)}
<h2>The economics, plainly</h2>
<p>A 600-square-foot paver driveway costs roughly <strong>$900&ndash;$2,100 per maintenance cycle</strong> — call it $300&ndash;$700 a year amortized. Rebuilding the same driveway after a decade of neglect costs <strong>$9,000&ndash;$15,000</strong>. The calendar is the whole game, which is why we log every job&rsquo;s date and send the reminder when a surface enters its window. Full scope and rates: <a href="/paver-sealing-repair/">paver sealing, cleaning &amp; repair</a> — and if the field is past rescue, we&rsquo;ll say so plainly and price the honest alternative: <a href="/paver-driveways/">a rebuild done right</a>.</p>'''
    write_post(post, standfirst, body, faqs=faqs, og=og_url("paver-sealing-repair"))


GUIDE_BUILDERS = {
    "pavers_vs_concrete": guide_pavers_vs_concrete,
    "pool_deck_material": guide_pool_deck_material,
    "hoa_arc": guide_hoa_arc,
    "cracking": guide_cracks,
    "sealing_schedule": guide_sealing_schedule,
}


# ============================================================================
# BLOG INDEX
# ============================================================================
def build_index():
    canonical = f"{SITE}/blog/"
    title = "Insights — Concrete & Paver Guides | Windermere Concrete"
    desc = clip_desc("Honest guides and 2026 cost breakdowns from a working Windermere, FL crew — pavers vs concrete, "
                     "pool deck materials, ARC approval, and city-by-city pricing across west Orlando.")
    schemas = [schema_breadcrumb([("Home", SITE + "/"), ("Insights", canonical)]),
               schema_webpage(canonical, title, desc)]
    cards = ""
    for p in GENERAL_BLOG_POSTS:
        cards += f'''<article class="post-card">
      <div class="pc-meta"><span>{p["category"]}</span><span>{p["date_modified"][:7]}</span></div>
      <h3><a href="/blog/{p["slug"]}/">{p["title"]}</a></h3>
      <a class="tlink" href="/blog/{p["slug"]}/">Read the guide</a>
    </article>'''
    cost_secs = ""
    for svc_slug in COST_PRIORITY_SERVICES:
        svc = SERVICES[svc_slug]
        links = " · ".join(
            f'<a href="/blog/{svc_slug}-cost-in-{c}-fl-2026/">{CITIES[c]["name"]}</a>' for c in TIER1)
        cost_secs += f'''<div style="padding:14px 0;border-bottom:1px dashed var(--hairline)">
      <strong style="font-family:var(--disp);color:var(--lake)">{svc["short"]} cost guides:</strong>
      <span style="line-height:2"> {links}</span>
    </div>'''
    body = f'''<div class="page-hero">
  <div class="wrap">
    <span class="eyebrow on-dark">Insights · Written by the crew</span>
    <h1>Guides, comparisons &amp; <em>real 2026 pricing</em></h1>
    <p class="ph-sub">No content-farm filler. Every guide here is written from the seat of the skid steer — material comparisons we actually install, cost tables we actually quote against, and the process notes that keep projects out of trouble.</p>
  </div>
</div>
{credo_bar()}
<section class="snug">
  <div class="wrap-wide">
    <div class="sect-head"><span class="eyebrow">Flagship Guides</span><h2>Start with the <em>big five</em></h2></div>
    <div class="post-grid">{cards}</div>
  </div>
</section>
<section class="snug" style="background:var(--pine-wash)">
  <div class="wrap">
    <div class="sect-head"><span class="eyebrow">Cost Library · 2026</span><h2>City-by-city <em>cost breakdowns</em></h2>
    <p class="lede">Every priority service, priced honestly for each of our twelve core cities:</p></div>
    {cost_secs}
  </div>
</section>
{final_cta(headline="Skip the reading — get the <em>written number</em> instead.")}'''
    write_page("blog/index.html",
               head(title, desc, canonical, json_ld=schemas),
               header(active="blog"), body,
               breadcrumbs_html=breadcrumbs([("Home", "/"), ("Insights", None)]))


def build_all():
    build_index()
    for p in GENERAL_BLOG_POSTS:
        GUIDE_BUILDERS[p["topic"]](p)
    for p in COST_BLOG_POSTS:
        build_cost_post(p)
    print(f"[blog] wrote 1 index + {len(GENERAL_BLOG_POSTS)} guides + {len(COST_BLOG_POSTS)} cost posts")


if __name__ == "__main__":
    build_all()
