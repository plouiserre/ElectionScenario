import unittest
from src.backend.domain.services.ProportionalDepartmentElection.DistrictsVoteFromDpt import DistrictsVoteFromDpt
from tests.utils.assert_helper import assert_candidate_with_district_and_percentage
from tests.utils.data.catalogData import generate_datas

class DistrictsVoteFromDptTest(unittest.TestCase): 
    def test_find_all_districts_from_allier_dpt(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")     
        all_datas_elections = elections_results[2024]   
        districts_vote_from_dpt = DistrictsVoteFromDpt()
        
        candidates_district_allier_department = districts_vote_from_dpt.Find("3", all_datas_elections)
    
        self.assertEqual(3, len(candidates_district_allier_department))
        assert_candidate_with_district_and_percentage("AGEZ|Blandine|FEMININ|REC|602|1.02|1ère circonscription|301||3", candidates_district_allier_department[0][0], self)
        assert_candidate_with_district_and_percentage("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301||3", candidates_district_allier_department[0][1], self)
        assert_candidate_with_district_and_percentage("GUILLAUMIN|Jean-Marie|MASCULIN|UDI|1303|2.20|1ère circonscription|301||3", candidates_district_allier_department[0][2], self)
        assert_candidate_with_district_and_percentage("COLLOT|Jean-Marc|MASCULIN|EXG|636|1.08|1ère circonscription|301||3", candidates_district_allier_department[0][3], self)
        assert_candidate_with_district_and_percentage("LARZAT|Stephane|MASCULIN|ENS|8811|14.91|1ère circonscription|301||3", candidates_district_allier_department[0][4], self)
        assert_candidate_with_district_and_percentage("BARDET|Alexandra|FEMININ|LR|7889|13.35|1ère circonscription|301||3", candidates_district_allier_department[0][5], self)
        assert_candidate_with_district_and_percentage("THÈS|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301||3", candidates_district_allier_department[0][6], self)
        
        assert_candidate_with_district_and_percentage("BOVET|Jorys|MASCULIN|RN|17810|34.33|2ème circonscription|302||3", candidates_district_allier_department[1][0], self)
        assert_candidate_with_district_and_percentage("LEFEBVRE|Romain|MASCULIN|LR|10204|19.67|2ème circonscription|302||3", candidates_district_allier_department[1][1], self)
        assert_candidate_with_district_and_percentage("HERITIER|Louise|FEMININ|UG|12482|24.06|2ème circonscription|302||3", candidates_district_allier_department[1][2], self)
        assert_candidate_with_district_and_percentage("GONÇALVES|Alice|FEMININ|REC|511|0.98|2ème circonscription|302||3", candidates_district_allier_department[1][3], self)
        assert_candidate_with_district_and_percentage("ROUSSEAUX|Nicolas|MASCULIN|DVD|3548|6.84|2ème circonscription|302||3", candidates_district_allier_department[1][4], self)
        assert_candidate_with_district_and_percentage("VANCEUNEBROCK|Laurence|FEMININ|ENS|6524|12.57|2ème circonscription|302||3", candidates_district_allier_department[1][5], self)
        assert_candidate_with_district_and_percentage("LEBEL|Bernard|MASCULIN|EXG|802|1.55|2ème circonscription|302||3", candidates_district_allier_department[1][6], self)

        assert_candidate_with_district_and_percentage("RAY|Nicolas|MASCULIN|LR|21464|40.05|3ème circonscription|303||3", candidates_district_allier_department[2][0], self)
        assert_candidate_with_district_and_percentage("QUENEY|Rémy|MASCULIN|RN|20270|37.82|3ème circonscription|303||3", candidates_district_allier_department[2][1], self)
        assert_candidate_with_district_and_percentage("RAMEAU|Jean-François|MASCULIN|EXG|923|1.72|3ème circonscription|303||3", candidates_district_allier_department[2][2], self)
        assert_candidate_with_district_and_percentage("JEUDI|Aline|FEMININ|UG|10935|20.40|3ème circonscription|303||3", candidates_district_allier_department[2][3], self)