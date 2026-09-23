#!/usr/bin/env python3
"""Dependency-free static site builder. Run from any directory with Python 3.10+."""
from pathlib import Path
from html import escape as e
import json
from urllib.parse import quote
from content import SOURCES, SERVICES, GUIDES, PROBLEMS, COUNTRIES, FAQS, BUSINESS, PUBLISHED, UPDATED, PUBLISHED_LABEL
ROOT=Path(__file__).resolve().parents[1]
BASE='https://ksa.salaroutsourcing.com'
PAGES={}
ARROW='<span aria-hidden="true">↗</span>'
def link(url,text,cls='text-link'):
    return f'<a class="{cls}" href="{e(url)}">{text} {ARROW}</a>'
def button(text='Check My Documents',url='/check-documents/',cls='btn'):
    return link(url,text,cls)
def wa_link(message=None):
    return 'https://wa.me/'+BUSINESS['whatsapp']+'?text='+quote(message or 'Hello SK Immigration Services, I need help with document attestation.')
def wa_button(label='WhatsApp us', message=None, cls='btn wa-btn'):
    return f'<a class="{cls}" href="{wa_link(message)}" rel="noopener"><span aria-hidden="true">✆</span> {label}</a>'
def contactstrip():
    return (f'<div class="topbar-strip"><div class="wrap"><span>Attestation desk · {BUSINESS["street"]}, {BUSINESS["locality"]}</span>'
            f'<span class="strip-links"><a href="tel:+{BUSINESS["whatsapp"]}">{BUSINESS["whatsappLabel"]}</a>'
            f'<a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a></span></div></div>')
def trustbar():
    return (f'<div class="trustbar"><div class="wrap"><strong>{BUSINESS["legalName"]}</strong>'
            f'<span>{BUSINESS["identifier"]}</span><span>{BUSINESS["street"]}, {BUSINESS["locality"]}</span>'
            f'<span>WhatsApp {BUSINESS["whatsappLabel"]}</span>'
            f'<span>Independent assistance — official decisions stay with the authorities</span>'
            f'<a href="{BUSINESS["verifyUrl"]}" rel="noopener">Verify our registration</a></div></div>')
def nap_strip():
    return (f'<div class="nap-strip"><p><strong>{BUSINESS["legalName"]}</strong> · {BUSINESS["identifier"]}<br>'
            f'{BUSINESS["street"]}, {BUSINESS["locality"]}, {BUSINESS["region"]}, Pakistan<br>'
            f'<a href="tel:+{BUSINESS["whatsapp"]}">{BUSINESS["telephone"]}</a> · <a href="{BUSINESS["maps"]}" rel="noopener">Get directions</a> · '
            f'<a href="{BUSINESS["verifyUrl"]}" rel="noopener">Verify our registration</a> · {BUSINESS["email"]}</p>'
            f'{wa_button("Message us on WhatsApp")}</div>')
def brand():
    return ('<a class="brand" href="/" aria-label="'+BUSINESS['name']+' home"><span class="brand-mark" aria-hidden="true">SK</span>'
            '<span><strong>'+BUSINESS['name']+'</strong><small>Attestation desk for Saudi Arabia, the UAE and the Gulf</small></span></a>')
def nav(path):
    items=[('/services/','Services'),('/guides/','Guides'),('/problems/','Document issues'),('/countries/saudi-arabia/','Saudi Arabia'),('/process/','Process'),('/contact/','Contact')]
    links=''.join(f'<a href="{u}"'+(' aria-current="page"' if path==u else '')+f'>{t}</a>' for u,t in items)
    return (f'<a class="skip" href="#main">Skip to content</a><header class="topbar">{contactstrip()}<div class="wrap nav">{brand()}'
            f'<nav class="nav-links" id="main-menu" aria-label="Main navigation">{links}</nav>'
            f'<div class="nav-actions">{wa_button("WhatsApp")}{button(cls="btn nav-cta")}</div>'
            f'<button type="button" class="menu-toggle" aria-controls="main-menu" aria-expanded="false"><span aria-hidden="true">Menu</span></button></div></header>')
FOOTER_LINKS={
 'Services':[('/services/mosadaqa-attestation/','Mosadaqa degree attestation'),('/services/saudi-culture-attestation/','Saudi Culture attestation'),('/services/saudi-embassy-attestation/','Saudi Embassy attestation'),('/services/qvp-attestation/','QVP attestation'),('/services/uae-embassy-attestation/','Apostille')],
 'Guidance':[('/guides/','All guides'),('/guides/mosadaqa-degree-attestation/','Mosadaqa: what it means'),('/guides/qvp-qualification-verification/','QVP verification'),('/guides/uae-embassy-attestation-process/','UAE attestation: stages'),('/sources/','Official sources')],
 'Document issues':[('/problems/degree-passport-name-mismatch/','Degree, passport, CNIC'),('/problems/mosadaqa-verification-query/','Mosadaqa or QVP query'),('/problems/document-rejected/','Rejected document'),('/problems/missing-document/','Missing document'),('/problems/','All document issues')],
 'Company':[('/about/','About us'),('/process/','Our process'),('/check-documents/','Check my document'),('/contact/','Contact and WhatsApp'),('/document-security/','Document security'),('/privacy/','Privacy'),('/terms/','Terms'),('/disclaimer/','Disclaimer')]
}
def footer():
    cols=''.join('<div><h3>'+title+'</h3><ul>'+''.join(f'<li><a href="{url}">{label}</a></li>' for url,label in ls)+'</ul></div>' for title,ls in FOOTER_LINKS.items())
    nap=(f'<div><h3>Office and contact</h3><ul><li>{BUSINESS["legalName"]}</li><li>{BUSINESS["identifier"]}</li>'
         f'<li>{BUSINESS["street"]}, {BUSINESS["locality"]}, {BUSINESS["region"]}, Pakistan</li>'
         f'<li><a href="tel:+{BUSINESS["whatsapp"]}">{BUSINESS["telephone"]}</a> · <a href="tel:+923045999859">{BUSINESS["officeLine"]}</a></li>'
         f'<li><a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a></li>'
         f'<li><a href="{BUSINESS["maps"]}" rel="noopener">Get directions</a> · <a href="{BUSINESS["verifyUrl"]}" rel="noopener">Verify our registration</a></li></ul></div>')
    return (f'<footer class="footer"><div class="wrap"><div class="footer-top">{brand()}'
            f'<div><p>Mosadaqa, Saudi Culture, Saudi Embassy, QVP and UAE Embassy attestation assistance for Pakistani documents.</p>{wa_button("Chat on WhatsApp")}</div></div>'
            f'<div class="footer-grid">{cols}{nap}</div>'
            f'<div class="footer-bottom"><span>© 2026 {BUSINESS["name"]}</span><p>Independent assistance. Official attestation, verification and acceptance decisions are made by the competent authorities and the receiving organisation.</p></div></div></footer>')
def cta():
    return (f'<section class="final-cta" id="contact"><div class="wrap"><div><p class="eyebrow">Start with a message</p>'
            f'<h2>Send the document type.<br>We map the stages.</h2><p>WhatsApp {BUSINESS["whatsappLabel"]} · {BUSINESS["street"]}, {BUSINESS["locality"]}. '
            f'Describe the document first — no scans or identity numbers are needed to begin.</p></div>'
            f'<div class="cta-actions">{wa_button("WhatsApp us now", "Hello SK Immigration Services, I need help with: ")}{button()}</div></div></section>')
def org_node():
    return {'@type':['Organization','ProfessionalService','LocalBusiness'],'@id':BUSINESS['entityId'],'name':BUSINESS['name'],'legalName':BUSINESS['legalName'],
     'alternateName':BUSINESS['alternateName'],'slogan':BUSINESS['slogan'],'description':BUSINESS['description'],'url':BUSINESS['entityUrl'],
     'email':BUSINESS['email'],'telephone':BUSINESS['telephone'],
     'logo':{'@type':'ImageObject','url':BUSINESS['logo'],'width':200,'height':60},'image':BASE+'/assets/social-card.png',
     'foundingDate':BUSINESS['foundingDate'],'identifier':{'@type':'PropertyValue','propertyID':'SECP CUIN','value':'0304985'},
     'address':{'@type':'PostalAddress','streetAddress':BUSINESS['street'],'addressLocality':BUSINESS['locality'],'addressRegion':BUSINESS['region'],'addressCountry':BUSINESS['country']},
     'contactPoint':[{'@type':'ContactPoint','contactType':'customer service','telephone':BUSINESS['telephone'],'email':BUSINESS['email'],'availableLanguage':['en','ur'],'areaServed':BUSINESS['country']},
                     {'@type':'ContactPoint','contactType':'office','telephone':BUSINESS['officeLine'],'email':BUSINESS['email'],'availableLanguage':['en','ur'],'areaServed':BUSINESS['country']}],
     'areaServed':[{'@type':'Country','name':c} for c in BUSINESS['areaServed']],'knowsAbout':BUSINESS['knowsAbout'],
     'sameAs':[BUSINESS['entityUrl'],BUSINESS['website'],BUSINESS['instagram']],'hasMap':BUSINESS['maps']}
def faq_node(items):
    return {'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in items]}
def save(path,title,desc,body,kind='WebPage',crumbs=None,extra=None,noindex=False):
    url=BASE+path
    org=org_node()
    page={'@type':'WebPage','@id':url+'#page','url':url,'name':title,'description':desc,'isPartOf':{'@id':BASE+'/#website'},'inLanguage':'en','isAccessibleForFree':True}
    if kind=='Article':page.update({'datePublished':PUBLISHED,'dateModified':UPDATED,'mainEntityOfPage':url})
    graph=[org,{'@type':'WebSite','@id':BASE+'/#website','url':BASE,'name':'SK Immigration Services','publisher':{'@id':BUSINESS['entityId']}},page]
    if crumbs:
        graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':name,'item':BASE+u} for i,(u,name) in enumerate([('/','Home')]+crumbs)]})
    if extra: graph.extend(extra if isinstance(extra,list) else [extra])
    article_meta=(f'<meta property="article:published_time" content="{PUBLISHED}"><meta property="article:modified_time" content="{UPDATED}">' if kind=='Article' else '')
    schema=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} | SK Immigration Services</title><meta name="description" content="{e(desc)}"><meta name="robots" content="{'noindex, follow' if noindex else 'index, follow, max-snippet:-1, max-image-preview:large'}"><meta name="theme-color" content="#101f2c"><link rel="canonical" href="{url}"><meta property="og:type" content="{'article' if kind=='Article' else 'website'}"><meta property="og:locale" content="en_PK">{article_meta}<meta property="og:site_name" content="SK Immigration Services"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/social-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="SK Immigration Services. Your Documents. The Right Path."><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{BASE}/assets/social-card.png"><link rel="alternate" type="application/atom+xml" title="SK Immigration Services guides and updates" href="/feed.xml"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/manrope.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/styles.css"><script type="application/ld+json">{schema}</script><script src="/script.js" defer></script></head><body>{nav(path)}<main id="main">{body}</main>{footer()}</body></html>'''
    dest=ROOT/(path.lstrip('/') if path.endswith('.html') else path.lstrip('/')+'index.html')
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(html)
    if not noindex:PAGES[path]=title

def heading(eyebrow,title,desc='',right=''):
    return f'<div class="section-head"><div><p class="eyebrow">{eyebrow}</p><h2>{title}</h2></div>{right or ("<p>"+desc+"</p>" if desc else "")}</div>'
def pagehead(title,desc,crumbs,category='A clearer document journey'):
    trail='<a href="/">Home</a>'+''.join(f'<span aria-hidden="true">/</span>'+ (f'<a href="{u}">{e(n)}</a>' if i<len(crumbs)-1 else f'<span aria-current="page">{e(n)}</span>') for i,(u,n) in enumerate(crumbs))
    return f'<header class="page-head"><div class="wrap"><nav class="breadcrumbs" aria-label="Breadcrumb">{trail}</nav><p class="eyebrow">{category}</p><h1>{title}</h1><p class="lede">{desc}</p></div></header>'
def sourcebox(keys):
    return '<div class="source-list">'+''.join(f'<a href="{e(SOURCES[k][1])}" rel="noopener">{SOURCES[k][0]} ↗</a>' for k in keys)+'</div>'
def relatedbox(urls):
    def label(u):
        slug=u.rstrip('/').split('/')[-1]
        for x in SERVICES+GUIDES+PROBLEMS:
            if x['slug']==slug:return x['title']
        if slug=='check-documents':return 'Check My Documents'
        return slug.replace('-',' ').capitalize()
    return '<div class="rows">'+''.join(link(u,label(u),'row-link') for u in urls)+'</div>'
def article(path,title,desc,answer,sections,sources,related,category,kind='WebPage',extra=None,faqs=None):
    parts=path.strip('/').split('/');crumbs=[('/'+parts[0]+'/',parts[0].replace('-',' ').title()),(path,title)] if len(parts)>1 else [(path,title)]
    content=f'<div class="answer-box"><p class="eyebrow">The short answer</p><p>{answer}</p></div>'
    content+=''.join(f'<section><h2>{h}</h2>{p if p.startswith("<") else "<p>"+p+"</p>"}</section>' for h,p in sections)
    if sources:content+='<section><h2>Official sources</h2>'+sourcebox(sources)+'<p class="small">Confirm current requirements directly with the competent authority before submitting or paying fees.</p></section>'
    if kind=='Article':
        content+='<section><h2>Our assistance</h2><p>We help identify the relevant requirements, organise preparation questions and explain applicable submission options. Official decisions remain with the authorities.</p><h2>Questions before you submit</h2><details><summary>Is this an official determination?</summary><p>No. This is general preparation guidance. The competent authority and receiving organisation decide what is acceptable.</p></details><details><summary>Can I ask about my particular situation?</summary><p>Yes. Start with a document assessment without uploading a file. An individual review may be needed before selecting a submission route.</p></details></section>'
        if faqs:content+='<section><h2>Frequently asked questions</h2>'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)+'</section>'
        content+='<p class="meta-line">Published by SK Immigration Services · Editorial update: '+PUBLISHED_LABEL+'<br>General preparation guidance. See our <a href="/editorial-policy/">editorial policy</a>.</p>'
    if related:content+='<section><h2>Related guidance</h2>'+relatedbox(related)+'</section>'
    aside=f'<aside class="aside-box"><p class="eyebrow">Your situation matters</p><h3>Find your next step.</h3><p>Tell us what you have and where it is going. No document uploads to begin.</p>{button()}<p>Independent assistance.<br>Official decisions stay with the authorities.</p></aside>'
    nodes=[extra] if extra else []
    if faqs:nodes.append(faq_node(faqs))
    save(path,title,desc,pagehead(title,desc,crumbs,category)+f'<div class="wrap content-layout"><article class="article-content">{content}</article>{aside}</div>'+cta(),kind=kind,crumbs=crumbs,extra=nodes)

def scene():
    return '''<div class="document-scene"><span class="scene-label">DOCUMENT INTELLIGENCE / A CLEARER JOURNEY</span><div class="orbit" aria-hidden="true"></div><div class="paper-stack" aria-hidden="true"><div class="paper"><div class="paper-top"><span>ACADEMIC RECORD</span><span>01 / PK</span></div><p class="paper-title" data-paper-title>Degree<br>Certificate</p><p class="paper-sub">YOUR NEXT CHAPTER STARTS HERE</p><div class="paper-lines"><i></i><i></i><i></i></div><div class="paper-seal">✳</div><div class="scan"></div></div></div><div class="floating-label"><span>✓</span> Clarity before submission</div><div class="scene-doc-tabs" aria-label="Preview document type"><button type="button" data-doc="Degree" aria-pressed="true">Degree</button><button type="button" data-doc="Transcript" aria-pressed="false">Transcript</button><button type="button" data-doc="Passport" aria-pressed="false">Passport</button><button type="button" data-doc="Certificate" aria-pressed="false">Certificate</button></div><div class="route-line" aria-hidden="true"></div><div class="destination-tag"><span class="globe-icon" aria-hidden="true">◎</span><div><small>THE DESTINATION</small><strong>Your next opportunity</strong></div></div><span class="scene-bottom">ILLUSTRATIVE PATH · NOT A LIVE STATUS</span></div>'''
# choices() retired in the service-focus change set
def servicecards():
    return '<div class="service-grid">'+''.join(f'<a class="service-card" href="/services/{s["slug"]}/"><div class="card-top"><span>0{i+1} / ASSISTANCE</span><span class="service-symbol" aria-hidden="true">{s["symbol"]}</span></div><h3>{s["title"]}</h3><p>{s.get("summary",s["desc"])}</p><span class="card-bottom">Explore service {ARROW}</span></a>' for i,s in enumerate(SERVICES))+'</div>'
def assessment():
    fields=[('service','Which service do you need?',[s['title'] for s in SERVICES]+['Not sure yet']),
     ('document','What document is it?',['Degree','Diploma','Transcript','Certificate','Other']),
     ('country','Where will it be used?',list(COUNTRIES)),
     ('issue','Is there any problem with it?',['No problem','Name mismatch','Father’s name mismatch','Spelling mistake','Date-of-birth mismatch','Mosadaqa or QVP query','Rejected or refused','Missing document','Not sure'])]
    form=''
    for i,(name,title,options) in enumerate(fields):
        opts=''.join(f'<label class="option"><input type="radio" name="{name}" value="{e(o)}" required><span>{e(o)}</span></label>' for o in options)
        form+=f'<fieldset data-step="{i}"'+(' hidden disabled' if i else '')+f'><legend tabindex="-1">{title}</legend><div class="options">{opts}</div></fieldset>'
    waass=wa_button('Send this on WhatsApp','Hello SK Immigration Services, I need help with: ').replace('class="btn wa-btn"','class="btn wa-btn request-whatsapp" data-wa-base="https://wa.me/923105507819"')
    walink=wa_link()
    return f'''<div class="assessment-layout"><div class="assessment-intro"><p class="eyebrow">Your document, understood</p><h2>Not sure which<br>stage you need?</h2><p>Mosadaqa, Saudi Culture, Saudi Embassy, QVP or apostille. Four questions tell us where to start.</p><div class="assessment-notes"><span>Four simple questions</span><span>No files or identity numbers needed</span><span>A starting point, before you submit</span></div></div><form class="assessment" data-assessment><div class="step-meta"><span data-step-label>01 / Service</span><span data-step-count>Step 1 of 4</span></div><div class="progress" role="progressbar" aria-label="Assessment progress" aria-valuemin="0" aria-valuemax="4" aria-valuenow="1"><i></i></div>{form}<p class="error" role="alert"></p><div class="form-controls"><button class="back-button" type="button" data-back hidden>← Back</button><span class="small" data-local-note>Stays in your browser</span><button class="btn" type="submit" data-next>Continue <span aria-hidden="true">→</span></button></div><div class="result" hidden><p class="eyebrow">Your document path</p><h3 tabindex="-1">A clearer starting point.</h3><p class="result-summary"></p><ol class="result-path"></ol><p class="result-notice">This is general guidance, not an official determination. Stages are conditional; do not assume every stage is required.</p><div class="actions">{waass}{button('Request a Document Assessment','/contact/','btn request-assessment')}<button class="restart" type="button">Start again ↺</button></div></div><noscript><p>JavaScript is needed for the guided assessment. You can <a href="{walink}">message us on WhatsApp</a> or <a href="/contact/">send the document type by email</a>.</p></noscript></form></div>'''
def problemcards():
    return '<div class="problems-grid">'+''.join(f'<a class="problem-card" href="/problems/{p["slug"]}/"><small>0{i+1} /</small><h3>{p["title"]}</h3><p>{p["tag"]} {ARROW}</p></a>' for i,p in enumerate(PROBLEMS))+'</div>'
def mismatch():
    return f'''<div class="mismatch"><div class="mismatch-demo"><div class="name-record"><div><small>Passport · illustrative example</small><strong>Muhammad Ali <mark>Khan</mark></strong></div><div class="doc-icon" aria-hidden="true"></div></div><div class="name-record"><div><small>Degree · illustrative example</small><strong>Muhammad Ali</strong></div><div class="doc-icon" aria-hidden="true"></div></div><div class="difference"><i aria-hidden="true"></i> NAME DIFFERENCE</div></div><div><p class="eyebrow">Small difference. Important question.</p><h2>Same person.<br>Different name?</h2><p>Do not alter documents blindly. Identify which authority needs to correct or verify the record.</p><div class="actions">{link('/guides/degree-name-different-from-passport/','Understand name mismatches')}</div></div></div>'''
JOURNEY=[('Identify','What document do you have?','Start with the exact document title, issuer, destination and purpose. Keep personal identifiers out of your first enquiry.'),('Verify','Who issued it?','Compare the details against the issuer’s records. Ask the responsible institution about any mismatch before arranging authentication.'),('Prepare','What comes first?','Confirm the current official checklist, accepted formats and submission arrangements. Keep originals with you until the route is clear.'),('Attest','The relevant authority','The competent authority makes its decision. HEC, IBCC or another authority may be relevant depending on your document.'),('Legalize','The applicable route','Confirm whether an apostille, embassy route or another process applies. Not every document needs every stage.'),('Ready','For your next chapter','Check the completed document against the recipient’s instructions. Authentication does not guarantee recognition or acceptance.')]
def journey():
    controls=''.join(f'<button type="button" data-journey="{i}" data-description="{e(d)}" aria-pressed="{str(i==0).lower()}"><small>0{i+1}</small><strong>{t}</strong><span class="j-question">{q}</span></button>' for i,(t,q,d) in enumerate(JOURNEY))
    return f'<div class="journey" aria-label="Explore the document journey">{controls}</div><div class="journey-detail"><div class="doc-icon" aria-hidden="true"></div><p aria-live="polite">{JOURNEY[0][2]}</p></div>'
def map_svg():
    return '''<svg class="map" viewBox="0 0 600 320" role="img" aria-label="Illustrative world map connecting Pakistan with international destinations"><defs><pattern id="dots" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#a9b29f"/></pattern></defs><g fill="url(#dots)"><path d="M34 76 66 44 111 34 138 52 160 50 196 76 166 99 154 128 122 136 114 156 95 146 78 124 53 119 47 99Z M166 160 196 166 218 184 214 211 199 242 184 279 169 271 158 245 148 222 142 195Z M204 33 239 26 251 42 237 71 220 77 204 59Z M272 88 289 65 322 58 338 77 329 103 305 116 281 110Z M278 125 319 113 347 132 359 163 341 198 329 232 308 229 293 202 272 177 263 144Z M337 70 366 48 413 52 442 44 467 54 502 58 548 85 565 107 541 128 509 133 491 159 465 173 451 193 431 178 416 142 396 150 371 131 347 113Z M461 205 478 200 492 215 478 229Z M493 232 525 223 546 241 548 270 527 280 491 263 481 247Z M567 275 576 266 580 280 570 289Z"/></g><path class="connection" d="M396 139 Q348 84 295 91 M396 139 Q286 14 110 98 M396 139 Q486 158 525 250 M396 139 Q377 134 360 158"/><circle cx="396" cy="139" r="5"/><circle cx="295" cy="91" r="3"/><circle cx="110" cy="98" r="3"/><circle cx="525" cy="250" r="3"/><circle cx="360" cy="158" r="3"/><text x="403" y="133">Pakistan</text></svg>'''
def destinations():
    options='<option value="">Select a destination</option>'+''.join(f'<option value="{e(k)}">{e(k)}</option>' for k in COUNTRIES)
    rows=''.join(f'<div class="destination-row" data-destination-key="{e(k)}"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k,v in COUNTRIES.items())
    return (f'<div class="destination-layout"><div>{map_svg()}</div><div class="destination-panel"><label for="destination">Choose your destination</label>'
      f'<select id="destination" data-destination>{options}</select><p class="destination-copy" aria-live="polite"></p>'
      f'<p class="mini-route">Issuer → Education authority → MOFA Pakistan → Saudi-side stage</p>'
      f'<div class="actions">{link("/countries/saudi-arabia/","Saudi Arabia guidance","text-link destination-guide")}{link("/services/mosadaqa-attestation/","Mosadaqa service")}{wa_button("Ask on WhatsApp","Hello SK Immigration Services, my document will be used in: ")}</div>'
      f'<p class="small">Illustrative stages. Requirements are not identical across destinations; the receiving organisation decides.</p></div></div>'
      f'<div class="destination-list"><h2>Preparation questions by destination</h2><dl>{rows}</dl><p class="small">Every destination in the selector is described in text on this page, so the guidance can be read without scripts.</p></div>')
def authority():
    return heading('Clearly independent','Who performs the<br>official attestation?','The distinction matters. Official authority and private assistance have different roles.')+'<div class="authority-grid">'+''.join(f'<div class="authority-item"><strong>{n}</strong><span>Official authority</span></div>' for n in ['HEC','IBCC','MOFA Pakistan','Saudi missions','Apostille authority','NADRA & DGIP'])+'</div>'+f'<div class="private-row"><div class="private-badge">SK Immigration Services<small>Independent assistance</small></div><p>These authorities make the official decisions. We provide independent professional assistance with preparation, requirements and applicable submission routes.</p></div>'
def guidecards():
    return '<div class="guide-grid">'+''.join(f'<article class="guide-card"><a href="/guides/{g["slug"]}/" class="guide-art" aria-label="Read: {e(g["title"])}"><div class="doc-icon" aria-hidden="true"></div><span aria-hidden="true">{["≠","→","/"][i]}</span><div class="doc-icon" aria-hidden="true"></div></a><div class="guide-meta"><span>{g["category"]}</span><span>3 min read</span></div><h3><a href="/guides/{g["slug"]}/">{g["title"]}</a></h3><p>{g.get("summary",g["desc"])}</p>{link("/guides/"+g["slug"]+"/","Read the guide")}</article>' for i,g in enumerate(GUIDES[:3]))+'</div>'
def faqs():
    filters=''.join(f'<button type="button" data-faq-filter="{c}" aria-pressed="{str(c=="All").lower()}">{c}</button>' for c in ['All']+sorted({c for c,_,_ in FAQS}))
    questions=''.join(f'<details data-faq-category="{c}"><summary>{q}</summary><p>{a}</p></details>' for c,q,a in FAQS)
    return f'<div class="faq-layout"><div><p class="eyebrow">Good questions. Clear answers.</p><h2>A little clarity<br>goes a long way.</h2><div class="faq-filters" aria-label="Filter questions">{filters}</div></div><div>{questions}</div></div>'
def build_home():
    body=f'''<section class="hero"><div class="wrap hero-inner"><div><p class="eyebrow">From Pakistan. For your next chapter.</p><h1>Your Documents.<br><span>The Right Path.</span></h1><p class="hero-description">Mosadaqa, Saudi Culture, Saudi Embassy, QVP and UAE Embassy attestation assistance for Pakistani documents — with clear guidance before you submit.</p><div class="actions">{button(cls='btn light')}{button('Explore Services','/services/','btn outline')}</div><p class="hero-trust"><b aria-hidden="true">◇</b> Independent assistance. Official processes. Clear guidance.</p></div>{scene()}</div><div class="wrap hero-foot"><span class="tiny-label">Guidance for official<br>document processes</span><strong>HEC</strong><strong>IBCC</strong><strong>MOFA</strong><strong>APOSTILLE</strong><strong>EMBASSIES</strong><span class="tiny-label">Independent.<br>Not government affiliated.</span></div></section><div class="path-strip"><div class="wrap"><span>A clearer journey</span><b>Your document</b><i>→</i><b>Verification</b><i>→</i><b>The right authority</b><i>→</i><b>Your destination</b></div></div>'''
    body+=trustbar()
    body+=f'<section class="section service-section" id="services"><div class="wrap">{heading("Expertise, with clarity","The right help.<br>At the right stage.",right=link("/services/","Explore all services"))}{servicecards()}</div></section>'
    body+=f'<section class="section assessment-section" id="assessment"><div class="wrap">{assessment()}</div></section>'
    body+=f'<section class="section" id="problems"><div class="wrap">{heading("When the path isn’t straightforward","Something isn’t right<br>with your document?",right=link("/check-documents/","Check My Case"))}{problemcards()}{mismatch()}</div></section>'
    body+=f'<section class="section process-section" id="process"><div class="wrap">{heading("From document to destination","Every stage.<br>A little more certainty.","Explore the journey. Your document may need some of these stages, depending on its purpose and destination.")}{journey()}</div></section>'
    body+=f'<section class="section" id="countries"><div class="wrap">{heading("Ready for what’s next","Where are your<br>documents going?","A destination is more than a country. It’s a specific set of requirements.")}{destinations()}</div></section>'
    body+=f'<section class="section authority-section"><div class="wrap">{authority()}</div></section>'
    body+=f'<section class="section service-section"><div class="wrap">{heading("Document knowledge center","Understand it.<br>Before you submit it.",right=link("/guides/","Explore the knowledge center"))}{guidecards()}</div></section>'
    body+=f'<section class="section" id="faq"><div class="wrap">{faqs()}</div></section>'
    body+=f'<div class="wrap"><section class="security"><div><p class="eyebrow">Care starts with the first question</p><h3>Your documents contain<br>sensitive information.</h3></div><div><p>Start with a description, not a document upload. The assessment runs in your browser and asks for no identity numbers. Before sharing files, clarify who will handle them, why they are needed and how long they will be kept.</p>{link("/document-security/","How to share information carefully")}</div></section></div>'+cta()
    save('/','Your Documents. The Right Path.','Independent attestation, Apostille and legalization assistance from Pakistan. Check your document pathway before you submit.',body,extra=faq_node([(q,a) for _,q,a in FAQS]))

def build_pages():
    save('/services/','Attestation services','Five services for Pakistani documents: Mosadaqa and QVP verification, Saudi Culture and Saudi Embassy attestation, and UAE Embassy attestation.',pagehead('Five services.<br>One clear sequence.','We assist only with Mosadaqa, Saudi Culture attestation, Saudi Embassy attestation, QVP qualification verification and apostille. Each service page explains the stages, the records that must match and what we cannot decide for you.',[('/services/','Services')])+f'<section class="section service-section"><div class="wrap"><h2 class="sr-only">Our services</h2>{servicecards()}</div></section>'+cta(),crumbs=[('/services/','Services')])
    for s in SERVICES:
        url='/services/'+s['slug']+'/'
        sections=[('Who this is for',s['audience'])]+list(s['steps'])+[('What to have ready','<ul>'+''.join(f'<li>{e(c)}</li>' for c in s['check'])+'</ul>')]
        service={'@type':'Service','@id':BASE+url+'#service','name':s['title'],'description':s['desc'],'provider':{'@id':BUSINESS['entityId']},'url':BASE+url,'areaServed':{'@type':'Country','name':'Pakistan'},'serviceType':s['title'],'mentions':[{'@type':'Thing','name':SOURCES[k][0],'url':SOURCES[k][1]} for k in s['sources']]}
        article(url,s['title'],s['desc'],s['answer'],sections,s['sources'],s['related'],s['category'],faqs=s['faqs'],extra=service)
    for p in PROBLEMS:
        article('/problems/'+p['slug']+'/',p['title'],p['desc'],p['answer'],p['sections'],p.get('sources',['hec','ibcc','mofa','nadra']),['/guides/'+p['guide']+'/','/check-documents/'],'Document problem')
    save('/problems/','Document problems, understood','Name mismatches, rejected records, missing documents and Mosadaqa queries: identify the issue and the responsible issuer before you pay for a stage.',pagehead('A complication.<br>Not a dead end.','Identify the issue before choosing the next step.',[('/problems/','Problems')])+f'<section class="section"><div class="wrap"><h2 class="sr-only">Document problem cases</h2>{problemcards()}{mismatch()}</div></section>'+cta(),crumbs=[('/problems/','Problems')])
    save('/guides/','Document Knowledge Center','Read source-linked guidance on attestation, apostille, verification and document problems before you submit a file or pay for a stage.',pagehead('Document<br>Knowledge Center','Understand your documents before you submit them.',[('/guides/','Guides')])+f'<section class="section"><div class="wrap"><h2 class="sr-only">Guides</h2>{guidecards()}<div class="rows" style="margin-top:45px">'+''.join(link('/guides/'+g['slug']+'/',g['title'],'row-link') for g in GUIDES[3:])+f'</div><p class="meta-line">Published by SK Immigration Services. Editorial updates: '+PUBLISHED_LABEL+'. Each guide links to official sources and distinguishes preparation guidance from official requirements.</p></div></section>'+cta(),crumbs=[('/guides/','Guides')])
    for g in GUIDES:
        if g['slug']=='hec-vs-ibcc':
            g['sections'].insert(1, ('Compare the starting points', '<table class="content-table"><thead><tr><th>Document</th><th>Starting enquiry</th></tr></thead><tbody><tr><td>University degree or transcript</td><td>HEC scope and issuing university</td></tr><tr><td>School-level certificate</td><td>IBCC scope and awarding board</td></tr><tr><td>Technical diploma or certificate</td><td>Exact qualification and competent awarding body</td></tr></tbody></table>'))
        url='/guides/'+g['slug']+'/'
        article(url,g['title'],g['desc'],g['answer'],g['sections'],g['sources'],g['related'],g['category'],kind='Article',faqs=g.get('faqs'),extra={'@type':'Article','@id':BASE+url+'#article','headline':g['title'],'description':g['desc'],'author':{'@id':BUSINESS['entityId']},'publisher':{'@id':BUSINESS['entityId']},'mainEntityOfPage':BASE+url,'datePublished':PUBLISHED,'dateModified':UPDATED,'image':BASE+'/assets/social-card.png','isAccessibleForFree':True,'inLanguage':'en','mentions':[{'@type':'Thing','name':SOURCES[k][0],'url':SOURCES[k][1]} for k in g['sources']]})
    save('/check-documents/','Check My Documents','Four questions to identify the checks your document may need, including the details that must match before an attestation stage.',pagehead('A clearer path<br>starts here.','Choose your document, destination, purpose and any issue. Your answers stay in this page until you choose to prepare an email request.',[('/check-documents/','Check my documents')])+f'<section class="section assessment-section"><div class="wrap">{assessment()}</div></section>',crumbs=[('/check-documents/','Check my documents')])
    save('/process/','From document to destination','See how assessment, preparation, verification, attestation and the applicable legalization stages fit together for your document.',pagehead('From document<br>to destination.','A considered sequence, shaped around your document and the organisation receiving it.',[('/process/','Our process')])+f'<section class="section process-section"><div class="wrap">{journey()}</div></section><section class="section"><div class="wrap"><h2 class="sr-only">Questions we work through</h2>'+''.join(f'<div class="security"><div><p class="eyebrow">0{i+1} / {t}</p><h3>{q}</h3></div><div><div class="doc-icon" aria-hidden="true" style="margin-bottom:18px"></div><p>{d}</p></div></div>' for i,(t,q,d) in enumerate(JOURNEY))+'</div></section>'+cta(),crumbs=[('/process/','Our process')])
    article('/countries/saudi-arabia/','Documents for Saudi Arabia','Saudi Arabia: clarify whether the request is Mosadaqa verification, QVP, an attestation stage or a combination, and keep its exact wording.',COUNTRIES['Saudi Arabia'],[('Academic verification, often called mosadaqa','Ask the requesting organisation whether it needs an academic record verified (the process commonly called mosadaqa), an authenticated original or both. Keep its exact wording, and confirm whether the submission is made electronically or as a document. Our <a href="/guides/mosadaqa-degree-attestation/">mosadaqa guide</a> sets out the stages and the records that are compared.'),('Record details are checked, not only stamps','A verification query usually concerns the record itself: a surname missing on the degree, a different father’s name, or a spelling difference between the CNIC and the passport. See <a href="/problems/degree-passport-name-mismatch/">degree, passport and CNIC name mismatch</a>.'),('Employment requests','Ask whether the request concerns authentication, academic verification or professional recognition. These are different checks, and a professional body may add its own requirements.'),('Technical occupations','A trade test or skills verification request is distinct from document attestation. Check the relevant programme and official booking route before making arrangements.'),('Your preparation checklist','<ol><li>Identify the Saudi organisation requesting the document.</li><li>Confirm the purpose and the exact qualification or record.</li><li>Compare the degree, transcript, CNIC and passport details.</li><li>Check official verification and the applicable legalization instructions.</li><li>Ask about translations and any further recipient-specific checks.</li></ol>'),('What varies','Do not assume that Saudi-bound documents always require an embassy route or always qualify for an apostille. Check treaty applicability, document scope and the recipient’s instructions.')],['mosadaqa','saudi','hec','mofa'],['/guides/mosadaqa-degree-attestation/','/problems/mosadaqa-verification-query/','/services/qvp-attestation/'],'Destination guidance')

def trust_pages():
    pages={
     'about':('Independent assistance.<br>Clear responsibility.','About SK Immigration Services','SK Immigration Services is a private document-assistance service for people preparing documents from Pakistan for international use.',[('What we do','We help explain document requirements, identify relevant authorities and organise preparation questions. Submission assistance is subject to the official rules for each document and authority.'),('What we do not decide','We do not issue government attestations or act as HEC, IBCC, MOFA, NAVTTC or an embassy. Eligibility, verification, corrections and acceptance remain with the competent institutions.'),('Our approach','Start with the document, clarify the destination and explain what needs to be checked. No invented guarantees, fixed government outcomes or claimed official partnerships.')]),
     'editorial-policy':('Clarity begins<br>with good sources.','Editorial policy','Our content separates preparation guidance from official requirements.',[('Sources and scope','Use the linked authority’s current instructions for submission decisions. Our guides explain questions and preparation steps; they are not official checklists or legal determinations.'),('Dates and reviewers','An editorial update date records a change to the page. It does not certify that every government rule was independently rechecked on that date. A named professional reviewer is identified only when a review has been completed and their role verified.'),('Corrections','Send the page link and a description of the issue to info@salaroutsourcing.com. Do not attach personal document scans. Official requirements take precedence over this website.'),('No manufactured trust','We do not publish fabricated reviews, acceptance statistics, qualifications or official affiliations. Source references are not endorsements of this business.')]),
     'document-security':('Important documents.<br>Considered sharing.','Document security','Your documents contain sensitive information. Share only what is needed for the current step.',[('What this website collects','The assessment uses document categories, destination, purpose and issue selections within the current page. It has no file upload and does not save answers in browser storage or send them automatically.'),('When you choose to contact us','The contact tool prepares an email draft in your own email application. The email is only sent when you send it there. Start with a general description; leave out passport numbers, identity numbers, scans and private case references.'),('Before sharing files','Ask who will access them, why each file is necessary, which transfer method to use, how long copies will be retained and how deletion is handled. This site does not provide a secure document vault or claim verified encryption for email.'),('Access, retention and deletion','Files sent by email are handled outside this website. Request the applicable access, retention and deletion arrangements before sending files. Email info@salaroutsourcing.com for access or deletion enquiries. Do not assume immediate or guaranteed deletion.')]),
     'privacy':('Your information.<br>A clear starting point.','Privacy information','This page describes the data flows implemented on this website.',[('Browsing','The static host may process connection information such as IP addresses and request logs. This website does not include analytics trackers, advertising scripts, account registration or third-party font requests.'),('Assessment answers','Selections exist in the page’s memory. They are not automatically transmitted, stored in local storage or saved in cookies. A reload clears them. Choosing a document assessment request passes only the category selections to the contact page in a URL fragment.'),('Email enquiries','The contact form prepares a draft using your email application. Nothing is submitted to a website form server. Once you send the email, your email provider and the recipient’s email systems process it. Include only the information needed for your question.'),('Retention and requests','This website does not operate a document database. Email access, retention and deletion depend on the operator’s email handling arrangements; a fixed retention schedule is not stated. Contact info@salaroutsourcing.com to ask about those arrangements or request deletion.'),('External links','Official authority sites have their own privacy practices. Following an external source link takes you to that provider.')]),
     'terms':('Clear expectations.<br>Before you begin.','Website terms of use','Use this website as a preparation resource for independent document assistance.',[('Information and official decisions','Content and assessment results are general guidance. Authorities and recipients set and decide their own requirements. Confirm the current official rules before submitting, travelling or paying fees.'),('Service arrangements','An enquiry does not create a paid service agreement. Any scope, assistance fee, third-party charges, handling arrangements and cancellation terms must be agreed separately before paid work begins.'),('Your documents','Provide accurate information. Do not alter official records or ask for fabricated stamps, credentials or approvals. Corrections must go through the responsible issuer.'),('Outcomes and timing','No approval, acceptance, turnaround or government outcome is guaranteed by this website. Delays and decisions may be outside a private assistance provider’s control.')]),
     'disclaimer':('Independent assistance.<br>Official processes.','Service disclaimer','SK Immigration Services is a private assistance service, not a government authority.',[('No government affiliation','We do not claim to be government approved, an official HEC or MOFA agent, an embassy representative or a government partner. References to authority names explain the process only.'),('Conditional guidance','Assessment paths are illustrative checks, not official instructions or a requirement to complete every stage. Requirements depend on the issuer, document, destination, purpose and recipient.'),('No legal determination','Guides do not replace advice from a qualified professional or an official decision. For legal instruments, disputes and immigration eligibility, obtain the appropriate professional or official advice.')])
    }
    METADESCRIPTIONS={
     'about':'Independent document assistance from Pakistan: what SK Immigration Services does, what we do not decide, and how we approach preparation and official processes.',
     'editorial-policy':'How this site sources, dates and corrects its guidance, and why preparation guidance is separated from official requirements.',
     'document-security':'What this website collects, when an email draft is prepared, and how to share sensitive documents with the parties who need them.',
     'privacy':'How browsing data, assessment answers and email enquiries are handled on this static website, and how to ask about access or deletion.',
     'terms':'The basis on which this website and its guidance may be used: information limits, service arrangements, documents and outcomes.',
     'disclaimer':'SK Immigration Services is a private assistance service, not a government authority, and does not decide eligibility, verification or acceptance.',
    }
    for slug,(title,label,desc,sections) in pages.items():
        article('/'+slug+'/',label,METADESCRIPTIONS[slug],desc,sections,[],['/contact/','/sources/'],title.replace('<br>',' '))
    article('/sources/','Start with the official source','Direct links to the institutions that publish and decide their own requirements for attestation, verification and legalization.','Authority links are provided for reference. Their inclusion does not imply endorsement, appointment or partnership.',[('How to use an official source','Find the exact document category, current application route and prerequisites. If the page does not answer your situation, ask the competent authority directly.'),('Check again before submission','Requirements, fees and appointments can change. A link to an authority is not a guarantee that any particular document qualifies.')],list(SOURCES),['/editorial-policy/','/guides/','/guides/mosadaqa-degree-attestation/'],'Source directory')
    content='''<form class="contact-form" data-contact><label>Your name <small>(optional)</small><input name="name" autocomplete="name" maxlength="100"></label><label>What would you like help with?<textarea name="message" required maxlength="3000" aria-describedby="message-help" placeholder="For example: I have a university degree for employment in the UAE. There is a spelling difference."></textarea></label><p class="small" id="message-help">Please leave out identity numbers, scans, private case references and confidential details.</p><label class="checkbox"><input type="checkbox" name="acknowledge" required><span>I understand this prepares an email draft and does not send my enquiry automatically.</span></label><button class="btn" type="submit">Prepare Email Request <span aria-hidden="true">↗</span></button><p class="contact-status" role="status"></p><div data-email-ready hidden><a class="btn" data-email-link href="mailto:Services@salaroutsourcing.com">Open Email Draft ↗</a><p class="small">Review and send from your email application. If it does not open, copy your message and email <a href="mailto:Services@salaroutsourcing.com">Services@salaroutsourcing.com</a>.</p></div></form>'''
    content+=nap_strip()
    save('/contact/','Request a Document Assessment','Describe your document and situation, and prepare an email request without uploading sensitive files or identity numbers.',pagehead('Let’s find<br>your next step.','Begin with a description of your situation. No sensitive document files needed.',[('/contact/','Contact')])+f'<div class="wrap content-layout"><div><h2 class="sr-only">Request a document assessment</h2>{content}<noscript><p>Email your enquiry directly to <a href="mailto:Services@salaroutsourcing.com">Services@salaroutsourcing.com</a>.</p></noscript></div><aside class="aside-box"><p class="eyebrow">Independent assistance</p><h3>A clear first conversation.</h3><p>Document type.<br>Destination.<br>Purpose.<br>Anything that needs attention.</p><p><a href="mailto:Services@salaroutsourcing.com">Services@salaroutsourcing.com</a></p>{link("/document-security/","Before sharing documents")}</aside></div>',crumbs=[('/contact/','Contact')])
    save('/404.html','Page not found','This page could not be found. Explore services or start a document assessment.',f'<div class="wrap empty-state"><p class="eyebrow" style="justify-content:center">A turn in the path</p><h1>404</h1><h2>Let’s get you back<br>on the right path.</h2><div class="actions" style="justify-content:center">{button("Go to Homepage","/")}{button("Explore Services","/services/","btn outline")}</div></div>',noindex=True)

STUBS=set()
def redirect_stub(target,label):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{label} | {BUSINESS["name"]}</title><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{BASE}{target}">'
            f'</head><body><p>This page has moved to <a href="{target}">{target}</a>.</p></body></html>')
def redirects():
    aliases={'/check-documents.html':'/check-documents/','/blog.html':'/guides/',
     '/blog/degree-name-different-from-passport.html':'/guides/degree-name-different-from-passport/',
     '/blog/hec-vs-ibcc.html':'/guides/hec-vs-ibcc/','/blog/mofa-attestation-guide.html':'/guides/mofa-attestation-pakistan/',
     '/blog/apostille-vs-embassy.html':'/guides/apostille-vs-embassy-attestation/',
     '/services/hec-attestation/':'/services/mosadaqa-attestation/','/services/ibcc-attestation/':'/services/qvp-attestation/',
     '/services/mofa-attestation/':'/services/saudi-culture-attestation/','/services/embassy-legalization/':'/services/saudi-embassy-attestation/',
     '/services/super-legalization/':'/services/saudi-embassy-attestation/','/services/apostille/':'/guides/apostille-vs-embassy-attestation/',
     '/countries/':'/countries/saudi-arabia/','/countries/uae/':'/services/uae-embassy-attestation/',
     '/documents/':'/services/mosadaqa-attestation/','/documents/degree/':'/services/mosadaqa-attestation/',
     '/documents/education/':'/guides/mosadaqa-degree-attestation/','/documents/personal/':'/services/uae-embassy-attestation/',
     '/documents/marriage-certificate/':'/services/saudi-embassy-attestation/','/documents/business/':'/services/saudi-embassy-attestation/',
     '/documents/international-use/':'/services/uae-embassy-attestation/'}
    for old,target in sorted(aliases.items()) if old != target:
        label=PAGES.get(target,'Moved')
        path=(ROOT/old.lstrip('/')) if old.endswith('.html') else (ROOT/old.strip('/')/'index.html')
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(redirect_stub(target,label))
        STUBS.add(('/'+str(path.relative_to(ROOT))).replace('/index.html','/') if not old.endswith('.html') else '/'+str(path.relative_to(ROOT)))
    (ROOT/'redirects.json').write_text(json.dumps(aliases,indent=2)+'\n')
    (ROOT/'_redirects').write_text(''.join(f'{old} {target} 301\n' for old,target in sorted(aliases.items()) if old != target if o != n))
def cleanup():
    keep={'index.html','404.html','tools/responsive-preview.html'}
    keep|={ (p.lstrip('/')+'index.html') if p.endswith('/') else p.lstrip('/') for p in PAGES }
    keep|={ (s.lstrip('/')+'index.html') if s.endswith('/') else s.lstrip('/') for s in STUBS }
    removed=[]
    for f in sorted(ROOT.rglob('*.html')):
        rel=str(f.relative_to(ROOT))
        if rel.startswith('.git/') or rel.startswith('tools/'): continue
        if rel not in keep:
            f.unlink(); removed.append(rel)
            parent=f.parent
            while parent!=ROOT and not any(parent.iterdir()): parent.rmdir(); parent=parent.parent
    return removed
def write_sitemap():
    entries=''.join(f'  <url><loc>{BASE}{p}</loc><lastmod>{UPDATED[:10]}</lastmod></url>\n' for p in sorted(PAGES))
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+entries+'</urlset>\n')
def write_robots():
    groups='User-agent: *\nAllow: /\nDisallow: /tools/\n'
    for bot in ['GPTBot','OAI-SearchBot','ChatGPT-User','ClaudeBot','Claude-SearchBot','PerplexityBot','Google-Extended','Applebot-Extended','Bingbot','CCBot']:
        groups+=f'\nUser-agent: {bot}\nAllow: /\nDisallow: /tools/\n'
    (ROOT/'robots.txt').write_text(groups+'\nSitemap: '+BASE+'/sitemap.xml\n')
KEY_PAGES={
 '/check-documents/':'Guided check that identifies the stages a document may need. No files required.',
 '/services/':'Assistance for educational, official-authority and international document processes.',
 '/guides/mosadaqa-degree-attestation/':'What mosadaqa means for a degree used in Saudi Arabia, and how a name difference between the degree, passport and CNIC is resolved.',
 '/guides/degree-name-different-from-passport/':'Which issuer corrects a name difference on a degree, passport or identity record.',
 '/problems/degree-passport-name-mismatch/':'Comparing degree, passport and CNIC records before attestation.',
 '/guides/hec-vs-ibcc/':'Which educational authority applies to a qualification.',
 '/guides/mofa-attestation-pakistan/':'Where the foreign affairs stage fits in the sequence.',
 '/guides/apostille-vs-embassy-attestation/':'How to establish which authentication route applies.',
 '/countries/saudi-arabia/':'Preparation questions for documents used in Saudi Arabia.',
 '/countries/uae/':'Preparation questions for documents used in the United Arab Emirates.',
 '/process/':'The stages from document to destination.',
 '/sources/':'Official authority sources, with direct links.',
}
def write_llms():
    out=['# '+BUSINESS['name'],'',
     '> '+BUSINESS['description']+' Official attestation, verification and acceptance decisions are made by the competent authorities and the receiving organisation, not by this website.','',
     '## Services','']
    for s in SERVICES:
        out.append(f'- [{s["title"]}]({BASE}/services/{s["slug"]}/): {s["summary"]}')
    out+=['','## Contact and office','',
     f'- WhatsApp and phone: {BUSINESS["telephone"]}',f'- Office line: {BUSINESS["officeLine"]}',
     f'- Email: {BUSINESS["email"]}',f'- Office: {BUSINESS["street"]}, {BUSINESS["locality"]}, {BUSINESS["region"]}, Pakistan',
     f'- Registered name: {BUSINESS["legalName"]} ({BUSINESS["identifier"]})',f'- Website: {BUSINESS["website"]}',
     f'- Main website: {BUSINESS["entityUrl"]}',f'- Editable verification page: {BUSINESS["verifyUrl"]}','',
     '## Purpose of this site','',
     'This site helps people in Pakistan prepare documents that will be used in Saudi Arabia and other Apostille destinations: Mosadaqa degree verification, Saudi Culture attestation, Saudi Embassy attestation, QVP qualification verification and apostille. It does not certify, verify or attest documents itself.','',
     '## Common questions asked of us','']
    for c,q,a in FAQS[:8]:
        out.append(f'- {q} {a}')
    out+=['','## Key pages','']
    out+=[f'- [{PAGES.get(u,u)}]({BASE}{u}): {d}' for u,d in {
     '/services/':'The five services we assist with.',
     '/guides/mosadaqa-degree-attestation/':'What mosadaqa means and how a degree file moves through the stages.',
     '/guides/qvp-qualification-verification/':'How QVP qualification verification differs from attestation.',
     '/guides/degree-name-different-from-passport/':'Which issuer corrects a name difference on a degree, passport or CNIC.',
     '/problems/degree-passport-name-mismatch/':'Comparing degree, passport and CNIC records before paying for a stage.',
     '/problems/mosadaqa-verification-query/':'What to do when a Mosadaqa or QVP query names a mismatch.',
     '/check-documents/':'Guided four-question check of the stages a document may need.',
     '/process/':'The stages from document to destination.',
     '/sources/':'Official authority sources with direct links.'}.items()]
    out+=['']
    (ROOT/'llms.txt').write_text('\n'.join(out))
def write_feed():
    items=''
    for g in GUIDES:
        u=BASE+'/guides/'+g['slug']+'/'
        items+=f'  <entry><title>{e(g["title"])}</title><link href="{u}"/><id>{u}</id><updated>{UPDATED}</updated><summary>{e(g["desc"])}</summary></entry>\n'
    (ROOT/'feed.xml').write_text('<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n  <title>'+BUSINESS['name']+' — guides and updates</title>\n  <link href="'+BASE+'/feed.xml" rel="self"/>\n  <link href="'+BASE+'/"/>\n  <updated>'+UPDATED+'</updated>\n  <id>'+BASE+'/</id>\n  <author><name>'+BUSINESS['name']+'</name></author>\n'+items+'</feed>\n')
def main():
    redirects();build_home();build_pages();trust_pages()
    write_sitemap();write_robots();write_llms();write_feed()
    gone=cleanup()
    if gone: print('Removed '+str(len(gone))+' retired page(s): '+', '.join(gone))
    print(f'Built {len(PAGES)} indexable pages, redirects, sitemap, robots.txt, llms.txt, feed.xml and _redirects.')
if __name__=='__main__':main()
