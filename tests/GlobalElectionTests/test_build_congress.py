import unittest
from unittest.mock import Mock
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection
from tests.utils.assert_helper import assert_party
from tests.utils.data.catalogData import generate_datas

class BuildCongressTest(unittest.TestCase):
    #TODO remove 95 from high_stable_with_candidates_2024
    def test_build_high_stable_congress(self):   
        year = 2024     
        all_congress_persons_number = 7   
        parties_2024 = generate_datas("party", "high_stable_with_candidates_2024")
        votes_results = self.__get_votes_results_data()
        stability_congress = StabilityCongress(all_congress_persons_number)
        representative_congress = RepresentativeCongress(all_congress_persons_number)
        build_congress = BuildCongress(stability_congress, representative_congress)

        congress = build_congress.Build(year, "OneTurn", parties_2024, votes_results)

        self.assertEqual(year, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("PERFECT", congress.stability_majority )
        self.assertEqual("LOW", congress.representative_congress)
        assert_party('Union de la gauche|UG|2|4', congress.parties[0], self)
        assert_party('Rassemblement National|RN|5|3', congress.parties[1], self)
        assert_party('Les Républicains|LR|4|1', congress.parties[2], self)


    def test_build_quite_stable_congress(self):
        year = 2024     
        all_congress_persons_number = 7   
        parties_2024 = generate_datas("party", "with_candidates_2024")
        votes_results = self.__get_votes_results_data()
        stability_congress = StabilityCongress(all_congress_persons_number)
        representative_congress = RepresentativeCongress(all_congress_persons_number)
        build_congress = BuildCongress(stability_congress, representative_congress)

        congress = build_congress.Build(2024, "OneTurn", parties_2024, votes_results)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("QUITE", congress.stability_majority )
        assert_party('Union de la gauche|UG|2|3', congress.parties[0], self)
        assert_party('Rassemblement National|RN|5|3', congress.parties[1], self)
        assert_party('Les Républicains|LR|4|1', congress.parties[2], self)


    def test_build_low_stable_congress(self):
        year = 2024
        all_congress_persons_number = 7        
        parties_2024 = generate_datas("party", "low_stable_with_candidates_2024")
        votes_results = self.__get_votes_results_data()
        stability_congress = StabilityCongress(all_congress_persons_number)
        representative_congress = RepresentativeCongress(all_congress_persons_number)
        build_congress = BuildCongress(stability_congress, representative_congress)

        congress = build_congress.Build(year, "OneTurn", parties_2024, votes_results)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("QUITE", congress.stability_majority )
        self.assertEqual("QUITE", congress.representative_congress)
        assert_party('Union de la gauche|UG|2|2', congress.parties[0], self)
        assert_party('Rassemblement National|RN|5|2', congress.parties[1], self)
        assert_party('Ensemble ! (Majorité présidentielle)|ENS|3|2', congress.parties[2], self)
        assert_party('Les Républicains|LR|4|1', congress.parties[3], self)
  

    def __get_votes_results_data(self):
        all_results = generate_datas("results_elections", "default7")
        return all_results