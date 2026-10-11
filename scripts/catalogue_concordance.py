"""Replay source-qualified catalogue joins without adjudicating readings or witnesses."""
import argparse, hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(root,p):return json.loads((root/p).read_bytes())
def calculate(root=ROOT,source_pdf=None):
 c=load(root,'catalogues/source-located-concordance.json');cat=load(root,'catalogues/master.json')['entries'];rows=c['rows'];source=c['source']
 if [r['catalogue_number'] for r in rows]!=list(range(1,254)):raise ValueError('source concordance coverage/order')
 if [r['catalogue_number'] for r in cat]!=list(range(1,255)):raise ValueError('native catalogue coverage/order')
 if source['pdf_sha256']!='747418cbc4d81b2c2198c5f4eae9ef51028a86a4aee5413d12315659b7099e57' or source['pdf_bytes']!=16322562:raise ValueError('source identity drift')
 if c['expert_validation_granted'] is not False:raise ValueError('unsupported expert validation')
 for r,e in zip(rows,cat):
  n=r['catalogue_number'];page=25 if n<=86 else 26 if n<=186 else 27
  if r['source_pdf_page']!=page or r['siglum']!=r['source_label'].rstrip('*'):raise ValueError('locator or label drift')
  if r['source_editorial_marker']!=('*' if r['source_label'].endswith('*') else None) or r['marker_meaning']!=('NOT_ADJUDICATED' if r['source_editorial_marker'] else None):raise ValueError('editorial marker drift')
  if r['identity_status']!='SOURCE_ATTRIBUTED_NAMESPACE_MAPPING_NOT_PHYSICAL_CERTIFICATION' or r['independent_witness'] is not False:raise ValueError('unsupported identity/witness assertion')
  control={k:r[k] for k in ('source_label','source_pdf_page','source_editorial_marker','marker_meaning','identity_status','independent_witness')};control.update(source_id='valerio2016thesis',source_pdf_sha256=source['pdf_sha256'])
  if e['siglum']!=r['siglum'] or e['concordance_control']!=control:raise ValueError('native join drift')
  if n<=186 and e['source_id']!='valerio2016thesis':raise ValueError('new mapping attribution')
 if rows[18]['source_label']!='ENKO Abou 016bis*' or rows[72]['source_label']!='ENKO Abou 069ter*' or rows[168]['source_label']!='ENKO? Mins 002':raise ValueError('source qualification lost')
 if cat[-1]['source_id']!='valerio2017' or not cat[-1]['siglum']:raise ValueError('separate final source lost')
 if source_pdf:
  p=Path(source_pdf)
  if hashlib.sha256(p.read_bytes()).hexdigest()!=source['pdf_sha256']:raise ValueError('original PDF digest mismatch')
  pages=subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True).split('\f');facts=[]
  rx=re.compile(r'(ADD)?##(\d{3})\.\s+([A-Z?]+\s+[A-Z][\w]+\s+\d{3}(?:bis|ter|a-b)?\*?)')
  for page in (25,26,27):
   for m in rx.finditer(pages[page-1]):facts.append((int(m[2]),m[3],page,bool(m[1])))
  if sorted(facts)!=[(r['catalogue_number'],r['source_label'],r['source_pdf_page'],r['add']) for r in rows]:raise ValueError('PDF table extraction differs from source register')
 occ=load(root,'occurrences/occurrences.json')['occurrences'];idx=load(root,'corpus/index.json')['records']
 return {'schema_version':'1.0','status':'PASS_SOURCE_ATTRIBUTED_MAPPING_REPLAY','controlled_slots':len(cat),'source_attributed_sigla':sum(bool(e['siglum']) for e in cat),'number_only_slots':sum(e['siglum'] is None for e in cat),'concordance_rows':len(rows),'newly_resolved_mappings':186,'concordance_sha256':hashlib.sha256((root/'catalogues/source-located-concordance.json').read_bytes()).hexdigest(),'catalogue_sha256':hashlib.sha256((root/'catalogues/master.json').read_bytes()).hexdigest(),'source_pdf_sha256':source['pdf_sha256'],'rich_records':len(idx),'encoded_occurrences':len(occ),'records_without_occurrences':len(set(idx)-{o['record_id'] for o in occ}),'expert_validation_granted':False,'independent_witnesses_added':0,'physical_identity_certifications_added':0,'boundary':'Factual namespace mappings only. Source editorial markers and uncertain site labels remain attributed; no readings or broader corpus-completeness claim.'}
def validate(root=ROOT):
 result=calculate(root)
 if result!=load(root,'analysis/catalogue-mapping-audit.json'):raise ValueError('mapping audit replay drift')
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--source-pdf');a=p.parse_args();result=calculate(source_pdf=a.source_pdf)
 if a.write:(ROOT/'analysis/catalogue-mapping-audit.json').write_text(json.dumps(result,indent=2)+'\n')
 else:validate()
 print(json.dumps(result))
