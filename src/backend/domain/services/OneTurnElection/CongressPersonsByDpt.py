class CongressPersonsByDpt : 
    def __init__(self):
        pass
    
    def Order(self, parties_info):
        congress_persons_by_dept = {}
        
        for party in parties_info : 
            for congress_person in party.congress_persons : 
                dpt_code = str(congress_person.district.department_code)
                if (dpt_code in congress_persons_by_dept ) == False : 
                    congress_persons_by_dept[dpt_code] = [congress_person]
                else : 
                    congress_persons_by_dept[dpt_code].append(congress_person)
        return congress_persons_by_dept