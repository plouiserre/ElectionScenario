import unittest
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from tests.utils.data.catalogData import generate_datas

class StabilityCongressTest(unittest.TestCase): 
    def test_valid_congress_is_very_stable(self):
        congress = generate_datas("congress", "very_stable")
        stability_congress = StabilityCongress(7)

        stability = stability_congress.Calculate(congress)

        self.assertEqual("PERFECT",stability)

    def test_valid_congress_is_stable(self):
        congress = generate_datas("congress", "stable")
        stability_congress = StabilityCongress(5)

        stability = stability_congress.Calculate(congress)

        self.assertEqual("GOOD",stability)

    def test_valid_congress_is_quite_stable(self): 
        congress = generate_datas("congress", "quite_stable")
        stability_congress = StabilityCongress(5)

        stability = stability_congress.Calculate(congress)

        self.assertEqual("QUITE",stability)

    def test_valid_congress_is_low_stable_three_family(self): 
        congress = generate_datas("congress", "low_stable")
        stability_congress = StabilityCongress(6)

        stability = stability_congress.Calculate(congress)

        self.assertEqual("LOW",stability)