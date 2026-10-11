"""Validate a blank, source-qualified expert packet, optionally rehash fetched images."""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(root,p):return json.loads((root/p).read_bytes())
def validate(root=ROOT,image_dir=None):
 packet=load(root,'research/uncovered-record-review-controls.json');images=load(root,'research/met-open-image-controls.json');coverage=load(root,'analysis/occurrence-coverage-v1.json')
 rows=packet['items']
 if next(r for r in load(root,'coverage/completeness-matrix.json')['dimensions'] if r['dimension']=='exact_siglum_reconciliation')['covered']!=254:raise ValueError('coverage matrix mapping count drift')
 layers=load(root,'coverage/layers.json')['layers']
 if next(r for r in layers if r['layer']=='exact_siglum')['numerator']!=254 or next(r for r in layers if r['layer']=='source_verified_occurrence')['numerator']!=12:raise ValueError('current coverage layer drift')
 if [r['record_id'] for r in rows]!=coverage['records_without_encoded_occurrences']:raise ValueError('uncovered population drift')
 if packet['expert_validation_granted'] is not False or images['expert_validation_granted'] is not False:raise ValueError('expert approval fabricated')
 byid={m['object_id']:m for m in images['objects']};seen=set()
 expected={331665:'2008.27',321391:'74.51.4316',240899:'74.51.1312',243938:'74.51.5057a'}
 if set(byid)!=set(expected) or len(images['objects'])!=4:raise ValueError('museum population drift')
 for n,m in byid.items():
  b=(root/m['api_snapshot']).read_bytes();d=json.loads(b)
  if hashlib.sha256(b).hexdigest()!=m['api_sha256'] or d['objectID']!=n or d['accessionNumber']!=expected[n] or d['isPublicDomain'] is not True or m['is_public_domain'] is not True:raise ValueError('API identity/rights pin drift')
  source_images=[d['primaryImage']]+d['additionalImages'];rs=[r for r in images['images'] if r['object_id']==n]
  if [r['image_index'] for r in rs]!=list(range(len(source_images))) or [r['url'] for r in rs]!=source_images:raise ValueError('image source scope drift')
  if m['image_indices_visually_inspected']!=list(range(len(source_images))) or m['images_redistributed_in_repository'] is not False:raise ValueError('inspection/redistribution scope drift')
  for r in rs:
   if r['rights']!='CC0-1.0' or r['image_is_independent_witness'] is not False or r['expert_reading_status']!='NOT_REVIEWED' or not re.fullmatch('[0-9a-f]{64}',r['sha256']) or min(r['bytes'],r['width'],r['height'])<=0:raise ValueError('image rights or review boundary drift')
   if image_dir:
    p=Path(image_dir)/(str(n)+'-'+str(r['image_index'])+'.jpg');b=p.read_bytes()
    if hashlib.sha256(b).hexdigest()!=r['sha256'] or len(b)!=r['bytes']:raise ValueError('image bytes mismatch')
 for r in rows:
  if r['reviewer'] is not None or r['review_date'] is not None or r['decision']!='UNREVIEWED' or r['independent_review_complete'] is not False or r['canonical_reading_admitted'] is not False or r['encoded_occurrences_added']!=0:raise ValueError('blank review promoted to acceptance')
  if not r['source_leads'] or not r['question'] or not (root/r['native_record']).is_file():raise ValueError('source/decision route missing')
  if r['status']=='CC0_IMAGE_EVIDENCE_LOCATED_EXPERT_IDENTIFICATION_PENDING':
   n=r['met_object_id'];d=load(root,byid[n]['api_snapshot']);identifiers=load(root,r['native_record'])['identifiers']
   if not any(i['value']==d['accessionNumber'] for i in identifiers):raise ValueError('museum inventory/native join drift')
   if r['priority_image_index'] not in byid[n]['image_indices_visually_inspected']:raise ValueError('priority view missing')
  elif r['status']=='DEPENDENT_EDITION_LOCATED_EXPERT_COLLATION_PENDING':
   if r['source_pdf_sha256']!=load(root,'catalogues/source-located-concordance.json')['source']['pdf_sha256'] or r['reported_primary_edition_locator']['status']!='REPORTED_BY_INSPECTED_THESIS_NOT_DIRECT_PRIMARY_INSPECTION':raise ValueError('edition provenance drift')
 counts={s:sum(r['status']==s for r in rows) for s in set(r['status'] for r in rows)}
 expected_counts={'DEPENDENT_EDITION_LOCATED_EXPERT_COLLATION_PENDING':8,'CC0_IMAGE_EVIDENCE_LOCATED_EXPERT_IDENTIFICATION_PENDING':4,'MUSEUM_METADATA_LOCATED_PRIMARY_SIGN_EVIDENCE_PENDING':2,'SOURCE_ACCESS_BLOCKED':1}
 if counts!=expected_counts or len(images['images'])!=14:raise ValueError('disposition coverage drift')
 if packet['summary']!={'uncovered_rich_records':15,'dependent_edition_located':8,'cc0_visual_evidence_located':4,'museum_metadata_only':2,'access_blocked':1,'expert_reviews_completed':0,'canonical_readings_added':0}:raise ValueError('summary falsely promotes review or coverage')
 return {'status':'PASS_SOURCE_QUALIFIED_BLANK_REVIEW_PACKET','records':15,'images':14,'expert_review_complete':False,'readings_added':0,'image_bytes_rehashed':bool(image_dir)}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--image-dir');a=p.parse_args();print(json.dumps(validate(image_dir=a.image_dir)))
