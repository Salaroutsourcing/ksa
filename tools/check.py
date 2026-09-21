#!/usr/bin/env python3
"""Validate static routes, anchors, metadata and structured data without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.ids=set(); self.links=[]; self.h1=0; self.canonical=[]; self.meta={}; self.schema=[]; self.in_schema=False; self.chunk=''; self.errors=[]; self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:self.errors.append('Duplicate id '+a['id'])
            self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='a':self.links.append(a.get('href',''))
        if tag in ('script','img') and a.get('src'): self.links.append(a['src'])
        if tag=='link':
            if a.get('rel')=='canonical':self.canonical.append(a['href'])
            else:self.links.append(a.get('href',''))
        if tag=='meta':self.meta[a.get('name',a.get('property',a.get('http-equiv','')))]=a.get('content','')
        if tag=='script' and a.get('type')=='application/ld+json':self.in_schema=True;self.chunk=''
    def handle_data(self,data):
        if self.in_schema:self.chunk+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.in_schema:self.schema.append(json.loads(self.chunk));self.in_schema=False
pages={f:Page(f.read_text()) for f in ROOT.rglob('*.html') if '.git' not in f.parts and 'tools' not in f.relative_to(ROOT).parts}
errors=[]
for file,p in pages.items():
    label=str(file.relative_to(ROOT));errors.extend(label+': '+s for s in p.errors)
    redirect='refresh' in p.meta
    if not redirect:
        if p.h1!=1:errors.append(label+': expected one h1')
        if len(p.canonical)!=1:errors.append(label+': expected canonical')
        for key in ['description','viewport','og:title','og:description','og:url','og:image','twitter:card']:
            if not p.meta.get(key):errors.append(label+': missing '+key)
        if not p.schema:errors.append(label+': missing schema')
        if p.canonical and p.canonical[0]!=p.meta['og:url']:errors.append(label+': canonical and OG differ')
    for href in p.links:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        if not href or href=='#':errors.append(label+': empty link');continue
        target=ROOT/unquote(u.path.lstrip('/')) if u.path.startswith('/') else file.parent/unquote(u.path)
        if not u.path:target=file
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(label+': missing '+href)
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(label+': missing anchor '+href)
urls=ET.parse(ROOT/'sitemap.xml').getroot()
for elem in urls:
    u=elem[0].text
    target=ROOT/urlsplit(u).path.lstrip('/')/'index.html'
    if target not in pages:errors.append('Sitemap missing target '+u)
    elif pages[target].canonical!=[u]:errors.append('Sitemap canonical mismatch '+u)
assert not errors, '\n'.join(errors)
print(f'PASS: {len(pages)} HTML pages, {len(urls)} sitemap URLs; all internal links, anchors, required metadata and JSON-LD valid.')
