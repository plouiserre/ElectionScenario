import copy
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
        all_datas_elections = elections_results[year]
        congress_persons_elected = {}
        departmental_assemblies = []
        for dept in all_datas_elections.all_departments: 
            departmental_assembly = self.congress_persons_by_departments.find_congress_persons(all_datas_elections, dept.code)
            departmental_assembly_unique = copy.deepcopy(departmental_assembly)
            departmental_assemblies.append(departmental_assembly_unique)
            congress_persons_elected[departmental_assembly_unique.department_code] = copy.deepcopy(departmental_assembly_unique.parties)
            
        all_parties = self.manage_congress_persons_by_department.group_by_parties(congress_persons_elected)
        parties = self.__ordered_all_parties(all_parties)
        
        all_departmental_assemblies = self.__regroup_all_departmental_assemblies(departmental_assemblies)

        congress_datas = factory_congress_datas(year, self.mode, parties, all_departmental_assemblies)
        congress = self.build_congress.Build(congress_datas, elections_results)
        return congress
    
    def __ordered_all_parties(self, all_parties):
        parties = []
        for party_code  in all_parties:
            parties.append(all_parties[party_code])

        sorted_parties = sorted(parties, key = lambda x: (x.elected_congress_persons), reverse= True)
        return sorted_parties
    
    def __regroup_all_departmental_assemblies(self, departmental_assemblies): 
        all_departmental_assemblies = []
        for departmental_assembly in departmental_assemblies :
            departmental_assembly_updated = departmental_assembly
            for party in departmental_assembly.parties : 
                for congress_person in party.congress_persons : 
                    departmental_assembly_updated.congress_persons.append(congress_person)
            all_departmental_assemblies.append(departmental_assembly_updated)
        return all_departmental_assemblies