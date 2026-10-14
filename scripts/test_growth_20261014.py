"""Reject altered historical evidence, false independence and extra source positions."""
import copy,json,tempfile,unittest
from pathlib import Path
from validate_growth_20261014 import ROOT,validate
class GrowthTests(unittest.TestCase):
 def test_native(self):self.assertEqual(validate()['total_occurrences'],26)
 def test_mutations(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)
   for p in ['occurrences/occurrences.json','research/source-growth-2026-10-14.json']:
    f=root/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes((ROOT/p).read_bytes())
   def reject(path,fn):
    f=root/path;b=f.read_bytes();x=json.loads(b);fn(x);f.write_text(json.dumps(x))
    try:
     with self.assertRaises(ValueError):validate(root)
    finally:f.write_bytes(b)
   reject('occurrences/occurrences.json',lambda x:x['occurrences'][0].update(published_sign_label='999'))
   reject('occurrences/occurrences.json',lambda x:x['occurrences'].pop())
   reject('research/source-growth-2026-10-14.json',lambda x:x.update(independent_review_complete=True))
   reject('research/source-growth-2026-10-14.json',lambda x:x['expected_additions'][0].update(source_role='primary_publication'))
   reject('research/source-growth-2026-10-14.json',lambda x:x['expected_additions'][0].update(published_sign_label='999'))
   reject('research/source-growth-2026-10-14.json',lambda x:x.update(bulk_republication_authorized=True))
if __name__=='__main__':unittest.main()
