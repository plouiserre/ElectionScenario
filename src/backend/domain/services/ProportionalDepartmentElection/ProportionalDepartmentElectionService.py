import copy
from src.backend.domain.models.congress import Congress
from src.backend.domain.models.factory import  factory_congress_datas
from src.backend.domain.ports.inside.ProportionalDepartmentElectionPort import ProportionalDepartmentElectionPort


class ProportionalDepartmentElectionService(ProportionalDepartmentElectionPort) : 
    def __init__(self, json_service, congress_persons_by_departments, manage_congress_persons_by_department, build_congress, mode):
        self.json_service = json_service
        self.congress_persons_by_departments = congress_persons_by_departments
        self.manage_congress_persons_by_department = manage_congress_persons_by_department
        self.build_congress = build_congress
        self.mode = mode

    def Determinate(self, year):
        elections_results = self.json_service.get_results()
        congress_persons_elected = {}
        for dept in elections_results[2024].all_departments: 
            results = self.congress_persons_by_departments.Choose(elections_results, year, dept.code)
            congress_persons_elected[results.department_code] = copy.deepcopy(results.parties)
            
        all_parties = self.manage_congress_persons_by_department.group_by_parties(congress_persons_elected)
        parties = self.__ordered_all_parties(all_parties)
        
        
        congress_datas = factory_congress_datas(year, self.mode, parties)
        congress = self.build_congress.Build(congress_datas, elections_results)
        return congress
    
    def __ordered_all_parties(self, all_parties):
        parties = []
        for party_code  in all_parties:
            parties.append(all_parties[party_code])

        sorted_parties = sorted(parties, key = lambda x: (x.elected_congress_persons), reverse= True)
        return sorted_parties      