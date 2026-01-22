import unittest
from src.backend.domain.services.OneTurnElection.CongressPersonsByDpt import CongressPersonsByDpt
from tests.utils.data.catalogData import generate_datas
from utils.assert_helper import assert_congress_person_with_district

class CongressPersonsByDptTest(unittest.TestCase):
    def test_order_congress_persons_by_dpts(self): 
        parties = generate_datas("party", "2024")
        elected_persons = generate_datas("candidate", ["ALBRAND", "BONY", "LE GENDRE", "VOYNET", "LAHAIS", "DECOURCELLE",  "MONTEIL", "ROSSET"])
        parties_info = self.__build_parties_info(parties, elected_persons)
        congress_persons_by_dpt = CongressPersonsByDpt()

        dpt_code_with_congress_persons = congress_persons_by_dpt.Order(parties_info)
        
        self.assertEqual(6, len(dpt_code_with_congress_persons))

        self.assertTrue("5" in dpt_code_with_congress_persons)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", dpt_code_with_congress_persons["5"][0], self)

        self.assertTrue("15" in dpt_code_with_congress_persons)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", dpt_code_with_congress_persons["15"][0], self)        

        self.assertTrue("25" in dpt_code_with_congress_persons)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", dpt_code_with_congress_persons["25"][0], self)

        self.assertTrue("35" in dpt_code_with_congress_persons)
        assert_congress_person_with_district("DECOURCELLE|Christophe|MASCULIN|LR|5218|6.93|2ème circonscription|3502|Ille-et-Vilaine|35", dpt_code_with_congress_persons["35"][0], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", dpt_code_with_congress_persons["35"][1], self)
        
        self.assertTrue("65" in dpt_code_with_congress_persons)        
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", dpt_code_with_congress_persons["65"][0], self)    

        self.assertTrue("75" in dpt_code_with_congress_persons)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", dpt_code_with_congress_persons["75"][0], self)    
        assert_congress_person_with_district("LE GENDRE|Gilles|MASCULIN|DVC|11071|19.62|2ème circonscription|7502|Paris|75", dpt_code_with_congress_persons["75"][1], self)  


    def __build_parties_info(self, parties, elected_persons): 
        parties_info = []
        for elected_person in elected_persons : 
            for party in parties : 
                if elected_person.parti_code == party.code : 
                    if (party in parties_info) == False : 
                        parties_info.append(party)
                    party.congress_persons.append(elected_person)
                    party.elected_congress_persons  += 1
        return parties_info