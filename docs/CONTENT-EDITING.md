# Editing your website

## Add a blog in GitHub

1. Open `content/blog/` in the repository.
2. Copy the structure of an existing article into a **new file** such as `preparing-your-documents.json`.
3. Set `slug` to `preparing-your-documents` — it must match the filename without `.json`.
4. Replace the title, description, answer, sections, category, dates and references. Use normal text inside the JSON strings; the builder safely escapes it, so HTML is not needed.
5. Set `status` to `draft` while writing, then `published` when ready.
6. Commit the file to `main`. The Actions workflow builds and publishes it automatically.

The article appears at `/blog/preparing-your-documents/`, in the blog listing, sitemap and feed. Newest published dates appear first; the homepage shows the first three articles. Search and category filters update automatically.

You can also create a draft locally:

```sh
python3 tools/new_content.py blog preparing-your-documents --title "Preparing your documents"
```

## Edit or add a service

Edit its individual file in `content/services/`. To add one, copy another service or run:

```sh
python3 tools/new_content.py services document-preparation --title "Document preparation"
```

Use `order` to control service order. Edit the scope in `answer` and `sections`, plus the preparation `steps`. Published services appear automatically in the service listing, homepage and footer.

Keep the service description within the assistance you can actually provide. Do not introduce official-agent claims, approval guarantees or restricted service offers. The validation checks reject the removed service terms in public copy.

## Fields you will use

- `status`: `draft` or `published`.
- `slug`: the permanent page URL name, matching the JSON filename.
- `title`, `description`, `answer`: page heading, short summary and main explanation.
- `sections`: a list of objects with `title` and `text`. Add as many sections as needed.
- `category`: any useful label. Blog filters update automatically.
- `icon`: use `file-text`, `file-search`, `graduation-cap`, `clipboard-check`, `globe`, `landmark`, `stamp`, `plane`, `route`, `users` or `shield-check`.
- `sources`: keys from the `sources` directory inside `content/site.json`, for example `["mosadaqa", "education"]`. Add a new source there before referencing its key.
- `related`: existing internal page URLs, for example `["/services/mosadaqa/"]`.
- `published`, `updated`: real publication and revision dates in `YYYY-MM-DD` format. Services use `updated` only.

JSON requires double quotes around strings and commas between fields. Escape a quotation mark inside a string as `\"`. A trailing comma is invalid. The build will reject malformed files rather than publishing them.

## Remove or rename a page

Set the record to `draft` or remove the JSON file, and remove links to it from other records. If it had a public URL, add its old URL and the relevant replacement URL to `content/redirects.json`, for example:

```json
"/blog/old-name/": "/blog/new-name/"
```

The old page becomes a noindex redirect. The builder removes obsolete generated HTML listed in the previous manifest. Broken internal links fail validation before publication.

## Other edits

Contact details and navigation are in `content/site.json`. The home layout is `templates/home.html`; shared header and footer are in `templates/partials/`. General pages are in `content/pages/`. Update the privacy information if the enquiry or data-handling behaviour changes.

## Local check and publishing

```sh
python3 tools/build.py
python3 tools/check.py
node --test tools/checker.test.cjs
python3 tools/export.py
```

Push to `main`, then wait for the **Validate and publish website** workflow to finish. A failed check prevents the deployment. Edit the source JSON and templates, not generated HTML. There is no admin dashboard: editing happens in GitHub or your local repository.
