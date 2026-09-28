#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
x=json.loads((R/'coverage/completeness-matrix.json').read_text())
print('Cypro-Minoan coverage —',x['as_of'])
for d in x['dimensions']:
 den=d['known']; val=f"{d['covered']}/{den}" if den is not None else f"{d['covered']} (open-world denominator)"
 print(f"- {d['dimension']}: {val} — {d['interpretation']}")
print('Aggregate completeness score: PROHIBITED')
