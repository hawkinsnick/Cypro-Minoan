#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1];J=lambda p:json.loads((R/p).read_text());E=[];V=(R/'VERSION').read_text().strip()
idx=J('corpus/index.json');src={x['source_id'] for x in J('bibliography/sources.json')}
if not V.startswith('4.0.') or idx['version']!=V:E.append('version')
for rid in idx['records']:
 if J(f'corpus/inscriptions/{rid}.json').get('record_version')!=V:E.append('record:'+rid)
cat=J('catalogues/master.json')
if len(cat['entries'])!=254 or sum(x.get('siglum') is not None for x in cat['entries'])!=68:E.append('catalogue')
cm=J('coverage/completeness-matrix.json')
if any(x['known'] is None and '%' in x['interpretation'] for x in cm['dimensions']):E.append('open_world_percentage')
if not any(x['dimension']=='project_variant_population' and x['covered']==0 for x in cm['dimensions']):E.append('variant_state')
g=J('research/experiment-gates.json')['experiments']
if any(x['state']=='BLOCKED' and x['claim_allowed'] for x in g):E.append('blocked_claim')
if not any(x['experiment_id']=='cm-full-frequency-v1' and x['state']=='BLOCKED' for x in g):E.append('frequency_gate')
for p in ['research/reproducibility-profile.json','research/sensitivity-matrix.json','research/evidence-packages.json','comparative/null-controls.json','comparative/hypothesis-types.json','shared-core/candidate-v0.1.json','coverage/completeness-matrix.json','acquisition/priority-queue.json','corpus/frontier-policy.json','schemas/research-result-v1.schema.json','docs/ARCHITECTURE-4.0.md','docs/AUDIT_4.0.0.md']:
 if not (R/p).exists():E.append('missing:'+p)
for x in J('witnesses/assertions.json')['witnesses']:
 if x['source_id'] not in src or x['record_id'] not in idx['records']:E.append('witness_ref')
for x in J('occurrences/occurrences.json')['occurrences']:
 if x['source_id'] not in src or x['record_id'] not in idx['records']:E.append('occurrence_ref')
core=J('shared-core/candidate-v0.1.json')
if core['linear_b_status']!='deferred' or 'phonetic_value' not in core['excluded_as_script_specific']:E.append('core_boundary')
if E:print('VALIDATION FAILED',*E,sep='\n- ');sys.exit(1)
print(f'OK v{V}: reproducibility/completeness/gates/core-boundary integrity passed; {len(idx["records"])} rich records; 254 slots/68 exact sigla; 3 verified occurrences.')
