import unittest
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from tests.utils.data.catalogData import generate_datas

class RepresentativeCongressTest(unittest.TestCase):
    def test_determine_congress_have_perfect_representative(self):
        results_elections = generate_datas("results_elections", "perfect")
        congress = generate_datas("congress", "perfectly_representative")
        representative_congress = RepresentativeCongress(20, 2024)
        
        representative = representative_congress.Calculate(congress, results_elections)

        self.assertEqual("PERFECT", representative)

    def test_determine_congress_have_good_representative(self):
        results_elections = generate_datas("results_elections", "good")
        congress = generate_datas("congress", "good_representative")
        representative_congress = RepresentativeCongress(20, 2024)
        
        representative = representative_congress.Calculate(congress, results_elections)

        self.assertEqual("GOOD", representative)

    def test_determine_congress_have_quite_representative(self):
        results_elections = generate_datas("results_elections", "quite")
        congress = generate_datas("congress", "quite_representative")
        representative_congress = RepresentativeCongress(20, 2024)
        
        representative = representative_congress.Calculate(congress, results_elections)

        self.assertEqual("QUITE", representative)

    def test_determine_congress_have_low_representative(self):
        results_elections = generate_datas("results_elections", "low")
        congress = generate_datas("congress", "low_representative")
        representative_congress = RepresentativeCongress(20, 2024)
        
        representative = representative_congress.Calculate(congress, results_elections)

        self.assertEqual("LOW", representative)