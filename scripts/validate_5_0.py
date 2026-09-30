#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1];J=lambda p:json.loads((R/p).read_text());E=[];V=(R/'VERSION').read_text().strip()
idx=J('corpus/index.json')
if not V.startswith('5.') or idx['version']!=V:E.append('version')
for rid in idx['records']:
 if not J(f'corpus/inscriptions/{rid}.json').get('record_version'):E.append('record version absent:'+rid)
cat=J('catalogues/master.json')
if len(cat['entries'])!=254 or sum(x.get('siglum') is not None for x in cat['entries'])!=68:E.append('catalogue')
g={x['experiment_id']:x for x in J('research/experiment-gates.json')['experiments']}
if any(x['state']=='BLOCKED' and x['claim_allowed'] for x in g.values()):E.append('blocked_claim')
rp={x['profile_id']:x for x in J('research/readiness-profiles.json')['profiles']}
if rp['corpus-frequency']['state']!='BLOCKED' or rp['catalogue-structure']['state']!='READY':E.append('readiness')
sn={x['snapshot_id']:x for x in J('research/dataset-snapshots.json')['snapshots']}
for x in ['cmoc-5.0-rich-records','cmoc-5.0-catalogue-control','cmoc-5.0-occurrences']:
 if x not in sn:E.append('snapshot:'+x)
graph=J('evidence/graph.json')
if any(e['type']=='SUPPORTS' and g.get(e['from'],{}).get('claim_allowed') is False for e in graph['edges']):E.append('blocked_support_edge')
ip=J('provenance/independence-policy.json')
if 'unknown never counts as demonstrably independent' not in ip['counting_rules']:E.append('independence')
neg=J('conformance/negative-fixtures.json')['fixtures']
if len(neg)<6 or any(x['expected']!='reject' for x in neg):E.append('negative_fixtures')
cm=J('coverage/completeness-matrix.json')
if any(x['known'] is None and '%' in x['interpretation'] for x in cm['dimensions']):E.append('open_world_percentage')
for p in ['evidence/graph-contract.json','research/dependency-contract.json','provenance/assertion-ledger.json','rights/representation-policy.json','conformance/positive-fixtures.json','docs/ARCHITECTURE-5.0.md','docs/AUDIT_5.0.0.md']:
 if not (R/p).exists():E.append('missing:'+p)
if E:print('VALIDATION FAILED',*E,sep='\n- ');sys.exit(1)
print(f'OK v{V}: readiness/evidence-graph/provenance/conformance integrity passed; {len(idx["records"])} rich records; 254 slots/68 exact sigla.')

