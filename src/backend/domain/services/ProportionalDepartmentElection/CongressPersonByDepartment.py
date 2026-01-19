from src.backend.domain.models.department_congress import DepartmentCongress

class CongressPersonByDepartment :          
    def __init__(self, number_congress_person, minimal_vote_congress_person, districts_vote_from_dpt, determinate_vote_by_party, 
                 determine_percentage_vote_by_party, determinate_seats_by_party_in_dept, select_congress_persons, regroup_congress_persons_by_parties, 
                 congress_persons_elected_for_each_department):
        self.number_congress_person = number_congress_person
        self.minimal_vote_congress_person = minimal_vote_congress_person
        self.districts_vote_from_dpt = districts_vote_from_dpt
        self.determinate_vote_by_party = determinate_vote_by_party
        self.determine_percentage_vote_by_party = determine_percentage_vote_by_party
        self.determinate_seats_by_party_in_dept = determinate_seats_by_party_in_dept
        self.select_congress_persons = select_congress_persons
        self.regroup_congress_persons_by_parties = regroup_congress_persons_by_parties
        self.congress_persons_elected_for_each_department = congress_persons_elected_for_each_department

    def Choose(self, elections_results, year , department_code):
        total_congress_person = self.number_congress_person.Calculate(department_code, elections_results, year)
        all_votes_from_dpt = self.districts_vote_from_dpt.Find(elections_results, department_code, year)
        all_candidates_from_districts = self.__regroup_all_candidates_from_districts(all_votes_from_dpt)
        parties_by_vote = self.determinate_vote_by_party.Calculate(all_candidates_from_districts)
        all_percentage_vote_by_party = self.determine_percentage_vote_by_party.Calculate(parties_by_vote)
        mode_design = self.minimal_vote_congress_person.Calculate(total_congress_person, all_percentage_vote_by_party)
        parties_seats_by_dept = self.determinate_seats_by_party_in_dept.Determinate(all_percentage_vote_by_party, mode_design, total_congress_person)
        congress_persons_elected = self.select_congress_persons.Choose(parties_seats_by_dept, all_candidates_from_districts)
        all_parties = self.regroup_congress_persons_by_parties.sort(congress_persons_elected, elections_results[year].all_parties)
        department_name = self.__find_department_name(elections_results[year].all_departments, department_code)
        number_congress_persons = self.congress_persons_elected_for_each_department.Determinate(elections_results, department_code, year)
        congress_departmental = self.__construct_department_congress(department_code, department_name, all_parties, number_congress_persons)
        return congress_departmental       
        
    def __regroup_all_candidates_from_districts(self, all_votes_from_dpt): 
        candidates = []
        for candidates_district in all_votes_from_dpt:
            for candidate in candidates_district : 
                candidates.append(candidate)
        return candidates          
    
    def __find_department_name(self, all_departments, department_code):
        department_name = ''
        for dept in all_departments : 
            if dept.code == department_code : 
                department_name = dept.name
        return department_name
    
    def __construct_department_congress(self, department_code, department_name, parties, number_congress_persons): 
        department_congress = DepartmentCongress()
        department_congress.department_code = department_code
        department_congress.department_name = department_name
        department_congress.parties = parties
        department_congress.number_congress_persons = number_congress_persons
        return department_congress
    
