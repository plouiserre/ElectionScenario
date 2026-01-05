import unittest
from src.backend.domain.services.GlobalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas

class RegroupByParties(unittest.TestCase):
    def test_regroups_congress_persons_by_parties(self):
        congress_persons = self.__get_congress_persons()
        all_parties = generate_datas("party", "")
        congress_persons_by_parties = RegroupCongressPersonsByParties()

        parties = congress_persons_by_parties.sort(congress_persons, all_parties['2024'])

        self.assertEqual(3, len(parties))

        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", parties[0].congress_persons[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", parties[0].congress_persons[1], self)        
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", parties[0].congress_persons[2], self)    

        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", parties[1].congress_persons[0], self)                          
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", parties[1].congress_persons[1], self)                          
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", parties[1].congress_persons[2], self)

        assert_congress_person_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|25792|34.24|2ème circonscription|3502|Ille-et-Vilaine|35", parties[2].congress_persons[0], self)
        assert_congress_person_with_district("VUILLEMIN|Benoît|MASCULIN|ENS|15026|26.79|2ème circonscription|2502|Doubs|25", parties[2].congress_persons[1], self)


    def __get_congress_persons(self):
        first_congress_person = generate_datas("candidate", ["LAHAIS"])[0]
        second_congress_person = generate_datas("candidate", ["VOYNET"])[0]
        third_congress_person = generate_datas("candidate", ["ROSSET"])[0]
        fourth_congress_person = generate_datas("candidate", ["GOULET"])[0]
        fifth_congress_person = generate_datas("candidate", ["MONTEIL"])[0]
        sixth_congress_person = generate_datas("candidate", ["ALBRAND"])[0]
        seventh_congress_person = generate_datas("candidate", ["MAILLART-MÉHAIGNERIE"])[0]
        eighth_congress_person = generate_datas("candidate", ["VUILLEMIN"])[0]
        return [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person, fifth_congress_person,
                sixth_congress_person, seventh_congress_person, eighth_congress_person]