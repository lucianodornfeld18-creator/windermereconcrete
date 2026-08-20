#!/usr/bin/env python3
"""Windermere Concrete — support pages: about, contact, faq, process, warranty,
financing, privacy, terms, thanks, 404."""
from _data import (BUSINESS, CITIES, SERVICES, SERVICE_ORDER, TIER1, TEL_LINK, SMS_LINK,
                   WA_LINK, CHECKLIST, EXCLUSIONS, clip_desc)
from _gen import (SITE, head, header, breadcrumbs, write_page, OG_DEFAULT,
                  answer_block, keyfact, CITABLE_LINE, contact_band, final_cta,
                  craft_code_section, faq_section, reviews_invite, credo_bar,
                  why_us_section, process_section, exclusions_block,
                  schema_organization, schema_website, schema_local_business,
                  schema_breadcrumb, schema_faqpage, schema_webpage)
from _build_services import page_hero, clip_title

B = BUSINESS


def simple_page(path, title, desc, h1, kicker, body_inner, active="", indexable=True, extra_schemas=None):
    canonical = f"{SITE}/{path}/" if path else f"{SITE}/"
    schemas = [schema_breadcrumb([("Home", SITE + "/"), (h1.replace("<em>", "").replace("</em>", ""), canonical)]),
               schema_webpage(canonical, title, desc)]
    if extra_schemas:
        schemas += extra_schemas
    body = f'''{page_hero(kicker, h1, desc)}
{credo_bar()}
<section class="snug"><div class="wrap">{body_inner}</div></section>
{final_cta()}'''
    write_page(f"{path}/index.html" if path else "index.html",
               head(title, desc, canonical, indexable=indexable, json_ld=schemas),
               header(active=active), body,
               breadcrumbs_html=breadcrumbs([("Home", "/"), (h1.replace("<em>", "").replace("</em>", ""), None)]))


# ---------------------------------------------------------------- ABOUT
def build_about():
    body = f'''
<div class="prose dropcap">
  <p><strong>Windermere Concrete LLC</strong> exists because of a gap we kept watching nobody fill. West Orlando&rsquo;s best neighborhoods &mdash; the Butler Chain communities, the golf-course streets, the historic brick districts &mdash; kept hiring hardscape two ways: metro-wide volume outfits that treat a Windermere motor court like any parking lot, or itinerant crews whose warranty lasts as long as their phone number. Between them sat an unserved standard: <em>estate-grade installation, from a local company, with its process in writing.</em> That is the company we built.</p>
  <p>We are a Service-Area Business based in Windermere, FL 34786, working across a 50-mile radius of west Orlando &mdash; from Dr. Phillips and Horizon West out to the Lake County hills and the Seminole corridor. We deliberately publish what most contractors keep vague: our <a href="/process/">48-checkpoint Craft Code</a>, our <a href="/concrete-driveways/">investment tables</a>, and the exact list of things we <em>don&rsquo;t</em> do. Fully insured, always; free estimates, always; a written workmanship warranty on every surface, always.</p>
  <p>What should you expect if you call? A same-day reply. A site walk where we probe your ground instead of eyeballing it. A written, line-itemized proposal within one business day &mdash; thickness, PSI, base spec, joint plan, all on paper. An ARC submittal package if your community needs one. And after the build: a hose test you watch, a care guide you keep, and a crew that comes back after the first heavy rain to watch the water behave. That last visit costs us an hour and tells you everything about how we intend to be judged.</p>
</div>
{keyfact(CITABLE_LINE)}
{exclusions_block()}
{contact_band(title="Meet us at your property this week.")}'''
    simple_page("about", clip_title("About Windermere Concrete | Estate-Grade Hardscape FL"),
                clip_desc("Windermere Concrete LLC — owner-run concrete, paver & travertine contractor based in Windermere, FL 34786, serving west Orlando. Our story, our standard, and what to expect."),
                "The company behind <em>the Craft Code</em>", "About Us", body, active="about",
                extra_schemas=[schema_organization()])


# ---------------------------------------------------------------- PROCESS
def build_process():
    canonical = f"{SITE}/process/"
    title = clip_title("The Windermere Craft Code — 48-Point Standard")
    desc = clip_desc("The Windermere Craft Code: the 48-checkpoint installation standard behind every driveway, "
                     "pool deck, patio, and paver project we build — published in full, phase by phase.")
    schemas = [schema_breadcrumb([("Home", SITE + "/"), ("The Craft Code", canonical)]),
               schema_webpage(canonical, title, desc)]
    body = f'''{page_hero("Our Standard · Published in Full", "The Windermere <em>Craft Code</em>",
                          "Most contractors describe their quality. We enumerated ours — forty-eight checkpoints across eight phases, verified on every project, with the evidence photographed. This page is the whole code, nothing withheld.")}
{credo_bar()}
<section class="snug">
  <div class="wrap">
    {answer_block("The Windermere Craft Code is a <strong>48-checkpoint installation standard</strong> applied to every project Windermere Concrete builds — eight phases from consultation to a white-glove handover, including subgrade probing, lift-compacted bases, engineered joints, a hose-tested drainage walkthrough, and a written workmanship warranty.")}
    <div class="prose">
      <p>Why publish it? Two reasons. First, accountability: a checklist you can read is a checklist you can hold us to, and we want to be held to it. Second, education: even if you never hire us, these forty-eight lines are a complete map of what separates hardscape that lasts from hardscape that gets redone &mdash; take them to any bidder and ask which ones are included. The contractors worth hiring won&rsquo;t flinch.</p>
    </div>
  </div>
</section>
{craft_code_section()}
{process_section()}
<section class="snug">
  <div class="wrap">
    {keyfact(CITABLE_LINE)}
    {contact_band(title="See the Code applied to your project.")}
  </div>
</section>
{final_cta()}'''
    write_page("process/index.html",
               head(title, desc, canonical, json_ld=schemas),
               header(active="process"), body,
               breadcrumbs_html=breadcrumbs([("Home", "/"), ("The Craft Code", None)]))


# ---------------------------------------------------------------- CONTACT
def build_contact():
    canonical = f"{SITE}/contact/"
    title = clip_title("Contact | Free Estimate — Windermere Concrete FL")
    desc = clip_desc("Request a free estimate from Windermere Concrete — same-day reply, written proposal within "
                     "one business day. Call, text, or send the form. Serving Windermere & west Orlando.")
    schemas = [schema_local_business(canonical, "Contact Windermere Concrete"),
               schema_breadcrumb([("Home", SITE + "/"), ("Contact", canonical)]),
               schema_webpage(canonical, title, desc)]
    svc_opts = "".join(f'<option>{SERVICES[s]["name"].replace("&amp;", "&")}</option>' for s in SERVICE_ORDER)
    city_opts = "".join(f'<option>{CITIES[c]["name"]}</option>' for c in TIER1) + "<option>Another city nearby</option>"
    body = f'''{page_hero("Contact · Same-Day Reply", "Let&rsquo;s look at <em>your project</em>",
                          "Call or text for the fastest answer, or send the form — every inquiry gets a same-day reply and a written, line-itemized proposal within one business day of the site walk.")}
{credo_bar()}
<section class="snug">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:start" class="contact-cols">
      <div>
        <div class="prose">
          <h2>Three ways to reach us</h2>
          <p><strong>Call:</strong> <a href="{TEL_LINK}">{B["phone_display"]}</a> &mdash; the fastest path to a scheduled walk.<br>
          <strong>Text:</strong> <a href="{SMS_LINK}">message us</a> photos of the area and rough dimensions; we&rsquo;ll reply with honest first thoughts.<br>
          <strong>Email:</strong> <a href="mailto:{B["email"]}">{B["email"]}</a></p>
          <h3>What happens after you reach out</h3>
          <ol>
            <li>Same-day reply, real human;</li>
            <li>Site walk scheduled &mdash; usually within days;</li>
            <li>We probe the ground, measure, review ARC rules, match samples;</li>
            <li>Written, line-itemized proposal within one business day;</li>
            <li>You decide, without a follow-up pressure campaign.</li>
          </ol>
          <p style="font-size:.9rem;color:var(--ink-soft)">Service area: Windermere, FL 34786 base &mdash; 50-mile radius across Orange, Lake, Seminole, Osceola &amp; north Polk counties. Hours: Mon&ndash;Fri 7:30&ndash;6:30, Sat 9&ndash;2.</p>
        </div>
      </div>
      <div class="formcard" id="proposal">
        <h2 style="margin-bottom:.4rem">Request your written proposal</h2>
        <p style="font-size:.86rem;color:var(--ink-soft);margin-bottom:1.2rem">Free · no pressure · reply the same day</p>
        <form method="POST" action="{{{{FORM_ENDPOINT}}}}">
          <div class="fgrid">
            <label>Name<input type="text" name="name" required autocomplete="name"></label>
            <label>Phone<input type="tel" name="phone" required autocomplete="tel"></label>
            <label class="full">Email<input type="email" name="email" required autocomplete="email"></label>
            <label>Service<select name="service">{svc_opts}<option>Something else / not sure</option></select></label>
            <label>City<select name="city">{city_opts}</select></label>
            <label class="full">Tell us about the project<textarea name="message" placeholder="Rough size, current surface, what you have in mind…"></textarea></label>
            <button class="btn btn-pine fsubmit" type="submit">Send &mdash; Get My Proposal</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>
<style>@media(max-width:860px){{.contact-cols{{grid-template-columns:1fr!important}}}}</style>
{final_cta()}'''
    write_page("contact/index.html",
               head(title, desc, canonical, json_ld=schemas),
               header(active="contact"), body,
               breadcrumbs_html=breadcrumbs([("Home", "/"), ("Contact", None)]))


# ---------------------------------------------------------------- FAQ (site-wide)
def build_faq():
    faqs = [
        ("Do you charge for estimates?",
         "Never. The site walk, the subgrade probing, the sample matching, and the written line-itemized proposal are all free — and the proposal is yours to compare against anyone. We win work on the specification, not on trapping you in a sales appointment."),
        ("Are you insured?",
         "Fully insured, and we provide the certificate without being asked twice — your HOA, property manager, or gated community's vendor desk can have it the same day. It is a basic credential, and any contractor who hesitates on it is telling you something."),
        ("How far do you travel?",
         "A 50-mile radius from Windermere, FL 34786 — which covers metro Orlando and the surrounding counties. Core markets get the fastest scheduling: Windermere, Dr. Phillips, Horizon West, Winter Garden, Gotha, Oakland, Montverde, Clermont, Winter Park, Maitland, Belle Isle, and Orlando."),
        ("What does the written warranty cover?",
         "Our workmanship — the parts of the project we control: base preparation, structural behavior of the installation, joint and edge systems, and finish application. It is printed, signed, and handed over at the walkthrough with your care guide and cure calendar. Material defects route to the manufacturer warranties, which we register where applicable. Full terms: our warranty page."),
        ("Do you offer financing?",
         "We keep a financing page with current options — for larger scopes like paver driveways and travertine decks, monthly terms often make the correct system affordable instead of the compromised one. Ask during the estimate and we'll walk the choices."),
        ("Who actually shows up to do the work?",
         "Our crew — the same one from stake-out to seal. We don't broker jobs to subcontractors you've never met, and the person who walked your site is reachable throughout the build. Small company, deliberately: the standard survives because the same hands apply it."),
        ("What don't you do?",
         "Foundations, structural or load-bearing slabs, retaining walls over four feet, room additions, pool shells, screen enclosures, and anything else requiring a state general-contractor license. We name it on every service page because pretending otherwise is how homeowners get hurt. Exterior flatwork, pavers, and natural stone — done to an obsessive standard — is the whole business."),
        ("How soon can you start?",
         "The proposal states a real start window, not a guess — it depends on season and scope, and we would rather tell you three honest weeks than a flattering two that slips. Once scheduled, we show up when the calendar says; weather is the only force that moves our dates, and Florida makes us say that out loud."),
    ]
    canonical = f"{SITE}/faq/"
    title = clip_title("FAQ | Windermere Concrete — Straight Answers")
    desc = clip_desc("Straight answers about hiring Windermere Concrete — estimates, insurance, warranty, financing, "
                     "scheduling, service radius, and what we deliberately don't do.")
    schemas = [schema_breadcrumb([("Home", SITE + "/"), ("FAQ", canonical)]),
               schema_faqpage(faqs), schema_webpage(canonical, title, desc)]
    body = f'''{page_hero("FAQ · The Company", "Straight answers, <em>before you call</em>",
                          "Everything homeowners ask about working with us — and the service pages carry their own technical FAQs on top of these.")}
{credo_bar()}
{faq_section(faqs, headline="The company, plainly")}
<section class="snug"><div class="wrap">{contact_band()}</div></section>
{final_cta()}'''
    write_page("faq/index.html",
               head(title, desc, canonical, json_ld=schemas),
               header(active=""), body,
               breadcrumbs_html=breadcrumbs([("Home", "/"), ("FAQ", None)]))


# ---------------------------------------------------------------- WARRANTY
def build_warranty():
    body = f'''
<div class="prose">
  <p>Every surface Windermere Concrete installs leaves with a <strong>signed, written workmanship warranty</strong>. Not a verbal assurance, not a line in an email — a document, handed over at the walkthrough beside your care guide and cure calendar.</p>
  <h2>What it covers</h2>
  <ul>
    <li><strong>Base performance:</strong> settlement, rutting, or heaving traceable to our preparation;</li>
    <li><strong>Structural workmanship:</strong> cracking outside the engineered joint plan on slabs; migration or spreading of properly restrained paver fields;</li>
    <li><strong>Joint &amp; edge systems:</strong> control joints, isolation joints, edge restraint, and polymeric jointing as installed;</li>
    <li><strong>Finish application:</strong> stamped texture, color systems, and sealer application performed to specification.</li>
  </ul>
  <h2>What it honestly can&rsquo;t cover</h2>
  <ul>
    <li>Hairline shrinkage cracking <em>inside</em> control joints (that is the system working — see <a href="/blog/why-concrete-cracks-central-florida/">why concrete cracks</a>);</li>
    <li>Damage from loads beyond the design brief — the dumpster on the patio, the loaded truck on the walkway;</li>
    <li>Acts of ground and sky beyond engineering: floods, sinkhole activity, root systems planted after installation;</li>
    <li>Normal wear of sacrificial layers — sealers are maintenance items with published renewal cycles.</li>
  </ul>
  <p>Claims are simple: call or email with photos, we come look — usually the same week — and warranty work is scheduled like any other job, with the same crew and the same standard. The warranty document you receive states the term for your specific scope; keep it with the job photos we send at handover.</p>
</div>
{keyfact(CITABLE_LINE)}
{contact_band(title="A warranty means the company plans to still be here.")}'''
    simple_page("warranty", clip_title("Written Workmanship Warranty | Windermere Concrete"),
                clip_desc("Every Windermere Concrete installation carries a signed written workmanship warranty — what it covers, what it can't, and how claims actually work."),
                "The warranty, <em>in writing</em>", "Warranty", body)


# ---------------------------------------------------------------- FINANCING
def build_financing():
    body = f'''
<div class="prose">
  <p>Estate-grade hardscape is a capital improvement, and we treat the paying for it as seriously as the building of it. Financing options are available on qualifying projects &mdash; typical uses: paver driveway conversions, travertine pool decks, and full outdoor-living builds where monthly terms make the <em>correct</em> system affordable instead of the compromised one.</p>
  <h2>How it works with us</h2>
  <ol>
    <li>Get the written proposal first &mdash; the number is the number, financed or not; we don&rsquo;t pad quotes to absorb financing costs;</li>
    <li>Tell us you&rsquo;d like terms; we&rsquo;ll walk the current options and lender links at the estimate;</li>
    <li>Approval decisions typically come quickly; work schedules once financing clears alongside any ARC approvals.</li>
  </ol>
  <p><strong>The honest note:</strong> financing is a tool, not a sales tactic. If the smarter move for your budget is phasing the project &mdash; the driveway this season, the pool deck next &mdash; we will say so and design the phases to build on each other. {{{{FINANCING_DETAILS}}}}</p>
</div>
{contact_band(title="Ask about current financing terms at your estimate.")}'''
    simple_page("financing", clip_title("Financing Options | Windermere Concrete FL"),
                clip_desc("Financing for qualifying Windermere Concrete projects — paver driveways, travertine pool decks, and outdoor-living builds. Get the written number first; terms explained at the estimate."),
                "Financing, <em>without theater</em>", "Financing", body)


# ---------------------------------------------------------------- PRIVACY & TERMS
def build_privacy():
    body = f'''
<div class="prose">
  <p><em>Effective date: July 1, 2026 · {B["legal_name"]}</em></p>
  <h2>What we collect</h2>
  <p>When you call, text, email, or submit our contact form, we collect what you provide: name, phone, email, project address or city, and project details. Our website itself sets no marketing cookies of its own; if analytics are enabled, they collect standard anonymous usage data (pages viewed, device type, approximate region).</p>
  <h2>How we use it</h2>
  <p>To respond to your inquiry, prepare your estimate and proposal, schedule and perform work, honor warranties, and send service reminders you&rsquo;d reasonably expect (like sealer renewal windows). We do not sell, rent, or trade your personal information &mdash; to anyone, ever.</p>
  <h2>Who sees it</h2>
  <p>Our small team; service providers strictly as needed to operate (form processing, scheduling, invoicing); and authorities if the law compels it. Nothing else.</p>
  <h2>Your choices</h2>
  <p>Ask what we hold about you, ask us to correct it, or ask us to delete it (subject to records we must keep for warranty and tax purposes) &mdash; one email to <a href="mailto:{B["email"]}">{B["email"]}</a> does any of the three. Opt out of reminders anytime by replying &ldquo;stop.&rdquo;</p>
  <h2>Security &amp; scope</h2>
  <p>Data is stored in reputable, access-controlled systems. This site is served over HTTPS. This policy covers windermereconcrete.com and our direct communications; links to third-party sites carry their own policies. Questions: <a href="mailto:{B["email"]}">{B["email"]}</a>.</p>
</div>'''
    simple_page("privacy-policy", clip_title("Privacy Policy | Windermere Concrete"),
                clip_desc("How Windermere Concrete LLC collects, uses, and protects your information — plainly stated. We never sell personal data."),
                "Privacy, <em>plainly stated</em>", "Privacy Policy", body)


def build_terms():
    body = f'''
<div class="prose">
  <p><em>Effective date: July 1, 2026 · {B["legal_name"]}</em></p>
  <h2>The site</h2>
  <p>windermereconcrete.com is provided as-is for information about our services. Content, pricing tables, and guides reflect typical conditions in our Central Florida service area at publication and are updated periodically; they are honest planning references, not binding offers. Your binding numbers live in your written proposal.</p>
  <h2>Estimates &amp; proposals</h2>
  <p>Estimates are free. Written proposals are firm for the period stated on their face and price the scope described; scope changes, concealed conditions revealed at demolition, and owner-requested additions are documented as written change orders before they bill. We never invoice surprises.</p>
  <h2>Content ownership</h2>
  <p>All site content &mdash; text, tables, the Windermere Craft Code, and imagery &mdash; is the property of {B["legal_name"]}. Reference it with attribution and a link; wholesale copying onto another contractor&rsquo;s site is both prohibited and, frankly, easy to spot.</p>
  <h2>Liability</h2>
  <p>Using this site creates no contractor-client relationship; that begins with a signed proposal. To the extent permitted by Florida law, we are not liable for damages arising from reliance on general site content, third-party links, or service interruptions of the site itself.</p>
  <h2>Governing law</h2>
  <p>These terms are governed by the laws of the State of Florida; venue is Orange County. Questions: <a href="mailto:{B["email"]}">{B["email"]}</a>.</p>
</div>'''
    simple_page("terms", clip_title("Terms of Service | Windermere Concrete"),
                clip_desc("Terms of use for windermereconcrete.com — estimates, proposals, content ownership, and the plain-language rules of the road."),
                "Terms, <em>without the fog</em>", "Terms of Service", body)


# ---------------------------------------------------------------- THANKS + 404
def build_thanks():
    canonical = f"{SITE}/thanks/"
    body = f'''{page_hero("Message Received", "Consider it <em>on our desk</em>",
                          "Your request is in. A real person replies the same business day — usually much sooner. If the project is urgent, the phone is faster:")}
<section class="snug"><div class="wrap" style="text-align:center">
  <a class="btn btn-pine" href="{TEL_LINK}">Call {B["phone_display"]}</a>
  <p style="margin-top:2rem"><a class="tlink" href="/blog/">Read a guide while you wait</a></p>
</div></section>'''
    write_page("thanks/index.html",
               head("Thank You | Windermere Concrete", "Your request was received — same-day reply guaranteed.",
                    canonical, indexable=False),
               header(), body)


def build_404():
    body = f'''{page_hero("404 · Not Found", "This page poured <em>somewhere else</em>",
                          "The address you followed doesn&rsquo;t exist here. The useful routes:")}
<section class="snug"><div class="wrap">
  <ul class="scope-cols" style="max-width:640px">
    <li><a href="/">Homepage</a></li>
    <li><a href="/concrete-driveways/">Concrete driveways</a></li>
    <li><a href="/paver-driveways/">Paver driveways</a></li>
    <li><a href="/travertine-pool-decks/">Travertine pool decks</a></li>
    <li><a href="/windermere/">Service areas</a></li>
    <li><a href="/blog/">Insights &amp; cost guides</a></li>
    <li><a href="/contact/">Contact — free estimate</a></li>
  </ul>
</div></section>'''
    html_head = head("Page Not Found | Windermere Concrete", "That page doesn't exist — here are the useful routes.",
                     f"{SITE}/404.html", indexable=False)
    write_page("404.html", html_head, header(), body)


def build_all():
    build_about(); build_process(); build_contact(); build_faq()
    build_warranty(); build_financing(); build_privacy(); build_terms()
    build_thanks(); build_404()
    print("[pages] wrote about, process, contact, faq, warranty, financing, privacy, terms, thanks, 404")


if __name__ == "__main__":
    build_all()
