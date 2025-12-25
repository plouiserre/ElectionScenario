import unittest
from unittest.mock import Mock
from src.backend.domain.services.GlobalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.GlobalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.DistrictsVoteFromDpt import DistrictsVoteFromDpt
from src.backend.domain.services.ProportionalDepartmentElection.ManageCongressPersonsByDepartment import ManageCongressPersonsByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.MinimalVoteCongressPerson import MinimalVoteCongressPerson
from src.backend.domain.services.ProportionalDepartmentElection.NumberCongressPerson import NumberCongressPerson
from src.backend.domain.services.ProportionalDepartmentElection.ProportionalDepartmentElectionService import ProportionalDepartmentElectionService
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

class ProportionalDepartmentElectionServiceTest(unittest.TestCase):
    def test_determinate_congress_with_proportional_department_election(self):
        year = 2024
        json_files = Mock()
        json_files.get_elections_data.return_value = generate_datas("results_elections", "three_departments_tmp_no_objects")        
        json_service = JsonResultsElection(json_files)
        total_congress_person = NumberCongressPerson()
        minimal_vote_congress_person = MinimalVoteCongressPerson()
        districts_vote_from_dpt = DistrictsVoteFromDpt()
        determinate_vote_by_party = DetermineVoteByParty()        
        percentage_vote_by_party = DeterminePercentageVoteByParty()
        congress_persons_by_departments = CongressPersonByDepartment(total_congress_person, minimal_vote_congress_person, districts_vote_from_dpt, 
                                                                     determinate_vote_by_party, percentage_vote_by_party)
        manage_congress_persons_by_department = ManageCongressPersonsByDepartment()        
        proportional_department_election_service = ProportionalDepartmentElectionService(json_service, congress_persons_by_departments, manage_congress_persons_by_department)        

        congress = proportional_department_election_service.Determinate(year)

        self.assertEqual(year, congress.year)
        self.assertEqual("PROPORTIONALITYDEPARTMENT", congress.mode)
        self.assertEqual("GOOD", congress.stability_majority)
        self.assertEqual("GOOD", congress.representative_congress)
        self.assertEqual(4, len(congress.parties))

        #RN 6
        assert_congress_person_with_district("THÈS|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301|Allier|3", congress.parties[0].congress_persons[0], self)
        assert_congress_person_with_district("QUENEY|Rémy|MASCULIN|RN|20270|37.82|3ème circonscription|303|Allier|3", congress.parties[0].congress_persons[1], self)        
        assert_congress_person_with_district("DE FOURNAS|Grégoire|MASCULIN|RN|35457|42.32|5ème circonscription|3305|Gironde|33", congress.parties[0].congress_persons[2], self)    
        assert_congress_person_with_district("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311|Gironde|33", congress.parties[0].congress_persons[3], self)    
        assert_congress_person_with_district("LAMARA|Laurent|MASCULIN|RN|31248|36.86|8ème circonscription|3308|Gironde|33", congress.parties[0].congress_persons[4], self)    
        assert_congress_person_with_district("MARQUES|François-Xavier|MASCULIN|RN|27868|38.54|9ème circonscription|3309|Gironde|33", congress.parties[0].congress_persons[5], self)    
        
        #UG 5
        assert_congress_person_with_district("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301|Allier|3", congress.parties[1].congress_persons[0], self)                          
        assert_congress_person_with_district("PRUD'HOMME|Loïc|MASCULIN|UG|30664|49.83|3ème circonscription|3303|Gironde|33", congress.parties[1].congress_persons[1], self)                          
        assert_congress_person_with_district("RECALDE|Marie|FEMININ|UG|27564|35.24|6ème circonscription|3306|Gironde|33", congress.parties[1].congress_persons[2], self)
        assert_congress_person_with_district("DAVID|Alain|MASCULIN|UG|27092|42.36|4ème circonscription|3304|Gironde|33", congress.parties[1].congress_persons[3], self)                          
        assert_congress_person_with_district("GOT|Pascale|FEMININ|UG|26631|31.79|5ème circonscription|3305|Gironde|33", congress.parties[1].congress_persons[4], self)
        
        #UXD 1
        assert_congress_person_with_district("LENOIR|Bartolomé|MASCULIN|UXD|20403|33.35|1ère circonscription|1501|Cantal|15", congress.parties[2].congress_persons[0], self)    
        
        #ENS 4
        assert_congress_person_with_district("CAZENAVE|Thomas|MASCULIN|ENS|28564|38.31|1ère circonscription|3301|Gironde|33", congress.parties[3].congress_persons[0], self)
        assert_congress_person_with_district("PANONACLE|Sophie|FEMININ|ENS|26881|31.71|8ème circonscription|3308|Gironde|33", congress.parties[3].congress_persons[1], self)
        assert_congress_person_with_district("POULLIAT|Eric|MASCULIN|ENS|25636|32.78|6ème circonscription|3306|Gironde|33", congress.parties[3].congress_persons[2], self)
        assert_congress_person_with_district("METTE|Sophie|FEMININ|ENS|21714|30.03|9ème circonscription|3309|Gironde|33", congress.parties[3].congress_persons[3], self)    