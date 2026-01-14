import unittest
from src.backend.domain.services.GlobalElection.CongressPersonsElectedEachDepartment import CongressPersonsElectedEachDepartment
from tests.utils.data.catalogData import generate_datas
 

class CongressPersonsElectedEachDepartmentTest(unittest.TestCase):
    def test_determine_number_congress_persons_for_3_dpts(self):
        elections_results = generate_datas("results_elections", "three_departments")
        congress_persons_elected_each_department = CongressPersonsElectedEachDepartment()

        departments = congress_persons_elected_each_department.determinate(elections_results, 2024)        
        
        self.assertEqual(3, departments[0].number_congress_persons)
        self.assertEqual(1, departments[1].number_congress_persons)
        self.assertEqual(12, departments[2].number_congress_persons)