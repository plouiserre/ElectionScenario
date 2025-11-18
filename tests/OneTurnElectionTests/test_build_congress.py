import unittest
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from tests.utils.assert_helper import assert_party
from tests.utils.data.catalogData import generate_datas

class BuildCongressTest(unittest.TestCase):
    def test_build_high_stable_congress(self):        
        parties_2024 = generate_datas("party", "high_stable_with_candidates_2024")
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("HIGH", congress.stability_majority )
        assert_party('Union de la gauche|UG|4', congress.parties[0], self)
        assert_party('Rassemblement National|RN|3', congress.parties[1], self)
        assert_party('Les Républicains|LR|1', congress.parties[2], self)

    def test_build_medium_stable_congress(self):
        parties_2024 = generate_datas("party", "with_candidates_2024")
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("MEDIUM", congress.stability_majority )
        assert_party('Union de la gauche|UG|3', congress.parties[0], self)
        assert_party('Rassemblement National|RN|3', congress.parties[1], self)
        assert_party('Les Républicains|LR|1', congress.parties[2], self)


    def test_build_low_stable_congress(self):
        parties_2024 = generate_datas("party", "low_stable_with_candidates_2024")
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("LOW", congress.stability_majority )
        assert_party('Union de la gauche|UG|2', congress.parties[0], self)
        assert_party('Rassemblement National|RN|2', congress.parties[1], self)
        assert_party('Ensemble ! (Majorité présidentielle)|ENS|2', congress.parties[2], self)
        assert_party('Les Républicains|LR|1', congress.parties[3], self)
  