"""Replay two attributed tablet positions; preserve earlier assertions and unresolved apparatus."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REGISTER='research/source-check-CMOC-0209-2026-10-14.json'
BASELINE='6b6240ca66c70ec01a8c33b48499985de894ea575344119122f18049fbbd521a'
REGISTER_PIN='4691085c9f571f32dd389941ba53f2e5f0e350768b91d13fa869132ad133393b'
COMPARISONS_PIN='a1622dfda467ddad29b04a730e7c9e4ab793b866039e0fe2b461ffc3a81d9b70'
def load(root,p):return json.loads((root/p).read_text())
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def additions(root=ROOT):
 x=load(root,REGISTER)
 if digest(x)!=REGISTER_PIN:raise ValueError('inspected CM209 provenance, uncertainty or apparatus drift')
 return x['expected_additions']
def validate(root=ROOT):
 rows=additions(root);native=load(root,'occurrences/occurrences.json')
 if digest({**native,'occurrences':native['occurrences'][:26]})!=BASELINE:raise ValueError('historical 26 assertions changed')
 if native['occurrences'][26:]!=rows:raise ValueError('CM209 finite tail changed or extra positions admitted')
 if len({r['record_id'] for r in native['occurrences']})!=13:raise ValueError('rich coverage drift')
 if digest(load(root,'research/source-reconciliation.json')['comparisons'][3:])!=COMPARISONS_PIN:raise ValueError('source differences or internal inconsistency changed')
 if any(r['record_id']=='CMOC-0209' and r['zone_id']=='A.II.5.01-first-group' for r in native['occurrences']):raise ValueError('internal source conflict selected without review')
 return {'status':'PASS_PARTIAL_CM209_SOURCE_CHECK','added_occurrences':2,'total_occurrences':28,'partially_covered_rich_records':13,'uncovered_rich_records':8,'full_tablet_transcription':False,'expert_acceptance':False}
if __name__=='__main__':print(json.dumps(validate()))
