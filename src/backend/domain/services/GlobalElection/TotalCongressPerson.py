class TotalCongressPerson:

    def __init__(self):
        pass

    def count_for_each_dpt(self, dpt_code, all_datas_elections): 
        number_congress_persons = 0
        for candidates_in_dpt in all_datas_elections.all_candidates : 
            department_code = candidates_in_dpt[0].district.department_code
            if department_code == dpt_code :
                number_congress_persons += 1            
        return number_congress_persons