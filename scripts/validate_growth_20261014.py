"""Validate finite source growth while preserving the entire prior occurrence snapshot."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HISTORICAL_BASELINE_SEMANTIC_SHA256='12b6a14dbd50324f83087f245ca65812509f8585474c1027e13b07b061aa0e92'
EXPECTED={'CMOC-0028':['110','96','34'],'CMOC-0032':['102','27','70','86'],'CMOC-0033':['87','82','24']}
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def additions(root=ROOT):
 x=json.loads((root/'research/source-growth-2026-10-14.json').read_text());rows=x['expected_additions']
 if x['source_pdf_sha256']!='747418cbc4d81b2c2198c5f4eae9ef51028a86a4aee5413d12315659b7099e57' or x['pdf_ordinals']!=[464,465] or x['printed_pages']!=[458,459]:raise ValueError('inspected source pin/locator drift')
 if len(rows)!=10 or len({r['occurrence_id'] for r in rows})!=10:raise ValueError('missing or duplicate finite assertion')
 if any(x[k] is not False for k in ['primary_edition_collated','independent_review_complete','bulk_republication_authorized']):raise ValueError('unsupported rights/acceptance promotion')
 for rid,labels in EXPECTED.items():
  selected=[r for r in rows if r['record_id']==rid]
  if [r['published_sign_label'] for r in selected]!=labels or [r['position'] for r in selected]!=list(range(1,len(labels)+1)):raise ValueError('source literal or order drift')
  for r in selected:
   if r['source_id']!='valerio2016thesis' or r['source_role']!='dependent_secondary' or r['certainty']!='certain' or not r['notes'] or not r['locator']:raise ValueError('provenance/qualification loss')
 return rows
def validate(root=ROOT):
 rows=additions(root);x=json.loads((root/'research/source-growth-2026-10-14.json').read_text());native=json.loads((root/'occurrences/occurrences.json').read_text());old={**native,'occurrences':native['occurrences'][:16]}
 if digest(old)!=HISTORICAL_BASELINE_SEMANTIC_SHA256 or x['historical_baseline_semantic_sha256']!=HISTORICAL_BASELINE_SEMANTIC_SHA256:raise ValueError('historical occurrence altered')
 if native['occurrences'][16:]!=rows:raise ValueError('unexpected source extension')
 if len({r['record_id'] for r in native['occurrences']})!=12:raise ValueError('coverage drift')
 return {'status':'PASS_FINITE_SOURCE_GROWTH','added_source_occurrences':10,'newly_source_encoded_records':3,'total_occurrences':26,'records_with_occurrences':12,'remaining_uncovered_rich_records':9,'independent_reviews_added':0}
if __name__=='__main__':print(json.dumps(validate()))
