#!/usr/bin/env python3
"""Build the static website from individual JSON records and shared HTML templates."""
from pathlib import Path
from string import Template
from html import escape
from urllib.parse import quote
from datetime import date
import json, re
ROOT=Path(__file__).resolve().parents[1]
SITE=json.loads((ROOT/'content/site.json').read_text())
BASE=SITE['url'].rstrip('/')
GENERATED=[]; PAGES={}
MANIFEST=ROOT/'.build-manifest.json'
PREVIOUS=json.loads(MANIFEST.read_text()) if MANIFEST.exists() else []
def esc(value):return escape(str(value),quote=True)
def load_records(kind):
    records=[]
    for file in sorted((ROOT/'content'/kind).glob('*.json')):
        item=json.loads(file.read_text())
        if item.get('status','published')!='published':continue
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',item['slug']):raise ValueError(f'Invalid slug: {file}')
        if item['slug']!=file.stem:raise ValueError(f'Slug must match filename: {file}')
        records.append(item)
    return sorted(records,key=lambda x:(x.get('published',''),x['slug']),reverse=True) if kind=='blog' else sorted(records,key=lambda x:(x.get('order',100),x['slug']))
SERVICES=load_records('services'); BLOGS=load_records('blog')
ICONS={
 'arrow-right':'<path d="M5 12h14M13 6l6 6-6 6"/>',
 'message-circle':'<path d="M21 11.5a8.4 8.4 0 0 1-9 8.5 9 9 0 0 1-4-.9L3 21l1.9-5a9 9 0 0 1-.9-4 8.4 8.4 0 0 1 8.5-9H13a8.4 8.4 0 0 1 8 8v.5Z"/><path d="M8 11h8M8 14h5"/>',
 'shield-check':'<path d="m12 3 8 3v6c0 5-8 9-8 9s-8-4-8-9V6l8-3Z"/><path d="m8 12 3 3 5-6"/>',
 'graduation-cap':'<path d="m2 9 10-5 10 5-10 5L2 9ZM6 11v6c4 3 8 3 12 0v-6M22 9v7"/>',
 'clipboard-check':'<rect x="5" y="5" width="14" height="16" rx="2"/><rect x="9" y="2" width="6" height="5" rx="1"/><path d="m8 14 3 3 5-6"/>',
 'landmark':'<path d="m3 8 9-5 9 5H3ZM5 11v7m5-7v7m4-7v7m5-7v7M3 21h18"/>',
 'stamp':'<path d="M5 17h14v4H5zM8 17v-5l2-2V6a2 2 0 0 1 4 0v4l2 2v5"/>',
 'plane':'<path d="m22 2-7 20-4-9-9-4L22 2ZM11 13 22 2"/>',
 'file-search':'<path d="M13 3H5v18h14V9l-6-6Zm0 0v6h6"/><circle cx="11" cy="14" r="3"/><path d="m13 16 3 3"/>',
 'file-text':'<path d="M13 3H5v18h14V9l-6-6Zm0 0v6h6M8 13h8M8 17h5"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
 'user-x':'<circle cx="9" cy="7" r="4"/><path d="M2 21v-3a7 7 0 0 1 12-5M17 14l5 5m0-5-5 5"/>',
 'users':'<circle cx="8" cy="8" r="3"/><path d="M2 21v-3a6 6 0 0 1 12 0v3M16 5a3 3 0 0 1 0 6m2 4a5 5 0 0 1 4 5"/>',
 'file-x':'<path d="M13 3H5v18h14V9l-6-6Zm0 0v6h6m-10 4 6 6m0-6-6 6"/>',
 'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
 'refresh-cw':'<path d="M20 7V2m0 5h-5M4 17v5m0-5h5M4 10a8 8 0 0 1 14-5l2 2M20 14a8 8 0 0 1-14 5l-2-2"/>',
 'route':'<circle cx="5" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 5h9a4 4 0 0 1 0 8H8a3 3 0 0 0 0 6h9"/>',
 'zap':'<path d="m13 2-9 12h7l-1 8 10-12h-7l1-8Z"/>',
 'moon':'<path d="M21 13a9 9 0 0 1-10-10 9 9 0 1 0 10 10Z"/>',
 'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
 'alert-triangle':'<path d="m12 3 10 18H2L12 3ZM12 9v5m0 3v1"/>'
}
def icon(name):return '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+ICONS.get(name,ICONS['file-text'])+'</svg>'
ARROW=icon('arrow-right')
WA='https://wa.me/'+SITE['whatsapp']+'?text='+quote('Hello SK Attestation Services, I would like guidance for my documents.')
def template(name,**data):return Template((ROOT/'templates'/name).read_text()).substitute(**data)
def cta():return template('partials/cta.html',arrow=ARROW,whatsapp=WA,chat_icon=icon('message-circle'))
def header(path):
    nav=''.join(f'<li><a href="{url}"'+(' aria-current="page"' if path==url else '')+f'>{esc(label)}</a></li>' for url,label in SITE['navigation'])
    mobile=''.join(f'<a href="{url}"'+(' aria-current="page"' if path==url else '')+f'>{esc(label)}</a>' for url,label in SITE['navigation'])
    return template('partials/header.html',navigation=nav,mobile_navigation=mobile,whatsapp=WA,theme_icon=icon('moon'),chat_icon=icon('message-circle'),menu_icon=icon('menu'))
def footer():
    links=''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s["title"])}</a></li>' for s in SERVICES)
    return template('partials/footer.html',address=esc(SITE['address']),service_links=links,whatsapp=WA,phone=esc(SITE['phone_display']),email=esc(SITE['email']),year=SITE['updated'][:4],arrow=ARROW,chat_icon=icon('message-circle'))
def write(relative,text):
    path=ROOT/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text);GENERATED.append(relative)
def schema(path,title,desc,kind,record,crumbs):
    org={'@type':'Organization','@id':BASE+'/#organization','name':SITE['name'],'url':BASE+'/','email':SITE['email'],'telephone':'+'+SITE['whatsapp'],'logo':BASE+'/assets/images/logo.svg','description':'Independent document preparation and process guidance from Pakistan.'}
    page={'@type':'WebPage','@id':BASE+path+'#page','url':BASE+path,'name':title,'description':desc,'isPartOf':{'@id':BASE+'/#website'}}
    graph=[org,{'@type':'WebSite','@id':BASE+'/#website','name':SITE['name'],'url':BASE+'/'},page]
    if crumbs:graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':BASE+u} for i,(u,n) in enumerate([('/','Home')]+crumbs)]})
    if kind=='Service':graph.append({'@type':'Service','name':title,'description':desc,'url':BASE+path,'provider':{'@id':BASE+'/#organization'},'mainEntityOfPage':{'@id':BASE+path+'#page'}})
    if kind=='Article':graph.append({'@type':'Article','headline':title,'description':desc,'url':BASE+path,'mainEntityOfPage':{'@id':BASE+path+'#page'},'author':{'@type':'Organization','name':record['author'],'url':BASE+'/about/'},'publisher':{'@id':BASE+'/#organization'},'datePublished':record['published'],'dateModified':record['updated'],'image':BASE+'/assets/images/social-card.png'})
    return json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')
def save(path,title,desc,body,kind='WebPage',record=None,crumbs=None,noindex=False):
    html=template('base.html',title=esc(title),site_name=esc(SITE['name']),description=esc(desc),robots='noindex, follow' if noindex else 'index, follow, max-image-preview:large',canonical=BASE+path,og_type='article' if kind=='Article' else 'website',origin=BASE,schema=schema(path,title,desc,kind,record,crumbs),header=header(path),body=body,footer=footer())
    relative=path.lstrip('/') if path.endswith('.html') else path.lstrip('/')+'index.html'
    write(relative,html)
    if not noindex:PAGES[path]={'title':title,'description':desc}
def breadcrumbs(items):
    return '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'+''.join('<span aria-hidden="true">/</span>'+ (f'<a href="{u}">{esc(n)}</a>' if i<len(items)-1 else f'<span aria-current="page">{esc(n)}</span>') for i,(u,n) in enumerate(items))+'</nav>'
def pagehead(title,desc,path,label=None):return f'<header class="page-header"><div class="content-wrap">{breadcrumbs([(path,label or title)])}<span class="eyebrow">{esc(SITE["tagline"])}</span><h1>{title}</h1><p class="page-description">{esc(desc)}</p></div></header>'
def sourcebox(keys):
    if not keys:return ''
    return '<section><h2>Official sources</h2><div class="sources-box">'+''.join(f'<a href="{esc(SITE["sources"][k]["url"])}" rel="noopener">{esc(SITE["sources"][k]["label"])} {ARROW}</a>' for k in keys)+'</div><p class="small">Confirm current requirements with the competent institution. A source link is not an endorsement of our service.</p></section>'
def page_label(url):
    for group,records in [('services',SERVICES),('blog',BLOGS)]:
        for r in records:
            if url==f'/{group}/{r["slug"]}/':return r['title']
    return url.strip('/').replace('-',' ').title()
def related(urls):return '<section><h2>Continue exploring</h2><ul class="related-list">'+''.join(f'<li><a href="{esc(u)}">{esc(page_label(u))}{ARROW}</a></li>' for u in urls)+'</ul></section>' if urls else ''
def sections(items):return ''.join(f'<section><h2>{esc(s["title"])}</h2><p>{esc(s["text"])}</p></section>' for s in items)
def detail(record,group):
    kind='Article' if group=='blog' else 'Service';path=f'/{group}/{record["slug"]}/'
    meta=f'<div class="article-meta"><span>By {esc(record["author"])}</span><span>Published <time datetime="{record["published"]}">{record["published"]}</time></span><span>Updated <time datetime="{record["updated"]}">{record["updated"]}</time></span><span>{read_time(record)} min read</span></div>' if kind=='Article' else ''
    steps='<section><h2>Your preparation checklist</h2><ol>'+''.join('<li>'+esc(s)+'</li>' for s in record['steps'])+'</ol></section>' if record.get('steps') else ''
    crumb=[('/'+group+'/',group.title()),(path,record['title'])]
    body=template('detail.html',breadcrumbs=breadcrumbs(crumb),category=esc(record['category']),title=esc(record['title']),description=esc(record['description']),meta=meta,answer=esc(record['answer']),sections=sections(record['sections']),steps=steps,sources=sourcebox(record.get('sources',[])),related=related(record.get('related',[])),arrow=ARROW,cta=cta())
    save(path,record['title'],record['description'],body,kind,record,crumb)
def read_time(record):return max(2,round(len(' '.join(s['text'] for s in record['sections']).split())/180))
def service_card(s,i):
    return f'<article class="service"><div class="service-bar"></div><span class="service-num" aria-hidden="true">{i:02}</span><div class="service-body"><div class="service-head"><div class="service-icon">{icon(s["icon"])}</div><h3><a href="/services/{s["slug"]}/">{esc(s["title"])}</a></h3></div><p>{esc(s["description"])}</p><div class="service-tags"><span class="tag">{esc(s["category"])}</span><span class="tag">Independent guidance</span></div><a class="service-link" href="/services/{s["slug"]}/">Explore service {ARROW}</a></div></article>'
def blog_card(b):
    url='/blog/'+b['slug']+'/'
    return f'<article class="blog-card" data-blog-category="{esc(b["category"])}"><a href="{url}" class="blog-thumb" aria-label="Read {esc(b["title"])}"><span class="blog-thumb-tag">{esc(b["category"])}</span><span class="blog-thumb-icon">{icon(b["icon"])}</span></a><div class="blog-body"><div class="blog-meta"><span>{b["published"]}</span><span>{read_time(b)} min read</span></div><h3><a href="{url}">{esc(b["title"])}</a></h3><p>{esc(b["description"])}</p><a class="blog-read" href="{url}">Read article {ARROW}</a></div></article>'
JOURNEY=[('Understand','The actual request','Identify the document, issuer, destination and the organisation requesting it. Ask for its requirements in writing.','file-search'),('Compare','The details that matter','Check the records for differences. The issuer handles corrections; the receiving organisation decides what it accepts.','clipboard-check'),('Prepare','The questions to resolve','Check the official instructions, accepted format, applicant responsibilities and current charges before choosing paid assistance.','file-text'),('Proceed','The official channel','Use the permitted application channel. Keep your account and consent under your control. The competent institution makes the decision.','route')]
def journey():
    buttons=''.join(f'<button class="track-stage{ " active" if i==0 else ""}" type="button" aria-pressed="{str(i==0).lower()}" data-stage="{i}" data-title="{esc(title)}" data-detail="{esc(text)}">{icon(ic)}<strong>{i+1:02} · {title}</strong><small>{sub}</small></button>' for i,(title,sub,text,ic) in enumerate(JOURNEY))
    return f'<div class="tracker"><div class="track-timeline" aria-label="Explore preparation stages">{buttons}</div><div class="track-detail" aria-live="polite"><h3>{JOURNEY[0][0]}</h3><p>{JOURNEY[0][2]}</p></div><p class="track-note">Illustrative preparation steps · No live status, official fee or completion-time estimate.</p></div>'
def issue_cards(limit=None):
    issues=json.loads((ROOT/'content/issues.json').read_text())
    return ''.join(f'<article class="service"><div class="service-body"><div class="service-head"><div class="service-icon">{icon(x["icon"])}</div><h3>{esc(x["title"])}</h3></div><p>{esc(x["text"])}</p><a class="service-link" href="/blog/{x["guide"]}/">Understand the issue {ARROW}</a></div></article>' for x in issues[:limit])
def checker():
    data=[('document','What document do you have?',['Degree / transcript','Diploma / certificate','Personal document','Business / legal document','Other / not sure']),('destination','Where is it needed?',['Saudi Arabia','United Arab Emirates','Other / not sure']),('issue','What needs attention?',['No known issue','Name or identity difference','Missing record','University reply pending','Previous rejection','Not sure which process'])]
    fields=''
    for i,(name,title,options) in enumerate(data):
        labels=''.join(f'<label class="est-option"><input type="radio" name="{name}" value="{esc(x)}" required><span>{esc(x)}</span></label>' for x in options)
        fields+=f'<fieldset data-step="{i}"'+(' hidden disabled' if i else '')+f'><legend tabindex="-1">{title}</legend><div class="est-options">{labels}</div></fieldset>'
    return f'<form class="estimator" data-checker><div class="checker-meta"><span data-step-name>Document</span><span data-step-count>Step 1 of 3</span></div><div class="estimator-steps" aria-hidden="true"><span class="est-step-pip active"></span><span class="est-step-pip"></span><span class="est-step-pip"></span></div>{fields}<p class="checker-error" role="alert"></p><div class="est-nav"><button class="btn btn-outline" type="button" data-back hidden>Back</button><span class="small" data-local>Stays in this page</span><button class="btn btn-primary" type="submit" data-next>Continue {ARROW}</button></div><div class="checker-result" hidden><span class="eyebrow">Your preparation checklist</span><h2 tabindex="-1">Start with these questions.</h2><p class="result-summary"></p><ol class="result-steps"></ol><p class="result-note">General preparation guidance only. No official decision, mandatory sequence, eligibility, fee or processing time is determined by this tool.</p><div class="est-nav"><a class="btn btn-primary" data-case-contact href="/contact/">Prepare my enquiry {ARROW}</a><button class="btn btn-outline" type="button" data-reset>Start again</button></div></div><noscript><p>Please <a href="/contact/">contact us</a> with your document type, destination and issue. The interactive checker requires JavaScript.</p></noscript></form>'
def faq():
    records=json.loads((ROOT/'content/faq.json').read_text());cats=['All']+list(dict.fromkeys(r['category'] for r in records))
    filters='<div class="faq-controls" aria-label="Filter questions">'+''.join(f'<button type="button" data-faq-filter="{esc(c)}" aria-pressed="{str(c=="All").lower()}">{esc(c)}</button>' for c in cats)+'</div>'
    return filters+''.join(f'<details data-faq-category="{esc(r["category"])}"><summary>{esc(r["question"])}</summary><p>{esc(r["answer"])}</p></details>' for r in records)
def build():
    hero=(ROOT/'templates/partials/hero-visual.html').read_text()
    hero=re.sub(r'<i data-lucide="([^"]+)"[^>]*></i>',lambda m:icon(m[1]),hero)
    hero=hero.replace('<div class="holo-wrap">','<div class="holo-wrap" aria-hidden="true">').replace('      <div class="chip-float chip-4">','      <div class="chip-float chip-4">')
    hero=hero.rstrip();pos=hero.rfind('</div>');hero=hero[:pos]+'<span class="holo-caption">Illustrative document journey</span>'+hero[pos:]
    home=template('home.html',spark_icon=icon('zap'),arrow=ARROW,hero_visual=hero,services=''.join(service_card(s,i+1) for i,s in enumerate(SERVICES)),journey=journey(),document_icon=icon('file-text'),globe_icon=icon('globe'),chat_icon=icon('message-circle'),issues=issue_cards(3),blogs=''.join(blog_card(b) for b in BLOGS[:3]),shield_icon=icon('shield-check'),cta=cta())
    save('/','Your Documents. A Clearer Next Step.','Independent Mosadaqa, qualification-verification and Saudi/UAE document guidance from Pakistan. Clear preparation, without official-agent claims.',home)
    desc='Independent preparation and requirements guidance for academic verification, destination requests and document issues.'
    save('/services/','Specialist document guidance',desc,pagehead('Specialist guidance.<br><span class="accent">Clearly defined.</span>',desc,'/services/','Services')+'<section class="section"><div class="grid-services">'+''.join(service_card(s,i+1) for i,s in enumerate(SERVICES))+'</div></section>'+cta(),crumbs=[('/services/','Services')])
    for record in SERVICES:detail(record,'services')
    for record in BLOGS:detail(record,'blog')
    cats=sorted(set(b['category'] for b in BLOGS))
    tools='<div class="blog-tools"><label class="field">Search articles<input type="search" data-blog-search placeholder="Search a topic or question"></label><label class="field">Category<select data-blog-filter><option value="All">All categories</option>'+''.join(f'<option>{esc(c)}</option>' for c in cats)+'</select></label></div>'
    desc='Practical guides for understanding your document request before you submit.'
    body=pagehead('Guides &amp; <span class="accent">insights.</span>',desc,'/blog/','Blog')+'<section class="section">'+tools+f'<p class="filter-status" role="status">{len(BLOGS)} articles</p><div class="blog-grid home-blog">'+''.join(blog_card(b) for b in BLOGS)+'</div><p class="empty-message" hidden>No articles match. Try a different topic or choose all categories.</p></section>'+cta()
    save('/blog/','Guides & insights',desc,body,crumbs=[('/blog/','Blog')])
    desc='Name differences, missing documents and unresolved queries: identify the question before the next application.'
    save('/document-issues/','Document issues, understood',desc,pagehead('A complication.<br><span class="accent">A clearer next question.</span>',desc,'/document-issues/','Document issues')+'<section class="section"><div class="grid-services">'+issue_cards()+'</div></section>'+cta(),crumbs=[('/document-issues/','Document issues')])
    desc='Three simple choices to help organise your next questions. No files, official fees or promised timelines.'
    save('/check-documents/','Check your document situation',desc,pagehead('Find your <span class="accent">starting point.</span>',desc,'/check-documents/','Check my case')+'<section class="section">'+checker()+'</section>',crumbs=[('/check-documents/','Check my case')])
    save('/process/','A clearer preparation process','Understand the request, compare records and prepare for the correct official channel.',pagehead('From uncertainty<br>to <span class="accent">a clearer next step.</span>','Start with preparation. Official processes depend on the document and recipient.','/process/','Our process')+'<section class="section">'+journey()+'</section>'+cta(),crumbs=[('/process/','Our process')])
    save('/faq/','Frequently asked questions','Clear answers about independent guidance, document issues, fees and applicant responsibilities.',pagehead('Good questions.<br><span class="accent">Clear answers.</span>','Understand our role, what varies and what to check first.','/faq/','FAQs')+'<section class="section">'+faq()+'</section>'+cta(),crumbs=[('/faq/','FAQs')])
    for file in sorted((ROOT/'content/pages').glob('*.json')):
        r=json.loads(file.read_text());path='/'+r['slug']+'/'
        body=pagehead(esc(r['headline']),r['description'],path,r['title'])+'<div class="content-wrap article-layout"><article class="article-body">'+sections(r['sections'])+'</article><aside class="article-aside"><span class="eyebrow">A clear first conversation</span><h2>Start with your situation.</h2><p>No private files are needed for an initial enquiry.</p><a class="btn btn-primary" href="/contact/">Contact us '+ARROW+'</a></aside></div>'+cta()
        save(path,r['title'],r['description'],body,crumbs=[(path,r['title'])])
    contact=template('contact.html',phone=esc(SITE['phone_display']),whatsapp=WA,address=esc(SITE['address']),contact_note=esc(SITE['contact_note']),email=esc(SITE['email']),chat_icon=icon('message-circle'),mail_icon=icon('mail'),globe_icon=icon('globe'),arrow=ARROW)
    save('/contact/','Contact SK Attestation Services','Describe your document and situation. Prepare a WhatsApp or email enquiry without uploading sensitive files.',pagehead('Let’s make the<br><span class="accent">next step clearer.</span>','A document type, a destination and the issue you want to understand. That is enough to begin.','/contact/','Contact')+contact,crumbs=[('/contact/','Contact')])
    save('/sources/','Official source directory','Find the institutions and official platforms that publish and decide their own requirements.',pagehead('Go to <span class="accent">the source.</span>','These reference links do not imply appointment, partnership or endorsement.','/sources/','Official sources')+'<section class="section">'+sourcebox(list(SITE['sources']))+'</section>',crumbs=[('/sources/','Sources')])
    save('/404.html','Page not found','This page could not be found. Find services or browse the document blog.','<section class="not-found"><h1>404</h1><h2>Let’s find the right page.</h2><p>This address may have changed. Start with our current services or articles.</p><a class="btn btn-primary" href="/">Back to home</a> <a class="btn btn-outline" href="/blog/">Browse articles</a></section>',noindex=True)
    # Old URLs stay useful, but contain no former service offers or indexed content.
    for old,target in json.loads((ROOT/'content/redirects.json').read_text()).items():
        if old in PAGES:continue
        if target not in PAGES:raise ValueError('Invalid redirect target '+target)
        rel=old.lstrip('/') if old.endswith('.html') else old.lstrip('/')+'index.html'
        write(rel,f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page moved | {esc(SITE["name"])}</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="{BASE+target}"><meta http-equiv="refresh" content="0;url={target}"></head><body><p>Our website has changed. <a href="{target}">Continue to {esc(PAGES[target]["title"])}</a>.</p></body></html>')
    write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{BASE+p}</loc></url>\n' for p in sorted(PAGES))+'</urlset>\n')
    write('robots.txt','User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
    rss='<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>SK Attestation Services Blog</title><link>'+BASE+'/blog/</link><description>Independent document preparation guidance</description>'
    for b in BLOGS:
        url=BASE+'/blog/'+b['slug']+'/'
        rss+=f'<item><title>{esc(b["title"])}</title><link>{url}</link><guid>{url}</guid><description>{esc(b["description"])}</description></item>'
    write('feed.xml',rss+'</channel></rss>')
    write('llms.txt','# SK Attestation Services\n\nIndependent document preparation and process guidance. No official-agent appointment or authority to issue authentication is claimed.\n\n## Services\n'+''.join(f'- [{s["title"]}]({BASE}/services/{s["slug"]}/): {s["description"]}\n' for s in SERVICES)+'\n## Articles\n'+''.join(f'- [{b["title"]}]({BASE}/blog/{b["slug"]}/)\n' for b in BLOGS)+'\n## Scope\nOfficial platforms, issuers and recipients make decisions. Applicant-only and restricted steps must follow the official rules.\n')
    for stale in set(PREVIOUS)-set(GENERATED):
        target=(ROOT/stale).resolve()
        if target.is_relative_to(ROOT) and target.suffix=='.html' and target.is_file():target.unlink()
    (ROOT/'.build-manifest.json').write_text(json.dumps(sorted(set(GENERATED)),indent=2)+'\n')
    print(f'Built {len(PAGES)} public pages: {len(SERVICES)} services and {len(BLOGS)} articles. Legacy URLs are noindex redirects.')
if __name__=='__main__':build()
