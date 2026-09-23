"""Editorial content. Keep requirements conditional; official authorities decide eligibility."""
PUBLISHED='2026-09-22T09:00:00+05:00'
UPDATED='2026-09-22T09:00:00+05:00'
PUBLISHED_LABEL='22 September 2026'
# Business details appear here so the footer, contact page and structured data stay consistent.
# Confirm each value before publishing changes.
BUSINESS = {
 'name':'SK Immigration Services',
 'legalName':'SK Immigration Services (SMC-Private) Limited',
 'alternateName':['SK Immigration','SK Consultant','SK Attestations'],
 'slogan':'Attestation desk of SK Immigration Services',
 'description':'Mosadaqa, Saudi Culture, Saudi Embassy, QVP and Apostille assistance for Pakistani documents. Independent preparation and follow-up; the authorities decide every outcome.',
 'email':'Services@salaroutsourcing.com',
 'telephone':'+92 310 5507819',
 'whatsapp':'923105507819',
 'whatsappLabel':'+92 310 5507819',
 'officeLine':'+92 304 5999859',
 'street':'Office No. 10, Alfazal Plaza 64C, Satellite Town',
 'locality':'Rawalpindi',
 'region':'Punjab',
 'country':'PK',
 'foundingDate':'2020',
 'identifier':'SECP CUIN 0304985',
 'entityId':'https://immigration.salaroutsourcing.com/#organization',
 'entityUrl':'https://immigration.salaroutsourcing.com/',
 'verifyUrl':'https://salaroutsourcing.com/trust.html',
 'instagram':'https://www.instagram.com/skimmigrationonservices/',
 'maps':'https://www.google.com/maps/search/?api=1&query=SK+Immigration+Services+Office+No.+10+Alfazal+Plaza+64C+Satellite+Town+Rawalpindi',
 'website':'https://ksa.salaroutsourcing.com',
 'logo':'https://immigration.salaroutsourcing.com/assets/img/logo.jpg',
 'areaServed':['Pakistan','Saudi Arabia','United Arab Emirates','Qatar','Kuwait','Oman','Bahrain'],
 'knowsAbout':['Mosadaqa degree verification for Saudi Arabia','Saudi Culture attestation','Saudi Embassy attestation','QVP Qualification Verification Program','Apostille for Pakistani documents','HEC degree attestation','Pakistan MOFA attestation','Degree name mismatch between degree, passport and CNIC'],
}
SOURCES = {'hec': ('HEC — Degree attestation', 'https://www.hec.gov.pk/english/services/students/DAS/Pages/Degree-Attestation.aspx'),
 'ibcc': ('IBCC — Attestation', 'https://ibcc.edu.pk/attestation/'),
 'mofa': ('MOFA Pakistan — Official website', 'https://mofa.gov.pk/'),
 'hcch': ('HCCH — Apostille Convention status and declarations', 'https://www.hcch.net/en/instruments/conventions/status-table/?cid=41'),
 'dgip': ('DGIP — Passport services', 'https://www.dgip.gov.pk/'),
 'nadra': ('NADRA — Identity services', 'https://www.nadra.gov.pk/'),
 'saudi': ('Saudi Ministry of Foreign Affairs', 'https://www.mofa.gov.sa/en/'),
 'mosadaqa': ('Mosadaqa E-Service — certificate verification', 'https://www.mosadaqa.sa/'),
 'saudi-moe': ('Saudi Ministry of Education', 'https://moe.gov.sa/en/'),
 'uae-mofa': ('UAE Ministry of Foreign Affairs — attestation of documents service', 'https://www.mofa.gov.ae/en/services/attestation'),
 'vfs-uae': ('UAE attestation document submission centres in Pakistan', 'https://visa.vfsglobal.com/pak/en/atu/apply-attestation'),
 'mofa-pk-apostille': ('MOFA Pakistan — Pakistan’s accession to the Apostille Convention, 9 March 2023', 'https://mofa.gov.pk/pakistans-accession-to-apostille-convention')}
SERVICES = [{'slug': 'mosadaqa-attestation',
  'symbol': 'م',
  'category': 'Saudi Arabia',
  'title': 'Mosadaqa degree attestation',
  'summary': 'Degree and certificate verification for Saudi Arabia, with the record details compared before any stage is paid for.',
  'desc': 'Mosadaqa assistance for degrees, diplomas and certificates used in Saudi Arabia: which records are compared, the order of the stages and how name differences are handled.',
  'answer': 'Mosadaqa is the term used in Pakistan for the verification of a degree or certificate so that Saudi authorities can rely on it. A file normally moves through the awarding institution, the '
            'education authority for that qualification, the Pakistani foreign-affairs stage and then the Saudi-side verification or attestation steps. We help you prepare and follow that sequence. The '
            'authorities make every decision.',
  'audience': 'Graduates, professionals and families in Pakistan whose degree, diploma, transcript or certificate will be submitted for work, residence or study in Saudi Arabia.',
  'steps': [('What we start with',
             'Your qualification, the awarding institution and the Saudi organisation that asked for the document. Its written wording usually decides which stages apply, so we work from that first.'),
            ('The stages we prepare',
             'Issuer verification, the education-authority stage for that qualification, the Pakistani foreign-affairs stage, and then the Saudi-side steps. Apostille and embassy legalization are different '
             'routes, so we check which one your destination actually expects.'),
            ('Records compared before submission',
             'Degree or certificate and transcript, CNIC or NICOP record, passport and the exact spelling used by the institution. A difference is resolved with the issuer of the incorrect record before '
             'another fee is paid.'),
            ('What we cannot do', 'We cannot issue a verification, decide eligibility or guarantee acceptance. We do not alter documents, and we do not submit anything without your written authority.')],
  'check': ['Degree or certificate and transcript exactly as issued',
            'CNIC or NICOP record and passport details',
            'Father’s name spelling across the academic record and identity documents',
            'The Saudi organisation’s written request, with the exact document names',
            'Any earlier Mosadaqa or verification query you received'],
  'sources': ['mosadaqa', 'saudi-moe', 'hec', 'mofa', 'saudi'],
  'related': ['/services/saudi-culture-attestation/', '/services/saudi-embassy-attestation/', '/guides/mosadaqa-degree-attestation/', '/problems/mosadaqa-verification-query/'],
  'faqs': [('What does Mosadaqa actually mean?',
            'In Pakistan the word is used for attestation or verification of a document, most often a degree or certificate that will be used in Saudi Arabia. It names the outcome, not one office, so the '
            'document still has to be checked and attested by the bodies competent for it.'),
           ('Does every Pakistani degree need Mosadaqa?',
            'No. It depends on the qualification, the awarding institution and what the Saudi organisation asks for. Start from its written request rather than from a general rule.'),
           ('What if my degree name differs from my passport or CNIC?',
            'That difference usually has to be settled on the record that is wrong: the awarding institution for the degree, NADRA for the identity record and the passport authority for the passport. Ask the '
            'receiving side what evidence it accepts for the difference before paying for another stage.'),
           ('How long does it take and what does it cost?',
            'Charges and turnaround come from the authorities handling each stage, so we do not publish numbers that may already be out of date. Send the document type and destination on WhatsApp and we will '
            'tell you the current amounts and sequence.')]},
 {'slug': 'saudi-culture-attestation',
  'symbol': '◎',
  'category': 'Saudi Arabia',
  'title': 'Saudi Culture attestation',
  'summary': 'The cultural-mission step of degree attestation for Saudi Arabia, prepared after the education and foreign-affairs stages.',
  'desc': 'Saudi Culture attestation for Pakistani degrees and certificates: where it sits in the Saudi chain, what is compared and why the earlier stages have to line up first.',
  'answer': 'The step described in Pakistan as Saudi Culture attestation is the Saudi-side stage that follows the education and foreign-affairs stages for an academic document. It is usually requested '
            'together with the Saudi Embassy stage or with online verification, depending on the document and the requesting organisation. We prepare the file so names, spellings and records agree before it '
            'reaches that stage.',
  'audience': 'Applicants whose Saudi employer, university or family sponsor asked for degree or certificate attestation through the Saudi cultural or embassy channel.',
  'steps': [('Where it sits in the chain',
             'After the issuing institution and the relevant education authority have dealt with the academic record, and after the Pakistani foreign-affairs stage. Submitting earlier is the most common '
             'reason for a return.'),
            ('What is compared',
             'The certificate, the transcript where one applies, the identity record and the passport. A spelling difference between the degree and the identity record is the usual reason for a query.'),
            ('Culture or Embassy?',
             'Do not assume both are always required, and do not assume either is enough by itself. The requesting organisation’s wording, the document type and current instructions decide. We check that '
             'first.'),
            ('What we cannot do', 'We cannot approve, verify or speed up an official stage, and we cannot promise a result. Official staff decide what is accepted.')],
  'check': ['Academic record and transcript after the education-authority stage',
            'Pakistan foreign-affairs stage where applicable',
            'Identity record and passport spelling',
            'The requesting organisation’s written instruction naming the stage',
            'Translation requirements if the document is not in Arabic or English'],
  'sources': ['saudi-moe', 'mosadaqa', 'saudi', 'mofa'],
  'related': ['/services/mosadaqa-attestation/', '/services/saudi-embassy-attestation/', '/guides/mosadaqa-degree-attestation/', '/problems/degree-passport-name-mismatch/'],
  'faqs': [('Is Saudi Culture attestation the same as Mosadaqa?',
            'The words are used loosely. Mosadaqa describes the verification outcome expected by the Saudi side; cultural-mission attestation is one of the stages that can serve it. Which stages your file '
            'needs depends on the document and the request.'),
           ('Can I skip the earlier stages?', 'Not normally. A Saudi-side stage sits after the education and foreign-affairs stages for a reason, and an out-of-order file is usually returned.'),
           ('Do you attend the mission on my behalf?',
            'Submission, representation and personal-appearance rules are set by the authority and can change. We confirm the current arrangement for your document instead of promising a service that may not '
            'be allowed.')]},
 {'slug': 'saudi-embassy-attestation',
  'symbol': '❖',
  'category': 'Saudi Arabia',
  'title': 'Saudi Embassy attestation',
  'summary': 'Embassy legalization of a Pakistani document for Saudi Arabia, prepared after the earlier verification stages.',
  'desc': 'Saudi Embassy attestation of Pakistani documents: what the embassy stage means, which earlier attestations must already be in place and what changes from case to case.',
  'answer': 'Saudi Embassy attestation is the consular legalization step for a Pakistani document that will be used in Saudi Arabia. It confirms the previous signatures and stamps rather than re-examining the '
            'contents of the document, so an incomplete earlier stage usually stops it. Academic documents often also pass a verification stage; commercial, family and personal records usually follow a '
            'different combination. We confirm the sequence for your document before anything is submitted.',
  'audience': 'Applicants with a degree, certificate or other Pakistani document that a Saudi employer, authority or sponsor wants legalized through the embassy channel.',
  'steps': [('What it confirms', 'That the signatures and seals already on the document are genuine. It is a legalization step, not an academic evaluation.'),
            ('The order matters',
             'The document must carry the earlier attestations the embassy stage expects. For academic records that normally includes the education-authority and foreign-affairs stages; for other documents it '
             'depends on the document and its purpose.'),
            ('Academic or non-academic', 'A degree is not handled like a power of attorney, a marriage record or a commercial paper. We check the category first so the file is not refused on the wrong route.'),
            ('What we cannot do', 'We cannot decide acceptance, waive a requirement or promise a turnaround. The mission and the Saudi receiving side decide.')],
  'check': ['The document itself and the earlier attestations it already carries',
            'Identity record and passport spelling',
            'The requesting organisation’s document list and purpose',
            'Translation or certified-copy requirements',
            'Whether the receiving side also expects online verification'],
  'sources': ['saudi', 'mofa', 'mosadaqa'],
  'related': ['/services/mosadaqa-attestation/', '/services/saudi-culture-attestation/', '/guides/apostille-vs-embassy-attestation/', '/problems/document-rejected/'],
  'faqs': [('Is embassy attestation always the last step?',
            'For many documents it is the final stage of the country chain, but an academic file can also carry a verification stage. Confirm against the request you received rather than a general rule.'),
           ('Does embassy attestation replace Mosadaqa?', 'No. They do different jobs. One legalizes signatures already on the document; the other relates to verification of the qualification.'),
           ('Can a rejected document be submitted again?', 'Often, once the stated reason is fixed. Read the notice first and correct the record it names rather than adding another stamp on top.')]},
 {'slug': 'qvp-attestation',
  'symbol': '◆',
  'category': 'Saudi Arabia',
  'title': 'QVP attestation',
  'summary': 'Qualification Verification Program support for professionals whose Saudi-side verification has been requested.',
  'desc': 'QVP attestation support for Pakistan: what the Qualification Verification Program checks, how it relates to degree attestation and what a query usually means.',
  'answer': 'QVP stands for Qualification Verification Program, the Saudi-side verification of a qualification that is commonly requested in connection with a work permit or visa. It confirms that the degree '
            'or diploma you submitted is genuine and matches the qualification you were hired for. It sits alongside degree attestation rather than replacing it: attestation authenticates the document, and '
            'the program verifies the qualification with the awarding institution. We prepare the Pakistani side of that file and help you answer the query you receive; the Saudi-side decision is not ours to '
            'make.',
  'audience': 'Professionals with a Saudi job offer or work-permit process who have been asked for QVP verification of their degree, diploma or professional qualification.',
  'steps': [('What the program looks at',
             'Your qualification, the awarding institution, the professional title it supports and the details on the document. A mismatch between any of these is the usual source of a query.'),
            ('How it relates to attestation',
             'Attestation and verification are different checks on the same document. A verified degree without the attestation stages, or the reverse, can leave a file incomplete for the employer or the '
             'authority.'),
            ('What the Pakistani side needs',
             'An accurate academic record, a transcript where the qualification requires one, and identity details that agree with the record. Where a name or an institution detail differs, it is corrected at '
             'source before resubmission.'),
            ('What we cannot do', 'We cannot influence the program’s assessment, its timing or its outcome, and we cannot complete a Saudi-side submission that the applicant or the employer has to make.')],
  'check': ['Degree or diploma exactly as issued, plus transcript if required',
            'The exact qualification and job title in the employer’s documents',
            'Institution name and accreditation details as they appear on the record',
            'CNIC or NICOP and passport details matching the record',
            'Any QVP query, email or reference number you already received'],
  'sources': ['mosadaqa', 'saudi-moe', 'saudi', 'hec'],
  'related': ['/services/mosadaqa-attestation/', '/guides/qvp-qualification-verification/', '/problems/mosadaqa-verification-query/', '/services/saudi-embassy-attestation/'],
  'faqs': [('Is QVP the same as Mosadaqa?',
            'They are related but not identical. Mosadaqa covers verification of an academic certificate for Saudi use; QVP is the qualification-verification programme that employers and the work-permit '
            'process commonly require. One file can involve both.'),
           ('My employer asked for QVP before I travel. What comes first?',
            'Establish the qualification the employer submitted, then make sure the academic record and identity details agree with it. Attestation stages and verification are prepared around that, and the '
            'ordering depends on your case.'),
           ('Can a name difference fail QVP?',
            'A difference between the degree, the passport and the identity record is a very common reason for a query. Resolve it with the issuer of the incorrect record before resubmitting.')]},
 {'slug': 'uae-embassy-attestation',
  'symbol': 'AE',
  'category': 'United Arab Emirates',
  'title': 'UAE Embassy attestation',
  'summary': 'Document legalisation for the UAE: attestation in Pakistan first, then the UAE embassy or consulate — including medical reports, marriage records and degrees.',
  'desc': 'UAE Embassy attestation for documents issued in Pakistan: what must be attached before the embassy stage and why files stall at the counter.',
  'answer': 'A document issued in Pakistan is attested inside Pakistan first — by the issuing authority, then commonly by MOFA Pakistan — and only then legalised by the UAE embassy or consulate. Medical '
            'reports, marriage records, police certificates and degrees all follow that order; the UAE side does not accept a Pakistani document on its own. We prepare and sequence the file, and the '
            'authorities decide.',
  'audience': 'People sending a Pakistani document to the UAE for employment, residency, a family visa, school admission, insurance or medical purposes, and people already in the UAE who need a Pakistani '
              'record legalised.',
  'steps': [('What the UAE side accepts',
             'Documents issued in Pakistan must carry the attestation of the Pakistani authority responsible for that record before the UAE embassy or consulate can legalise them. Degrees and transcripts '
             'normally go through the awarding institution and the education authority first; marriage, birth, police and medical records start with the office that issued them.'),
            ('The order that matters',
             'Issuing authority → MOFA Pakistan (Islamabad or a camp office) → UAE embassy or consulate in Pakistan. If the document will be used inside the UAE, translation into Arabic and any further '
             'attestation by the UAE Ministry of Foreign Affairs may also be requested by the organisation receiving it.'),
            ('Medical reports and certificates',
             'A medical report or fitness certificate issued in Pakistan is not accepted directly by UAE authorities: it is attested by MOFA Pakistan and then legalised by the UAE embassy or consulate. If you '
             'are already inside the UAE, medical fitness for residency is normally completed at a UAE-approved health centre instead, which is a different process from legalising a Pakistani report.'),
            ('Where files stall',
             'Attestation missing from the preceding stage, a name or date of birth that differs from the passport or Emirates ID, a copy where an original is required, an expired certificate, or a report '
             'signed by a practitioner whose signature is not already on record. Counter staff check the earlier stage before they look at anything else.')],
  'check': ['The exact document — original or certified copy, and whether it has an expiry',
            'The issuing office and its current attestation requirement',
            'Name, father’s name and date of birth as they appear on the passport or Emirates ID',
            'Whether the receiving organisation wants Arabic translation or a further UAE-side attestation',
            'The written request you received, including any reference number'],
  'sources': ['uae-mofa', 'vfs-uae', 'mofa', 'hec', 'nadra'],
  'related': ['/guides/uae-embassy-attestation-process/', '/guides/medical-report-attestation/', '/problems/document-rejected/', '/services/saudi-embassy-attestation/'],
  'faqs': [('Which documents do you handle for the UAE?',
            'Degrees, transcripts, diplomas, marriage and divorce records, birth certificates, police character certificates, medical reports, experience letters and commercial documents. The route depends on '
            'the record rather than the destination.'),
           ('Do I need MOFA Pakistan before the UAE embassy?',
            'For documents issued in Pakistan, yes in ordinary practice: the embassy stage checks that the earlier Pakistani attestation is present. Confirm the current requirement with the authority handling '
            'your document before you send anything.'),
           ('Can a medical report be attested after the test in the UAE?',
            'Medical fitness completed inside the UAE is handled by UAE-approved health centres. A report issued in Pakistan is a different case: it is attested in Pakistan and then legalised for use in the '
            'UAE.'),
           ('Does an apostille replace the UAE embassy stage?',
            'Not for a document issued in Pakistan. Apostille certificates are issued by designated authorities of contracting states to the Hague Convention; Pakistan’s own issuance arrangements have been '
            'subject to legislation, and an agent cannot issue an apostille. Ask which authority will issue the certificate before paying anyone, and confirm the requirement with the UAE side.')]}]
GUIDES = [{'slug': 'degree-name-different-from-passport',
  'title': 'Degree name different from passport?',
  'category': 'Document problems',
  'summary': 'Identify which record needs attention before starting attestation.',
  'desc': 'A degree, passport or CNIC that shows a different spelling or a missing surname needs the right issuer, not another stamp. Compare the records first.',
  'answer': 'Compare the degree, passport and identity record. Ask the institution responsible for the incorrect record about its correction process. Do not edit the document yourself or assume an affidavit '
            'will be accepted.',
  'sections': [('Why the distinction matters',
                'A missing surname, transliteration difference or changed name may need a different response. The spelling that appears most often is not, by itself, proof that a record is correct.'),
               ('Which issuer handles which record',
                '<table class="content-table"><thead><tr><th>Record showing the difference</th><th>Who can correct or verify it</th></tr></thead><tbody><tr><td>Degree or transcript</td><td>The university or '
                'board that issued the academic record</td></tr><tr><td>Passport</td><td>DGIP, through its passport service</td></tr><tr><td>CNIC, B-form or identity '
                'record</td><td>NADRA</td></tr><tr><td>Marriage or name-change record</td><td>The civil registration or issuing authority</td></tr></tbody></table>'),
               ('A practical sequence',
                'Record the exact difference. Identify the issuer of each document. Ask the receiving institution what evidence it will accept. Then obtain written correction or verification instructions from '
                'the relevant issuer.'),
               ('Documents to have available',
                'Keep your degree, transcript, passport, identity record and the receiving organisation’s request available for your own comparison. At the first enquiry, describe the difference without '
                'sending document numbers or scans.'),
               ('Common problems',
                'Avoid handwritten changes, unverified agents promising a new stamp, and assuming that a “one and the same person” affidavit is universally sufficient. Where the difference concerns a name '
                'used before or after marriage, the supporting civil record matters as much as the correction itself.'),
               ('What varies',
                'University correction procedures, identity record changes and acceptance by a foreign institution are separate decisions. Passport enquiries belong with DGIP; identity record enquiries belong '
                'with NADRA.'),
               ('Name differences and Saudi-bound records',
                'If your degree is being authenticated for use in Saudi Arabia, the same records are compared during the verification stage commonly called <a '
                'href="/guides/mosadaqa-degree-attestation/">mosadaqa</a>. Resolve the difference with the issuer before that stage begins, so you are not paying for a submission that will be queried.')],
  'sources': ['hec', 'dgip', 'nadra'],
  'faqs': [('Can I correct the degree after attestation?',
            'Correcting an academic record after authentication usually means the authenticated document no longer matches the corrected record, so the stages may need to be repeated. Ask the issuer and the '
            'receiving organisation before you start either process.'),
           ('Which spelling should I change?',
            'Change the record that is actually wrong, not the document that is easiest to alter. The issuer that holds the source record decides what its corrected version says.'),
           ('Is a spelling difference always a problem?',
            'Not always. Some receiving organisations accept a documented variation, a translation note or a supporting identity record. The organisation that will use the document decides what it accepts.')],
  'related': ['/problems/degree-passport-name-mismatch/', '/services/mosadaqa-attestation/', '/services/mosadaqa-attestation/', '/guides/mosadaqa-degree-attestation/']},
 {'slug': 'mofa-attestation-pakistan',
  'title': 'MOFA attestation: where to begin',
  'category': 'Attestation essentials',
  'summary': 'Start with the document category and the authority that comes before MOFA.',
  'desc': 'Start with the document category and the authority that comes before the foreign affairs stage, then confirm the current instructions for your document.',
  'answer': 'Identify your document and its prerequisite verification before choosing a submission route. Check MOFA’s current instructions for that category rather than using a single checklist for every '
            'document.',
  'sections': [('What the MOFA stage means',
                'Foreign affairs authentication is part of a wider document journey. It does not replace checking the original record or establishing acceptance by the receiving organisation.'),
               ('A practical sequence',
                'Identify the issuer, establish any preceding educational or other authority stage, confirm current MOFA requirements, then confirm what the recipient needs after authentication.'),
               ('Documents to have available',
                'The exact document title, issuing authority, existing verification and written destination requirements are useful starting information. The official checklist determines which originals and '
                'supporting records to submit. Where names differ across records, resolve the difference with the issuer first.'),
               ('Common problems', 'Missing prerequisites, inconsistent identity details and using a submission route that is not permitted for the document can cause avoidable difficulties.'),
               ('What varies', 'Official fees, permitted representation, appearance requirements, appointment arrangements and the destination route. Confirm these before travel or payment.')],
  'sources': ['mofa', 'hec', 'ibcc'],
  'related': ['/services/saudi-culture-attestation/', '/guides/apostille-vs-embassy-attestation/', '/process/']},
 {'slug': 'mosadaqa-degree-attestation',
  'title': 'Mosadaqa degree attestation in Pakistan',
  'category': 'Saudi Arabia',
  'summary': 'What the term means, which stages apply and how name differences are resolved.',
  'desc': 'Mosadaqa means attestation or verification of a document for Saudi use. See which records must match and how name differences are resolved.',
  'answer': 'Mosadaqa means your document has been authenticated or verified for use in Saudi Arabia. For a degree, the file normally goes through the issuing institution and the educational authority first, '
            'then the foreign affairs stage, and finally whatever the Saudi side requires. If your degree, passport or CNIC details differ, resolve the difference with the issuer of the incorrect record '
            'before paying for attestation stages.',
  'sections': [('What “mosadaqa” actually means',
                'Mosadaqa (also written musadaqa or mosa daqa) is used in Pakistan for the attestation, authentication or verification of a document, and in practice it is used most often for degrees and '
                'certificates going to Saudi Arabia. It does not name one office that you visit. Your document still has to be checked by the institution that issued it and authenticated by the bodies '
                'competent for that document, and the Saudi side still decides what it accepts.'),
               ('Mosadaqa, HEC and IBCC are not the same thing',
                '<table class="content-table"><thead><tr><th>Term you will see</th><th>What it refers to</th><th>Who decides</th></tr></thead><tbody><tr><td>Mosadaqa / musadaqa</td><td>The authenticated or '
                'verified document a Saudi employer, university or authority asks for</td><td>Whichever authorities are competent for the document</td></tr><tr><td>HEC</td><td>Attestation service for eligible '
                'higher-education documents issued in Pakistan</td><td>HEC</td></tr><tr><td>IBCC</td><td>Attestation for relevant school-level qualifications and board-issued '
                'records</td><td>IBCC</td></tr><tr><td>Certificate verification (e-service)</td><td>Destination-side verification of an academic record</td><td>The authority receiving the '
                'submission</td></tr></tbody></table><p class="small">Read the table as a map of roles, not as a fixed sequence. Eligibility and the applicable stages depend on your qualification and its '
                'issuer.</p>'),
               ('A practical sequence for a degree',
                '<ol><li>Write down the exact qualification, awarding institution and campus.</li><li>Compare the name and date details across the degree, transcript, CNIC and passport.</li><li>Ask the issuer '
                'about any difference in the academic record before applying anywhere else.</li><li>Check the educational authority’s current eligibility and application instructions for your '
                'qualification.</li><li>Confirm the foreign affairs stage that applies to the document category.</li><li>Ask the Saudi organisation what it needs to receive: a verification submission, an '
                'authenticated original, or both.</li><li>Keep the recipient’s written wording with your file before you pay for any stage.</li></ol>'),
               ('Name differences on the degree, passport and CNIC',
                '<table class="content-table"><thead><tr><th>Where the difference is</th><th>Who can correct it</th><th>What to keep</th></tr></thead><tbody><tr><td>Name, father’s name or spelling on the '
                'degree or transcript</td><td>The university or board that issued the record</td><td>Your correction or verification request and the issuer’s written reply</td></tr><tr><td>Surname missing or '
                'added, or a name spelled differently on the passport</td><td>DGIP, through its passport service</td><td>Your passport application record</td></tr><tr><td>Name, father’s name or date of birth '
                'on the CNIC, B-form or identity record</td><td>NADRA</td><td>Your NADRA processing record</td></tr><tr><td>A name that changed after marriage or by registration</td><td>The authority that '
                'registered the change</td><td>The registration or name-change record</td></tr></tbody></table><p>A common case is a degree in a short form of the name while the passport and CNIC carry the '
                'full form, or a father’s name recorded differently on the degree. The comparison during verification is between the records you submit, so the correction has to be made on the record that is '
                'wrong.</p>'),
               ('Where a name mismatch usually stops the process',
                'A verification query commonly concerns the record details rather than the stamps: a surname missing on the degree, a different father’s name, a transliteration or spelling difference between '
                'the CNIC and the passport, or a changed name with no supporting record. The notice normally names the document and the discrepancy. Work from that wording, ask the issuer about correction or '
                'verification, and let the receiving authority confirm what evidence it will accept instead of buying another attestation stage first.'),
               ('Special cases worth checking early',
                '<ul><li>Degrees issued under an abbreviated or short name, with the full name on the CNIC and passport.</li><li>Father’s name differences where the passport and the degree were issued from '
                'different records.</li><li>Name changes after marriage, where the marriage registration record is the supporting evidence.</li><li>Qualifications from a renamed or merged institution, where '
                'the verification request names an institution that no longer exists under that title.</li><li>Documents where the date of birth differs between the academic record and the identity '
                'record.</li></ul>'),
               ('Fees and timelines',
                'This website does not publish fees or turnaround times. Official charges, appointment arrangements and processing times change, and they differ by document and by case. Confirm the current '
                'amount and the processing arrangement with the authority handling your stage before you pay anyone.'),
               ('How we help with a Mosadaqa or verification query',
                'We compare the records you hold, write out the exact difference, and prepare the questions to put to the issuer and to the receiving authority. We can sequence the stages so a correction '
                'happens before authentication rather than after it. We do not correct records, and we do not decide eligibility or acceptance.')],
  'sources': ['mosadaqa', 'saudi-moe', 'saudi', 'hec', 'nadra', 'dgip'],
  'faqs': [('Is Mosadaqa an office I visit?',
            'Mosadaqa describes the authenticated or verified document rather than a single office. The stages are handled through the issuing institution, the Pakistani educational authority and the '
            'Saudi-side verification or consular channel. The wording on your notice tells you where to follow up.'),
           ('My degree name does not match my passport or CNIC. Can verification still proceed?',
            'A difference between records is normally raised as a query that has to be resolved on the record that is wrong. The university corrects the academic record, DGIP the passport and NADRA the '
            'identity record. Ask the receiving authority what evidence it accepts for the difference.'),
           ('Does a “one and the same person” affidavit solve a name difference?',
            'Sometimes an organisation accepts a sworn declaration or a registered name-change record, and sometimes it requires the underlying record to be corrected. Ask the receiving authority in writing '
            'first and keep the answer with your file.'),
           ('Do you issue Mosadaqa certificates or attestations?',
            'No. SK Attestations is an independent assistance service. The competent authorities make the official decisions. We help compare records, prepare questions and sequence the stages for your '
            'document.'),
           ('Can a Mosadaqa process be completed without the original degree?',
            'That depends on the stage and the authority. Some submissions are electronic or verification-based, and others require the original document or an authenticated copy. Confirm the requirement for '
            'your document before sending originals anywhere.')],
  'related': ['/countries/saudi-arabia/', '/problems/degree-passport-name-mismatch/', '/problems/mosadaqa-verification-query/', '/services/mosadaqa-attestation/']},
 {'slug': 'apostille-vs-embassy-attestation',
  'title': 'Apostille or embassy legalisation?',
  'category': 'The right route',
  'summary': 'Why an apostille is not something an agent can issue for a Pakistani document, and when the embassy route applies.',
  'desc': 'The applicable route depends on treaty status, the document and the recipient, not the destination name alone. Check the right question first.',
  'answer': 'Establish whether the Apostille Convention applies to the document and between the relevant states. If it does not, ask the competent authorities about the applicable legalization route. Confirm '
            'the recipient’s instructions in either case.',
  'sections': [('Two routes, one initial question', 'Start with who is receiving the document and why. A university, employer, court or public office may have additional requirements beyond authentication.'),
               ('A practical sequence',
                'Identify the country of issue and destination. Check the HCCH status table and relevant declarations. Ask the competent authority about the document’s scope. Obtain the receiving '
                'organisation’s written instructions.'),
               ('Documents to have available', 'The document category, issuing country, destination and the recipient’s request. Check whether a translation, a copy or the original is requested.'),
               ('Common problems', 'Country membership alone does not resolve treaty applicability. Entry-into-force dates, objections, document exclusions and the intended use may matter.'),
               ('What varies', 'Translation, professional recognition, equivalence and destination-side procedures are separate questions. Do not treat a stamp as a guarantee that all of them are satisfied.')],
  'sources': ['hcch', 'mofa'],
  'related': ['/services/saudi-embassy-attestation/', '/services/mosadaqa-attestation/', '/services/uae-embassy-attestation/']},
 {'slug': 'hec-vs-ibcc',
  'title': 'HEC or IBCC: which authority applies?',
  'category': 'Education',
  'summary': 'Look at the qualification and awarding body, not just the word “certificate”.',
  'desc': 'Look at the qualification level and awarding body rather than the word “certificate” when you decide which educational authority to approach.',
  'answer': 'HEC’s attestation service concerns eligible higher-education documents. For school-level qualifications, check IBCC’s scope and requirements. Technical qualifications and diplomas need a closer '
            'look at their issuer and level.',
  'sections': [('Why the issuer matters', 'A university transcript, school certificate and vocational certificate can all describe education, but they are not interchangeable for attestation.'),
               ('A practical sequence', 'Write down the exact qualification, awarding body and campus. Check the relevant authority’s scope. Identify prerequisites and only then select a submission route.'),
               ('Documents to have available',
                'Your qualification title, transcript or marks record, awarding institution and existing verification details. Use the authority’s current checklist for submission documents.'),
               ('Common problems', 'Assuming every diploma goes through IBCC or every certificate goes through HEC can send a file to the wrong place.'),
               ('What varies', 'Equivalence, recognition and attestation are distinct processes. A foreign qualification or technical certificate may need a different enquiry.')],
  'sources': ['hec', 'ibcc', 'mofa'],
  'related': ['/services/mosadaqa-attestation/', '/services/qvp-attestation/', '/services/qvp-attestation/']},
 {'slug': 'why-documents-get-rejected',
  'title': 'Why was your document rejected?',
  'category': 'Problem solving',
  'summary': 'Use the stated reason to decide the next step.',
  'desc': 'A query or rejection notice tells you which part of the file needs attention. Read the stated reason before you resubmit or pay again.',
  'answer': 'Keep the rejection or query notice. Identify whether the issue concerns the record, missing supporting material, eligibility or submission method before attempting another application.',
  'sections': [('Start with the actual notice',
                'A rejection does not always mean the underlying document is invalid. Read the authority’s explanation and distinguish a request for information from a final decision.'),
               ('A practical sequence',
                'Save the notice and reference privately. Identify each requested change. Ask the responsible authority for clarification where needed. Resolve the issue through that authority before '
                'resubmitting.'),
               ('Documents to have available', 'The query wording, document category and a list of what was submitted. Remove personal identifiers when describing the issue in an initial email.'),
               ('Common problems', 'Resubmitting the same file without addressing the reason, changing the wrong record or buying an additional attestation that does not answer the query.'),
               ('What varies', 'Review, correction, appeal and reapplication procedures belong to the deciding authority. Do not assume one authority’s procedure applies to another.')],
  'sources': ['hec', 'ibcc', 'mofa'],
  'related': ['/problems/document-rejected/', '/problems/missing-document/', '/contact/']},
 {'slug': 'qvp-qualification-verification',
  'category': 'Saudi Arabia',
  'title': 'QVP: qualification verification',
  'summary': 'What the Qualification Verification Program checks, how it differs from attestation and what to fix before you resubmit.',
  'desc': 'QVP verification for Pakistani qualifications: what the program checks, how it differs from degree attestation, why queries happen and what to correct first.',
  'answer': 'QVP is the Saudi-side qualification-verification process that employers and work-permit applications commonly trigger. It checks that the degree or diploma you submitted is genuine and matches '
            'the qualification and job title your employer filed. Attestation and verification are separate checks on the same document, and a file usually needs both. Name or institution differences are the '
            'most common reason for a query, and they are corrected at the issuing side rather than by adding another stamp.',
  'sections': [('Verification is not the same as attestation',
                'Attestation confirms that the signatures and seals on a document are genuine. Verification confirms that the qualification itself is real and matches what was submitted. One does not replace '
                'the other, and a file can be returned for missing either.'),
               ('What the program compares',
                'The degree or diploma, the transcript where the qualification requires one, the awarding institution, the professional title the employer filed, and the identity details on the record. A '
                'difference between any two of these is the usual source of a query.'),
               ('Where queries usually come from',
                'A surname missing on the degree, a father’s name spelled differently on the identity record, a transliteration difference between the CNIC and the passport, or an institution name written '
                'differently from its official form. The notice you receive normally names the document and the discrepancy.'),
               ('How we help',
                'We compare the records you hold, list the exact differences, prepare the questions to put to the awarding institution or the identity authority, and sequence the correction so that the '
                'verification and attestation stages are not paid for twice.'),
               ('What we cannot do',
                'We cannot influence the programme’s decision, its timing or its outcome, and we do not alter documents or add unsupported statements. The employing organisation and the Saudi-side authority '
                'decide the result.')],
  'sources': ['mosadaqa', 'saudi-moe', 'saudi', 'hec'],
  'related': ['/services/qvp-attestation/', '/services/mosadaqa-attestation/', '/problems/mosadaqa-verification-query/', '/problems/degree-passport-name-mismatch/'],
  'faqs': [('Does QVP replace degree attestation?',
            'No. Attestation deals with the document as a document, verification deals with the qualification. Employers and authorities can ask for both, and the order is set by the process you are in.'),
           ('Can I start QVP before the attestation stages?',
            'Sometimes the correction work has to come first. If a record detail is wrong, that is fixed at the issuing side before the file goes anywhere else, otherwise the same query returns.'),
           ('Does a name difference always fail verification?',
            'Not always, but it is the most common reason for a query. Ask the receiving side what evidence it accepts for the difference rather than assuming an affidavit will be accepted.')]},
 {'slug': 'uae-embassy-attestation-process',
  'category': 'United Arab Emirates',
  'title': 'UAE Embassy attestation: stages',
  'summary': 'The order documents from Pakistan must follow for the UAE, and what the embassy stage actually checks.',
  'desc': 'How UAE Embassy attestation works for Pakistani documents: the stages in order, what the embassy counter checks, and how to avoid paying twice for the same file.',
  'answer': 'The UAE embassy or consulate legalises a Pakistani document only after the earlier Pakistani attestation is in place. The usual order is issuing authority, then MOFA Pakistan, then the UAE '
            'embassy or consulate — with Arabic translation and UAE-side attestation added later if the receiving organisation asks for them.',
  'sections': [('Why the order cannot be skipped',
                'Each stage authenticates the signature and seal of the stage before it. An embassy officer is checking that MOFA Pakistan has already attested the document; if that is missing, nothing later '
                'can fix it. Files that stall at the counter are almost always missing an earlier step, not the last one.'),
               ('The stages in order',
                '<ol><li>The issuing office attests the record, or confirms it — for a degree that means the awarding institution and normally the education authority.</li><li>MOFA Pakistan attests the '
                'document at Islamabad or a camp office.</li><li>The UAE embassy or consulate legalises it; submissions in Pakistan are handled through the designated service centres.</li><li>If required for '
                'use inside the UAE, Arabic translation and further attestation by the UAE Ministry of Foreign Affairs are added by the receiving organisation’s requirements.</li></ol>'),
               ('Documents people send most often',
                '<ul><li>Degrees and transcripts for employment and professional licensing</li><li>Marriage certificates and Nikah Nama for family visas and sponsorship</li><li>Birth certificates for '
                'dependants</li><li>Police character certificates for residency and employment</li><li>Medical reports and fitness certificates</li><li>Experience letters and salary certificates</li></ul>'),
               ('What the counter checks first',
                'The name on the document against the passport or Emirates ID, the date of birth, the presence of the preceding attestation, whether the document is the version the receiving organisation '
                'asked for, and whether it is still valid. A transliteration difference in a name is the most common reason for a query.'),
               ('What we do, and what we do not',
                'We compare the records you hold, list the exact differences, prepare the questions for the issuing office and sequence the stages so nothing is paid for twice. We do not issue attestations, '
                'we do not influence a decision, and we cannot shorten an authority’s processing time.')],
  'sources': ['uae-mofa', 'vfs-uae', 'mofa', 'hec'],
  'related': ['/services/uae-embassy-attestation/', '/guides/medical-report-attestation/', '/problems/degree-passport-name-mismatch/', '/problems/document-rejected/'],
  'faqs': [('How do I know whether my document needs the embassy stage?',
            'Ask the organisation that will use the document. Employment, residency and school files in the UAE normally need it; the exact wording of their request tells you what to prepare.'),
           ('Can the UAE embassy stage be done from inside the UAE?',
            'A document issued in Pakistan is normally legalised on the Pakistani side. Confirm the current arrangement with the UAE authority or the receiving organisation before sending originals anywhere.'),
           ('What if my Nikah Nama spelling differs from my passport?',
            'Sort the difference out with the office that issued the record before the attestation stages, and ask the receiving organisation what evidence it accepts. Attestation does not correct a '
            'record.')]},
 {'slug': 'medical-report-attestation',
  'category': 'Documents',
  'title': 'Medical report attestation',
  'summary': 'Why a medical report issued in Pakistan is not accepted on its own in the Gulf, and the stages that make it usable.',
  'desc': 'Medical report and fitness certificate attestation for the Gulf: who signs, which attestations come first, and how to prepare a report that is not rejected later.',
  'answer': 'A medical report issued in Pakistan is not accepted directly abroad. It is attested by the issuing hospital or practitioner, then by MOFA Pakistan, and then legalised by the embassy or consulate '
            'of the destination country. If the medical examination is carried out inside the Gulf state, it follows that country’s own approved health-centre process instead.',
  'sections': [('Two different medical processes',
                'There is a difference between legalising a report that already exists and completing a medical examination that a country requires. Employment and residency files usually require the '
                'examination to be done at an approved centre. A report you already hold — for insurance, a school, a court or a previous employer — is legalised as a document, and that is where attestation '
                'stages apply.'),
               ('Who signs, and why that matters',
                'The signature and stamp of the hospital or practitioner must be recognisable to the attesting authority. Reports signed by a practitioner whose signature is not on record, printed on plain '
                'paper, or issued without a hospital stamp are commonly refused at the first stage. Ask the hospital for a signed and stamped original on letterhead before starting.'),
               ('The stages in order',
                '<ol><li>Hospital or practitioner issues a signed, stamped original — with the patient’s name exactly as it appears on the passport.</li><li>The relevant health authority confirms it where '
                'that is required.</li><li>MOFA Pakistan attests the document.</li><li>The destination embassy or consulate legalises it.</li><li>Arabic translation and any further destination-side '
                'attestation are added if the receiving organisation asks for them.</li></ol>'),
               ('Why medical reports are queried',
                '<ul><li>Patient name or date of birth differing from the passport</li><li>Father’s name missing or spelled differently</li><li>No hospital stamp, no doctor’s signature on record, or a '
                'photocopy</li><li>A report older than the receiving organisation accepts</li><li>Diagnosis wording or a format the destination does not recognise</li></ul>'),
               ('How to avoid a second trip',
                'Decide the destination and purpose first, ask the receiving organisation for its written requirement, then prepare one clean original and keep a copy of everything you submit. Corrections '
                'belong with the hospital that issued the report, not with the attesting authority.')],
  'sources': ['mofa', 'uae-mofa', 'saudi', 'nadra'],
  'related': ['/services/uae-embassy-attestation/', '/services/saudi-embassy-attestation/', '/guides/uae-embassy-attestation-process/', '/problems/degree-passport-name-mismatch/'],
  'faqs': [('Can I attest a medical report I got last year?',
            'That depends on what the receiving organisation accepts. Some require a recent report; others accept an older one once it is attested. Ask first, then prepare the original.'),
           ('Do you arrange the medical test itself?',
            'No. Required medical examinations are carried out at the approved centres that the destination country designates. We help with the attestation of reports and documents, and with understanding '
            'which stage applies.'),
           ('My report has my father’s name missing — is that a problem?',
            'It can be, because name consistency is one of the first things checked. Ask the hospital about issuing a corrected original and ask the receiving organisation what evidence it accepts for the '
            'difference.')]}]
PROBLEMS = [
 dict(slug='name-mismatch',title='Name doesn’t match',tag='Passport ≠ Degree',desc='Passport, degree or identity record spelling differences: identify which issuer corrects which record before you pay for an attestation stage.',answer='Compare the actual records and identify the institution responsible for the difference. Do not change a document yourself.',guide='degree-name-different-from-passport',sections=[('Start with the comparison','Write down the name exactly as it appears on each document: degree, transcript, passport, CNIC or B-form. Note which field differs, not just that something differs.'),('Separate the records','An academic record, a passport and an identity record are held by different issuers. Only the issuer of the incorrect record can change it.'),('Ask before you pay','Ask the receiving organisation what evidence it accepts and whether the difference affects its decision. Do not buy an additional attestation stage to answer a question about a name.')]),
 dict(slug='degree-passport-name-mismatch',title='Degree, passport and CNIC name mismatch',tag='Three records, one name',desc='Degree, passport and CNIC names that differ: compare the records, identify the correct issuer and resolve the difference before attestation.',answer='A difference between the degree, passport and CNIC is resolved on the record that is wrong, not with an extra stamp: the university corrects the degree, DGIP the passport and NADRA the identity record. Ask the receiving organisation what evidence it accepts before spending on attestation stages.',guide='degree-name-different-from-passport',sections=[('What the three records are used for','<table class="content-table"><thead><tr><th>Record</th><th>What an authority compares it against</th></tr></thead><tbody><tr><td>Degree or transcript</td><td>The university’s own record of your qualification and name</td></tr><tr><td>Passport</td><td>The identity record and, in many processes, the name a document will be issued under</td></tr><tr><td>CNIC, B-form or identity record</td><td>The civilian identity record and the supporting family details it contains</td></tr></tbody></table>'),('The differences we see most often','<ul><li>A short or abbreviated name on the degree, with the full name on the CNIC and passport.</li><li>A surname present on the passport and missing from the degree.</li><li>A father’s name written differently on the degree and on the identity record.</li><li>Spellings that changed between two transliterations of the same name.</li><li>A name changed after marriage, without the registration record attached.</li><li>A date of birth that differs between the academic record and the identity record.</li></ul>'),('Which issuer you approach','<ol><li>Difference on the degree or transcript: ask the university or board that issued the record. Keep its written reply.</li><li>Difference on the passport: the passport service that issued it deals with the record.</li><li>Difference on the CNIC, B-form or family details: the national identity authority deals with the record.</li><li>Difference caused by marriage or a registered name change: the authority that registered the change.</li></ol><p>An affidavit or “one and the same person” declaration is sometimes accepted and sometimes not. Ask the receiving organisation in writing before relying on one.</p>'),('Order matters','Correcting a record after authentication usually means the authenticated document no longer matches the corrected record, and the stages may have to be repeated. Compare the records first, resolve the difference, and only then begin the authentication and legalization stages.'),('If the document is for Saudi Arabia','Academic records used in Saudi Arabia are compared during the verification stage commonly called <a href="/guides/mosadaqa-degree-attestation/">mosadaqa</a>. The same records are checked there, so the difference has to be resolved at source rather than explained later.'),('What we can and cannot do','We can list the exact differences, prepare the questions for each issuer, and sequence the correction and authentication stages. We do not alter documents, influence a decision, or guarantee that a receiving organisation will accept a particular explanation.')]),
 dict(slug='document-rejected',title='Document rejected',tag='Something is missing',desc='Use the authority’s stated reason as the starting point, and distinguish a request for information from a final decision before resubmitting.',answer='Use the authority’s stated reason as the starting point. Repeating a submission without addressing the query may not resolve it.',guide='why-documents-get-rejected',sections=[('Read the notice twice','Distinguish a request for further information from a refusal on eligibility. They lead to different next steps, and one of them may not need a new application at all.'),('Match the reason to the right issuer','A query about the underlying record belongs with the issuer. A query about the submission belongs with the authority that received it. Sending both to the wrong place wastes a cycle.'),('Prepare the reply before paying again','List what has changed since the first submission. If nothing has changed, ask the authority what it needs rather than repeating the same file with an extra stamp.')]),
 dict(slug='previously-rejected',title='Previously rejected',tag='Understand before resubmitting',desc='Reworking a file that was rejected earlier: what to review, what to change and what to confirm before a second submission.',answer='A previous rejection needs a review of the reason and what has changed. Additional stamps alone may not address the issue.',guide='why-documents-get-rejected',sections=[('Establish what has actually changed','Write down each point of the earlier query and what you have done about it. An unchanged file submitted again usually produces the same result.'),('Decide whether a correction or a clarification is needed','Some queries are answered with a corrected record, others with a document the issuer sends directly, and others with a written clarification from the authority that raised them.'),('Keep one private summary of the file','A short private summary of documents, stages, dates and reference numbers makes a second submission easier to prepare and easier to explain. Do not include identity numbers in an initial email to a new adviser.')]),
 dict(slug='which-authority',title='Not sure which authority',tag='HEC? IBCC? MOFA?',desc='Which authority to approach first depends on the qualification level, the awarding body and the intended use rather than the document title alone.',answer='The document’s issuer and qualification level determine which authority to check first. The name of the document alone may be insufficient.',guide='hec-vs-ibcc',sections=[('Identify the awarding body','Write down the institution or board that awarded the qualification and the level of the award. This decides the first enquiry.'),('Separate the stages','Verification of the original record, educational attestation, foreign affairs authentication and destination-side checks are different stages with different officeholders.'),('Confirm with the issuer of the requirement','Ask the organisation that asked for the document what it actually needs: verification, an authenticated original, an equivalence decision or a combination.')]),
 dict(slug='apostille-or-embassy',title='Apostille or embassy?',tag='Which route applies?',desc='Treaty status, the document category and the recipient’s instructions decide whether an apostille or a consular route applies to your file.',answer='Check treaty applicability and the receiving organisation’s instructions before choosing an authentication route.',guide='apostille-vs-embassy-attestation',sections=[('Treaty status is document-specific','Membership of the Convention does not by itself decide the route. Entry into force, declarations and the type of document can all matter.'),('The recipient still decides','A destination-side authority may require its own legalization stage or an internal procedure after authentication. Ask for its written instructions.'),('Do not buy both routes','If the applicable route is unclear, ask the competent authority before paying for two sets of stamps. An unnecessary stage usually delays rather than helps.')]),
 dict(slug='missing-document',title='Missing document',tag='What do you need first?',desc='Work out whether the missing item is an original record, supporting evidence or an earlier verification, and ask about replacement records.',answer='Find out whether the missing item is an original record, supporting evidence or an earlier verification. These need different next steps.',guide='why-documents-get-rejected',sections=[('Classify the missing item','An original certificate, a supporting identity record and an earlier verification certificate are obtained from different places, and often on different timelines.'),('Ask about replacement records','An issuer may be able to reissue or verify a lost record. Ask what the process is and whether it issues the record directly to the requesting authority.'),('Confirm what the recipient will accept','Before ordering a replacement, confirm whether the receiving organisation requires the original, a certified copy or direct verification.')]),
 dict(slug='mosadaqa-verification-query',title='Mosadaqa verification query',tag='Degree queried for Saudi use',desc='A Mosadaqa or certificate-verification query about a degree: what it usually concerns, what to prepare and who to ask before resubmitting.',answer='A verification query usually concerns the record details or the document itself rather than the stamps. Read the exact wording, resolve the issue at the issuing institution, and let the receiving authority confirm what it will accept.',guide='mosadaqa-degree-attestation',sections=[('What the query usually concerns','<ul><li>A name, father’s name or date of birth that differs between the degree and the identity records submitted.</li><li>An institution, programme title or year that the awarding body records differently.</li><li>A document that is illegible, altered-looking or missing a page.</li><li>An unclear submission: the wrong document uploaded, or a verification step still pending.</li></ul><p>The exact wording decides the next step. Work from the notice rather than from a general checklist.'),('Prepare the comparison before you reply','Put the degree, transcript, CNIC, passport and the notice side by side. Write out each difference and the record that carries it. This is what both the issuer and the receiving authority will ask about.'),('Who to ask','The awarding institution answers questions about its own record. The identity authority answers questions about the CNIC or B-form. The authority that raised the query answers questions about what it will accept next. Ask each in writing and keep the replies with your file.'),('What we help with','We prepare the comparison, draft the questions for each office, and set the order of the correction and verification steps so a query is not answered with an unnecessary extra attestation. We do not alter records or decide the outcome.')]),
]
COUNTRIES = {'Saudi Arabia': 'For Saudi Arabia, ask the requesting organisation whether it needs Mosadaqa verification of an academic record, an employment attestation or a combination, and keep its exact wording. Name '
                 'and record details are usually compared before anything else is checked.',
 'United Arab Emirates': 'For the UAE, a document issued in Pakistan is attested inside Pakistan first, then legalised by the UAE embassy or consulate. Medical reports, marriage records and degrees all follow '
                         'that order. Confirm with the receiving organisation whether Arabic translation or a further UAE-side attestation is also required.',
 'Qatar': 'For Qatar, identify the receiving organisation and its document requirement. Attestation of the Pakistani record normally precedes the embassy or consulate stage, and the destination may ask for '
          'Arabic translation.',
 'Kuwait': 'For Kuwait, start with the exact document and the requesting organisation. Employment and residency files usually need the Pakistani record attested before the embassy stage.',
 'Oman': 'For Oman, confirm whether the requirement is document attestation, professional licensing or a medical process, because each one has a different starting point.',
 'Bahrain': 'For Bahrain, check the receiving organisation’s written requirement first, then prepare the original document and its earlier attestation.',
 'United Kingdom': 'For the United Kingdom, ask the receiving organisation what it accepts for a Pakistani record, and whether a certified translation or an issuer verification is needed.',
 'Europe': 'Europe is not a single document jurisdiction. Identify the specific country and the organisation using the document before choosing a route.',
 'Canada': 'For Canada, the receiving body usually decides: an employer, a university, a licensing body and an immigration process may each ask for different evidence.',
 'Australia': 'For Australia, ask whether the recipient needs an original, a certified copy or direct issuer verification, and whether a translation is required.',
 'Other': 'Start with the exact destination and the organisation receiving the document. Send us the wording of the request and we will map it to the stages.'}
FAQS = [('Services',
  'Which services do you provide?',
  'Five: Mosadaqa degree attestation for Saudi Arabia, Saudi Culture attestation, Saudi Embassy attestation, QVP qualification verification and UAE Embassy attestation for documents issued in Pakistan. We do '
  'not provide services outside this list.'),
 ('Services',
  'Do you issue attestations or certificates yourselves?',
  'No. SK Immigration Services prepares and sequences files. HEC, IBCC, MOFA Pakistan, the Saudi mission, the UAE embassy or consulate and the destination authorities make every official decision.'),
 ('Services',
  'Can you guarantee an attestation or a visa outcome?',
  'No, and treat anyone who guarantees one with caution. Eligibility, verification and acceptance belong to the authorities and to the organisation receiving your document.'),
 ('Services',
  'What does it cost and how long does it take?',
  'Official charges and processing arrangements change and vary by document, so this site does not publish amounts or timelines. Ask us on WhatsApp with your document type and we will tell you what applies to '
  'your case at that moment.'),
 ('Services',
  'Can someone submit my documents on my behalf?',
  'Representation, personal appearance and courier rules differ by authority and document. Check the current instruction and authorise anyone only after you know what will happen to your original documents.'),
 ('Mosadaqa',
  'What does mosadaqa mean?',
  'Mosadaqa is the term used in Pakistan for the attestation or verification of a degree or certificate, most often for documents that will be used in Saudi Arabia. It is not a single office: the record still '
  'passes through the education authority and the Pakistani and Saudi-side stages that apply to your document.'),
 ('Mosadaqa',
  'Why did Mosadaqa return a query on my degree?',
  'Queries nearly always name a record detail: a missing surname, a father’s name spelled differently on the CNIC or passport, a date of birth that differs, or an awarding institution whose verification is '
  'not complete. Read the exact wording and fix the record with the issuer before paying for another stage.'),
 ('Mosadaqa',
  'My degree name does not match my passport or CNIC. What comes first?',
  'Compare the three records and write down the exact difference. Only the issuer of the incorrect record can correct it: the university for the degree, NADRA for the identity record, DGIP for the passport. '
  'Ask the receiving organisation what evidence it accepts for the difference before you submit anything.'),
 ('Mosadaqa',
  'Is an affidavit enough for a name difference?',
  'Not on its own. Some organisations accept a sworn declaration or a NADRA name-change record; others require the underlying record to be corrected. Ask in writing, keep the answer, and do not alter a '
  'document yourself.'),
 ('Saudi Arabia',
  'Do I need both Saudi Culture and Saudi Embassy attestation?',
  'Do not assume both. The stages that apply depend on the document, its purpose and what the requesting organisation asks for. Ask which one is required for your file before paying for a stage.'),
 ('Saudi Arabia',
  'Are requirements the same for every Saudi organisation?',
  'No. An employer, a university, a licensing body and a residency file may each require different verification or attestation. Obtain the requirement in writing.'),
 ('QVP',
  'What is QVP?',
  'QVP is the Qualification Verification Program: a Saudi-side verification of an academic qualification, commonly required in connection with work permits and professional employment. It checks the record, '
  'not the stamps, which is why record details must match before submission.'),
 ('QVP',
  'Is QVP the same as Mosadaqa?',
  'No. Mosadaqa describes attestation of the document; QVP is qualification verification in the Saudi-side process. Both may apply to the same degree, at different points in the file.'),
 ('UAE',
  'Which documents do you attest for the UAE?',
  'Degrees and transcripts, marriage records and Nikah Nama, birth certificates, police character certificates, medical reports, experience letters and commercial documents — each following the stages that '
  'apply to that record.'),
 ('UAE',
  'Can my Pakistani medical report be used for a UAE visa?',
  'A report issued in Pakistan is not accepted directly: it is attested by the issuing hospital or practitioner, then by MOFA Pakistan, then legalised by the UAE embassy or consulate. Medical fitness required '
  'for residency inside the UAE is carried out at approved health centres, which is a separate process.'),
 ('UAE',
  'Why was my document refused at the embassy counter?',
  'Most often because an earlier stage is missing, the name or date of birth differs from the passport, the document is a copy where an original is needed, or the certificate has expired. The counter checks '
  'the preceding attestation before anything else.'),
 ('Documents',
  'Should I upload my documents to this website?',
  'No. This website has no upload function and the assessment asks for no identity numbers. Start with the document type, the destination and the problem in words, and share documents only when it is '
  'necessary with the people who must handle them.'),
 ('Documents',
  'What should I have ready before I contact you?',
  'The exact document name, the issuing office, where it will be used, any written request you received, and the differences you already know about in names and dates. That is enough to tell you which stage '
  'applies.'),
 ('Trust',
  'How do I know you are a real business?',
  'The office is at Office No. 10, Alfazal Plaza 64C, Satellite Town, Rawalpindi, and the company is SK Immigration Services (SMC-Private) Limited, SECP CUIN 0304985. Our registration and contact details are '
  'published for verification, and our main website explains the same position.'),
 ('Trust',
  'Do you promise to get my document approved?',
  'No. We explain the stages, prepare the questions, compare records and keep the sequence in order so nothing is paid for twice. The decision stays with the authority.'),
 ('Process',
  'How does your process work?',
  'You describe the document and the request you received; we map it to the stages, list the records to compare and set out what to fix first. You then decide whether to proceed, and you review every '
  'submission yourself.')]
