import unittest
from src.backend.domain.services.GlobalElection.CongressPersonElected import CongressPersonElected
from tests.utils.data.catalogData import generate_datas
from tests.utils.assert_helper import assert_congress_person_with_district

class CongressPersonElectedTest(unittest.TestCase):
    def test_select_candidates_elected(self): 
        candidates = generate_datas("candidate", "")
        congress_person_elected = CongressPersonElected()
        score = {'UG': 3, 'RN': 3, 'ENS': 2, 'LR': 0}

        congress_persons = congress_person_elected.Choose(score, candidates)

        self.assertEqual(8, len(congress_persons))
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", congress_persons[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", congress_persons[1], self)        
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", congress_persons[2], self)    
        
        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", congress_persons[3], self)                          
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", congress_persons[4], self)                          
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", congress_persons[5], self)

        assert_congress_person_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|25792|34.24|2ème circonscription|3502|Ille-et-Vilaine|35", congress_persons[6], self)
        assert_congress_person_with_district("VUILLEMIN|Benoît|MASCULIN|ENS|15026|26.79|2ème circonscription|2502|Doubs|25", congress_persons[7], self)
        