import unittest
from src.backend.domain.models.factory import factory_congress_person
from src.backend.usecases.OneTurnElection.DeterminatePartyInfo import DeterminatePartyInfo
from utils.assert_helper import assert_congress_person_with_district, assert_party
from utils.generateData import build_first_district, build_second_district, build_third_district, build_fourth_district, build_fifth_district, build_sixth_district, build_seventh_district, get_all_parties_without_elected_persons_2024

class DeterminatePartyInfoTest(unittest.TestCase):
    def test_calculate_party_info(self):
        parties = get_all_parties_without_elected_persons_2024()
        elected_persons = self.__build_elected_persons()
        determinate_party_info = DeterminatePartyInfo(parties)

        parties_infos = determinate_party_info.Calculate(elected_persons)

        assert_party("Union de la gauche|UG|42.86", parties_infos[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", parties_infos[0].congress_persons[0], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", parties_infos[0].congress_persons[1], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", parties_infos[0].congress_persons[2], self)    
        assert_party("Les Républicains|LR|14.29", parties_infos[1], self)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", parties_infos[1].congress_persons[0], self)
        assert_party("Rassemblement National|RN|42.86", parties_infos[2], self)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", parties_infos[2].congress_persons[0], self)
        assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", parties_infos[2].congress_persons[1], self)
        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", parties_infos[2].congress_persons[2], self)
        


    def __build_elected_persons(self):
        first_elected_person = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, build_first_district())
        second_elected_person = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, build_second_district())
        third_elected_person = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, build_third_district())
        fourth_elected_person = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, build_fourth_district())
        fifth_elected_person = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, build_fifth_district())
        sixth_elected_person =factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, build_sixth_district())
        seventh_elected_person = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, build_seventh_district())
        elected_persons = [first_elected_person, second_elected_person, third_elected_person, fourth_elected_person, 
                           fifth_elected_person, sixth_elected_person, seventh_elected_person]
        return elected_persons


    