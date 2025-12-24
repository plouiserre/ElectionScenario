class DistrictsVoteFromDpt():
    def __init__(self):
        pass

    def Find(self, elections_results, dpt_code, year):
        all_candidates_good_year = elections_results[year].all_candidates
        last_district = ""
        all_candidates_from_district = []
        all_candidates = []
        for all_candidates_in_districts in all_candidates_good_year: 
            for candidate in all_candidates_in_districts : 
                if candidate.district.department_code == dpt_code :
                    if last_district == "" :
                        last_district = candidate.district.code
                    if last_district == candidate.district.code : 
                        all_candidates_from_district.append(candidate)
                    else : 
                        all_candidates.append(all_candidates_from_district)
                        all_candidates_from_district = []
                        last_district = candidate.district.code
                        all_candidates_from_district.append(candidate)
                else : 
                    if len(all_candidates_from_district) > 0 : 
                        all_candidates.append(all_candidates_from_district)
                        all_candidates_from_district = []
        return all_candidates