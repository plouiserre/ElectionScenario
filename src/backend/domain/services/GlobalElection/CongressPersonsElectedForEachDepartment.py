class CongressPersonsElectedForEachDepartment:

    def __init__(self):
        pass

    def Determinate(self, elections_results, year):
        number_elected_persons_by_dept = {}
        depts_completed = []
        election = elections_results[year]
        for candidates_in_dpt in election.all_candidates : 
            department_code = candidates_in_dpt[0].district.department_code
            if department_code in number_elected_persons_by_dept :
                number_elected_persons_by_dept[department_code] += 1
            else :
                number_elected_persons_by_dept[department_code] = 1
        for departement in elections_results[year].all_departments : 
            if departement.code in number_elected_persons_by_dept : 
                departement.number_congress_persons = number_elected_persons_by_dept[departement.code]
                depts_completed.append(departement)
        return depts_completed