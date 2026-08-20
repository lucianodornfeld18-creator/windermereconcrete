#!/usr/bin/env python3
"""
Windermere Concrete — Master Data Module
Concrete, paver & travertine contractor · Service-Area Business · Windermere FL 34786.
Service entries live in _svc_part1..4.py; city entries in _cities_part1..4.py.
Imported by _gen.py and every _build_*.py script.

NON-NEGOTIABLE CONSTRAINTS (build brief):
  * NEW business — NEVER invent reviews, ratings, stats, years, or testimonials.
    Unknowns are clearly-labeled {{PLACEHOLDERS}} listed in WHAT-I-NEED-FROM-YOU.md.
  * NEVER print a street address (SAB — city + ZIP context only).
  * NEVER mention any license or license number. "Fully Insured" / "Free Estimates" only.
  * ZERO copy shared with ocoeeconcrete.com or lakewoodranchconcretefl.com.
"""


# ============================================================================
# META-DESCRIPTION HELPER — word-boundary trim for the 130–158 char window.
# ============================================================================
def clip_desc(s, n=156):
    s = " ".join(str(s).split())
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(" ,;·–-") + "…"


# ============================================================================
# BUSINESS IDENTITY — placeholders for everything the owner must supply.
# ============================================================================
BUSINESS = {
    "name": "Windermere Concrete",
    "legal_name": "Windermere Concrete LLC",
    "domain": "windermereconcrete.com",
    # ---- Owner-supplied contact details ----
    "phone": "+16894076658",
    "phone_display": "(689) 407-6658",
    "phone_tel": "+16894076658",
    "email": "hello@windermereconcrete.com",
    # ---- Remaining placeholders (see WHAT-I-NEED-FROM-YOU.md) ----
    "year_founded": "{{YEAR}}",
    "rating": "{{RATING}}",
    "review_count": "{{REVIEW_COUNT}}",
    "unique_stat_full": "{{UNIQUE_STAT}}",
    # ---- Fixed / safe to publish ----
    "street": "",                          # SAB — address HIDDEN, never printed
    "city": "Windermere",
    "city_slug": "windermere",
    "state": "FL",
    "state_long": "Florida",
    "zip": "34786",
    "county": "Orange County",
    "country": "US",
    "lat": "28.4953",
    "lng": "-81.5348",
    "tagline": "Finished to estate standard.",
    "tagline_long": "Windermere&rsquo;s concrete, paver &amp; travertine specialists &mdash; estate-grade driveways, pool decks, patios, and hardscape for the Butler Chain communities and greater west Orlando.",
    "checklist_name": "The Windermere Craft Code",
    "checklist_points": 48,
    "guarantee": "A signed workmanship warranty accompanies every surface we install.",
    "response_time": "Same-day reply &mdash; written proposal within one business day.",
    "arc_promise": "ARC / HOA submittal support included on every estimate.",
    # ---- Profiles (fill when live) ----
    "google_profile": "{{GOOGLE_PROFILE_URL}}",
    "google_review_url": "{{GOOGLE_REVIEW_URL}}",
    "facebook": "{{FACEBOOK_URL}}",
    "instagram": "{{INSTAGRAM_URL}}",
    "yelp": "",
    "thumbtack": "",
    "angi": "",
    "houzz": "",
    "pinterest": "",
    "bbb": "",
    "hours": [
        ("Monday", "07:30", "18:30"),
        ("Tuesday", "07:30", "18:30"),
        ("Wednesday", "07:30", "18:30"),
        ("Thursday", "07:30", "18:30"),
        ("Friday", "07:30", "18:30"),
        ("Saturday", "09:00", "14:00"),
        ("Sunday", "Closed", "Closed"),
    ],
    # Engine toggles — NEW business has no reviews/ratings yet.
    "has_reviews": False,
}

# Contact links
WA_LINK = "https://wa.me/16894076658?text=Hello%20Windermere%20Concrete%20%E2%80%94%20I%27d%20like%20a%20written%20proposal."
SMS_LINK = f"sms:{BUSINESS['phone']}?body=Hello%20Windermere%20Concrete%20%E2%80%94%20I%27d%20like%20a%20written%20proposal."
TEL_LINK = f"tel:{BUSINESS['phone']}"


# ============================================================================
# CITIES — merged from part files, ordered by tier.
# ============================================================================
from _cities_part1 import CITIES as _c1
from _cities_part2 import CITIES as _c2
from _cities_part3 import CITIES as _c3
from _cities_part4 import CITIES as _c4
CITIES = {**_c1, **_c2, **_c3, **_c4}

TIER1 = [
    "windermere", "dr-phillips", "horizon-west", "winter-garden", "gotha", "oakland",
    "montverde", "clermont", "orlando", "winter-park", "maitland", "belle-isle",
]
TIER2 = [
    "lake-nona", "celebration", "kissimmee", "st-cloud", "davenport", "champions-gate",
    "minneola", "groveland", "oviedo", "lake-mary", "sanford", "altamonte-springs",
]
CITY_ORDER = TIER1 + TIER2
CITIES = {k: CITIES[k] for k in CITY_ORDER if k in CITIES}

# Anti-cannibalization vs ocoeeconcrete.com: these appear ONLY in areaServed
# schema / prose mentions — never as dedicated pages.
AREASERVED_ONLY = ["Ocoee", "Apopka", "Winter Springs", "Casselberry", "Edgewood"]


# ============================================================================
# SERVICES — 12 hubs (merged from service part files)
# ============================================================================
from _svc_part1 import SERVICES as _s1
from _svc_part2 import SERVICES as _s2
from _svc_part3 import SERVICES as _s3
from _svc_part4 import SERVICES as _s4
SERVICES = {**_s1, **_s2, **_s3, **_s4}

SERVICE_ORDER = [
    "concrete-driveways", "concrete-patios", "concrete-pool-decks", "stamped-concrete",
    "concrete-slabs", "concrete-repair-resurfacing", "sidewalks-walkways",
    "paver-driveways", "paver-patios", "travertine-pool-decks",
    "paver-sealing-repair", "driveway-extensions",
]
SERVICES = {k: SERVICES[k] for k in SERVICE_ORDER if k in SERVICES}

SERVICE_GROUPS = [
    ("Concrete", ["concrete-driveways", "concrete-patios", "concrete-pool-decks",
                  "stamped-concrete", "concrete-slabs", "concrete-repair-resurfacing",
                  "sidewalks-walkways"]),
    ("Pavers &amp; Travertine", ["paver-driveways", "paver-patios", "travertine-pool-decks",
                                 "paver-sealing-repair", "driveway-extensions"]),
]

# Services that get a per-city cost guide on the blog (quality over quantity)
COST_PRIORITY_SERVICES = [
    "concrete-driveways", "paver-driveways", "concrete-patios",
    "concrete-pool-decks", "travertine-pool-decks", "stamped-concrete",
]


# ============================================================================
# THE WINDERMERE CRAFT CODE — 48 checkpoints (8 phases × 6). Unique to this
# brand: different name, number, phase structure, and wording vs both sisters.
# ============================================================================
CHECKLIST = {
    "name": "The Windermere Craft Code",
    "points": 48,
    "phases": [
        {
            "roman": "I",
            "title": "Consultation &amp; Design Fit",
            "items": [
                "Walk the property with the owner and map the exact footprint",
                "Match material, color, and finish samples to the home&rsquo;s architecture",
                "Review community ARC / HOA design standards before anything is priced",
                "Photograph existing surfaces, elevations, and tie-in points",
                "Identify pool cages, lanais, and structures the new surface must respect",
                "Deliver a written, line-itemized proposal within one business day",
            ],
        },
        {
            "roman": "II",
            "title": "Ground Truth",
            "items": [
                "Probe the subgrade for organics, muck pockets, and loose fill",
                "Trace irrigation, low-voltage lighting, and utility runs before digging",
                "Establish fall lines so every surface sheds water away from the home",
                "Confirm setbacks and easements against the plat where applicable",
                "Plan equipment access to protect lawns, gates, and driveways",
                "Stake and string the final layout for owner sign-off",
            ],
        },
        {
            "roman": "III",
            "title": "Demolition &amp; Excavation",
            "items": [
                "Saw-cut clean separation lines before any breakout begins",
                "Remove existing concrete or pavers and haul debris the same day",
                "Excavate to the engineered depth for the specified system",
                "Undercut soft zones and rebuild them with structural fill",
                "Protect adjacent surfaces, borders, and plantings during removal",
                "Re-verify grades after excavation, before base goes in",
            ],
        },
        {
            "roman": "IV",
            "title": "Base Engineering",
            "items": [
                "Place crushed base rock in measured lifts &mdash; never one dump",
                "Compact each lift mechanically and check with a probe rod",
                "Screed the setting bed (sand or concrete) to uniform depth",
                "Install geotextile separation where soils demand it",
                "Hold positive slope through the base, not just the surface",
                "Document the finished base with photos before covering it",
            ],
        },
        {
            "roman": "V",
            "title": "Forming &amp; Reinforcement",
            "items": [
                "Set forms to string lines and verify diagonals on rectangles",
                "Place reinforcement &mdash; fiber mix, wire, or rebar &mdash; per the proposal",
                "Chair steel to ride mid-slab, never resting on grade",
                "Lay out control-joint positions before the truck is scheduled",
                "Isolate the new work from the house, pool shell, and footers",
                "Final pre-pour inspection signed off by the crew lead",
            ],
        },
        {
            "roman": "VI",
            "title": "Placement &amp; Finish",
            "items": [
                "Confirm mix design and PSI on the ticket before discharge",
                "Screed, bull-float, and finish within the working window",
                "Apply the specified texture &mdash; broom, stamp, trowel, or exposed",
                "Lay pavers or travertine to the approved pattern and bond lines",
                "Cut borders and soldier courses tight, with consistent joints",
                "Match color and release against the approved sample in daylight",
            ],
        },
        {
            "roman": "VII",
            "title": "Lock-In &amp; Cure",
            "items": [
                "Saw or tool control joints at the engineered spacing and depth",
                "Cure slabs with compound or wet-cure &mdash; never left to chance",
                "Compact the paver field and drive sand fully into the joints",
                "Activate polymeric sand with a controlled wetting pass",
                "Set edge restraint so the field cannot migrate",
                "Post cure/set times and protect the surface from traffic",
            ],
        },
        {
            "roman": "VIII",
            "title": "White-Glove Handover",
            "items": [
                "Pressure-rinse the work zone and remove every form and stake",
                "Hose-test drainage with the owner watching the water move",
                "Apply sealer at the correct cure window when sealing is scoped",
                "Walk the finished surface together, corner to corner",
                "Hand over the care guide, cure calendar, and warranty in writing",
                "Follow up after the first heavy rain to confirm performance",
            ],
        },
    ],
}
_total = sum(len(p["items"]) for p in CHECKLIST["phases"])
assert _total == 48, f"Craft Code totals {_total}, not 48 — fix _data.py"


# ============================================================================
# REVIEWS — NEW business: NONE invented. Engine renders an invitation instead.
# ============================================================================
REVIEWS = []


# ============================================================================
# SHARED COPY — factual/process-based only. No invented numbers.
# ============================================================================
HERO_TRUST_BADGES = [
    "Fully Insured",
    "Free Estimates",
    "Written Workmanship Warranty",
    "ARC / HOA Submittal Support",
    "The Windermere Craft Code &mdash; 48 checkpoints",
]

WHY_US_POINTS = [
    {
        "num": "i",
        "title": "Built for architectural-review communities.",
        "body": "Isleworth, Keene&rsquo;s Pointe, Bella Collina, Windermere Downs &mdash; the communities we serve review every driveway color, paver blend, and border detail before a shovel moves. We prepare the sample boards, spec sheets, and drawings your ARC asks for, and we build exactly what was approved. Your project clears review once, not twice.",
    },
    {
        "num": "ii",
        "title": "Travertine and premium materials, handled correctly.",
        "body": "A travertine pool deck is not a paver job with prettier stone. It wants a different setting bed, different joint treatment, and a sealer that respects the stone&rsquo;s pores. We work in travertine, marble pavers, clay brick, and architectural-slab concrete weekly &mdash; and we&rsquo;ll tell you honestly when a humbler material serves the space better.",
    },
    {
        "num": "iii",
        "title": "The base decides everything. We engineer it.",
        "body": "Central Florida&rsquo;s sugar-sand soil forgives nothing built on a skipped base. Every project under the Windermere Craft Code gets measured lifts of crushed rock, mechanical compaction checked lift by lift, and photo documentation of the base before it disappears under your new surface. That&rsquo;s the part of the job you never see &mdash; and the reason it stays flat.",
    },
    {
        "num": "iv",
        "title": "Published pricing. Written proposals. No theater.",
        "body": "Our investment tables are printed on this site, by material and finish, at honest Central Florida rates. After the site visit you receive a line-itemized written proposal within one business day &mdash; and the number on it is the number you pay unless the scope itself changes.",
    },
    {
        "num": "v",
        "title": "One crew, start to finish.",
        "body": "The crew that stakes your layout is the crew that pours, lays, seals, and walks the finished surface with you. No handoffs between a sales office and a subcontractor you&rsquo;ve never met. Questions during the build go to the person standing on your property.",
    },
    {
        "num": "vi",
        "title": "Insured, warrantied, and accountable after the rain.",
        "body": "We carry full insurance, every installation leaves with a signed workmanship warranty, and we come back after the first heavy rain to watch the water move &mdash; because a drainage promise means nothing until the sky tests it.",
    },
]

PROCESS_STEPS = [
    {"num": "01", "title": "Site Consultation", "body": "We walk the property together, measure the footprint, review your community&rsquo;s ARC standards, and match samples to the home. You receive a written, line-itemized proposal within one business day."},
    {"num": "02", "title": "Approval &amp; Scheduling", "body": "We prepare the ARC / HOA submittal package where one is required, lock the material order, and give you a real start window &mdash; not a moving target."},
    {"num": "03", "title": "The Build", "body": "Demolition, base engineering, forming, and placement &mdash; every step gated by the 48-checkpoint Windermere Craft Code, with the same crew from stake-out to seal."},
    {"num": "04", "title": "White-Glove Handover", "body": "We hose-test the drainage in front of you, walk the surface corner to corner, and hand over the care guide, cure calendar, and written workmanship warranty."},
]

# What we deliberately do NOT do — published for trust + legal safety.
EXCLUSIONS = [
    "House foundations or structural / load-bearing slabs",
    "Retaining walls over four feet",
    "Room additions or any work requiring a state general-contractor license",
    "Pool shells, screen enclosures, or roofed structures",
]


# ============================================================================
# BLOG — 5 general guides + per-city cost guides for 6 priority services.
# Slug pattern intentionally distinct from sister sites: [svc]-cost-in-[city]-fl-2026
# ============================================================================
GENERAL_BLOG_POSTS = [
    {
        "slug": "pavers-vs-concrete-florida",
        "title": "Pavers vs. Concrete in Florida: A Contractor&rsquo;s Straight Answer (2026)",
        "meta_desc": "Pavers or poured concrete for your Florida driveway, patio, or pool deck? Installed cost, lifespan, repairs, HOA approval, and resale — compared by a crew that installs both.",
        "category": "Comparison",
        "primary_city": "Windermere",
        "primary_service": "paver-driveways",
        "topic": "pavers_vs_concrete",
        "date_published": "2026-05-06",
        "date_modified": "2026-06-28",
    },
    {
        "slug": "best-pool-deck-material-florida",
        "title": "The Best Pool Deck Material for Florida: Travertine, Pavers, or Concrete?",
        "meta_desc": "Travertine, brick pavers, or finished concrete for a Florida pool deck? Barefoot temperature, slip grip, salt tolerance, and installed cost — scored side by side.",
        "category": "Materials",
        "primary_city": "Windermere",
        "primary_service": "travertine-pool-decks",
        "topic": "pool_deck_material",
        "date_published": "2026-04-14",
        "date_modified": "2026-06-20",
    },
    {
        "slug": "hoa-arc-approval-hardscape-windermere",
        "title": "Getting Hardscape Through ARC Review in Windermere &amp; West Orlando",
        "meta_desc": "How architectural review works for driveways, pavers, and pool decks in Windermere, Isleworth, Keene's Pointe, and Horizon West — and how to clear it on the first submittal.",
        "category": "HOA &amp; ARC",
        "primary_city": "Windermere",
        "primary_service": "paver-driveways",
        "topic": "hoa_arc",
        "date_published": "2026-03-18",
        "date_modified": "2026-06-12",
    },
    {
        "slug": "why-concrete-cracks-central-florida",
        "title": "Why Concrete Cracks in Central Florida &mdash; and What a Correct Pour Does Differently",
        "meta_desc": "Sugar-sand soil, afternoon storms, and missing joints crack Central Florida concrete. The real failure chain — and the base, steel, and joint work that interrupts it.",
        "category": "Craft",
        "primary_city": "Orlando",
        "primary_service": "concrete-driveways",
        "topic": "cracking",
        "date_published": "2026-02-24",
        "date_modified": "2026-05-30",
    },
    {
        "slug": "paver-cleaning-sealing-schedule-florida",
        "title": "How Often Should You Seal &amp; Re-Sand Pavers in Florida? The Real Schedule",
        "meta_desc": "The honest Florida paver maintenance calendar: when to clean, re-sand, and seal; what polymeric sand actually does; and what each service costs in the Orlando area.",
        "category": "Maintenance",
        "primary_city": "Winter Garden",
        "primary_service": "paver-sealing-repair",
        "topic": "sealing_schedule",
        "date_published": "2026-01-27",
        "date_modified": "2026-05-15",
    },
]

COST_BLOG_POSTS = []
for _svc_slug in COST_PRIORITY_SERVICES:
    _svc = SERVICES[_svc_slug]
    _kw = _svc["short"].lower()
    for _city_slug in TIER1:
        _city = CITIES[_city_slug]
        COST_BLOG_POSTS.append({
            "slug": f"{_svc_slug}-cost-in-{_city_slug}-fl-2026",
            "service_slug": _svc_slug,
            "city_slug": _city_slug,
            "service_name": _svc["name"],
            "service_short": _svc["short"],
            "city_name": _city["name"],
            "keyword": _kw,
            "title": f"What {_svc['short']} Cost in {_city['name']}, FL (2026 Rates)",
            "meta_desc": clip_desc(
                f"Current {_kw} pricing in {_city['name']}, FL — installed rates by material and "
                f"finish, what moves the number up or down locally, and how to budget the project in 2026."
            ),
            "category": "Cost Guide",
            "primary_city": _city["name"],
            "primary_service": _svc_slug,
            "topic": "cost_guide",
            "date_published": "2026-02-10",
            "date_modified": "2026-06-25",
        })


# ============================================================================
# SOCIAL + DIRECTORY NETWORK
# ============================================================================
SOCIAL_LINKS = [
    ("Facebook", BUSINESS["facebook"]),
    ("Instagram", BUSINESS["instagram"]),
]
DIRECTORY_NETWORK = [
    "Google Business Profile", "Bing Places", "Apple Business Connect", "Nextdoor",
    "Yelp", "Houzz", "Angi", "Thumbtack", "HomeAdvisor", "Porch", "BuildZoom",
    "Better Business Bureau", "Facebook", "Instagram", "Pinterest", "Foursquare",
    "Yellow Pages", "Superpages", "Manta", "Hotfrog", "Brownbook", "Cylex",
    "Alignable", "ChamberofCommerce.com", "EZlocal", "ShowMeLocal", "Trustpilot",
]
