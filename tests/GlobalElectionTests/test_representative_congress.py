import unittest
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from tests.utils.data.catalogData import generate_datas

class RepresentativeCongressTest(unittest.TestCase):
    def test_determine_congress_have_perfect_representative(self):
        results_elections = generate_datas("results_elections", "perfect")
        congress = generate_datas("congress", "perfectly_representative")
        representative_congress = RepresentativeCongress()
        
        representative = representative_congress.Calculate(congress, results_elections)

        self.assertEqual("PERFECT", representative)