#!/usr/bin/env python3
"""Validate the exact publish manifest, metadata, local links and content scope."""
import json
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = json.loads((ROOT / 'content/site.json').read_text())
BASE = SITE['url'].rstrip('/')
MANIFEST = json.loads((ROOT / '.build-manifest.json').read_text())

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.headings, self.canonicals = set(), [], [], []
        self.meta, self.schemas, self.errors, self.visible = {}, [], [], []
        self.script = False
        self.schema = False
        self.chunk = ''
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('Duplicate id: ' + a['id'])
            self.ids.add(a['id'])
        if re.fullmatch('h[1-6]', tag): self.headings.append(int(tag[1]))
        if tag == 'button' and 'type' not in a: self.errors.append('Button missing type')
        if tag == 'img' and 'alt' not in a: self.errors.append('Image missing alt')
        if any(k.startswith('on') for k in a): self.errors.append('Inline event handler')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a['href'])
        elif a.get('href'): self.links.append(a['href'])
        if a.get('src'): self.links.append(a['src'])
        if tag == 'meta': self.meta[a.get('name', a.get('property', a.get('http-equiv', '')))] = a.get('content', '')
        if tag in ('script', 'style'):
            self.script = True
            self.schema = a.get('type') == 'application/ld+json'
            self.chunk = ''
    def handle_data(self, data):
        if self.schema: self.chunk += data
        if not self.script: self.visible.append(data)
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            if self.schema:
                try: self.schemas.extend(json.loads(self.chunk)['@graph'])
                except (ValueError, KeyError): self.errors.append('Invalid JSON-LD')
            self.script = self.schema = False

pages = {ROOT / f: Page((ROOT / f).read_text()) for f in MANIFEST if f.endswith('.html')}
errors, indexable, titles, descriptions = [], set(), set(), set()
for file, page in pages.items():
    def fail(message): errors.append(f'{file.relative_to(ROOT)}: {message}')
    for error in page.errors: fail(error)
    if len(page.canonicals) != 1: fail('Expected one canonical')
    if re.search(r'\b(?:HEC|HSC|IBCC|MOFA|apostille)\b', ' '.join(page.visible), re.I): fail('Removed service terminology reintroduced')
    redirect = 'refresh' in page.meta
    if redirect:
        if not page.meta.get('robots', '').startswith('noindex'): fail('Redirect must be noindex')
    else:
        if page.headings.count(1) != 1: fail('Expected one h1')
        for key in ['description', 'viewport', 'og:title', 'og:description', 'og:url', 'og:image', 'og:type', 'twitter:card']:
            if not page.meta.get(key): fail('Missing ' + key)
        if not page.schemas: fail('Missing structured data')
        if page.canonicals != [page.meta.get('og:url')]: fail('Canonical differs from OG URL')
        for node in page.schemas:
            fields = {'Article': ['headline', 'author', 'publisher', 'datePublished', 'dateModified', 'mainEntityOfPage'], 'Service': ['name', 'provider', 'url'], 'Organization': ['name', 'url', 'telephone', 'logo']}.get(node.get('@type'), [])
            for field in fields:
                if not node.get(field): fail('Missing structured data field ' + field)
        if not page.meta.get('robots', '').startswith('noindex'):
            canonical = page.canonicals[0]
            indexable.add(canonical)
            if not canonical.startswith(BASE + '/'): fail('Wrong canonical origin')
            for key, bucket in [('og:title', titles), ('description', descriptions)]:
                if page.meta[key] in bucket: fail('Duplicate ' + key)
                bucket.add(page.meta[key])
    for href in page.links:
        url = urlsplit(href)
        if url.scheme in ('mailto', 'tel'): continue
        if url.netloc and url.netloc != urlsplit(BASE).netloc: continue
        if href == '#' or url.scheme == 'javascript': fail('Placeholder or unsafe link'); continue
        target = ROOT / unquote(url.path.lstrip('/')) if url.path.startswith('/') else file.parent / unquote(url.path)
        if not url.path: target = file
        target = target.resolve()
        if target.is_dir(): target /= 'index.html'
        if not target.exists(): fail('Missing target ' + href)
        elif target.suffix == '.html' and target not in pages: fail('HTML target excluded from publish manifest: ' + href)
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids: fail('Missing anchor ' + href)
locs = {e.text for e in ET.parse(ROOT / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
if locs != indexable: errors.append('Sitemap does not match indexable pages')
for page in pages.values():
    if 'refresh' in page.meta and page.canonicals[0] not in indexable: errors.append('Redirect to missing page')
articles = sum(n.get('@type') == 'Article' for p in pages.values() for n in p.schemas)
if len(ET.parse(ROOT / 'feed.xml').findall('./channel/item')) != articles: errors.append('Feed must contain every published article')
if f'Sitemap: {BASE}/sitemap.xml' not in (ROOT / 'robots.txt').read_text(): errors.append('Missing robots sitemap')
for css in (ROOT / 'assets/css').glob('*.css'):
    for path in re.findall(r'url\([\'"]?([^\)\'\"]+)', css.read_text()):
        if not path.startswith(('data:', 'http')) and not ((ROOT / path.lstrip('/')) if path.startswith('/') else (css.parent / path)).resolve().exists(): errors.append(f'Missing CSS asset: {path}')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages, {len(indexable)} indexable URLs, {articles} articles; links, assets, metadata, structured data, redirects and removed-service checks.')
