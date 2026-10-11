import copy,json,tempfile,shutil,unittest
from pathlib import Path
from validate_reconciliation import ROOT,IS_CH,validate,alias_key,catalogue_refs
class ReconciliationTests(unittest.TestCase):
 def test_valid(self):validate()
 def test_namespace_collision_is_not_identity(self):
  self.assertNotEqual(alias_key('HM','museum','2245'),alias_key('INSCRIBE','museum','2245'))
  self.assertNotEqual(alias_key('inventory','museum','Σ-K 2850'),alias_key('inventory','museum','Σ-Κ 2850'))
 def test_unknown_catalogue_namespace_excluded(self):self.assertEqual(catalogue_refs({'identifiers':[{'system':'Unregistered catalogue','value':'25'}]}),(set(),[]))
 def test_conflicting_catalogue_ids_rejected(self):
  with self.assertRaises(ValueError):catalogue_refs({'identifiers':[{'system':'Olivier 2007 catalogue','value':'25'},{'system':'Ferrara 2013 catalogue','value':'26'}]})
 def test_mutations(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
   def reject(path,mutation):
    p=root/path;original=p.read_bytes();x=json.loads(original);mutation(x);p.write_text(json.dumps(x))
    try:
     with self.assertRaises(ValueError):validate(root)
    finally:p.write_bytes(original)
   reject('research/identity-reconciliation-v2.json',lambda x:x['rows'].pop())
   reject('research/identity-reconciliation-v2.json',lambda x:x.update(physical_duplicates_adjudicated=0))
   reject('research/reference-reconciliation-v2.json',lambda x:x.update(independent_review_complete=True))
   path='corpus/critical-readings.json' if IS_CH else 'occurrences/occurrences.json'
   reject(path,lambda x:x.append(x[0]) if IS_CH else x['occurrences'].append(x['occurrences'][0]))
   if IS_CH:reject('research/reference-reconciliation-v2.json',lambda x:next(y for y in x['existing_reading_dispositions'] if y['apparatus'])['apparatus'].clear())
if __name__=='__main__':unittest.main()
