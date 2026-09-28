#!/usr/bin/env python3
import json,pathlib,collections
R=pathlib.Path(__file__).resolve().parents[1]
occ=json.loads((R/'occurrences/occurrences.json').read_text())['occurrences']
gates={x['experiment_id']:x for x in json.loads((R/'research/experiment-gates.json').read_text())['experiments']}
g=gates['cm-full-frequency-v1']
out={'experiment_id':g['experiment_id'],'state':g['state'],'claim_allowed':g['claim_allowed'],'occurrence_count':len(occ),'descriptive_counts':dict(collections.Counter(x.get('published_sign_label') for x in occ)),'warning':'Counts describe only the explicitly encoded source-verified subset; they are not corpus-wide frequencies.'}
print(json.dumps(out,indent=2,ensure_ascii=False))
