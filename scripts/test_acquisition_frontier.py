import copy,unittest
from acquisition_frontier import load,validate,FILES
class FrontierGuards(unittest.TestCase):
 def setUp(self):self.data=[load(p) for p in FILES]
 def reject(self,mutate):
  d=copy.deepcopy(self.data);mutate(d)
  with self.assertRaises((ValueError,KeyError)):validate(*d)
 def test_actual_views(self):validate(*self.data)
 def test_duplicate_row(self):self.reject(lambda d:d[0]['records'].append(copy.deepcopy(d[0]['records'][0])))
 def test_candidate_as_core(self):self.reject(lambda d:d[0]['records'][0].update(catalogue_number=255))
 def test_anchor_certainty(self):self.reject(lambda d:d[0]['records'][0]['classification_assertions'][0].update(certainty='CERTAIN'))
 def test_licence_override(self):self.reject(lambda d:d[0].update(license='project NC'))
 def test_alternative_suppression(self):self.reject(lambda d:d[0]['records'][1]['classification_assertions'].pop())
 def test_range_loss(self):self.reject(lambda d:d[0]['records'][1].update(published_sign_count=4))
 def test_blocked_access_as_delivery(self):self.reject(lambda d:d[1]['routes'][1].update(source_payload_acquired=True))
