import unittest
from unittest.mock import Mock
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.domain.services.ProportionalNationalElection.ProportionalNationalElectionService import ProportionalNationalElectionService
from src.backend.domain.services.GlobalElection.SeatsResults import SeatsResults
from src.backend.domain.services.ProportionalNationalElection.AllocateSeatsForParties import AllocateSeatsForParties
from src.backend.domain.services.GlobalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.ProportionalNationalElection.RemoveSmallParties import RemoveSmallParties
from src.backend.domain.services.GlobalElection.CongressPersonElected import CongressPersonElected
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas

class ProportionalNationalElectionServiceTest(unittest.TestCase):
    def test_simulate_congress_with_proportional_election(self):
        total_elected_congress_persons = 8
        year = 2024
        json_files = Mock()
        json_files.get_elections_data.return_value = generate_datas("results_elections", "json_results")
        representative_congress = RepresentativeCongress(total_elected_congress_persons)
        stability_congress = StabilityCongress(total_elected_congress_persons)
        build_congress = BuildCongress(stability_congress, representative_congress)
        json_service = JsonResultsElection(json_files)

        seats_results = SeatsResults()
        remove = RemoveSmallParties()
        allocate_seats_by_parties = AllocateSeatsForParties(total_elected_congress_persons)
        congress_person_elected = CongressPersonElected()
        regroup_by_parties = RegroupCongressPersonsByParties()
        proportional_national_election_service = ProportionalNationalElectionService(json_service, seats_results, remove, allocate_seats_by_parties, 
                                                                                     congress_person_elected, regroup_by_parties, build_congress)

        congress = proportional_national_election_service.Simulate(year)

        self.assertEqual(year, congress.year)
        self.assertEqual("PROPORTIONALITYNATIONAL", congress.mode)
        self.assertEqual("QUITE", congress.stability_majority)
        self.assertEqual("GOOD", congress.representative_congress)
        self.assertEqual(3, len(congress.parties))

        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", congress.parties[0].congress_persons[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", congress.parties[0].congress_persons[1], self)        
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", congress.parties[0].congress_persons[2], self)    

        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", congress.parties[1].congress_persons[0], self)                          
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", congress.parties[1].congress_persons[1], self)                          
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", congress.parties[1].congress_persons[2], self)

        assert_congress_person_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|25792|34.24|2ème circonscription|3502|Ille-et-Vilaine|35", congress.parties[2].congress_persons[0], self)
        assert_congress_person_with_district("VUILLEMIN|Benoît|MASCULIN|ENS|15026|26.79|2ème circonscription|2502|Doubs|25", congress.parties[2].congress_persons[1], self)