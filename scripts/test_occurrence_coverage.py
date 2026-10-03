import copy,json,unittest
from occurrence_coverage import R,coverage
class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.records=json.loads((R/'corpus/index.json').read_text())['records'];self.occ=json.loads((R/'occurrences/occurrences.json').read_text())['occurrences']
    def test_replay_known_scope(self):
        r=coverage(self.records,self.occ)
        self.assertEqual(r,json.loads((R/'analysis/occurrence-coverage-v1.json').read_text()))
        self.assertEqual((r['rich_records'],r['records_with_encoded_occurrences'],r['encoded_occurrences']),(21,6,12))
        self.assertEqual(sum(s['occurrences'] for s in r['source_strata'] if s['source_role']=='primary_publication'),6)
        self.assertFalse(r['sign_labels_merged']);self.assertFalse(r['corpus_wide_frequency_allowed'])
    def test_comparative_citations_cannot_be_promoted(self):
        bad=copy.deepcopy(self.occ);bad[-1]['source_role']='primary_publication'
        with self.assertRaises(ValueError):coverage(self.records,bad)
        bad=copy.deepcopy(self.occ);del bad[-1]['source_role']
        with self.assertRaises(ValueError):coverage(self.records,bad)
        bad=copy.deepcopy(self.occ);bad[3]['record_id']='CMOC-0025'
        with self.assertRaises(ValueError):coverage(self.records,bad)
    def test_same_locus_with_new_id_is_not_new_evidence(self):
        duplicate=copy.deepcopy(self.occ[-1]);duplicate['occurrence_id']='TEST-ONLY'
        with self.assertRaises(ValueError):coverage(self.records,self.occ+[duplicate])
    def test_bad_provenance_rejected(self):
        for k,v in [('record_id','missing'),('source_id','unclassified'),('locator','')]:
            bad=copy.deepcopy(self.occ);bad[0][k]=v
            with self.subTest(k=k),self.assertRaises(ValueError):coverage(self.records,bad)
        with self.assertRaises(ValueError):coverage(self.records,self.occ+[self.occ[0]])
if __name__=='__main__':unittest.main()
