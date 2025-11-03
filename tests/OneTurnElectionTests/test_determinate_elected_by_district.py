import unittest
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.generateDataCandidates import get_candidates_from_seventh_district_choosen

class DeterminateElectedPersonByDistrictTest(unittest.TestCase):
    def test_determinate_elected_person(self):
        candidates = get_candidates_from_seventh_district_choosen()
        determinate = DeterminateElectedPersonByDistrict()

        elected_person = determinate.Find(candidates)

        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", elected_person, self)

