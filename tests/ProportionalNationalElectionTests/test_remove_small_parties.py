import unittest
from src.backend.domain.services.ProportionalNationalElection.RemoveSmallParties import RemoveSmallParties

class RemoveSmallPartiesTest(unittest.TestCase):
    def test_remove_small_parties(self):
        datas = {'EXG': 0.93, 'ENS': 22.91, 'UG': 29.75, 'DIV': 0.54, 'RN': 29.07, 'REC': 0.59, 'DVD': 4.86, 'LR': 7.05, 'ECO': 0.67, 'DVG': 0.52, 'REG': 0.36, 'DVC': 2.75}        
        remove = RemoveSmallParties()

        results = remove.Choose(datas)

        self.assertEqual(4, len(results))
        self.assertEqual(22.91, results['ENS'])
        self.assertEqual(29.75, results['UG'])
        self.assertEqual(29.07, results['RN'])
        self.assertEqual(7.05, results['LR'])