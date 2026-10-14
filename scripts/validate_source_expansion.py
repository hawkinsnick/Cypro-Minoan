"""Replay bounded source expansion and denominators; never infer physical totals."""
import argparse,collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(root,p):return json.loads((root/p).read_text())
def require(ok,msg):
 if not ok:raise ValueError(msg)
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
EXPECTED_ASSERTIONS_SHA='81e8c3d1f37b4d47c096d462ea8e2f7e99ff1957baa14b40a4af88008c5c6856'
IS_CH=False
KEY='expected_readings' if IS_CH else 'expected_occurrences'
def validate_new(rows,root=ROOT):
 checkpoint=load(root,'research/source-check-2026-10-11.json')
 require(digest(checkpoint['receipts'])=='2cbe436f47bcdc412c05cab51d6e0fead3db9ff67bd23d82e1f420a0dcd9644d','inspected source receipt drift')
 expected=checkpoint[KEY]
 if not IS_CH:
  from validate_growth_20261014 import additions
  from validate_CM209_20261014 import additions as cm209_additions
  growth=additions(root)+cm209_additions(root)
  require([r for r in rows if r not in growth]==expected,'historical source assertions changed')
  require([r for r in rows if r in growth]==growth,'finite source addition drift')
  rows=[r for r in rows if r not in growth]
 require(digest(expected)==EXPECTED_ASSERTIONS_SHA,'source assertions differ from inspected checkpoint')
 require(rows==expected,'new source assertions, loci or editorial qualification drift')
 require(checkpoint['independent_review_complete'] is False and checkpoint['physical_inscription_population'] is None,'unsupported scientific promotion')
 require(all(r['status']=='ACCESSED' and len(r['sha256'])==64 for r in checkpoint['receipts']),'missing acquisition provenance')
 return expected
validate_new_readings=validate_new
validate_new_occurrences=validate_new
def joins(record,slots):
 systems={'Olivier 2007 catalogue','Ferrara 2013 catalogue','Ferrara/addendum catalogue'}
 refs=[i for i in record.get('identifiers',[]) if i['system'] in systems]
 nums={int(i['value']) for i in refs}
 require(nums<=slots,'catalogue join outside bounded slots')
 require(len(nums)<=1,'conflicting catalogue identifiers require explicit adjudication')
 return [{'catalogue_number':n,'record_id':record['id'],'basis':refs,'status':'NATIVE_SOURCE_ASSERTED_NOT_PHYSICAL_CERTIFICATION'} for n in sorted(nums)]
def build(root=ROOT):
 check=load(root,'research/source-check-2026-10-11.json'); reconciliation=load(root,'research/source-reconciliation.json')
 paths=['research/source-check-2026-10-11.json','research/source-reconciliation.json']
 result={'schema_version':'1.0','checked':'2026-10-11','boundary':'Edition/date-bounded project views. Catalogue rows, rich records and reading versions are different units; views overlap and must not be summed.','physical_inscription_population':None,'complete_language_corpus_claim_allowed':False,'independent_review_complete':False,'disputed_records':sorted({x['record_id'] for x in reconciliation['comparisons']}),'views':[]}
 if IS_CH:
  paths+=['corpus/chic-catalogue-spine.json','corpus/critical-readings.json','corpus/context-assertions.json']
  cat=load(root,paths[2]); rows=load(root,paths[3]);ids=[r['id'] for r in cat]
  require(len(ids)==len(set(ids))==331,'catalogue duplicate/membership drift')
  require(ids==[f'CHIC-{i:03d}' for i in range(1,332)],'bounded CHIC membership drift')
  validate_new([r for r in rows if r['source_id']!='CHIC1996'],root)
  require(all(r['object_id'] in ids for r in rows),'reading outside catalogue')
  sources=collections.defaultdict(list)
  for r in rows:sources[r['source_id']].append(r)
  covered={r['object_id'] for r in rows}
  result['views']=[{'view_id':'CHIC1996_001_331','edition_scope':'CHIC 1996 numbered identities 001–331; no later additions implied','unit':'catalogue_identity','included_ids':ids,'denominator':len(ids),'identities_with_any_source_checked_reading':sorted(covered),'identities_without_any_source_checked_reading':sorted(set(ids)-covered),'reading_versions':len(rows),'source_strata':[{'source_id':s,'role':'primary_edition' if s=='CHIC1996' else 'dependent_digital_reference','reading_versions':len(rs),'covered_ids':sorted({r['object_id'] for r in rs})} for s,rs in sorted(sources.items())],'duplicate_catalogue_ids':[],'physical_duplicate_adjudication':'NOT_ESTABLISHED','series_denominators':dict(collections.Counter(r['series'] for r in cat))}]
  result['object_concordance']=reconciliation['comparisons']
 else:
  paths+=['catalogues/master.json','corpus/index.json','occurrences/occurrences.json','catalogues/source-located-concordance.json']
  cat=load(root,paths[2])['entries'];idx=load(root,paths[3]);rows=load(root,paths[4])['occurrences'];ids=idx['records'];slots={r['catalogue_number'] for r in cat}
  require(len(cat)==len(slots)==254 and slots==set(range(1,255)),'bounded catalogue duplicate/membership drift')
  require(len(ids)==len(set(ids))==21,'rich record membership drift')
  validate_new([r for r in rows if r['source_id']=='valerio2016thesis'],root)
  links=[]; inventories=collections.defaultdict(set)
  for rid in ids:
   p='corpus/inscriptions/'+rid+'.json';paths.append(p);record=load(root,p);links+=joins(record,slots)
   for i in record['identifiers']:
    if 'inventory' in i['system'].lower() or 'registration' in i['system'].lower() or i['system']=='Met object number':inventories[i['system'],i['value']].add(rid)
  linked={r['record_id'] for r in links};matched={r['catalogue_number'] for r in links};covered={o['record_id'] for o in rows}
  require(len(linked)==14,'explicit catalogue rich-record join drift')
  require(covered<=set(ids),'occurrence outside rich record view')
  collisions=[{'namespace':n,'literal_identifier':v,'record_ids':sorted(rs),'status':'IDENTIFIER_COLLISION_REQUIRES_REVIEW_NOT_AUTOMATIC_MERGE'} for (n,v),rs in inventories.items() if len(rs)>1]
  result['views']=[{'view_id':'bounded_001_254','edition_scope':'1–217 Olivier 2007, 218–244 Ferrara 2013 additions, 245–253 Valério 2014/2016, 254 later 2017 source; project control view, not terminal corpus population','unit':'catalogue_slot','included_ids':sorted(slots),'denominator':len(slots),'slots_with_explicit_rich_join':sorted(matched),'slots_without_explicit_rich_join':sorted(slots-matched),'duplicate_catalogue_ids':[],'physical_duplicate_adjudication':'NOT_ESTABLISHED'},{'view_id':'committed_rich_records','edition_scope':'Committed core/candidate record index at 2026-10-11','unit':'rich_record','included_ids':ids,'denominator':len(ids),'records_with_encoded_occurrences':sorted(covered),'records_without_encoded_occurrences':sorted(set(ids)-covered),'records_with_explicit_catalogue_join':sorted(linked),'records_with_unresolved_catalogue_join':sorted(set(ids)-linked),'source_occurrence_assertions':len(rows),'full_transcription_coverage_established':False,'primary_occurrences':sum(o['source_role']=='primary_publication' for o in rows),'dependent_secondary_occurrences':sum(o['source_role']=='dependent_secondary' for o in rows)}]
  result['object_concordance']=links;result['inventory_collisions']=collisions
 result['inputs']=[{'path':p,'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in paths]
 return result
def validate(root=ROOT):
 expected=build(root);require(load(root,'research/coverage-denominators.json')==expected,'bounded denominator or source receipt drift')
 comparisons=load(root,'research/source-reconciliation.json')
 require(digest(comparisons['comparisons'][:3])=='76a34c6571cc53bece9ae8ad0b63f2b12724895065e1a7cae9b13f2002ffed09','historical competing assertions changed')
 require(digest(comparisons['comparisons'])=='5aeb01ac7d68ea113f709099ff5988f0df51fb96463be37735dfe43f1ab90c2a','inspected competing source assertions drift')
 require(comparisons['independent_review_complete'] is False and comparisons['primary_reading_agreement_certified'] is False,'unsupported reconciliation promotion')
 for c in comparisons['comparisons']:
  require(len(c['assertions'])==2 and all(a['locator'] and a['source_id'] and a['inspection'] for a in c['assertions']),'disagreement provenance lost')
  require(c['status'].startswith('UNRESOLVED') and c['interventions']==[],'unreviewed editorial adjudication')
 return {'status':'PASS_BOUNDED_SOURCE_EXPANSION','views':len(expected['views']),'physical_population':None,'independent_review_complete':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 if a.write:(ROOT/'research/coverage-denominators.json').write_text(json.dumps(build(),ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(validate()))
