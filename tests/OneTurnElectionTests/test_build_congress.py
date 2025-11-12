import unittest
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from tests.utils.data.generateParties import get_parties_with_elected_persons_2024

class BuildCongressTest(unittest.TestCase):
    def test_build_simple_congress(self):
        parties_2024 = get_parties_with_elected_persons_2024()
        parties_2024_original = parties_2024.copy()
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.__assert_build_congress(parties_2024_original, congress)
        
    def __assert_build_congress(self, parties_2024, congress):
        parties_expected = get_parties_with_elected_persons_2024()
        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        for idx in range(len(parties_expected)):
            self.assertEqual(parties_2024[idx].code, parties_expected[idx].code)
            self.assertEqual(parties_2024[idx].name, parties_expected[idx].name)
            self.assertEqual(parties_2024[idx].elected_congress_persons, parties_expected[idx].elected_congress_persons)
            self.assertEqual(len(parties_2024[idx].congress_persons), len(parties_expected[idx].congress_persons))
        