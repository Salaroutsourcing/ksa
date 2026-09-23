#!/usr/bin/env python3
"""Create an unpublished article or service record without changing existing content."""
import argparse
import json
import re
from datetime import date
from pathlib import Path
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('kind', choices=['blog', 'services'])
parser.add_argument('slug', help='Lowercase URL name, for example preparing-your-documents')
parser.add_argument('--title', required=True)
a = parser.parse_args()
if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', a.slug): parser.error('Use lowercase letters, numbers and hyphens for the slug.')
root = Path(__file__).resolve().parents[1]
file = root / 'content' / a.kind / (a.slug + '.json')
record = {'status': 'draft', 'slug': a.slug, 'title': a.title, 'icon': 'file-text', 'category': 'Document preparation', 'description': 'Replace with a short, specific page description.', 'answer': 'Replace with the main answer or service scope.', 'sections': [{'title': 'What to understand first', 'text': 'Replace with your article or service information.'}], 'sources': [], 'related': [], 'updated': date.today().isoformat()}
if a.kind == 'blog': record.update(author='SK Attestation Services', published=date.today().isoformat())
else: record.update(order=100, steps=['Replace with the preparation checklist.'])
with file.open('x') as out: json.dump(record, out, indent=2, ensure_ascii=False); out.write('\n')
print(f'Created draft: {file.relative_to(root)}. Edit the content, then change status to published when ready.')
