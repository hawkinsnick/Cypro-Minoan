"""Validate bounded source-growth views; do not certify ancient objects or readings."""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path):return json.loads((ROOT/path).read_text())
def require(ok,message):
 if not ok:raise ValueError(message)
def digest(raw):return hashlib.sha256(raw).hexdigest()
def nonadmission(row):
 require(row['reading_admitted'] is False and row['images_included'] is False,'unsupported reading/image admission')

FILES=['research/louvre-object-concordance.json','research/tiryns-clay-ball-primary-context.json']
def validate(museum,primary,source_dir=None):
 rows=museum['records'];require(len(rows)==len({r['id'] for r in rows})==9,'museum row loss/collision')
 for r in rows:
  nonadmission(r);require(r['physical_identity_certified'] is False,'unsupported identity')
  native=load('corpus/inscriptions/'+r['native_record_id']+'.json');n=int(r['native_record_id'].split('-')[1])
  principal=[i['value'] for i in r['inventory_assertions'] if i['type']=='Numéro principal']
  require(principal==[native['object']['inventory_number']],'numeric catalogue join without inventory agreement')
  require(len(r['edition_locators'])==2 and {e['author'] for e in r['edition_locators']}=={'Olivier','Ferrara'} and all(e['source_reported_catalogue_number']==n for e in r['edition_locators']),'edition join or source locator drift')
  require(all(d['unit']=='cm' for d in r['dimension_assertions']),'source unit changed')
  require(r['sign_count_comparison']!='UNRESOLVED','unresolved sign count requires explicit review')
  if source_dir:
   p=Path(source_dir)/('louvre-native-'+str(n)+'.json');raw=p.read_bytes();require(digest(raw)==r['source_sha256'],'museum source byte drift');s=json.loads(raw)
   require(s['objectNumber']==r['inventory_assertions'] and s['dimension']==r['dimension_assertions'] and s['dateCreated']==r['date_assertions'],'literal source qualifications changed')
 require(primary['source_pdf_included'] is False and primary['source_images_included'] is False,'restricted source payload admitted')
 require(primary['visually_inspected_pdf_pages']==[2,16,39] and len(primary['records'])==1,'primary inspection scope drift')
 p=primary['records'][0];nonadmission(p);require(p['source_id']==primary['source_id'] and p['source_url']==primary['source_url'],'primary row source attribution drift')
 require(p['database_identifier']['literal']=='TN 241' and p['database_identifier']['namespace_is_museum_inventory'] is False,'footnote number or database ID promoted to museum inventory')
 require(p['diameter_cm']=={'min':1.7,'max':1.75,'locator':'printed p. 15 / PDF p. 16'} and p['weight_g']=={'min':5.0,'max':5.1,'locator':'printed p. 15 / PDF p. 16'},'primary factual ranges drift')
 require(p['sign_count_assertion']['certainty']=='PARTLY_DAMAGED' and p['sign_count_assertion']['complete_reading_claim'] is False and p['reading_admitted'] is False and p['independent_review_complete'] is False,'source damage/admission qualifier lost')
 require(p['appendix_table_assertions']['number_of_signs_literal']=='3 (?) signs' and p['appendix_table_assertions']['source_qualification_preserved'] is True,'appendix count qualifier lost')
 require(p['within_source_disagreements']==[{'field':'excavation_coordinate_segment','main_description':'VB','main_locator':'printed p. 15 / PDF p. 16','appendix_table':'VC','appendix_locator':'printed p. 38 / PDF p. 39','status':'UNRESOLVED_SOURCE_LITERAL_DIFFERENCE','interventions':[]}],'unreviewed within-source coordinate adjudication')
 require(p['native_readings_overwritten'] is False and p['physical_identity_certified'] is False,'unsupported native reading or identity change')
 context=p['existing_occurrence_context'];actual=[o['occurrence_id'] for o in load('occurrences/occurrences.json')['occurrences'] if o['record_id']==p['native_record_id']]
 require(context['occurrence_ids']==actual and context['native_occurrences_changed'] is False and context['source_surface_damage']=='PARTLY_DAMAGED_FIRST_SIGN_FROM_LEFT','native/source apparatus join drift')
 if source_dir:
  raw=(Path(source_dir)/'tiryns-clay-ball.pdf').read_bytes();require(raw.startswith(b'%PDF-') and digest(raw)==primary['source_sha256'],'not the inspected primary PDF')
 return {'museum_object_rows':9,'primary_context_rows':1,'reading_admissions':0,'independent_review_complete':False}

def build(source_dir=None):
 result=validate(*(load(p) for p in FILES),source_dir=source_dir)
 return dict(schema_version='1.0',checked='2026-10-12',status='PASS_BOUNDED_SOURCE_GROWTH',scope=result,inputs=[{'path':p,'sha256':digest((ROOT/p).read_bytes())} for p in FILES])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--source-dir',type=Path);a=p.parse_args();d=build(a.source_dir);path=ROOT/'analysis/source-growth-2026-10-12.json'
 if a.write:path.write_text(json.dumps(d,indent=2)+'\n')
 else:require(json.loads(path.read_text())==d,'source-growth audit drift')
 print(json.dumps(d['scope']))
