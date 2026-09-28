#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f"{p.relative_to(ROOT)}: {e}")
idx=json.loads((ROOT/'corpus/index.json').read_text())
actual=[p for p in (ROOT/'corpus/inscriptions').glob('*.json') if p.name!='TEMPLATE.json']
if idx['record_count'] != len(actual): errors.append(f"corpus/index.json record_count={idx['record_count']} but found {len(actual)} records")
required=['README.md','RESEARCH_ETHICS.md','CONTRIBUTING.md','CITATION.cff','LICENSE','schemas/inscription.schema.json','schemas/sign.schema.json','schemas/assertion.schema.json','bibliography/sources.json']
for x in required:
    if not (ROOT/x).exists(): errors.append(f"missing required file: {x}")
if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'OK: JSON parses; corpus index consistent; required foundation files present. Records: {len(actual)}')
