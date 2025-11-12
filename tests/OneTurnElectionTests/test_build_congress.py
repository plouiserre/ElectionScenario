import unittest
from tests.utils.data.generateDataDistricts import build_first_district, build_second_district, build_third_district, build_fourth_district, build_fifth_district, build_sixth_district, build_seventh_district
from src.backend.domain.models.factory import factory_congress_person, factory_district, factory_party
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from tests.utils.assert_helper import assert_party
from tests.utils.data.generateParties import get_parties_with_elected_persons_2024

class BuildCongressTest(unittest.TestCase):
    def test_build_high_stable_congress(self):
        new_district = factory_district("11ème circonscription", 9311, "Seine-Saint-Denis", 93)       
        new_congress_persons = factory_congress_person("AUTAIN", "Clémentine", "FEMININ", "UG", 22209, 62.65, new_district)        
        parties_2024 = get_parties_with_elected_persons_2024()
        parties_2024[0].congress_persons.append(new_congress_persons)
        parties_2024[0].elected_congress_persons = 4
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("HIGH", congress.stability_majority )
        assert_party('Union de la gauche|UG|4', congress.parties[0], self)
        assert_party('Rassemblement National|RN|3', congress.parties[1], self)
        assert_party('Les Républicains|LR|1', congress.parties[2], self)

    def test_build_medium_stable_congress(self):
        parties_2024 = get_parties_with_elected_persons_2024()
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("MEDIUM", congress.stability_majority )
        assert_party('Union de la gauche|UG|3', congress.parties[0], self)
        assert_party('Rassemblement National|RN|3', congress.parties[1], self)
        assert_party('Les Républicains|LR|1', congress.parties[2], self)


    def test_build_low_stable_congress(self):
        parties_2024 = self.__low_stable_parties_with_elected_persons_2024()
        build_congress = BuildCongress()

        congress = build_congress.Build(2024, "OneTurn", parties_2024)

        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("LOW", congress.stability_majority )
        assert_party('Union de la gauche|UG|2', congress.parties[0], self)
        assert_party('Rassemblement National|RN|2', congress.parties[1], self)
        assert_party('Ensemble ! (Majorité présidentielle)|ENS|2', congress.parties[2], self)
        assert_party('Les Républicains|LR|1', congress.parties[3], self)


    def __low_stable_parties_with_elected_persons_2024(self):
        parties = []
        _first_elected_person_ug = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, build_third_district())
        _second_elected_person_ug = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, build_fourth_district())
        parties.append(factory_party('Union de la gauche','UG', [_first_elected_person_ug, _second_elected_person_ug]))
        first_elected_person_lr = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, build_second_district())
        parties.append(factory_party('Les Républicains', 'LR', [first_elected_person_lr]))
        first_elected_person_rn = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, build_first_district())
        second_elected_person_rn = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, build_fifth_district())
        parties.append(factory_party('Rassemblement National', 'RN', [first_elected_person_rn, second_elected_person_rn]))
        first_elected_person_ens = factory_congress_person("FINE", "Sébastien", "MASCULIN", "ENS", 10338, 26.70, build_first_district())
        second_elected_person_ens = factory_congress_person("MAILLART-MÉHAIGNERIE", "Laurence", "FEMININ", "ENS", 25792, 34.24, build_fourth_district())
        parties.append(factory_party('Ensemble ! (Majorité présidentielle)', 'ENS', [first_elected_person_ens, second_elected_person_ens]))
        return parties
  