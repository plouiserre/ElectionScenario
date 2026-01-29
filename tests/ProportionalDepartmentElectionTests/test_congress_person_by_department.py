import unittest
from src.backend.domain.services.GlobalElection.TotalCongressPerson import TotalCongressPerson
from src.backend.domain.services.GlobalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.GlobalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from src.backend.domain.services.GlobalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.GlobalElection.SelectCongressPerson import SelectCongressPersons
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.DeterminateSeatByPartyInDept import DeterminateSeatsByPartyInDept
from src.backend.domain.services.ProportionalDepartmentElection.DistrictsVoteFromDpt import DistrictsVoteFromDpt
from src.backend.domain.services.ProportionalDepartmentElection.ModeDesignCongressPerson import ModeDesignCongressPerson
from tests.utils.assert_helper import assert_candidate_with_district_and_percentage
from tests.utils.data.catalogData import generate_datas

class CongressPersonByDepartmentTest(unittest.TestCase):
    def test_choose_congress_persons_for_cantal_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = "15"
        mode_design_congress_person = ModeDesignCongressPerson()
        districts_vote_from_dpt = DistrictsVoteFromDpt()
        determinate_vote_by_party = DetermineVoteByParty()
        percentage_vote_by_party = DeterminePercentageVoteByParty()
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        select_congress_persons = SelectCongressPersons()
        regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
        total_congress_person = TotalCongressPerson()

        congress_persons_by_department = CongressPersonByDepartment(mode_design_congress_person, districts_vote_from_dpt, determinate_vote_by_party, 
                                                                    percentage_vote_by_party, determinate_seats_by_party_in_dept,
                                                                    select_congress_persons, regroup_congress_persons_by_parties, total_congress_person)                                                                    

        all_datas_elections = elections_results[2024]
        department_congress = congress_persons_by_department.Choose(all_datas_elections, department_code)
        
        self.assertEqual("15", department_congress.department_code)
        self.assertEqual("Cantal", department_congress.department_name)
        self.assertEqual(1, department_congress.number_congress_persons)
        assert_candidate_with_district_and_percentage("DESCOEUR|Vincent|MASCULIN|DVD|16615|37.66|1ère circonscription|1501||15", department_congress.parties[0].congress_persons[0], self)        

    def test_choose_congress_persons_for_allier_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = "3"
        mode_design_congress_person = ModeDesignCongressPerson()
        districts_vote_from_dpt = DistrictsVoteFromDpt()
        determinate_vote_by_party = DetermineVoteByParty()
        percentage_vote_by_party = DeterminePercentageVoteByParty()
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        select_congress_persons = SelectCongressPersons()
        regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
        total_congress_person = TotalCongressPerson()

        congress_persons_by_department = CongressPersonByDepartment(mode_design_congress_person, districts_vote_from_dpt, determinate_vote_by_party, 
                                                                    percentage_vote_by_party, determinate_seats_by_party_in_dept,
                                                                    select_congress_persons, regroup_congress_persons_by_parties, total_congress_person)
        all_datas_elections = elections_results[2024]
        department_congress = congress_persons_by_department.Choose(all_datas_elections, department_code)

        self.assertEqual("3", department_congress.department_code)
        self.assertEqual("Allier", department_congress.department_name)
        self.assertEqual(3, department_congress.number_congress_persons)
        assert_candidate_with_district_and_percentage("THÈS|Anne-Marie|FEMININ|RN|22816|38.61|1ère circonscription|301||3", department_congress.parties[0].congress_persons[0], self)
        assert_candidate_with_district_and_percentage("MONNET|Yannick|MASCULIN|UG|17043|28.84|1ère circonscription|301||3", department_congress.parties[1].congress_persons[0], self)                          
        assert_candidate_with_district_and_percentage("RAY|Nicolas|MASCULIN|LR|21464|40.05|3ème circonscription|303||3", department_congress.parties[2].congress_persons[0], self)                          
        
        
    def test_choose_congress_persons_for_gironde_department(self):
        elections_results = generate_datas("results_elections", "three_departments_tmp")
        department_code = "33"
        mode_design_congress_person = ModeDesignCongressPerson()
        districts_vote_from_dpt = DistrictsVoteFromDpt()
        determinate_vote_by_party = DetermineVoteByParty()
        percentage_vote_by_party = DeterminePercentageVoteByParty()
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        select_congress_persons = SelectCongressPersons()
        regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
        total_congress_person = TotalCongressPerson()

        congress_persons_by_department = CongressPersonByDepartment(mode_design_congress_person, districts_vote_from_dpt, determinate_vote_by_party, 
                                                                    percentage_vote_by_party, determinate_seats_by_party_in_dept,
                                                                    select_congress_persons, regroup_congress_persons_by_parties, total_congress_person)

        all_datas_elections = elections_results[2024]
        department_congress = congress_persons_by_department.Choose(all_datas_elections, department_code)

        self.assertEqual("33", department_congress.department_code)
        self.assertEqual("Gironde", department_congress.department_name)
        self.assertEqual(12, department_congress.number_congress_persons)
        assert_candidate_with_district_and_percentage("PRUD'HOMME|Loïc|MASCULIN|UG|30664|49.83|3ème circonscription|3303||33", department_congress.parties[0].congress_persons[0], self)                          
        assert_candidate_with_district_and_percentage("THIERRY|Nicolas|MASCULIN|UG|26547|49.45|2ème circonscription|3302||33", department_congress.parties[0].congress_persons[1], self)                          
        assert_candidate_with_district_and_percentage("DAVID|Alain|MASCULIN|UG|27092|42.36|4ème circonscription|3304||33", department_congress.parties[0].congress_persons[2], self)                          
        assert_candidate_with_district_and_percentage("SAINT-PASTEUR|Sébastien|MASCULIN|UG|21913|38.50|7ème circonscription|3307||33", department_congress.parties[0].congress_persons[3], self)
        
        assert_candidate_with_district_and_percentage("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311||33", department_congress.parties[1].congress_persons[0], self)    
        assert_candidate_with_district_and_percentage("CHADOURNE|Sandrine|FEMININ|RN|25037|43.80|10ème circonscription|3310||33", department_congress.parties[1].congress_persons[1], self)    
        assert_candidate_with_district_and_percentage("DE FOURNAS|Grégoire|MASCULIN|RN|35457|42.32|5ème circonscription|3305||33", department_congress.parties[1].congress_persons[2], self)    
        assert_candidate_with_district_and_percentage("MARQUES|François-Xavier|MASCULIN|RN|27868|38.54|9ème circonscription|3309||33", department_congress.parties[1].congress_persons[3], self)    
        
        assert_candidate_with_district_and_percentage("CAZENAVE|Thomas|MASCULIN|ENS|28564|38.31|1ère circonscription|3301||33", department_congress.parties[2].congress_persons[0], self)
        assert_candidate_with_district_and_percentage("COUILLARD|Bérangère|FEMININ|ENS|18854|33.12|7ème circonscription|3307||33", department_congress.parties[2].congress_persons[1], self)
        assert_candidate_with_district_and_percentage("POULLIAT|Eric|MASCULIN|ENS|25636|32.78|6ème circonscription|3306||33", department_congress.parties[2].congress_persons[2], self)
        assert_candidate_with_district_and_percentage("PANONACLE|Sophie|FEMININ|ENS|26881|31.71|8ème circonscription|3308||33", department_congress.parties[2].congress_persons[3], self)
        
