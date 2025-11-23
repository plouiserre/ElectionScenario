import unittest
from src.backend.domain.services.ProportionalNationalElection.DeterminateSeatsByParty import DeterminateSeatsByParty

class DeterminateSeatsByPartyTest(unittest.TestCase): 
    def test_determinate_seats_by_party_with_eight_seats_available(self):
        datas = {'ENS': 22.91, 'UG': 29.75, 'RN': 29.07, 'LR': 7.05}
        seats_by_party = DeterminateSeatsByParty(8)

        results = seats_by_party.Calculate(datas)

        self.assertEqual(2, results['ENS'])
        self.assertEqual(3, results['UG'])
        self.assertEqual(3, results['RN'])
        self.assertEqual(0, results['LR'])

    def test_determinate_seats_by_party_with_seven_seats_available(self):
        datas = {'ENS': 22.91, 'UG': 29.75, 'RN': 29.07, 'LR': 7.05}
        seats_by_party = DeterminateSeatsByParty(7)

        results = seats_by_party.Calculate(datas)

        self.assertEqual(1, results['ENS'])
        self.assertEqual(3, results['UG'])
        self.assertEqual(3, results['RN'])
        self.assertEqual(0, results['LR'])