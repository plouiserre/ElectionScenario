import unittest
from src.backend.domain.services.OneTurnElection.DeterminatePartyInfo import DeterminatePartyInfo
from utils.assert_helper import assert_congress_person_with_district, assert_party
from tests.utils.data.catalogData import generate_datas

class DeterminatePartyInfoTest(unittest.TestCase):
    def test_calculate_party_info(self):
        elected_persons = generate_datas("candidate", ["ALBRAND", "BONY", "VOYNET", "LAHAIS", "BABIN", "MONTEIL", "ROSSET"])
        determinate_party_info = DeterminatePartyInfo()

        parties_infos = determinate_party_info.Calculate(elected_persons)

        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", parties_infos["5"][0], self)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", parties_infos["15"][0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", parties_infos["25"][0], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", parties_infos["35"][0], self)
        assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", parties_infos["45"][0], self)
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", parties_infos["65"][0], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", parties_infos["75"][0], self)    
        