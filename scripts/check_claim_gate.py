#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1]
g={x['experiment_id']:x for x in json.loads((R/'research/experiment-gates.json').read_text())['experiments']}
eid=sys.argv[1] if len(sys.argv)>1 else 'cm-full-frequency-v1'
x=g[eid]
print(json.dumps({'experiment_id':eid,'state':x['state'],'claim_allowed':x['claim_allowed'],'prerequisites':x['prerequisites']},indent=2))
sys.exit(0 if x['claim_allowed'] else 2)
