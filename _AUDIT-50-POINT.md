# 50-POINT SEO/GEO/AEO AUDIT — windermereconcrete.com
Build: 2026-07-02 · 269 HTML pages · 267 sitemap URLs · verified programmatically (link crawl, JSON-LD parse, title/desc scan, sister-site duplication probes).

## TECHNICAL (1–14)
| # | Check | Status |
|---|---|---|
| 1 | Canonical tag on every page, self-referencing, non-www https | **PASS** |
| 2 | robots.txt — valid, sitemap ref, /thanks/ + 404 blocked | **PASS** |
| 3 | Titles keyword-first, ≤62 chars, 0 duplicates across 269 pages | **PASS** |
| 4 | Meta descriptions 110–160 chars on all indexable pages (only noindex thanks/404 shorter) | **PASS** |
| 5 | OG + Twitter card meta on every page, per-service OG images | **PASS** |
| 6 | sitemap.xml — 267 URLs, priorities/changefreq/lastmod | **PASS** |
| 7 | `_headers` — HSTS, nosniff, frame, referrer, permissions policies + cache rules | **PASS** |
| 8 | `_redirects` — www/http canonicalization + 40 slug-variant 301s + 404 fallback | **PASS** |
| 9 | Mobile responsive (3 breakpoints), sticky mobile call bar, viewport meta | **PASS** |
| 10 | Single inlined CSS (zero render-blocking external CSS), fonts preconnected | **PASS** |
| 11 | 0 broken internal links (268 hrefs crawled, 0 missing targets) | **PASS** |
| 12 | Semantic HTML: single h1/page, header/main/footer/nav/article landmarks, aria labels | **PASS** |
| 13 | noindex on /thanks/ + 404; everything else index,follow with max-snippet directives | **PASS** |
| 14 | IndexNow | **PENDING** — needs owner key (WHAT-I-NEED #8); instructions delivered |
| — | GA4 | **PENDING BY DESIGN** — emits only when real {{GA4_ID}} supplied (no fake tag) |

## SCHEMA (15–24)
| # | Check | Status |
|---|---|---|
| 15 | Organization (@id, areaServed 24 cities + 5 areaServed-only, knowsAbout, slogan) | **PASS** |
| 16 | LocalBusiness + HomeAndConstructionBusiness dual-type on money pages | **PASS** |
| 17 | Service schema on all 12 hubs + 144 service-city pages | **PASS** |
| 18 | FAQPage schema on home, hubs, svc-city, city, FAQ, guides, cost posts | **PASS** |
| 19 | BreadcrumbList site-wide | **PASS** |
| 20 | Article schema on all 77 blog posts (dates, author, publisher) | **PASS** |
| 21 | WebSite + WebPage with @id graph linking | **PASS** |
| 22 | GeoCoordinates + PostalAddress (city+ZIP only — SAB, street hidden) | **PASS** |
| 23 | 1,235 JSON-LD blocks — 100% parse-valid | **PASS** |
| 24 | AggregateRating/Review — correctly ABSENT (no reviews yet; auto-enables via has_reviews) | **PASS** (honest) |

## GEO (25–33)
| # | Check | Status |
|---|---|---|
| 25 | 24 city pages (12 Tier-1 + 12 Tier-2) with unique 2,300+ word bodies | **PASS** |
| 26 | 144 service×city pages (12×12 Tier-1), unique city-woven content | **PASS** |
| 27 | Real neighborhoods per city (9–18 each) + ZIP chips on city & svc-city pages | **PASS** |
| 28 | geo.region/geo.position/ICBM meta on every page | **PASS** |
| 29 | areaServed city-level in schema; Ocoee/Apopka as areaServed-only (sister firewall) | **PASS** |
| 30 | NAP block in footer (city+ZIP, SAB-safe), llms.txt, schema — consistent | **PASS** |
| 31 | County + landmark + terrain context per city (soil/water-table notes) | **PASS** |
| 32 | Tier-grouped service-area section on homepage + nav dropdown | **PASS** |
| 33 | Embedded map | **DEFERRED** — add GBP embed after profile exists (avoids fake pin for SAB) |

## AEO (34–41)
| # | Check | Status |
|---|---|---|
| 34 | Direct-answer block (40–60 words, price-anchored) opens every money page | **PASS** |
| 35 | Citable stat repeated verbatim site-wide ("48-checkpoint Windermere Craft Code…") | **PASS** |
| 36 | "According to Windermere Concrete…" framing in keyfact + llms.txt | **PASS** |
| 37 | Comparison tables (options tables on all services; scorecards in guides) | **PASS** |
| 38 | `<details>` FAQs + matching FAQPage schema everywhere | **PASS** |
| 39 | llms.txt with key facts, services, cities, citable fact | **PASS** |
| 40 | AI crawlers (GPTBot, ClaudeBot, Perplexity, etc.) explicitly allowed in robots.txt | **PASS** |
| 41 | Definitional sentences + "on average / at 2026 rates" framing in cost content | **PASS** |

## CONTENT & ANTI-CANNIBALIZATION (42–47)
| # | Check | Status |
|---|---|---|
| 42 | Keyword map enforced: 1 primary/page; hub vs city-page title collision FIXED (0 dups) | **PASS** |
| 43 | Blog never targets money-page primaries; cost guides link UP to money pages | **PASS** |
| 44 | Tier-1 money pages 2,300–2,650 words; hubs ~2,600; guides 1,200–1,400 + tables | **PASS** |
| 45 | Keyword density safe — semantic breadth (materials/finishes/synonyms) over repetition | **PASS** |
| 46 | 0 sister-site phrase overlap (6 brand probes × 2 directions, all negative); different checklist name/number (48 vs 42 vs 38), palette, fonts, layout, slugs, voice | **PASS** |
| 47 | No invented reviews/ratings/stats/years; all unknowns as labeled {{PLACEHOLDERS}}; no license mentions (0 found); no street address | **PASS** |

## E-E-A-T & CONVERSION (48–50)
| # | Check | Status |
|---|---|---|
| 48 | About + Process (Craft Code published in full) + Warranty + Privacy + Terms + FAQ | **PASS** |
| 49 | Sticky call/proposal floats (desktop rail + mobile bottom bar), contact bands, estimate card in hero, response-time promise site-wide | **PASS** |
| 50 | "What we don't do" honesty blocks + exclusions list (no GC-license work) on every service | **PASS** |

**SCORE: 47 PASS / 0 FAIL / 3 PENDING-ON-OWNER (IndexNow key, GA4 ID, GBP map embed — all in WHAT-I-NEED-FROM-YOU.md)**

## Residual notes for the re-audit of this audit
- Contact placeholders are resolved: the built site uses (689) 407-6658, hello@windermereconcrete.com, and `/api/contact`. The remaining built-content placeholder is {{FINANCING_DETAILS}} (1 occurrence).
- Images: 16 files needed per images/IMAGE-MANIFEST.md; no `<img>` tags ship broken (design is CSS-first), only OG/schema URLs await the files.
- Cost-guide length (~1,300 words) is intentional: table-dense, answer-first AEO format; expand top performers after Search Console data arrives.
