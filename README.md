# SK Attestations

A lightweight, static document-assistance website. Midnight navy / warm ivory design, locally hosted Manrope variable font, CSS/SVG document animations and accessible native controls. No production JavaScript dependencies, build service, analytics or document-upload backend.

## Preview

From this repository:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Use an HTTP server rather than opening HTML files directly: routes and assets are root-relative. `tools/responsive-preview.html` provides 320, 390, 768 and 1440px frames for development checks (noindex, excluded from sitemap).

## Edit and rebuild

- `tools/content.py`: business/entity details, service, guide, document, destination, problem-case and FAQ content, including the Mosadaqa degree guide.
- `tools/build.py`: reusable navigation, footer, card, assessment, guide, service, problem, country and trust-page templates; metadata, JSON-LD, `sitemap.xml` with `lastmod`, `robots.txt`, `llms.txt` and `feed.xml`.
- `styles.css`: design tokens, layouts, responsive rules, motion and reduced-motion support.
- `script.js`: progressively enhanced navigation, four-step assessment, destination selection (guidance is read from the text already in the page), FAQs and email draft preparation. No runtime `fetch`.
- `assets/`: locally hosted font and its OFL license, icon, brand mark (`logo.svg`), social share image. Destination guidance lives in the HTML, not in JSON fetched at runtime.

```sh
python3 tools/build.py
python3 tools/check.py
node --test tools/assessment.test.cjs
```

Python 3.10+ and Node 18+ are enough. There are no packages to install for build or tests. Commit generated HTML and assets along with source changes. CI rebuilds, runs `tools/check.py`, runs the Node tests and fails if the committed output is stale.

## Hosting

The existing `.nojekyll` and `CNAME` are retained. GitHub Pages can serve the committed root directly. The canonical origin is `https://ksa.salaroutsourcing.com`, configured in `tools/build.py`. If the origin changes, update it and rebuild. No deployment or push is performed by the build.

There are 37 indexable pages covering five services only: Mosadaqa degree attestation, Saudi Culture attestation, Saudi Embassy attestation, QVP qualification verification and UAE Embassy attestation (documents issued in Pakistan, including medical reports). Apostille is not offered as a service: apostille certificates are issued only by the designated authority of a contracting state, and an agent cannot issue one. `sitemap.xml` lists canonical clean URLs with an ISO `lastmod`; `robots.txt` references it and states an explicit policy for search and AI crawlers; `llms.txt` maps the most useful pages for assistants; `feed.xml` carries the guides. Organization, WebSite, WebPage, Article, FAQPage, Service and BreadcrumbList data reflect visible content, and the Organization node carries the published contact details, service area and subject areas. No ratings, fake reviews, invented persons or ineligible rich-result claims are included.

Legacy `.html` URLs have canonical links and immediate HTML redirects, including the formerly missing guide targets. `redirects.json` documents the mapping for a future host with real HTTP redirects. GitHub Pages cannot configure arbitrary HTTP 301s. `404.html` is the custom GitHub Pages error page; the Python development server uses its own default error response for missing URLs.

## Assessment and contact

The assessment produces conditional preparation checks, never a government determination. It does not classify a country as requiring a fixed route or silently treat an unknown document as a degree. Document problems are shown before authentication stages. Purpose affects the preparation guidance.

Answers stay in page memory, with no cookies or browser storage. A chosen assessment handoff uses a URL fragment containing only the fixed category selections; the contact page removes it from the displayed URL. The form prepares a `mailto:` draft for the existing `info@salaroutsourcing.com` address. Visitors review and send it themselves. The website does not submit messages, store records, upload documents or claim a secure vault.

## Content and operational boundaries

The existing business name and contact address are retained. Unverified credentials, incorporation numbers, founding dates, named review teams, fees, processing times, partnerships and blanket destination rules are not republished. Guide and problem pages are written per topic: no page reuses another page's sections. Only two dedicated country pages are published; the destination selector supplies distinct preparation questions for the other listed destinations instead of generating repetitive country pages, and that guidance is always present as text in the page so it can be read without scripts.

Guide dates are clearly **editorial updates**, not claimed expert review dates. The content links to official sources; live submission checklists should always be checked with the responsible authority. HEC, HCCH and NAVTTC references were accessible during implementation; some MOFA/IBCC pages blocked or timed out. No detailed, unverified fee, representation, processing-time or treaty guarantees are derived from those unavailable pages.

The privacy/security pages accurately describe the implemented website. Company email access rules, retention periods and deletion procedures were not supplied; the site explicitly asks visitors to clarify those arrangements before sending files. The operator should supply its actual policies and any verified reviewer credentials before making stronger claims.

## Validation scope

- All generated internal links, anchors, assets, one-H1 structure, heading order, canonical and social metadata, title and description lengths, duplicate titles/descriptions, sitemap consistency in both directions (entry to page and page to entry), JSON-LD syntax and required fields per node type, plus `robots.txt`, `llms.txt` and `feed.xml`.
- Nine regression tests covering issue-first ordering, unknown records, diploma ambiguity, purpose-specific guidance, conditional country handling, Mosadaqa verification queries, every destination with published guidance and untrusted input rejection.
- Browser checks: complete assessment, validation, email handoff (not sent), mobile menu/Escape, destination selection, journey stages, FAQ filters, legacy redirects and representative content pages.
- Responsive homepage widths: 320, 390, 768, 1440px, with no horizontal overflow.
- Reduced-motion CSS disables animations and transitions; visible focus states, labelled fieldsets and native radio keyboard operation.

This is a static performance-focused implementation, not a promise of a Lighthouse score or search ranking. Field Core Web Vitals and real email delivery must be measured after publication; no production changes have been made by this work.

## Search and answer-engine notes

- Content lives in the generated HTML. The destination guidance, FAQ answers and problem copy are readable without JavaScript, so crawlers and assistants see the same text a visitor sees.
- The FAQ block on the homepage and the Mosadaqa guide is mirrored by a `FAQPage` graph for the visible questions; nothing is marked up that a visitor cannot read.
- No fee, timeline, treaty or approval claim is published. Those numbers change and belong to the competent authority, so the pages say so and point to the official source instead.
- `llms.txt` summarises the site and links the canonical pages most likely to answer a question. It is generated, so it cannot drift from the site.
- Titles stay within search-result width and every page has a unique description; the checker fails the build otherwise.


## Service focus, contact and entity signals

The site advertises exactly the five services listed in SERVICES, and `tools/check.py` fails if a service page exists that is not advertised or an advertised service page is missing. Published contact and entity details (name, legal name, SECP CUIN, office address, WhatsApp, office line, email, Google Maps link, Instagram) live in the BUSINESS block of `tools/content.py` and are used for the header contact strip, the footer, the contact page, `llms.txt` and the Organization JSON-LD, whose `@id` is the main business entity so assistants consolidate one business rather than several. Every page carries a WhatsApp action. Retired URLs (`/services/apostille/`, `/services/hec-attestation/`, `/documents/*`, `/countries/uae/`, `/navttc/`, legacy `/blog/*.html`) are redirected with a generated `_redirects` file plus HTML fallback stubs.
