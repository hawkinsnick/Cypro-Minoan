#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1];J=lambda p:json.loads((R/p).read_text());E=[]
g={x['experiment_id']:x for x in J('research/experiment-gates.json')['experiments']}
graph=J('evidence/graph.json')
for e in graph['edges']:
 if e['type']=='SUPPORTS' and e['from'] in g and not g[e['from']]['claim_allowed']:E.append('blocked experiment supports claim')
types={x['type']:x for x in J('comparative/hypothesis-types.json')['types']}
for n in ['graphic_similarity','structural_similarity','distributional_similarity','proposed_historical_relationship']:
 if types[n]['phonetic_implication'] is not False:E.append('phonetic leakage:'+n)
if any(x['transitive'] for x in types.values()):E.append('unexpected transitivity')
if 'unknown never counts as demonstrably independent' not in J('provenance/independence-policy.json')['counting_rules']:E.append('independence leakage')
if E:print('5.0 CONFORMANCE FAILED',*E,sep='\n- ');sys.exit(1)
print('OK: negative epistemic constraints hold.')
