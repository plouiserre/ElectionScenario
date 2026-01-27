class CongressPersonsElectedForEachDepartment:

    def __init__(self):
        pass

    #TODO à supprimer!!!!!!!!!!!!!
    def DeterminateAllDepartments(self, all_datas_elections):
        number_elected_persons_by_dept = {}
        depts_completed = []
        for candidates_in_dpt in all_datas_elections.all_candidates : 
            department_code = candidates_in_dpt[0].district.department_code
            if department_code in number_elected_persons_by_dept :
                number_elected_persons_by_dept[department_code] += 1
            else :
                number_elected_persons_by_dept[department_code] = 1
        for departement in all_datas_elections.all_departments : 
            if departement.code in number_elected_persons_by_dept : 
                departement.number_congress_persons = number_elected_persons_by_dept[departement.code]
                depts_completed.append(departement)
        return depts_completed
    

    def Determinate(self, dpt_code, all_datas_elections): 
        number_congress_persons = 0
        for candidates_in_dpt in all_datas_elections.all_candidates : 
            department_code = candidates_in_dpt[0].district.department_code
            if department_code == dpt_code :
                number_congress_persons += 1            
        return number_congress_persons