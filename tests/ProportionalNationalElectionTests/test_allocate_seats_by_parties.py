import unittest
from src.backend.domain.services.ProportionalNationalElection.AllocateSeatsForParties import AllocateSeatsForParties

class AllocateSeatsForPartiesTest(unittest.TestCase): 
    def test_allocate_seats_for_parties_with_eight_seats_available(self):
        datas = {'ENS': 22.91, 'UG': 29.75, 'RN': 29.07, 'LR': 7.05}
        allocate_seats_by_parties = AllocateSeatsForParties(8)

        results = allocate_seats_by_parties.allocate(datas)

        self.assertEqual(2, results['ENS'])
        self.assertEqual(3, results['UG'])
        self.assertEqual(3, results['RN'])
        self.assertEqual(0, results['LR'])

    def test_allocate_seats_for_parties_with_seven_seats_available(self):
        datas = {'ENS': 22.91, 'UG': 29.75, 'RN': 29.07, 'LR': 7.05}
        allocate_seats_by_parties = AllocateSeatsForParties(7)

        results = allocate_seats_by_parties.allocate(datas)

        self.assertEqual(1, results['ENS'])
        self.assertEqual(3, results['UG'])
        self.assertEqual(3, results['RN'])
        self.assertEqual(0, results['LR'])