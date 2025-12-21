import unittest
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.NumberCongressPerson import NumberCongressPerson
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas

class CongressPersonByDepartmentTest(unittest.TestCase):
    def test_choose_congress_persons_for_cantal_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = "15"
        number_congress_person = NumberCongressPerson()
        congress_persons_by_department = CongressPersonByDepartment(number_congress_person)

        department_congress = congress_persons_by_department.Choose(elections_results, 2024, department_code)

        self.assertEqual(15, department_congress.department_code)
        self.assertEqual("Cantal", department_congress.department_name)
        assert_congress_person_with_district("LENOIR|Bartolomé|MASCULIN|UXD|20403|33.35|1ère circonscription|1501|Cantal|15", department_congress.parties[0].congress_persons[0], self)        


    def test_choose_congress_persons_for_allier_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = "3"
        number_congress_person = NumberCongressPerson()
        congress_persons_by_department = CongressPersonByDepartment(number_congress_person)

        department_congress = congress_persons_by_department.Choose(elections_results, 2024, department_code)

        self.assertEqual(3, department_congress.department_code)
        self.assertEqual("Allier", department_congress.department_name)
        assert_congress_person_with_district("THÈS|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301|Allier|3", department_congress.parties[0].congress_persons[0], self)
        assert_congress_person_with_district("QUENEY|Rémy|MASCULIN|RN|20270|37.82|3ème circonscription|303|Allier|3", department_congress.parties[0].congress_persons[1], self)        
        assert_congress_person_with_district("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301|Allier|3", department_congress.parties[1].congress_persons[0], self)                          
        
    def test_choose_congress_persons_for_gironde_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = "33"
        number_congress_person = NumberCongressPerson()
        congress_persons_by_department = CongressPersonByDepartment(number_congress_person)

        department_congress = congress_persons_by_department.Choose(elections_results, 2024, department_code)

        self.assertEqual(33, department_congress.department_code)
        self.assertEqual("Gironde", department_congress.department_name)
        assert_congress_person_with_district("PRUD'HOMME|Loïc|MASCULIN|UG|30664|49.83|3ème circonscription|3303|Gironde|33", department_congress.parties[0].congress_persons[0], self)                          
        assert_congress_person_with_district("RECALDE|Marie|FEMININ|UG|27564|35.24|6ème circonscription|3306|Gironde|33", department_congress.parties[0].congress_persons[1], self)
        assert_congress_person_with_district("DAVID|Alain|MASCULIN|UG|27092|42.36|4ème circonscription|3304|Gironde|33", department_congress.parties[0].congress_persons[2], self)                          
        assert_congress_person_with_district("GOT|Pascale|FEMININ|UG|26631|31.79|5ème circonscription|3305|Gironde|33", department_congress.parties[0].congress_persons[3], self)
        assert_congress_person_with_district("DE FOURNAS|Grégoire|MASCULIN|RN|35457|42.32|5ème circonscription|3305|Gironde|33", department_congress.parties[1].congress_persons[0], self)    
        assert_congress_person_with_district("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311|Gironde|33", department_congress.parties[1].congress_persons[1], self)    
        assert_congress_person_with_district("LAMARA|Laurent|MASCULIN|RN|31248|36.86|8ème circonscription|3308|Gironde|33", department_congress.parties[1].congress_persons[2], self)    
        assert_congress_person_with_district("MARQUES|François-Xavier|MASCULIN|RN|27868|38.54|9ème circonscription|3309|Gironde|33", department_congress.parties[1].congress_persons[3], self)    
        assert_congress_person_with_district("CAZENAVE|Thomas|MASCULIN|ENS|28564|38.31|1ère circonscription|3301|Gironde|33", department_congress.parties[2].congress_persons[0], self)
        assert_congress_person_with_district("PANONACLE|Sophie|FEMININ|ENS|26881|31.71|8ème circonscription|3308|Gironde|33", department_congress.parties[2].congress_persons[1], self)
        assert_congress_person_with_district("POULLIAT|Eric|MASCULIN|ENS|25636|32.78|6ème circonscription|3306|Gironde|33", department_congress.parties[2].congress_persons[2], self)
        assert_congress_person_with_district("METTE|Sophie|FEMININ|ENS|21714|30.03|9ème circonscription|3309|Gironde|33", department_congress.parties[2].congress_persons[3], self)
        
