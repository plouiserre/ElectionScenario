from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.department_congress import DepartmentCongress
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

class CongressPersonByDepartment : 
    def __init__(self):
        pass

    def Choose(self, elections_results, department_code):
        uxd_party = self.__construct_uxd_party()
        parties = [uxd_party]
        department_congress = self.__construct_department_congress(15, "Cantal", parties)
        return department_congress

    def __construct_uxd_party(self) : 
        first_congress_person = self.__construct_congress_person("LENOIR", "Bartolomé", "MASCULIN", "UXD", 20403, 33.35, "1ère circonscription", 1501, "Cantal", 15)
        congress_persons = [first_congress_person]
        uxd_party = self.__construct_party("Union de l'extrême droite", "UXD", 5, 1, congress_persons)
        return uxd_party
    
    def __construct_congress_person(self, last_name, first_name, sexe, parti_code, vote, vote_percentage, district_name, district_code, department_name, department_code) : 
        congress_person = CongressPerson()
        congress_person.last_name = last_name
        congress_person.first_name = first_name
        congress_person.sexe = sexe
        congress_person.parti_code = parti_code
        congress_person.vote = vote
        congress_person.vote_percentage = vote_percentage
        congress_person.district = District()
        congress_person.district.code = district_code
        congress_person.district.name = district_name
        congress_person.district.department_name = department_name
        congress_person.district.department_code = department_code
        return congress_person
    
    def __construct_party(self, name, code, family, elected_congress_persons, congress_persons):
        party = Party()
        party.name = name
        party.code = code
        party.family = family
        party.elected_congress_persons = elected_congress_persons
        party.congress_persons = congress_persons
        return party
    
    def __construct_department_congress(self, department_code, department_name, parties): 
        department_congress = DepartmentCongress()
        department_congress.department_code = department_code
        department_congress.department_name = department_name
        department_congress.parties = parties
        return department_congress
    
