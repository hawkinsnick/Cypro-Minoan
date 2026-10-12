import copy,unittest
from source_growth import load,validate,FILES
class SourceGrowthGuards(unittest.TestCase):
 def setUp(self):self.data=[load(p) for p in FILES]
 def reject(self,mutator):
  d=copy.deepcopy(self.data);mutator(d)
  with self.assertRaises((ValueError,KeyError)):validate(*d)
 def test_native_views(self):validate(*self.data)
 def test_duplicate_source_id(self):self.reject(lambda d:d[0]['records'].append(copy.deepcopy(d[0]['records'][0])))
 def test_reading_admission(self):self.reject(lambda d:d[0]['records'][0].update(reading_admitted=True))
 def test_image_admission(self):self.reject(lambda d:d[0]['records'][0].update(images_included=True))
 def test_inventory_mismatch(self):self.reject(lambda d:d[0]['records'][0]['inventory_assertions'][0].update(value='wrong'))
 def test_footnote_as_identifier(self):self.reject(lambda d:d[1]['records'][0]['database_identifier'].update(literal='TN 2413'))
 def test_unit_drift(self):self.reject(lambda d:d[0]['records'][0]['dimension_assertions'][0].update(unit='mm'))
 def test_damage_erasure(self):self.reject(lambda d:d[1]['records'][0]['sign_count_assertion'].update(certainty='certain'))
 def test_appendix_qualifier(self):self.reject(lambda d:d[1]['records'][0]['appendix_table_assertions'].update(number_of_signs_literal='3 signs'))
