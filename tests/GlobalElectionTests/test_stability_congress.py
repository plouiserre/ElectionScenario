import unittest
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from tests.utils.data.catalogData import generate_datas

class StabilityCongressTest(unittest.TestCase): 
    def test_valid_congress_is_very_stable(self):
        congress =generate_datas("congress", "")
        stability_congress = StabilityCongress()

        stability = stability_congress.Calculate(congress)

        self.assertEqual("PERFECT",stability)