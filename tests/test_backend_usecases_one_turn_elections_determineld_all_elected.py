import unittest
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.generateData import get_candidates_from_all_districts
from src.backend.usecases.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.usecases.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict

class DeterminateAllElectedPersonsTest(unittest.TestCase):
    def test_find_all_elected_persons(self): 
        candidates = get_candidates_from_all_districts()
        determinate_by_district = DeterminateElectedPersonByDistrict()
        determinate = DeterminateAllElectedPersons(determinate_by_district)

        elected_persons = determinate.find_them_all(candidates)
    
        assert_congress_person_with_district("ALBRAND|Louis|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", elected_persons[0], self)
        assert_congress_person_with_district("BONY|Jean Yves|12383|34.29|2ème circonscription|1502|Cantal|15", elected_persons[1], self)
        assert_congress_person_with_district("VOYNET|Dominique|19160|34.16|2ème circonscription|2502|Doubs|25", elected_persons[2], self)
        assert_congress_person_with_district("LAHAIS|Tristan|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", elected_persons[3], self)
        assert_congress_person_with_district("BABIN|Elodie|18957|32.91|2ème circonscription|4502|Loiret|45", elected_persons[4], self)
        assert_congress_person_with_district("GOULET|Florence|19011|50.63|2ème circonscription|5502|Meuse|55", elected_persons[5], self)
        assert_congress_person_with_district("ROSSET|Marine|18845|33.4|2ème circonscription|7502|Paris|75", elected_persons[6], self)