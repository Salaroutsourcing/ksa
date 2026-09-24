#!/usr/bin/env python3
"""Export only public pages and assets. Never deploy source files or local tools."""
import json
import shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for relative in json.loads((ROOT / '.build-manifest.json').read_text()) + ['CNAME', '.nojekyll', 'google73cb9920efe3c5ae.html']:
    source = (ROOT / relative).resolve()
    if not source.is_relative_to(ROOT) or relative.startswith('.') and relative != '.nojekyll':
        raise ValueError('Invalid public path: ' + relative)
    target = OUT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
shutil.copytree(ROOT / 'assets', OUT / 'assets')
print('Public website exported to _site/; content sources, templates and tools excluded.')
