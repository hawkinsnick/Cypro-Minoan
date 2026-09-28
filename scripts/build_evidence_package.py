#!/usr/bin/env python3
import json,pathlib,hashlib
R=pathlib.Path(__file__).resolve().parents[1]
spec=json.loads((R/'research/evidence-packages.json').read_text())
out={'version':spec['version'],'packages':[]}
for p in spec['packages']:
 files=[]
 for rel in p['inputs']:
  q=R/rel
  files.append({'path':rel,'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'bytes':q.stat().st_size})
 out['packages'].append({**p,'files':files})
print(json.dumps(out,indent=2))
