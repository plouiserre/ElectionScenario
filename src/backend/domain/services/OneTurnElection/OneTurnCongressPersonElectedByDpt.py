#TODO changer noms
class OneTurnCongressPersonElectedByDpt : 
    def __init__(self):
        self.elected_persons = []
        self.elected_persons_count = 0
        self.all_congress_persons_by_dpt = {}

    def regroup(self, elected_persons):
        self.elected_persons = elected_persons
        self.__order_congress_persons_by_dpt()
        return self.all_congress_persons_by_dpt
    
    def __order_congress_persons_by_dpt(self): 
        for elected_person in self.elected_persons : 
            dpt_code = str(elected_person.district.department_code)
            if (dpt_code in self.all_congress_persons_by_dpt) == False : 
                self.all_congress_persons_by_dpt[dpt_code] = []
            self.all_congress_persons_by_dpt[dpt_code].append(elected_person)