"""Hostile evidence mutations must fail without promoting source observations."""
import copy,json,shutil,tempfile,unittest
from pathlib import Path
from validate_source_expansion import ROOT,IS_CH,KEY,validate,validate_new,joins
class EvidenceTests(unittest.TestCase):
 def test_valid(self):validate()
 def test_label_changes_rejected(self):
  rows=json.loads((ROOT/'research/source-check-2026-10-11.json').read_text())[KEY];bad=copy.deepcopy(rows)
  if IS_CH:bad[0]['tokens'][0]['form']='invented'
  else:bad[0]['published_sign_label']='invented'
  with self.assertRaises(ValueError):validate_new(bad)
 def test_primary_promotion_rejected(self):
  rows=json.loads((ROOT/'research/source-check-2026-10-11.json').read_text())[KEY];bad=copy.deepcopy(rows)
  if IS_CH:bad[0]['source_id']='CHIC1996'
  else:bad[0]['source_role']='primary_publication'
  with self.assertRaises(ValueError):validate_new(bad)
 def test_duplicate_locus_rejected(self):
  rows=json.loads((ROOT/'research/source-check-2026-10-11.json').read_text())[KEY]
  with self.assertRaises(ValueError):validate_new(rows+[rows[0]])
 def test_catalogue_identifier_conflict(self):
  record={'id':'test','identifiers':[{'system':'Olivier 2007 catalogue','value':'25'},{'system':'Ferrara 2013 catalogue','value':'26'}]}
  with self.assertRaises(ValueError):joins(record,set(range(1,255)))
 def test_identifier_namespace_is_preserved(self):
  record={'id':'test','identifiers':[{'system':'Met object number','value':'25'}]}
  self.assertEqual(joins(record,set(range(1,255))),[])
 def test_denominator_unit_mutation_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
   p=root/'research/coverage-denominators.json';d=json.loads(p.read_text());d['views'][0]['unit']='physical_inscription';p.write_text(json.dumps(d))
   with self.assertRaises(ValueError):validate(root)
if __name__=='__main__':unittest.main()
