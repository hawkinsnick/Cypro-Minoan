"""Validate fixed reading coverage, source apparatus and namespace-qualified identities."""
import collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
IS_CH=False
PINS={'research/reference-reconciliation-v2.json': '5b9d01ef7296c7ebcebdbae44b38c239b8fda0d092dc75584c4bed1466e01c02', 'research/identity-reconciliation-v2.json': 'f1800080d2e0d3b28998f179f478b69315e02f04d52ebb2598a3db8fce3ead66', 'research/donnelly-existing-assertion-check.json': 'e6d193dfee40d65b0fbfacbc96ff007992193019ab65d8b532ea70edf9963948'}
SYSTEMS={'Olivier 2007 catalogue','Ferrara 2013 catalogue','Ferrara/addendum catalogue'}
def load(root,p):return json.loads((root/p).read_text())
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def require(ok,msg):
 if not ok:raise ValueError(msg)
def catalogue_refs(record):
 refs=[i for i in record['identifiers'] if i['system'] in SYSTEMS];nums={int(i['value']) for i in refs}
 require(len(nums)<=1 and nums<=set(range(1,255)),'conflicting or unbounded catalogue reference')
 return nums,refs
def alias_key(namespace,repository,literal):return namespace,repository,literal

def validate(root=ROOT):
 for p,pin in PINS.items():require(digest(load(root,p))==pin,'audited reconciliation changed: '+p)
 if not IS_CH:
  checked=load(root,'research/donnelly-existing-assertion-check.json');require(checked['new_occurrences_added']==0 and checked['expert_acceptance_granted'] is False,'existing source check promoted')
  record=load(root,'corpus/inscriptions/CMOC-LVR-AM1639.json');assertions=[a for a in record['assertions'] if a['assertion_type']=='scholarly_sign_identification']
  require(len(assertions)==1 and assertions[0]['value']=='CM102' and assertions[0]['uncertainty']=='probable','existing metadata source uncertainty changed')
 ref=load(root,'research/reference-reconciliation-v2.json');identity=load(root,'research/identity-reconciliation-v2.json');freeze=ref['frozen_inventory']
 require(hashlib.sha256((root/freeze['path']).read_bytes()).hexdigest()==freeze['sha256'],'reading inventory changed during reconciliation-only work')
 require(ref['independent_review_complete'] is False and identity['physical_duplicates_adjudicated'] is None,'unreviewed scientific promotion')
 native=load(root,freeze['path']);readings=native if IS_CH else native['occurrences'];require(len(readings)==freeze['count'],'reading count drift')
 assignments=ref['existing_reading_dispositions' if IS_CH else 'existing_occurrence_dispositions'];key='reading_id' if IS_CH else 'occurrence_id'
 require([x[key] for x in assignments]==[x[key] for x in readings],'missing/duplicate reading disposition')
 require(all(x['independent_review_complete'] is False for x in assignments),'expert acceptance fabricated')
 rows=identity['rows'];require(len({x['record_id'] for x in rows})==len(rows),'duplicate identity row')
 aliases=collections.defaultdict(set)
 if IS_CH:
  ids=[x['id'] for x in load(root,'corpus/chic-catalogue-spine.json')];require([x['record_id'] for x in rows]==ids,'catalogue membership/order changed')
  context=load(root,'corpus/context-assertions.json')['records']
  for row in rows:
   expected=[]
   for c in context:
    if c['object_id']!=row['record_id']:continue
    values={x['field']:x['value'] for x in c['assertions']}
    if values.get('inventory_number') not in (None,'Unknown','-'):expected.append(('INSCRIBE museum inventory',values.get('repository'),values['inventory_number']))
   require([alias_key(x['namespace'],x.get('repository'),x['literal']) for x in row['identifier_assertions']]==expected,'inventory namespace/value lost')
 else:
  idx=load(root,'corpus/index.json');require([x['record_id'] for x in rows]==idx['records'],'rich record membership/order changed')
  cats=load(root,'catalogues/master.json')['entries'];matched=set()
  for row in rows:
   record=load(root,'corpus/inscriptions/'+row['record_id']+'.json');nums,refs=catalogue_refs(record);matched|=nums
   require(row['catalogue_slots']==sorted(nums),'unsupported catalogue join')
   require([(x['namespace'],x['literal'],x['source_id']) for x in row['identifier_assertions']]==[(x['system'],x['value'],x['source_id']) for x in record['identifiers']],'identifier or source namespace lost')
   require(row['membership']==('candidate' if row['record_id'] in idx['candidate_records'] else 'core'),'candidate promoted into core')
  for c in cats:require((c['ingestion_status']=='rich_record_available')==(c['catalogue_number'] in matched),'stale ingestion marker')
  require(len(matched)==14,'catalogue joins drift')
 for row in rows:
  require(row['physical_identity_adjudicated'] is False,'source identity promoted to physical certification')
  for a in row['identifier_assertions']:aliases[alias_key(a['namespace'],a.get('repository'),a['literal'])].add(row['record_id'])
 actual=[{'namespace':n,'repository':r,'literal':v,'record_ids':sorted(ids),'status':'ALIAS_COLLISION_REVIEW_REQUIRED_NOT_AUTOMATIC_DUPLICATE'} for (n,r,v),ids in aliases.items() if len(ids)>1]
 require(actual==identity['literal_alias_collisions'],'duplicate/collision inventory drift')
 return {'status':'PASS_RECONCILIATION_FIXED_COVERAGE','reading_assertions':len(readings),'identity_rows':len(rows),'reading_coverage_changed':False,'physical_certification':False}
if __name__=='__main__':print(json.dumps(validate()))
