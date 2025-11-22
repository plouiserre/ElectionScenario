import unittest
from src.backend.domain.services.ProportionalNationalElection.ProportionalNationalElectionService import ProportionalNationalElectionService
from src.backend.domain.services.ProportionalNationalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.ProportionalNationalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas

class ProportionalNationalElectionServiceTest(unittest.TestCase):
    def test_determinate_congress_with_proportional_election(self):
        all_candidates_data = generate_datas("candidate", "")        
        all_parties = generate_datas("party", "")
        vote_by_party_service = DetermineVoteByParty()
        percentage_vote_by_party_service = DeterminePercentageVoteByParty()
        proportional_national_election_service = ProportionalNationalElectionService(vote_by_party_service, percentage_vote_by_party_service)

        congress = proportional_national_election_service.Determinate(2024, all_candidates_data, all_parties)

        self.assertEqual(2024, congress.year)
        self.assertEqual("PROPORTIONALITYNATIONAL", congress.mode)
        self.assertEqual(3, len(congress.parties))

        assert_congress_person_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|25792|34.24|2ème circonscription|3502|Ille-et-Vilaine|35", congress.parties[0].congress_persons[0], self)
        assert_congress_person_with_district("VUILLEMIN|Benoît|MASCULIN|ENS|15026|26.79|2ème circonscription|2502|Doubs|25", congress.parties[0].congress_persons[1], self)
        
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", congress.parties[1].congress_persons[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", congress.parties[1].congress_persons[1], self)        
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", congress.parties[1].congress_persons[2], self)    

        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", congress.parties[2].congress_persons[0], self)                          
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", congress.parties[2].congress_persons[1], self)                          
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", congress.parties[2].congress_persons[2], self)
        