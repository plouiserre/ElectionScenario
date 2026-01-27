class NumberCongressPerson : 
    def __init__(self):
        pass

    def Calculate(self, department_code, all_datas_elections):        
        self.all_datas_elections = all_datas_elections
        self.department_code = department_code
        total_congress_man = self.__get_number_districts()
        return total_congress_man
        
    def __get_number_districts(self) : 
        districts_from_department = []
        candidates_from_district = self.all_datas_elections.all_candidates
        for candidates in candidates_from_district : 
            first_candidate = candidates[0]
            if first_candidate.district.department_code == self.department_code :
                districts_from_department.append(first_candidate.district)
        numbers_districts = len(districts_from_department)
        return numbers_districts