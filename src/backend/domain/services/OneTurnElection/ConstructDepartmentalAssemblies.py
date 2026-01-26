import copy
from src.backend.domain.models.department_congress import DepartmentCongress

class ConstructDepartmentalAssemblies : 
    def __init__(self):
        pass

    def Build(self, parties_info, parties, departments): 
        departmentals_assemblies = []
        for dpt_code in parties_info : 
            dpt_code_not_clean = dpt_code
            dpt_code_clean = self.__fix_dpt_code(dpt_code)
            dpt = self.__find_dpt(departments, dpt_code_clean)
            congress_persons = parties_info[dpt_code_not_clean]
            all_parties_completed = self.__get_all_parties_completed(congress_persons, parties)
            dpt_assembly = self.__build_department_assembly(dpt, all_parties_completed, congress_persons)
            departmentals_assemblies.append(dpt_assembly)
        return departmentals_assemblies

    #tmp
    def __fix_dpt_code(self, dpt_code): 
        if len(dpt_code) == 2 and dpt_code[0] == '0' : 
            return dpt_code[1]
        else :
            return dpt_code

    def __find_dpt(self, departments, dpt_code): 
        department = None
        for dpt in departments : 
            if dpt.code == dpt_code :
                department = dpt
                break
        return department

    def __get_all_parties_completed(self, congress_persons, parties): 
        all_parties_completed = []
        all_parties_extract = {}
        parties_updated = copy.deepcopy(parties)
        for congress_person in congress_persons : 
            for party in parties_updated : 
                if party.code == congress_person.parti_code : 
                    if (party.code in all_parties_extract) == False : 
                        all_parties_extract[party.code] = party
                    party.congress_persons.append(congress_person)
                    party.elected_congress_persons += 1
        for parti_code in all_parties_extract : 
            party = all_parties_extract[parti_code]
            all_parties_completed.append(party)
        return all_parties_completed

    def __build_department_assembly(self, department, parties, congress_persons):
        department_congress = DepartmentCongress()
        department_congress.department_code = department.code
        department_congress.department_name = department.name
        department_congress.parties = parties
        department_congress.congress_persons = congress_persons
        department_congress.number_congress_persons = len(department_congress.congress_persons)
        return department_congress