class CongressPersonsByDepartments : 
    def __init__(self):
        pass

    def regroup_from_congress_dpts(self, departments_congress, departments):
        congress_persons_by_dpts = {}
        for dept in departments : 
            congress_persons = self.__search_congress_persons_for_this_dpt(departments_congress, dept.code)
            congress_persons_sorted = sorted(congress_persons, key=lambda x: x.last_name)
            congress_persons_by_dpts[dept.code] = congress_persons_sorted
        return congress_persons_by_dpts
    
    def __search_congress_persons_for_this_dpt(self, departments_congress, dpt_code):
        congress_persons = []
        for department_congress in departments_congress : 
            if str(department_congress.department_code ) == dpt_code : 
                for party in department_congress.parties : 
                    for congress_person in party.congress_persons : 
                        congress_persons.append(congress_person)
        return congress_persons