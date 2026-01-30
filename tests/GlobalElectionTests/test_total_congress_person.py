import unittest
from src.backend.domain.services.GlobalElection.TotalCongressPerson import TotalCongressPerson
from tests.utils.data.catalogData import generate_datas
 

class CongressPersonsElectedForEachDepartmentTest(unittest.TestCase):
    def test_determine_number_congress_persons_for_allier_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        all_datas_elections = elections_results[2024]
        total_congress_person = TotalCongressPerson()

        number_congress_persons = total_congress_person.count_for_each_dpt('3', all_datas_elections)        
        
        self.assertEqual(3, number_congress_persons)

    def test_determine_number_congress_persons_for_cantal_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        all_datas_elections = elections_results[2024]
        total_congress_person = TotalCongressPerson()

        number_congress_persons = total_congress_person.count_for_each_dpt('23', all_datas_elections)        
        
        self.assertEqual(1, number_congress_persons)


    def test_determine_number_congress_persons_for_gironde_dpt(self):
        elections_results = generate_datas("results_elections", "three_departments")
        all_datas_elections = elections_results[2024]
        total_congress_person = TotalCongressPerson()

        number_congress_persons = total_congress_person.count_for_each_dpt('33', all_datas_elections)        
        
        self.assertEqual(12, number_congress_persons)