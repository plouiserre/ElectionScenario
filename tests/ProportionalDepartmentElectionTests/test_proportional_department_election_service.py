import unittest
from unittest.mock import Mock
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.domain.services.GlobalElection.TotalCongressPerson import TotalCongressPerson
from src.backend.domain.services.GlobalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.GlobalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from src.backend.domain.services.GlobalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.SelectCongressPerson import SelectCongressPersons
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.DeterminateSeatByPartyInDept import DeterminateSeatsByPartyInDept
from src.backend.domain.services.ProportionalDepartmentElection.DistrictsVoteFromDpt import DistrictsVoteFromDpt
from src.backend.domain.services.ProportionalDepartmentElection.ManageCongressPersonsByDepartment import ManageCongressPersonsByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.ModeDesignCongressPerson import ModeDesignCongressPerson
# from src.backend.domain.services.ProportionalDepartmentElection.NumberCongressPerson import NumberCongressPerson
from src.backend.domain.services.ProportionalDepartmentElection.ProportionalDepartmentElectionService import ProportionalDepartmentElectionService
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

class ProportionalDepartmentElectionServiceTest(unittest.TestCase):
    def test_determinate_congress_with_proportional_department_election(self):
        total_congress_persons_in_dpt = 16
        year = 2024
        mode = "proportionalDepartmental"
        json_files = Mock()
        json_files.get_elections_data.return_value = generate_datas("results_elections", "three_departments_tmp_no_objects")        
        json_service = JsonResultsElection(json_files)
        # number_congress_person = NumberCongressPerson()
        mode_design_congress_person = ModeDesignCongressPerson()
        districts_vote_from_dpt = DistrictsVoteFromDpt()
        determinate_vote_by_party = DetermineVoteByParty()        
        percentage_vote_by_party = DeterminePercentageVoteByParty()        
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        select_congress_persons = SelectCongressPersons()
        regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
        total_congress_person = TotalCongressPerson()
        

        congress_persons_by_departments = CongressPersonByDepartment(mode_design_congress_person, districts_vote_from_dpt, 
                                                                    determinate_vote_by_party, percentage_vote_by_party, determinate_seats_by_party_in_dept,
                                                                    select_congress_persons, regroup_congress_persons_by_parties, total_congress_person)
        manage_congress_persons_by_department = ManageCongressPersonsByDepartment()        
        stability_congress = StabilityCongress(total_congress_persons_in_dpt)
        representative_congress = RepresentativeCongress(total_congress_persons_in_dpt)
        build_congress = BuildCongress(stability_congress, representative_congress)
        proportional_department_election_service = ProportionalDepartmentElectionService(json_service, congress_persons_by_departments, manage_congress_persons_by_department, 
                                                                                         build_congress, mode)        

        congress = proportional_department_election_service.Determinate(year)

        self.assertEqual(year, congress.year)
        self.assertEqual("proportionalDepartmental", congress.mode)
        self.assertEqual("QUITE", congress.stability_majority)
        self.assertEqual("PERFECT", congress.representative_congress)
        self.assertEqual(5, len(congress.parties))            
        
        self.__assert_congress_persons_by_parties(congress)
        self.__assert_congress_persons_by_department(congress)


    def __assert_congress_persons_by_parties(self, congress) : 
        #RN 5
        assert_congress_person_with_district("THÈS|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301|Allier|3", congress.parties[0].congress_persons[0], self)
        assert_congress_person_with_district("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311|Gironde|33", congress.parties[0].congress_persons[1], self)    
        assert_congress_person_with_district("CHADOURNE|Sandrine|FEMININ|RN|25037|43.80|10ème circonscription|3310|Gironde|33", congress.parties[0].congress_persons[2], self)    
        assert_congress_person_with_district("DE FOURNAS|Grégoire|MASCULIN|RN|35457|42.32|5ème circonscription|3305|Gironde|33", congress.parties[0].congress_persons[3], self)    
        assert_congress_person_with_district("MARQUES|François-Xavier|MASCULIN|RN|27868|38.54|9ème circonscription|3309|Gironde|33", congress.parties[0].congress_persons[4], self)
        
        #UG 5
        assert_congress_person_with_district("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301|Allier|3", congress.parties[1].congress_persons[0], self)                          
        assert_congress_person_with_district("PRUD'HOMME|Loïc|MASCULIN|UG|30664|49.83|3ème circonscription|3303|Gironde|33", congress.parties[1].congress_persons[1], self)                          
        assert_congress_person_with_district("THIERRY|Nicolas|MASCULIN|UG|26547|49.45|2ème circonscription|3302|Gironde|33", congress.parties[1].congress_persons[2], self)                          
        assert_congress_person_with_district("DAVID|Alain|MASCULIN|UG|27092|42.36|4ème circonscription|3304|Gironde|33", congress.parties[1].congress_persons[3], self)                          
        assert_congress_person_with_district("SAINT-PASTEUR|Sébastien|MASCULIN|UG|21913|38.50|7ème circonscription|3307|Gironde|33", congress.parties[1].congress_persons[4], self)

        #ENS 4
        assert_congress_person_with_district("CAZENAVE|Thomas|MASCULIN|ENS|28564|38.31|1ère circonscription|3301|Gironde|33", congress.parties[2].congress_persons[0], self)
        assert_congress_person_with_district("COUILLARD|Bérangère|FEMININ|ENS|18854|33.12|7ème circonscription|3307|Gironde|33", congress.parties[2].congress_persons[1], self)
        assert_congress_person_with_district("POULLIAT|Eric|MASCULIN|ENS|25636|32.78|6ème circonscription|3306|Gironde|33", congress.parties[2].congress_persons[2], self)
        assert_congress_person_with_district("PANONACLE|Sophie|FEMININ|ENS|26881|31.71|8ème circonscription|3308|Gironde|33", congress.parties[2].congress_persons[3], self)
        
        #LR 1
        assert_congress_person_with_district("RAY|Nicolas|MASCULIN|LR|21464|40.05|3ème circonscription|303|Allier|3", congress.parties[3].congress_persons[0], self)

        #DVD 1
        assert_congress_person_with_district("DESCOEUR|Vincent|MASCULIN|DVD|16615|37.66|1ère circonscription|1501|Cantal|15", congress.parties[4].congress_persons[0], self)


    def __assert_congress_persons_by_department(self, congress):   
        assert_congress_person_with_district("THÈS|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301|Allier|3", congress.departmental_assemblies[0].congress_persons[0], self)     
        assert_congress_person_with_district("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301|Allier|3", congress.departmental_assemblies[0].congress_persons[1], self)        
        assert_congress_person_with_district("RAY|Nicolas|MASCULIN|LR|21464|40.05|3ème circonscription|303|Allier|3", congress.departmental_assemblies[0].congress_persons[2], self)

        assert_congress_person_with_district("DESCOEUR|Vincent|MASCULIN|DVD|16615|37.66|1ère circonscription|1501|Cantal|15", congress.departmental_assemblies[1].congress_persons[0], self)

        assert_congress_person_with_district("PRUD'HOMME|Loïc|MASCULIN|UG|30664|49.83|3ème circonscription|3303|Gironde|33", congress.departmental_assemblies[2].congress_persons[0], self)
        assert_congress_person_with_district("THIERRY|Nicolas|MASCULIN|UG|26547|49.45|2ème circonscription|3302|Gironde|33", congress.departmental_assemblies[2].congress_persons[1], self)
        assert_congress_person_with_district("DAVID|Alain|MASCULIN|UG|27092|42.36|4ème circonscription|3304|Gironde|33", congress.departmental_assemblies[2].congress_persons[2], self)
        assert_congress_person_with_district("SAINT-PASTEUR|Sébastien|MASCULIN|UG|21913|38.50|7ème circonscription|3307|Gironde|33", congress.departmental_assemblies[2].congress_persons[3], self)
        assert_congress_person_with_district("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311|Gironde|33", congress.departmental_assemblies[2].congress_persons[4], self)
        assert_congress_person_with_district("CHADOURNE|Sandrine|FEMININ|RN|25037|43.80|10ème circonscription|3310|Gironde|33", congress.departmental_assemblies[2].congress_persons[5], self)
        assert_congress_person_with_district("DE FOURNAS|Grégoire|MASCULIN|RN|35457|42.32|5ème circonscription|3305|Gironde|33", congress.departmental_assemblies[2].congress_persons[6], self)
        assert_congress_person_with_district("MARQUES|François-Xavier|MASCULIN|RN|27868|38.54|9ème circonscription|3309|Gironde|33", congress.departmental_assemblies[2].congress_persons[7], self)
        assert_congress_person_with_district("CAZENAVE|Thomas|MASCULIN|ENS|28564|38.31|1ère circonscription|3301|Gironde|33", congress.departmental_assemblies[2].congress_persons[8], self)
        assert_congress_person_with_district("COUILLARD|Bérangère|FEMININ|ENS|18854|33.12|7ème circonscription|3307|Gironde|33", congress.departmental_assemblies[2].congress_persons[9], self)
        assert_congress_person_with_district("POULLIAT|Eric|MASCULIN|ENS|25636|32.78|6ème circonscription|3306|Gironde|33", congress.departmental_assemblies[2].congress_persons[10], self)
        assert_congress_person_with_district("PANONACLE|Sophie|FEMININ|ENS|26881|31.71|8ème circonscription|3308|Gironde|33", congress.departmental_assemblies[2].congress_persons[11], self)
        