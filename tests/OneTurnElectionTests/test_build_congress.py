import unittest
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from tests.utils.data.generateParties import get_parties_with_elected_persons_2024

class BuildCongressTest(unittest.TestCase):
    def test_build_simple_congress(self):
        parties_2024 = get_parties_with_elected_persons_2024(42.86, 14.28, 42.86)
        parties_2024_original = parties_2024.copy()
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.__assert_build_conggress(parties_2024_original, congress, 42.86, 14.28, 42.86)


    def test_build_congress_with_no_one_hundred_by_more_than_zero_point_zero_one_percent(self):
        parties_2024 = get_parties_with_elected_persons_2024(42.86, 14.29, 42.86)
        parties_2024_original = parties_2024.copy()
        build_congress = BuildCongress()


        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.__assert_build_conggress(parties_2024_original, congress, 42.86, 14.28, 42.86)


    def test_build_congress_with_no_one_hundred_by_more_than_zero_point_zero_two_percent(self):
        parties_2024 = get_parties_with_elected_persons_2024(42.87, 14.29, 42.86)
        parties_2024_original = parties_2024.copy()
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.__assert_build_conggress(parties_2024_original, congress, 42.87, 14.27, 42.86)

    
    def test_build_congress_with_no_one_hundred_by_less_than_zero_point_zero_two_percent(self):
        parties_2024 = get_parties_with_elected_persons_2024(42.84, 14.28, 42.86)
        parties_2024_original = parties_2024.copy()

        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.__assert_build_conggress(parties_2024_original, congress, 42.84, 14.30, 42.86)


    def __assert_build_conggress(self, parties_2024, congress, percentage_first_party, percentage_second_party, percentage_third_party):
        parties_expected = get_parties_with_elected_persons_2024(percentage_first_party, percentage_second_party, percentage_third_party)
        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        for idx in range(len(parties_expected)):
            self.assertEqual(parties_2024[idx].code, parties_expected[idx].code)
            self.assertEqual(parties_2024[idx].name, parties_expected[idx].name)
            self.assertEqual(parties_2024[idx].percentage, parties_expected[idx].percentage)
            self.assertEqual(len(parties_2024[idx].congress_persons), len(parties_expected[idx].congress_persons))
        