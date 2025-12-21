import unittest
from src.backend.domain.services.ProportionalDepartmentElection.NumberCongressPerson import NumberCongressPerson
from tests.utils.data.catalogData import generate_datas

class NumberCongressPersonTest(unittest.TestCase):
    def test_number_congress_person_cantal_department(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")
        total_congress_person = NumberCongressPerson()

        congress_persons_total = total_congress_person.Calculate("15", elections_results, 2024)

        self.assertEqual(1,congress_persons_total)


    def test_number_congress_person_allier_department(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")
        total_congress_person = NumberCongressPerson()

        congress_persons_total = total_congress_person.Calculate("3", elections_results, 2024)

        self.assertEqual(3,congress_persons_total)


    def test_number_congress_person_gironde_department(self):
        elections_results  = generate_datas("results_elections", "three_departments_tmp")
        total_congress_person = NumberCongressPerson()

        congress_persons_total = total_congress_person.Calculate("33", elections_results, 2024)

        self.assertEqual(12,congress_persons_total)