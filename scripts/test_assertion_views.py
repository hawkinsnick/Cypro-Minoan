import copy,csv,io,json,shutil,tempfile,unittest
from pathlib import Path
from assertion_views import ROOT,build,csv_text,validate
class DeliveryTests(unittest.TestCase):
 def test_roundtrip(self):
  data=build();rows=list(csv.DictReader(io.StringIO(csv_text(data))))
  for source,row in zip(data['assertions'],rows):
   for k in ['source_assertion','reconciliation_context','source_disagreements','identity_context']:self.assertEqual(source[k],json.loads(row[k+'_json']))
 def test_uncertainty_and_alternative_present(self):
  data=build()['assertions']
  if (ROOT/'corpus/critical-readings.json').exists():
   face=next(v for v in data if v['record_id']=='CHIC-252' and v['source_assertion']['surface_id']=='c');self.assertEqual(face['source_assertion']['tokens'][0]['form'],'062');self.assertEqual(face['reconciliation_context']['apparatus'][0]['count'],3)
   stone=next(v for v in data if v['record_id']=='CHIC-328');self.assertTrue(any(a.get('source_label')=='065' for a in stone['reconciliation_context']['apparatus']))
  else:self.assertEqual(sum(bool(v['source_disagreements']) for v in data),3)
 def test_hostile_context_losses(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
   def reject(path,fn):
    p=root/path;old=p.read_bytes();x=json.loads(old);fn(x);p.write_text(json.dumps(x))
    try:
     with self.assertRaises((ValueError,KeyError)):validate(root)
    finally:p.write_bytes(old)
   reject('research/qualified-assertion-views.json',lambda x:x['assertions'][0].pop('reconciliation_context'))
   reject('research/qualified-assertion-views.json',lambda x:x['assertions'][0].update(independent_review_complete=True))
   key='existing_reading_dispositions' if (ROOT/'corpus/critical-readings.json').exists() else 'existing_occurrence_dispositions'
   reject('research/reference-reconciliation-v2.json',lambda x:x[key].pop())
   reject('research/reference-reconciliation-v2.json',lambda x:x[key][0].update(record_id='wrong-record'))
if __name__=='__main__':unittest.main()
