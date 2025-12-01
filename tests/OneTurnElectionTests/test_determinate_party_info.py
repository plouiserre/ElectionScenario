import unittest
from src.backend.domain.models.factory import factory_congress_person
from src.backend.domain.services.OneTurnElection.DeterminatePartyInfo import DeterminatePartyInfo
from utils.assert_helper import assert_congress_person_with_district, assert_party
from tests.utils.data.catalogData import generate_datas

class DeterminatePartyInfoTest(unittest.TestCase):
    def test_calculate_party_info(self):
        parties = generate_datas("party", "2024")
        elected_persons = self.__build_elected_persons()
        elected_persons = generate_datas("candidate", ["ALBRAND", "BONY", "VOYNET", "LAHAIS", "BABIN", "MONTEIL", "ROSSET"])
        determinate_party_info = DeterminatePartyInfo(parties)

        parties_infos = determinate_party_info.Calculate(elected_persons)

        #TODO factorize with test_json_results_election!!!!
        assert_party("Union de la gauche|UG|2|3", parties_infos[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", parties_infos[0].congress_persons[0], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", parties_infos[0].congress_persons[1], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", parties_infos[0].congress_persons[2], self)    
        assert_party("Les Républicains|LR|4|1", parties_infos[1], self)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", parties_infos[1].congress_persons[0], self)
        assert_party("Rassemblement National|RN|5|3", parties_infos[2], self)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", parties_infos[2].congress_persons[0], self)
        assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", parties_infos[2].congress_persons[1], self)
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", parties_infos[2].congress_persons[2], self)
   

    def __build_elected_persons(self):
        first_elected_person = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, generate_datas("district","first_district"))
        second_elected_person = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, generate_datas("district", "second_district"))
        third_elected_person = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, generate_datas("district","third_district"))
        fourth_elected_person = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, generate_datas("district","fourth_district"))
        fifth_elected_person = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91,  generate_datas("district","fifth_district"))
        sixth_elected_person =factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, generate_datas("district","sixth_district"))
        seventh_elected_person = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, generate_datas("district","seventh_district"))
        elected_persons = [first_elected_person, second_elected_person, third_elected_person, fourth_elected_person, 
                            fifth_elected_person, sixth_elected_person, seventh_elected_person]
        return elected_persons


    