#!/usr/bin/env python3
"""Validate routes, anchors, metadata, structured data, crawlable content and generators.

Dependency-free. Fails loudly (non-zero exit) on any finding so CI blocks a regression
instead of shipping one.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from content import BUSINESS, COUNTRIES, FAQS, GUIDES, PROBLEMS  # noqa: E402

BASE = "https://ksa.salaroutsourcing.com"
REQUIRED_META = ["description", "viewport", "og:title", "og:description", "og:url", "og:image", "og:type", "og:locale", "twitter:card"]
TITLE_MIN, TITLE_MAX = 15, 60
DESC_MIN, DESC_MAX = 100, 170
NEW_PAGES = {
    "/guides/mosadaqa-degree-attestation/": ["mosadaqa", "CNIC", "passport", "degree", "HEC"],
    "/problems/mosadaqa-verification-query/": ["mosadaqa", "query", "record"],
}


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.headings = []
        self.buttons = []
        self.images = []
        self.canonical = []
        self.meta = {}
        self.schema = []
        self.errors = []
        self.in_schema = False
        self.in_button = 0
        self.chunk = ""
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                self.errors.append("Duplicate id " + a["id"])
            self.ids.add(a["id"])
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append(int(tag[1]))
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "img":
            self.images.append(a.get("alt", ""))
            if a.get("src"):
                self.links.append(a["src"])
        if tag in ("script", "link") and a.get("src"):
            self.links.append(a["src"])
        if tag == "button":
            self.in_button += 1
            self.buttons.append(a)
            if "type" not in a:
                self.errors.append("button without a type attribute")
        elif tag == "p" and self.in_button:
            self.errors.append("p element inside button")
        if tag == "link":
            if a.get("rel") == "canonical":
                self.canonical.append(a["href"])
            elif a.get("href"):
                self.links.append(a["href"])
        if tag == "meta":
            self.meta[a.get("name", a.get("property", a.get("http-equiv", "")))] = a.get("content", "")
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_schema = True
            self.chunk = ""

    def handle_data(self, data):
        if self.in_schema:
            self.chunk += data

    def handle_endtag(self, tag):
        if tag == "button" and self.in_button:
            self.in_button -= 1
        if tag == "script" and self.in_schema:
            try:
                self.schema.append(json.loads(self.chunk))
            except json.JSONDecodeError as exc:
                self.errors.append("invalid JSON-LD: " + str(exc))
            self.in_schema = False

    def types(self):
        found = []
        for block in self.schema:
            for node in block.get("@graph", [block]):
                if isinstance(node, dict) and node.get("@type"):
                    found.append(node["@type"])
        return found

    def nodes(self, kind):
        found = []
        for block in self.schema:
            for node in block.get("@graph", [block]):
                if isinstance(node, dict) and node.get("@type") == kind:
                    found.append(node)
        return found


pages = {
    f: Page(f.read_text())
    for f in ROOT.rglob("*.html")
    if ".git" not in f.parts and "tools" not in f.relative_to(ROOT).parts
}
errors = []


def rel(file, message):
    errors.append(str(file.relative_to(ROOT)) + ": " + message)


for file, page in sorted(pages.items()):
    label = str(file.relative_to(ROOT))
    for message in page.errors:
        rel(file, message)
    redirect = "refresh" in page.meta
    if not redirect:
        if len(page.canonical) != 1:
            rel(file, "expected exactly one canonical")
        for key in REQUIRED_META:
            if not page.meta.get(key):
                rel(file, "missing " + key)
        if not page.schema:
            rel(file, "missing structured data")
    # heading order: never skip a level downwards
    order = [h for h in page.headings]
    previous = 0
    for level in order:
        if previous and level > previous + 1 and not redirect:
            rel(file, f"heading jump h{previous} -> h{level}")
            break
        previous = level
    if len(page.canonical) == 1 and not redirect and not page.meta.get("robots", "").startswith("noindex"):
        canonical = page.canonical[0]
        if not canonical.startswith(BASE):
            rel(file, "canonical is not on the canonical origin")
        if page.meta.get("og:url") and page.meta["og:url"] != canonical:
            rel(file, "canonical and og:url differ")
        title = page.meta.get("og:title", "")
        description = page.meta.get("description", "")
        if not (TITLE_MIN <= len(title) <= TITLE_MAX):
            rel(file, f"og:title length {len(title)} outside {TITLE_MIN}-{TITLE_MAX}")
        if not (DESC_MIN <= len(description) <= DESC_MAX):
            rel(file, f"description length {len(description)} outside {DESC_MIN}-{DESC_MAX}")
        types = page.types()
        if ("Article" in types) != (page.meta.get("og:type") == "article"):
            rel(file, "og:type does not match the structured data type")
        if "Article" in types and not page.meta.get("article:published_time"):
            rel(file, "article page without article:published_time")
    for href in page.links:
        url = urlsplit(href)
        if url.scheme == "mailto" or url.netloc:
            if url.netloc and url.netloc != "ksa.salaroutsourcing.com":
                continue
            if url.scheme == "mailto":
                continue
        if not href or href == "#":
            rel(file, "empty link")
            continue
        if url.path.startswith("/"):
            target = ROOT / unquote(url.path.lstrip("/"))
        else:
            target = file.parent / unquote(url.path)
        if not url.path:
            target = file
        target = target.resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            rel(file, "missing link target " + href)
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            rel(file, "missing anchor " + href)
    for alt in page.images:
        if not alt:
            rel(file, "image without alt text")

# --- named pages, structured data and metadata contracts ----------------------
for path, required in NEW_PAGES.items():
    target = ROOT / path.strip("/") / "index.html"
    if target not in pages:
        errors.append("missing expected page " + path)
        continue
    text = target.read_text()
    for term in required:
        if term.lower() not in text.lower():
            errors.append(f"{path}: expected the term '{term}'")

guide = ROOT / "guides/mosadaqa-degree-attestation/index.html"
if guide in pages:
    node = pages[guide].nodes("Article")
    if not node:
        errors.append("mosadaqa guide: no Article node")
    else:
        for field in ["headline", "datePublished", "dateModified", "author", "publisher", "mainEntityOfPage"]:
            if not node[0].get(field):
                errors.append(f"mosadaqa guide: Article node missing {field}")
        if not node[0].get("mentions"):
            errors.append("mosadaqa guide: Article node has no entity mentions")

for name, page in pages.items():
    org = page.nodes("Organization")
    for fragment in page.nodes("Organization") + page.nodes("WebSite"):
        for field in ["name", "url"]:
            if not fragment.get(field):
                errors.append(f"{name}: organization node missing {field}")
    if org:
        for field in ["logo", "image", "address", "telephone", "contactPoint", "areaServed", "knowsAbout"]:
            if not org[0].get(field):
                errors.append(f"{name}: organization node missing {field}")
        break
for name, page in pages.items():
    for article in page.nodes("Article"):
        for field in ["headline", "datePublished", "dateModified", "author", "publisher"]:
            if not article.get(field):
                errors.append(f"{name}: article node missing {field}")
    for service in page.nodes("Service"):
        for field in ["name", "description", "provider", "url"]:
            if not service.get(field):
                errors.append(f"{name}: service node missing {field}")
    for faq in page.nodes("FAQPage"):
        if not faq.get("mainEntity"):
            errors.append(f"{name}: FAQPage without questions")
        for question in faq.get("mainEntity") or []:
            if question.get("@type") != "Question" or not question.get("name"):
                errors.append(f"{name}: malformed FAQ question")
            if not (question.get("acceptedAnswer") or {}).get("text"):
                errors.append(f"{name}: FAQ question without answer text")

required_faq_pages = ["index.html", "guides/mosadaqa-degree-attestation/index.html"]
for path in required_faq_pages:
    page = pages.get(ROOT / path)
    if page is None:
        errors.append("missing " + path)
    elif not page.nodes("FAQPage"):
        errors.append(path + ": expected a FAQPage node mirroring the visible questions")

# --- duplicate titles and descriptions ---------------------------------------
titles, descriptions = {}, {}
for file, page in pages.items():
    if "refresh" in page.meta or page.meta.get("robots", "").startswith("noindex"):
        continue
    for key, bucket in ((page.meta.get("og:title"), titles), (page.meta.get("description"), descriptions)):
        if key:
            bucket.setdefault(key, []).append(str(file.relative_to(ROOT)))
for bucket, label in ((titles, "title"), (descriptions, "description")):
    for value, files in bucket.items():
        if len(files) > 1:
            errors.append(f"duplicate {label} on {', '.join(sorted(files))}")

# --- crawlable content (no JavaScript-only guidance) -------------------------
countries_html = (ROOT / "countries/index.html").read_text() if (ROOT / "countries/index.html").exists() else ""
home_html = (ROOT / "index.html").read_text()
for name, copy in COUNTRIES.items():
    probe = copy[:40]
    if probe not in countries_html:
        errors.append("destination text missing from /countries/: " + name)
for script in ["script.js"]:
    if "fetch(" in (ROOT / script).read_text():
        errors.append(script + ": runtime fetch reintroduced (content must be in the HTML)")
for asset in ["styles.css", "script.js", "assets/logo.svg", "assets/favicon.svg", "assets/manrope.woff2", "assets/social-card.png", "feed.xml", "llms.txt"]:
    if not (ROOT / asset).exists():
        errors.append("missing asset " + asset)
if FAQS and "FAQPage" not in json.dumps([p.schema for p in [pages[ROOT / "index.html"]]]):
    errors.append("home page FAQ structured data missing")

# --- sitemap, robots, feed, llms ---------------------------------------------
sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
locs = []
for entry in sitemap:
    loc = entry.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    lastmod = entry.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
    if loc is None or not loc.text:
        errors.append("sitemap entry without loc")
        continue
    if lastmod is None or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lastmod.text or ""):
        errors.append("sitemap entry without ISO lastmod for " + loc.text)
    if not loc.text.startswith(BASE + "/"):
        errors.append("sitemap URL outside the canonical origin: " + loc.text)
    locs.append(loc.text)
    target = ROOT / urlsplit(loc.text).path.lstrip("/") / "index.html"
    if target not in pages:
        errors.append("sitemap target missing " + loc.text)
    elif pages[target].canonical != [loc.text]:
        errors.append("sitemap canonical mismatch " + loc.text)
indexable = set()
for f, page in pages.items():
    if f.name != "index.html" or not page.canonical:
        continue
    if "refresh" in page.meta or page.meta.get("robots", "").startswith("noindex"):
        continue
    indexable.add(page.canonical[0])
missing_from_sitemap = sorted(indexable - set(locs))
if missing_from_sitemap:
    errors.append("indexable pages missing from sitemap: " + ", ".join(missing_from_sitemap))
robots = (ROOT / "robots.txt").read_text()
if f"Sitemap: {BASE}/sitemap.xml" not in robots:
    errors.append("robots.txt does not reference the sitemap")
if "\nDisallow: /\n" in robots:
    errors.append("robots.txt blocks the whole site")
if "Disallow: /tools/" not in robots:
    errors.append("robots.txt does not exclude /tools/")
if "GPTBot" not in robots or "PerplexityBot" not in robots:
    errors.append("robots.txt has no explicit AI crawler policy")
feed = ET.parse(ROOT / "feed.xml").getroot()
entries = feed.findall("{http://www.w3.org/2005/Atom}entry")
if len(entries) < len(GUIDES):
    errors.append(f"feed.xml has {len(entries)} entries for {len(GUIDES)} guides")
for entry in entries:
    for tag in ["title", "link", "id", "updated", "summary"]:
        if entry.find("{http://www.w3.org/2005/Atom}" + tag) is None:
            errors.append("feed entry missing " + tag)
llms = (ROOT / "llms.txt").read_text()
if not llms.startswith("# " + BUSINESS["name"]):
    errors.append("llms.txt does not start with the business name")
if llms.count("](" + BASE) < 12:
    errors.append("llms.txt links too few canonical pages")
for fragment in ["/guides/mosadaqa-degree-attestation/", BUSINESS["email"], BUSINESS["telephone"]]:
    if fragment not in llms:
        errors.append("llms.txt missing " + fragment)

# --- content contracts for the problem pages ---------------------------------
for problem in PROBLEMS:
    for field in ["slug", "title", "tag", "desc", "answer", "sections", "guide"]:
        if not problem.get(field):
            errors.append(f"problem '{problem.get('slug')}' missing {field}")
    if problem.get("sections") and len(problem["sections"]) < 3:
        errors.append(f"problem '{problem['slug']}' has fewer than three sections")

if errors:
    raise SystemExit("\n".join(sorted(set(errors))))
print(
    f"PASS: {len(pages)} HTML pages, {len(locs)} sitemap URLs, {len(GUIDES)} guides and "
    f"{len(PROBLEMS)} problem pages; links, anchors, metadata lengths, heading order, "
    f"structured data, crawlable destination text, robots, llms.txt and feed valid."
)
