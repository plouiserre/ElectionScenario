import unittest
from src.backend.domain.services.GlobalElection.CongressPersonsElectedForEachDepartment import CongressPersonsElectedForEachDepartment
from tests.utils.data.catalogData import generate_datas
 

class CongressPersonsElectedForEachDepartmentTest(unittest.TestCase):
    def test_determine_number_congress_persons_for_allier_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate(elections_results, '3', 2024)        
        
        self.assertEqual(3, number_congress_persons)

    def test_determine_number_congress_persons_for_cantal_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate(elections_results, '23', 2024)        
        
        self.assertEqual(1, number_congress_persons)


    def test_determine_number_congress_persons_for_gironde_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate(elections_results, '33', 2024)        
        
        self.assertEqual(12, number_congress_persons)