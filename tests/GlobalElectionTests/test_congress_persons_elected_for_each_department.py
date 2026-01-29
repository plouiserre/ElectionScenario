import unittest
from src.backend.domain.services.GlobalElection.CongressPersonsElectedForEachDepartment import CongressPersonsElectedForEachDepartment
from tests.utils.data.catalogData import generate_datas
 

class CongressPersonsElectedForEachDepartmentTest(unittest.TestCase):
    def test_determine_number_congress_persons_for_allier_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        all_datas_elections = elections_results[2024]
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate('3', all_datas_elections)        
        
        self.assertEqual(3, number_congress_persons)

    def test_determine_number_congress_persons_for_cantal_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        all_datas_elections = elections_results[2024]
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate('23', all_datas_elections)        
        
        self.assertEqual(1, number_congress_persons)


    def test_determine_number_congress_persons_for_gironde_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        all_datas_elections = elections_results[2024]
        congress_persons_elected_each_department = CongressPersonsElectedForEachDepartment()

        number_congress_persons = congress_persons_elected_each_department.Determinate('33', all_datas_elections)        
        
        self.assertEqual(12, number_congress_persons)