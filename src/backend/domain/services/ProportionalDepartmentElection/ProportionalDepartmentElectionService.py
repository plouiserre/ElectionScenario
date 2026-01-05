import copy
from src.backend.domain.ports.inside.ProportionalDepartmentElectionPort import ProportionalDepartmentElectionPort
from src.backend.domain.models.congress import Congress
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

class ProportionalDepartmentElectionService(ProportionalDepartmentElectionPort) : 
    def __init__(self, json_service, congress_persons_by_departments, manage_congress_persons_by_department):
        self.json_service = json_service
        self.congress_persons_by_departments = congress_persons_by_departments
        self.manage_congress_persons_by_department = manage_congress_persons_by_department

    def Determinate(self, year):
        elections_results = self.json_service.get_results()
        congress_persons_elected = {}
        for dept in elections_results[year].all_departments : 
            results = self.congress_persons_by_departments.Choose(elections_results, year, dept.code)
            congress_persons_elected[results.department_code] = copy.deepcopy(results.parties)
            
        all_parties = self.manage_congress_persons_by_department.group_by_parties(congress_persons_elected)
        parties = self.__ordered_all_parties(all_parties)
        
        congress = self.__construct_congress(year, "PROPORTIONALITYDEPARTMENT", "GOOD", "GOOD", parties)
        return congress
    
    def __ordered_all_parties(self, all_parties):
        parties = []
        for party_code  in all_parties:
            parties.append(all_parties[party_code])
        return parties           

    def __construct_congress(self, year, mode, stability_majority, representative_congress, parties):
        congress = Congress()
        congress.year = year
        congress.mode = mode
        congress.stability_majority = stability_majority
        congress.representative_congress = representative_congress
        congress.parties = parties
        return congress