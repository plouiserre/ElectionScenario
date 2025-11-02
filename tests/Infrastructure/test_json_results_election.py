import unittest
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection
from tests.utils.assert_helper import assert_congress_person_with_district, assert_party
from tests.utils.generateData import get_parties_with_elected_persons_2024

class JsonResultsElectionTest(unittest.TestCase):
    def test_transform_data_from_json_to_congress_model(self):
        json_results_election = JsonResultsElection()

        congress = json_results_election.get_results()
        
        parties_expected = get_parties_with_elected_persons_2024(42.86, 14.28, 42.86)
        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        assert_party("Union de la gauche|UG|42.86", parties_expected[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", parties_expected[0].congress_persons[0], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", parties_expected[0].congress_persons[1], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", parties_expected[0].congress_persons[2], self)    
        assert_party("Les Républicains|LR|14.29", parties_expected[1], self)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", parties_expected[1].congress_persons[0], self)
        assert_party("Rassemblement National|RN|42.86", parties_expected[2], self)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", parties_expected[2].congress_persons[0], self)
        assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", parties_expected[2].congress_persons[1], self)
        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", parties_expected[2].congress_persons[2], self)