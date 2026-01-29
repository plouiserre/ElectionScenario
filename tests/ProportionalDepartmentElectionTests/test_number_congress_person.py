import unittest
from src.backend.domain.services.ProportionalDepartmentElection.NumberCongressPerson import NumberCongressPerson
from tests.utils.data.catalogData import generate_datas

class NumberCongressPersonTest(unittest.TestCase):
    def test_number_congress_person_cantal_department(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")
        all_datas_elections = elections_results[2024]
        total_congress_person = NumberCongressPerson()

        congress_persons_total = total_congress_person.Calculate("15", all_datas_elections)

        self.assertEqual(1,congress_persons_total)


    def test_number_congress_person_allier_department(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")
        all_datas_elections = elections_results[2024]
        total_congress_person = NumberCongressPerson()

        congress_persons_total = total_congress_person.Calculate("3", all_datas_elections)

        self.assertEqual(3,congress_persons_total)


    def test_number_congress_person_gironde_department(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")
        all_datas_elections = elections_results[2024]
        total_congress_person = NumberCongressPerson()

        congress_persons_total = total_congress_person.Calculate("33", all_datas_elections)

        self.assertEqual(12,congress_persons_total)