"""Loss-aware assertion delivery: literal source + reconciliation + identity context."""
import argparse,csv,io,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(root,p):return json.loads((root/p).read_text())
def build(root=ROOT):
 ch=(root/'corpus/critical-readings.json').exists();canonical=load(root,'corpus/critical-readings.json' if ch else 'occurrences/occurrences.json');raw=canonical if ch else canonical['occurrences'];key='reading_id' if ch else 'occurrence_id'
 ref=load(root,'research/reference-reconciliation-v2.json');qualified=ref['existing_reading_dispositions' if ch else 'existing_occurrence_dispositions'];index={q[key]:q for q in qualified}
 if len(index)!=len(qualified) or set(index)!={r[key] for r in raw}:raise ValueError('missing, orphan or duplicate reconciliation assertion')
 identities=load(root,'research/identity-reconciliation-v2.json')['rows'];identity={r['record_id']:r for r in identities}
 if len(identity)!=len(identities):raise ValueError('duplicate identity disposition')
 comparisons=load(root,'research/source-reconciliation.json')['comparisons'];views=[]
 for row in raw:
  rid=row['object_id'] if ch else row['record_id'];q=index[row[key]]
  if q['record_id']!=rid or rid not in identity:raise ValueError('wrong record/reconciliation join')
  disputes=[c for c in comparisons if c['record_id']==rid and (c.get('field')!='published_sign_label' or (c.get('zone_id')==row.get('zone_id') and c.get('position')==row.get('position')))]
  views.append({'assertion_id':row[key],'record_id':rid,'source_assertion':row,'reconciliation_context':q,'source_disagreements':disputes,'identity_context':identity[rid],'certainty_scope':'Certainty in the literal source assertion is certainty of attribution/encoding, not independent sign, language or physical-identity acceptance.','full_transcription_inferred':False,'independent_review_complete':False})
 return {'schema_version':'1.0','scope':'Existing assertions joined to full encoded reconciliation and identity context; no new readings or occurrences.','preferred_researcher_view':True,'source_literal_files_unchanged':True,'assertion_count':len(views),'assertions':views}
def csv_text(data):
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator="\n");w.writerow(['assertion_id','record_id','source_assertion_json','reconciliation_context_json','source_disagreements_json','identity_context_json','certainty_scope','full_transcription_inferred','independent_review_complete'])
 for r in data['assertions']:w.writerow([r['assertion_id'],r['record_id']]+[json.dumps(r[k],ensure_ascii=False,sort_keys=True) for k in ['source_assertion','reconciliation_context','source_disagreements','identity_context']]+[r['certainty_scope'],False,False])
 return out.getvalue()
def validate(root=ROOT):
 data=build(root)
 if load(root,'research/qualified-assertion-views.json')!=data:raise ValueError('qualified view lost or changed assertion/context')
 if (root/'exports/qualified-assertions.csv').read_bytes()!=csv_text(data).encode():raise ValueError('qualified CSV lost context')
 return {'status':'PASS_LOSS_AWARE_ASSERTION_DELIVERY','assertions':len(data['assertions']),'reading_growth':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--record');p.add_argument('--format',choices=['json','csv'],default='json');a=p.parse_args();data=build()
 if a.write:
  (ROOT/'research/qualified-assertion-views.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');(ROOT/'exports').mkdir(exist_ok=True);(ROOT/'exports/qualified-assertions.csv').write_bytes(csv_text(data).encode());print(json.dumps(validate()))
 else:
  if a.record:data['assertions']=[r for r in data['assertions'] if r['record_id']==a.record];data['assertion_count']=len(data['assertions'])
  print(csv_text(data) if a.format=='csv' else json.dumps(data,ensure_ascii=False,indent=2),end='\n' if a.format=='json' else '')
