#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1]; J=lambda p:json.loads((R/p).read_text()); E=[]
V=(R/'VERSION').read_text().strip(); idx=J('corpus/index.json'); src={x['source_id'] for x in J('bibliography/sources.json')}
if V!='3.0.0':E.append('VERSION')
if idx['version']!=V or idx['record_count']!=len(idx['records']):E.append('index')
for rid in idx['records']:
 p=R/'corpus/inscriptions'/f'{rid}.json'
 if not p.exists() or J(p.relative_to(R)).get('record_version')!=V:E.append('record:'+rid)
cat=J('catalogues/master.json')
if len(cat['entries'])!=254 or cat['entry_count']!=254:E.append('catalogue_count')
if sum(x.get('siglum') is not None for x in cat['entries'])!=68:E.append('exact_sigla')
occ=J('occurrences/occurrences.json')['occurrences']
if any(x['record_id'] not in idx['records'] or x['source_id'] not in src for x in occ):E.append('occurrence_refs')
wit=J('witnesses/assertions.json')['witnesses']
if any(x['record_id'] not in idx['records'] or x['source_id'] not in src for x in wit):E.append('witness_refs')
dq=J('corpus/discovery-queue.json')['items']
for x in dq:
 if x['status']=='ingested' and x.get('record_id') not in idx['records']:E.append('discovery:'+x['key'])
lin=J('provenance/source-lineage.json')['lineages']
if any(x['source_id'] not in src or (x.get('parent_source_id') and x['parent_source_id'] not in src) for x in lin):E.append('lineage_refs')
g=J('research/experiment-gates.json')['experiments']
if any(x['state']=='BLOCKED' and x['claim_allowed'] for x in g):E.append('blocked_claim')
cl=J('research/claim-registry.json')['claims']
if any(x['status']=='blocked_experiment' and 'BLOCKED' not in str(g) for x in cl):E.append('claim_gate')
u=J('signs/unicode-14plus.json')
if len(u['characters'])!=99:E.append('unicode')
cov=J('coverage/layers.json')['layers']
if len({x['layer'] for x in cov})!=len(cov):E.append('coverage_layers')
fix=J('interchange/fixtures/cm-record-v0.1.json')
if fix.get('project')!='cypro-minoan' or not all(k in fix for k in ['record_id','assertions','rights']):E.append('interop_fixture')
for p in ['docs/ARCHITECTURE-3.0.md','docs/AUDIT_3.0.0.md','docs/RELEASE-CRITERIA-3.0.md','research/dataset-snapshots.json','research/experiment-specifications.json','catalogues/reconciliation-ledger.json','corpus/frontier-registry.json','palaeography/variant-registry.json']:
 if not (R/p).exists():E.append('missing:'+p)
if E: print('VALIDATION FAILED',*E,sep='\n- ');sys.exit(1)
print(f'OK v{V}: {idx["record_count"]} rich records; 254 controlled slots/68 exact sigla; {len(occ)} occurrences; {len(wit)} witnesses; 99 Unicode characters; gates/lineage/interchange integrity passed.')
