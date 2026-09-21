# SK Attestations

A lightweight, static document-assistance website. Midnight navy / warm ivory design, locally hosted Manrope variable font, CSS/SVG document animations and accessible native controls. No production JavaScript dependencies, build service, analytics or document-upload backend.

## Preview

From this repository:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Use an HTTP server rather than opening HTML files directly: routes and assets are root-relative. `tools/responsive-preview.html` provides 320, 390, 768 and 1440px frames for development checks (noindex, excluded from sitemap).

## Edit and rebuild

- `tools/content.py`: service, guide, document, destination and FAQ content.
- `tools/build.py`: reusable navigation, footer, card, assessment, guide, service, problem, country and trust-page templates; metadata and JSON-LD.
- `styles.css`: design tokens, layouts, responsive rules, motion and reduced-motion support.
- `script.js`: progressively enhanced navigation, four-step assessment, destination selection, FAQs and email draft preparation.
- `assets/`: locally hosted font and its OFL license, icon, social share image, generated destination data.

```sh
python3 tools/build.py
python3 tools/check.py
node --test tools/assessment.test.cjs
```

Python 3.10+ and Node 18+ are enough. There are no packages to install for build or tests. Commit generated HTML and assets along with source changes. CI validates generation, links, metadata and assessment logic.

## Hosting

The existing `.nojekyll` and `CNAME` are retained. GitHub Pages can serve the committed root directly. The canonical origin is `https://ksa.salaroutsourcing.com`, configured in `tools/build.py`. If the origin changes, update it and rebuild. No deployment or push is performed by the build.

There are 43 indexable pages. `sitemap.xml` includes canonical clean URLs; `robots.txt` references it. Organization, WebSite, WebPage, Service, Article and BreadcrumbList data reflect visible content. No ratings, fake reviews, invented persons or ineligible FAQ rich-result claims are included.

Legacy `.html` URLs have canonical links and immediate HTML redirects, including the formerly missing guide targets. `redirects.json` documents the mapping for a future host with real HTTP redirects. GitHub Pages cannot configure arbitrary HTTP 301s. `404.html` is the custom GitHub Pages error page; the Python development server uses its own default error response for missing URLs.

## Assessment and contact

The assessment produces conditional preparation checks, never a government determination. It does not classify a country as requiring a fixed route or silently treat an unknown document as a degree. Document problems are shown before authentication stages. Purpose affects the preparation guidance.

Answers stay in page memory, with no cookies or browser storage. A chosen assessment handoff uses a URL fragment containing only the fixed category selections; the contact page removes it from the displayed URL. The form prepares a `mailto:` draft for the existing `info@salaroutsourcing.com` address. Visitors review and send it themselves. The website does not submit messages, store records, upload documents or claim a secure vault.

## Content and operational boundaries

The existing business name and contact address are retained. Unverified credentials, incorporation numbers, founding dates, named review teams, fees, processing times, partnerships and blanket destination rules are not republished. The useful mismatch guide was rewritten around issuer responsibility and source-linked preparation questions. Only two dedicated country pages are published; the destination selector supplies distinct preparation questions for the other listed destinations instead of generating repetitive country pages.

Guide dates are clearly **editorial updates**, not claimed expert review dates. The content links to official sources; live submission checklists should always be checked with the responsible authority. HEC, HCCH and NAVTTC references were accessible during implementation; some MOFA/IBCC pages blocked or timed out. No detailed, unverified fee, representation, processing-time or treaty guarantees are derived from those unavailable pages.

The privacy/security pages accurately describe the implemented website. Company email access rules, retention periods and deletion procedures were not supplied; the site explicitly asks visitors to clarify those arrangements before sending files. The operator should supply its actual policies and any verified reviewer credentials before making stronger claims.

## Validation scope

- All generated internal links, anchors, assets, one-H1 structure, canonical and social metadata, sitemap consistency and JSON-LD syntax.
- Seven regression tests covering issue-first ordering, unknown records, diploma ambiguity, purpose-specific guidance, conditional country handling and untrusted input rejection.
- Browser checks: complete assessment, validation, email handoff (not sent), mobile menu/Escape, destination selection, journey stages, FAQ filters, legacy redirects and representative content pages.
- Responsive homepage widths: 320, 390, 768, 1440px, with no horizontal overflow.
- Reduced-motion CSS disables animations and transitions; visible focus states, labelled fieldsets and native radio keyboard operation.

This is a static performance-focused implementation, not a promise of a Lighthouse score or search ranking. Field Core Web Vitals and real email delivery must be measured after publication; no production changes have been made by this work.
