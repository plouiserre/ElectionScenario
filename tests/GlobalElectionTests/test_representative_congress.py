import unittest
from tests.utils.data.catalogData import generate_datas

class RepresentativeCongress(unittest.TestCase):
    def test_determine_congress_have_perfect_representative(self):
        results = generate_datas("results_elections", "")
        
        self.assertEqual(1,2)