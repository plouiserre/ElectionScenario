
class DeterminateAllElectedPersons : 
    def __init__(self, determinate_elected_person_by_district):
        self.determinate_elected_person_by_district = determinate_elected_person_by_district

    def find_them_all(self, candidates_by_district):
        all_elected_persons = []
        for candidates in candidates_by_district:
            elected_person = self.determinate_elected_person_by_district.Find(candidates)
            all_elected_persons.append(elected_person)
        return all_elected_persons