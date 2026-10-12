"""Validate the acquisition frontier without glyph, core or expert admission."""
import argparse,collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p,root=ROOT):return json.loads((root/p).read_text())
def require(ok,msg):
 if not ok:raise ValueError(msg)
def sha(raw):return hashlib.sha256(raw).hexdigest()
FILES=['research/dor-2025-provisional-candidates.json','research/source-access-followthrough.json']
def validate(candidates,access,root=ROOT,source_dir=None):
 rows=candidates['records'];require(len(rows)==len({r['id'] for r in rows})==2 and {r['id'] for r in rows}=={'CM-CAND-DOR-2025-ANCHOR','CM-CAND-DOR-2025-BLACK-DIPINTO'},'candidate membership drift')
 require(candidates['license']=='CC BY 4.0' and candidates['license_url']=='https://creativecommons.org/licenses/by/4.0/' and len(candidates['authors_as_published'])==16,'source licence/attribution drift')
 require(candidates['visually_inspected_pdf_pages']==[10,11],'inspected candidate source scope drift')
 idx=load('corpus/index.json',root)
 for r in rows:
  require(r['id'] not in idx['records'] and r['catalogue_number'] is None and r['museum_inventory'] is None,'candidate admitted or assigned synthetic ancient inventory')
  require(r['record_status']=='PROVISIONAL_SOURCE_ATTRIBUTED_CANDIDATE' and r['canonical_reading_admitted'] is False and r['encoded_occurrences_added']==0 and r['independent_review_complete'] is False and r['physical_identity_certified'] is False,'candidate upgraded to accepted reading/witness')
  require(r['source_license']=='CC BY 4.0' and r['images_included'] is False,'source licence superseded or image admitted')
 anchor=next(r for r in rows if r['id'].endswith('ANCHOR'));jar=next(r for r in rows if r['id'].endswith('DIPINTO'))
 require(anchor['classification_assertions'][0]['certainty']=='APPEARS_TO_BE' and anchor['source_sign_assertion']['label']=='CM 102' and anchor['source_sign_assertion']['variant']=='7','tentative anchor classification drift')
 require(anchor['source_sign_assertion']['canonical_native_sign_id'] is None and anchor['source_sign_assertion']['namespace']=='Polig and Donnelly 2022 signary as cited by Yasur-Landau et al. 2025','unreviewed native signary equivalence')
 require(all(r['exclude_from_confirmed_CM_counts'] is True and r['complete_source_transcription'] is False for r in rows),'candidate or partial scope promoted')
 require({a['script'] for a in jar['classification_assertions']}=={'Cypro-Minoan','Cypro-syllabic'} and all(a['certainty']=='POSSIBLE_ALTERNATIVE' for a in jar['classification_assertions']),'alternative script suppressed')
 require(jar['published_sign_count']=={'min':4,'max':5,'qualifier':'possible linear script signs'} and jar['exclude_from_confirmed_CM_counts'] is True,'uncertain range promoted to a confirmed count')
 require(len(access['routes'])==2 and access['routes'][0]['sign_level_primary_evidence_acquired'] is False and access['routes'][1]['status']==403 and access['routes'][1]['source_payload_acquired'] is False and access['routes'][1]['protection_bypassed'] is False,'source access promoted to sign delivery')
 require(access['routes'][0]['record_id']=='CMOC-LVR-AM2716' and [r['value'] for r in access['routes'][0]['inventory_assertions'] if r['type']=='Numéro principal']==[load('corpus/inscriptions/CMOC-LVR-AM2716.json',root)['object']['inventory_number']],'museum/core inventory mismatch')
 if source_dir:
  raw=(Path(source_dir)/'dor2025.pdf').read_bytes();require(raw.startswith(b'%PDF-') and sha(raw)==candidates['source_pdf_sha256'],'candidate PDF source bytes drift')
  raw=(Path(source_dir)/'am2716.json').read_bytes();require(sha(raw)==access['routes'][0]['sha256'] and json.loads(raw)['objectNumber']==access['routes'][0]['inventory_assertions'],'museum source bytes/inventory drift')
 return dict(provisional_candidate_objects=2,accepted_new_readings=0,controlled_catalogue_slots_unchanged=len(load('catalogues/master.json',root)['entries']),rich_records_unchanged=len(idx['records']),source_access_blocked_objects=1,expert_acceptance=False)

def build(root=ROOT,source_dir=None):
 scope=validate(*(load(p,root) for p in FILES),root=root,source_dir=source_dir)
 return dict(schema_version='1.0',checked='2026-10-12',status='PASS_BOUNDED_ACQUISITION_FRONTIER',scope=scope,inputs=[dict(path=p,sha256=sha((root/p).read_bytes())) for p in FILES])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--source-dir',type=Path);a=p.parse_args();d=build(source_dir=a.source_dir);out=ROOT/'analysis/acquisition-frontier-2026-10-12.json'
 if a.write:out.write_text(json.dumps(d,indent=2)+'\n')
 else:require(json.loads(out.read_text())==d,'frontier receipt drift')
 print(json.dumps(d['scope']))
