import unittest
from src.backend.domain.services.GlobalElection.CongressPersonsElectedForEachDepartment import CongressPersonsElectedForEachDepartment
from tests.utils.data.catalogData import generate_datas
 

class CongressPersonsElectedForEachDepartmentTest(unittest.TestCase):
    def test_determine_number_congress_persons_for_3_dpts(self):
        elections_results = generate_datas("results_elections", "three_departments")
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        departments = congress_persons_elected_each_department.Determinate(elections_results, 2024)        
        
        self.assertEqual(3, departments[0].number_congress_persons)
        self.assertEqual(1, departments[1].number_congress_persons)
        self.assertEqual(12, departments[2].number_congress_persons)


    def test_determine_number_congress_persons_for_gironde_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate(elections_results, '33', 2024)        
        
        self.assertEqual(12, number_congress_persons)