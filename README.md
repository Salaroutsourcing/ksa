# SK Attestation Services

Website: https://ksa.salaroutsourcing.com/

A static, multi-page website based on the supplied neon design. Each blog post and service has its own editable JSON file and its own public page. Shared layouts, styles and scripts are separate.

## Where to edit

| Change | Source folder or file |
| --- | --- |
| Add or edit a blog post | `content/blog/` — one JSON file per article |
| Add or edit a service | `content/services/` — one JSON file per service |
| Business details and navigation | `content/site.json` |
| About, privacy and other information pages | `content/pages/` |
| FAQs and document issues | `content/faq.json`, `content/issues.json` |
| Page layouts | `templates/` |
| Header, footer and shared sections | `templates/partials/` |
| Design and responsive styling | `assets/css/` |
| Interactive behaviour | `assets/js/` |
| Brand images and fonts | `assets/images/`, `assets/fonts/` |

Read [the editing guide](docs/CONTENT-EDITING.md) for a step-by-step example.

## Preview and validate

Python 3.10+ is required to build; Node 22 is used for checker tests.

```sh
python3 tools/build.py
python3 tools/check.py
node --test tools/checker.test.cjs
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Rebuild and refresh after editing content or templates. The HTML files in `/blog/`, `/services/` and other page folders are generated. Edit their sources to avoid losing changes on the next build.

## Publishing

Push to `main` to build, validate and publish through GitHub Pages automatically. Pull requests run the checks without deploying. See the repository's **Actions → Validate and publish website** for deployment progress. Generated HTML does not need to be manually updated for an online content edit; the workflow generates it before deployment.

`python3 tools/export.py` creates `_site/` containing only public pages and assets. Content source files, templates, development tools and documentation are excluded. `CNAME` retains the existing custom domain.

The site is static: it has no admin login, database or file-upload system. The enquiry form prepares a WhatsApp or email draft; the visitor reviews and sends it in that application. It does not submit a message itself.

## Service scope

Restricted attestation offers and appointed-agent claims have been removed. The remaining content describes independent preparation and requirements guidance. Official platforms, issuers and receiving institutions decide requirements and outcomes. Former URLs redirect to relevant current pages and are marked noindex; they do not retain the old service content.
