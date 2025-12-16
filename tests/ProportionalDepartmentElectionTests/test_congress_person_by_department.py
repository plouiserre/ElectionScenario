import unittest
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas

class CongressPersonByDepartmentTest(unittest.TestCase):
    def test_choose_congress_persons_for_cantal_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = 15
        congress_persons_by_department = CongressPersonByDepartment()

        department_congress = congress_persons_by_department.Choose(elections_results, department_code)

        self.assertEqual(15, department_congress.department_code)
        self.assertEqual("Cantal", department_congress.department_name)
        assert_congress_person_with_district("LENOIR|Bartolomé|MASCULIN|UXD|20403|33.35|1ère circonscription|1501|Cantal|15", department_congress.parties[0].congress_persons[0], self)        