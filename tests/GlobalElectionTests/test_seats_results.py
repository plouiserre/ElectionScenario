import unittest
from src.backend.domain.services.GlobalElection.SeatsResults import SeatsResults
from tests.utils.data.catalogData import generate_datas


class DeterminePercentageVoteByPartyTest(unittest.TestCase): 
    def test_calculate_all_percentage_vote_for_all_parties(self):
        vote_all_parties = {"EXG" : 3905, "ENS" : 95884, "UG" : 124540, "DIV" : 2260, "RN" : 121673, "REC" : 2449, "DVD" : 20345, 
                            "LR" : 29527, "ECO" : 2799, "DVG" : 2189, "REG" : 1486, "DVC" : 11501}        
        seats_results = SeatsResults()

        percentages = seats_results.calculate_percentage(vote_all_parties)

        self.assertEqual(0.93, percentages["EXG"])
        self.assertEqual(22.91, percentages["ENS"])
        self.assertEqual(29.75, percentages["UG"])
        self.assertEqual(0.54, percentages["DIV"])
        self.assertEqual(29.07, percentages["RN"])
        self.assertEqual(0.59, percentages["REC"])
        self.assertEqual(4.86, percentages["DVD"])
        self.assertEqual(7.05, percentages["LR"])
        self.assertEqual(0.67, percentages["ECO"])
        self.assertEqual(0.52, percentages["DVG"])
        self.assertEqual(0.36, percentages["REG"])
        self.assertEqual(2.75, percentages["DVC"])

def test_calculate_all_vote_for_all_parties(self):
        all_candidates = generate_datas("candidate", "")
        seats_results = SeatsResults()

        results = seats_results.calculate_vote_each_party(all_candidates)

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