import copy,json,tempfile,unittest
from pathlib import Path
from validate_CM209_20261014 import ROOT,REGISTER,validate
class Boundary(unittest.TestCase):
 def test_native(self):self.assertEqual(validate()['total_occurrences'],28)
 def reject(self,path,mutate):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)
   for p in [REGISTER,'occurrences/occurrences.json','research/source-reconciliation.json']:
    target=root/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/p).read_bytes())
   target=root/path;x=json.loads(target.read_text());mutate(x);target.write_text(json.dumps(x))
   with self.assertRaises(ValueError):validate(root)
 def test_uncertainty_cannot_be_stripped(self):self.reject(REGISTER,lambda x:x['expected_additions'][1].update(certainty='certain'))
 def test_historical_source_cannot_change(self):self.reject('occurrences/occurrences.json',lambda x:x['occurrences'][0].update(published_sign_label='08'))
 def test_internal_conflict_cannot_be_selected(self):
  def change(x):
   o=copy.deepcopy(x['occurrences'][-1]);o.update(zone_id='A.II.5.01-first-group',published_sign_label='09');x['occurrences'].append(o)
  self.reject('occurrences/occurrences.json',change)
 def test_wrong_record_join(self):self.reject('occurrences/occurrences.json',lambda x:x['occurrences'][-1].update(record_id='CMOC-0216'))
 def test_disagreement_cannot_be_adjudicated(self):self.reject('research/source-reconciliation.json',lambda x:x['comparisons'][-1].update(status='ACCEPTED'))
if __name__=='__main__':unittest.main()
