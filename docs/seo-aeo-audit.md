# Current site publishing and search notes

The September 2026 replacement uses individual service and article content files, generated static pages and the supplied neon visual direction.

- Public pages include unique titles/descriptions, canonical URLs, Open Graph/social images and relevant Organization, WebPage, Article or Service structured data.
- Article dates and bylines are visible. Official references are linked where relevant; no appointment or endorsement is implied.
- The sitemap and RSS feed are built from published content. Drafts are excluded.
- Retired routes are noindex HTML redirects with canonical links to the replacement pages. GitHub Pages does not provide arbitrary server-side 301 rules.
- No unsupported review ratings, success statistics, fee estimates or turnaround promises are included.
- Source JSON, templates and local QA tools are excluded from the deployed artifact.
- Search ranking or rich-result appearance is not guaranteed.

Run `python3 tools/check.py` after building to validate metadata, structured data, links, redirects and removed-service copy.
