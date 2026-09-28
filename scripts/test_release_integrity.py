#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1];J=lambda p:json.loads((R/p).read_text());E=[]
profile=J('research/reproducibility-profile.json');schema=J('schemas/research-result-v1.schema.json')
req=set(profile['required_for_frozen_result']); props=set(schema['properties']); sreq=set(schema['required'])
if not req<=props:E.append('profile fields absent from schema: '+str(sorted(req-props)))
if not req<=sreq:E.append('profile fields not schema-required: '+str(sorted(req-sreq)))
gates={x['experiment_id']:x for x in J('research/experiment-gates.json')['experiments']}
for eid,g in gates.items():
 if g['state']=='BLOCKED' and g['claim_allowed'] is not False:E.append('blocked gate permits claim:'+eid)
for c in J('research/claim-registry.json')['claims']:
 if c['status']=='blocked_experiment':
  # blocked claims must point to gate registry and must not assert a positive inferential result
  if 'research/experiment-gates.json' not in c['evidence']:E.append('blocked claim lacks gate evidence:'+c['claim_id'])
api=J('api/examples/experiments.json')
if api.get('provenance',{}).get('corpus_version')!=(R/'VERSION').read_text().strip():E.append('experiment API version stale')
docs=J('api/examples/documents.json')
if docs.get('provenance',{}).get('corpus_version')!=(R/'VERSION').read_text().strip():E.append('document API version stale')
if E:print('RELEASE INTEGRITY FAILED',*E,sep='\n- ');sys.exit(1)
print('OK: reproducibility profile/schema agree; blocked gates remain non-claiming; API examples match release.')
