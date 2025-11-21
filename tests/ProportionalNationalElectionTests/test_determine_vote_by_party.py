import unittest
from src.backend.domain.services.ProportionalNationalElection.DetermineVoteByParty import DetermineVoteByParty
from tests.utils.data.catalogData import generate_datas

class DetermineVoteByPartyTest(unittest.TestCase):
    def test_calculate_all_vote_for_all_parties(self):
        all_candidates = generate_datas("candidate", "")
        determine_vote = DetermineVoteByParty()

        results = determine_vote.Calculate(all_candidates)

        self.assertEqual(3905, results["EXG"])
        self.assertEqual(95884, results["ENS"])
        self.assertEqual(124540, results["UG"])
        self.assertEqual(2260, results["DIV"])
        self.assertEqual(121673, results["RN"])
        self.assertEqual(2449, results["REC"])
        self.assertEqual(20345, results["DVD"])
        self.assertEqual(29527, results["LR"])
        self.assertEqual(2799, results["ECO"])
        self.assertEqual(2189, results["DVG"])
        self.assertEqual(1486, results["REG"])
        self.assertEqual(11501, results["DVC"])