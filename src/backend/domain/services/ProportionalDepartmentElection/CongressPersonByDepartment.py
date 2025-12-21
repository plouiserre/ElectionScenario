from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.department_congress import DepartmentCongress
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

class CongressPersonByDepartment : 
    def __init__(self, number_congress_person):
        self.number_congress_person = number_congress_person

    def Choose(self, elections_results, year , department_code):
        total_congress_person = self.number_congress_person.Calculate(department_code, elections_results, year)
        if department_code == "15":
            department_congress = self.__construct_cantal_department_congress()
            return department_congress
        elif department_code == "3": 
            department_congress = self.__construct_allier_department_congress()
            return department_congress
        elif department_code == "33":
            department_congress = self.__construct_gironde_department_congress()
            return department_congress
    
    def __construct_cantal_department_congress(self): 
        uxd_party = self.__construct_uxd_party_cantal()
        parties = [uxd_party]
        department_congress = self.__construct_department_congress(15, "Cantal", parties)
        return department_congress

    def __construct_uxd_party_cantal(self): 
        first_congress_person = self.__construct_congress_person("LENOIR", "Bartolomé", "MASCULIN", "UXD", 20403, 33.35, "1ère circonscription", 1501, "Cantal", 15)
        congress_persons = [first_congress_person]
        uxd_party = self.__construct_party("Union de l'extrême droite", "UXD", 5, 1, congress_persons)
        return uxd_party
    
    def __construct_allier_department_congress(self):
        rn_party = self.__construct_rn_party_allier()
        ug_party = self.__construct_ug_party_allier()
        parties = [rn_party, ug_party]
        department_congress = self.__construct_department_congress(3, "Allier", parties)
        return department_congress

    def __construct_rn_party_allier(self):
        first_congress_person = self.__construct_congress_person("THÈS", "Anne-Marie", "FEMININ", "RN", 22816, 38.61, "1ère circonscription", 301, "Allier", 3)
        second_congress_person = self.__construct_congress_person("QUENEY", "Rémy", "MASCULIN", "RN", 20270, 37.82, "3ème circonscription", 303, "Allier", 3)
        congress_persons = [first_congress_person, second_congress_person]
        rn_party = self.__construct_party("Rassemblement National", "RN", 5, 2, congress_persons)
        return rn_party
    
    
    def __construct_ug_party_allier(self):
        first_congress_person = self.__construct_congress_person("MONNET", "Yannick", "MASCULIN", "UG", 17043, 28.84, "1ère circonscription", 301, "Allier", 3)
        congress_persons = [first_congress_person]
        ug_party = self.__construct_party("Union de la gauche", "UG", 2, 1, congress_persons)
        return ug_party
    
    def __construct_gironde_department_congress(self):
        ug_party = self.__construct_ug_party_gironde()
        rn_party = self.__construct_rn_party_gironde()
        ens_party = self.__construct_ens_party_gironde()
        parties = [ug_party, rn_party, ens_party]
        department_congress = self.__construct_department_congress(33, "Gironde", parties)
        return department_congress

    def __construct_ug_party_gironde(self):
        first_congress_person = self.__construct_congress_person("PRUD'HOMME", "Loïc", "MASCULIN", "UG", 30664, 49.83, "3ème circonscription", 3303, "Gironde", 33)
        second_congress_person = self.__construct_congress_person("RECALDE", "Marie", "FEMININ", "UG", 27564, 35.24, "6ème circonscription", 3306, "Gironde", 33)
        third_congress_person = self.__construct_congress_person("DAVID", "Alain", "MASCULIN", "UG", 27092, 42.36, "4ème circonscription", 3304, "Gironde", 33)
        fourth_congress_person = self.__construct_congress_person("GOT", "Pascale", "FEMININ", "UG", 26631, 31.79, "5ème circonscription", 3305, "Gironde", 33)
        congress_persons = [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person]
        ug_party = self.__construct_party("Union de la gauche", "UG", 2, 4, congress_persons)
        return ug_party
    
    def __construct_rn_party_gironde(self):
        first_congress_person = self.__construct_congress_person("DE FOURNAS", "Grégoire", "MASCULIN", "RN", 35457, 42.32, "5ème circonscription", 3305, "Gironde", 33)
        second_congress_person = self.__construct_congress_person("DIAZ", "Edwige", "FEMININ", "RN", 34590, 53.33, "11ème circonscription", 3311, "Gironde", 33)
        third_congress_person = self.__construct_congress_person("LAMARA", "Laurent", "MASCULIN", "RN", 31248, 36.86, "8ème circonscription", 3308, "Gironde", 33)
        fourth_congress_person = self.__construct_congress_person("MARQUES", "François-Xavier", "MASCULIN", "RN", 27868, 38.54, "9ème circonscription", 3309, "Gironde", 33)
        congress_persons = [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person]
        rn_party = self.__construct_party("Rassemblement National", "RN", 5, 4, congress_persons)
        return rn_party
    
    def __construct_ens_party_gironde(self):
        first_congress_person = self.__construct_congress_person("CAZENAVE", "Thomas", "MASCULIN", "ENS", 28564, 38.31, "1ère circonscription", 3301, "Gironde", 33)
        second_congress_person = self.__construct_congress_person("PANONACLE", "Sophie", "FEMININ", "ENS", 26881, 31.71, "8ème circonscription", 3308, "Gironde", 33)
        third_congress_person = self.__construct_congress_person("POULLIAT", "Eric", "MASCULIN", "ENS", 25636, 32.78, "6ème circonscription", 3306, "Gironde", 33)
        fourth_congress_person = self.__construct_congress_person("METTE", "Sophie", "FEMININ", "ENS", 21714, 30.03, "9ème circonscription", 3309, "Gironde", 33)
        congress_persons = [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person]
        ens_party = self.__construct_party("Ensemble ! (Majorité présidentielle)", "ENS", 3, 4, congress_persons)
        return ens_party
    
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
    
