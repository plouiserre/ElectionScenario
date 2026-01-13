import unittest
from tests.utils.assert_helper import assert_candidate_with_district_and_percentage
from src.backend.domain.services.GlobalElection.CongressPersonsByDepartement import CongressPersonsByDepartments
from tests.utils.data.catalogData import generate_datas

class CongressPersonsByDepartmentsTest(unittest.TestCase):
    def test_congress_persons_are_regrouped_by_dept_from_dpt_congress(self):
        congress_persons_by_dpts = CongressPersonsByDepartments()
        congress_departments = generate_datas("department_congress", "three_departments_congress")
        
        congress_persons_regroup_by_dpt = congress_persons_by_dpts.regroup_from_congress_dpts(congress_departments)

        self.__assert_cantal_congress_person_department(congress_persons_regroup_by_dpt["15"])
        self.__assert_allier_congress_person_department(congress_persons_regroup_by_dpt["3"])
        self.__assert_gironde_congress_person_department(congress_persons_regroup_by_dpt["33"])

    def __assert_cantal_congress_person_department(self, congress_persons_cantal):        
        self.assertEqual(1, len(congress_persons_cantal))
        assert_candidate_with_district_and_percentage("DESCOEUR|Vincent|MASCULIN|DVD|16615|37.66|1ère circonscription|1501||15", congress_persons_cantal[0], self)       

    def __assert_allier_congress_person_department(self, congress_persons_allier):     
        self.assertEqual(3, len(congress_persons_allier))        
        assert_candidate_with_district_and_percentage("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301||3", congress_persons_allier[0], self)
        
        assert_candidate_with_district_and_percentage("RAY|Nicolas|MASCULIN|LR|21464|40.05|3ème circonscription|303||3", congress_persons_allier[1], self)

        assert_candidate_with_district_and_percentage("THES|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301||3", congress_persons_allier[2], self)

    def __assert_gironde_congress_person_department(self, congress_persons_gironde): 
        self.assertEqual(12, len(congress_persons_gironde))
        assert_candidate_with_district_and_percentage("CAZENAVE|Thomas|MASCULIN|ENS|28564|38.31|1ère circonscription|3301||33", congress_persons_gironde[0], self)

        assert_candidate_with_district_and_percentage("CHADOURNE|Sandrine|FEMININ|RN|26547|43.80|10ème circonscription|3310||33", congress_persons_gironde[1], self)

        assert_candidate_with_district_and_percentage("COUILLARD|Bérangère|FEMININ|ENS|18854|33.12|7ème circonscription|3307||33", congress_persons_gironde[2], self)

        assert_candidate_with_district_and_percentage("DAVID|Alain|MASCULIN|UG|27092|42.36|4ème circonscription|3304||33", congress_persons_gironde[3], self)

        assert_candidate_with_district_and_percentage("DE FOURNAS|Grégoire|MASCULIN|RN|35457|42.32|5ème circonscription|3305||33", congress_persons_gironde[4], self)

        assert_candidate_with_district_and_percentage("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311||33", congress_persons_gironde[5], self)

        assert_candidate_with_district_and_percentage("MARQUES|François-Xavier|MASCULIN|RN|27868|38.54|9ème circonscription|3309||33", congress_persons_gironde[6], self)

        assert_candidate_with_district_and_percentage("PANONACLE|Sophie|FEMININ|ENS|26881|31.71|8ème circonscription|3308||33", congress_persons_gironde[7], self)

        assert_candidate_with_district_and_percentage("POUILLAT|Eric|MASCULIN|ENS|25636|32.78|6ème circonscription|3306||33", congress_persons_gironde[8], self)

        assert_candidate_with_district_and_percentage("PRUD'HOMME|Loïc|MASCULIN|UG|30664|49.83|3ème circonscription|3303||33", congress_persons_gironde[9], self)

        assert_candidate_with_district_and_percentage("SAINT-PASTEUR|Sébastien|MASCULIN|UG|21913|38.50|7ème circonscription|3307||33", congress_persons_gironde[10], self)

        assert_candidate_with_district_and_percentage("THIERRY|Nicolas|MASCULIN|UG|26547|49.45|2ème circonscription|3302||33", congress_persons_gironde[11], self)