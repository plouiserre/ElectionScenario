from src.backend.domain.ports.inside.ProportionalDepartmentElectionPort import ProportionalDepartmentElectionPort
from src.backend.domain.models.congress import Congress
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

class ProportionalDepartmentElectionService(ProportionalDepartmentElectionPort) : 
    def __init__(self, json_service, congress_persons_by_departments, manage_congress_persons_by_department):
        self.json_service = json_service
        self.congress_persons_by_departments = congress_persons_by_departments
        self.manage_congress_persons_by_department = manage_congress_persons_by_department

    def Determinate(self, year):
        elections_results = self.json_service.get_results()
        congress_persons_elected = {}
        for dept in elections_results[year].all_departments : 
            results = self.congress_persons_by_departments.Choose(elections_results, dept.code)
            congress_persons_elected[results.department_code] = results.parties
            
        all_parties = self.manage_congress_persons_by_department.group_by_parties(congress_persons_elected)
        parties = self.__ordered_all_parties(all_parties)
        
        congress = self.__construct_congress(year, "PROPORTIONALITYDEPARTMENT", "GOOD", "GOOD", parties)
        return congress
    
    def __ordered_all_parties(self, all_parties):
        parties = []
        for party_code  in all_parties:
            parties.append(all_parties[party_code])
        return parties
    

    def __construct_rn_party(self) : 
        first_congress_person = self.__construct_congress_person("THÈS", "Anne-Marie", "FEMININ", "RN", 22816, 38.61, "1ère circonscription", 301, "Allier", 3)
        second_congress_person = self.__construct_congress_person("QUENEY", "Rémy", "MASCULIN", "RN", 20270, 37.82, "3ème circonscription", 303, "Allier", 3)
        third_congress_person = self.__construct_congress_person("DE FOURNAS", "Grégoire", "MASCULIN", "RN", 35457, 42.32, "5ème circonscription", 3305, "Gironde", 33)
        fourth_congress_person = self.__construct_congress_person("DIAZ", "Edwige", "FEMININ", "RN", 34590, 53.33, "11ème circonscription", 3311, "Gironde", 33)
        fifth_congress_person = self.__construct_congress_person("LAMARA", "Laurent", "MASCULIN", "RN", 31248, 36.86, "8ème circonscription", 3308, "Gironde", 33)
        sixth_congress_person = self.__construct_congress_person("MARQUES", "François-Xavier", "MASCULIN", "RN", 27868, 38.54, "9ème circonscription", 3309, "Gironde", 33)
        congress_persons = [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person, fifth_congress_person, 
                            sixth_congress_person]
        rn_party = self.__construct_party("RASSEMBLEMENT NATIONAL", "RN", 5, 6, congress_persons)
        return rn_party        

    def __construct_ug_party(self) : 
        first_congress_person = self.__construct_congress_person("MONNET", "Yannick", "MASCULIN", "UG", 17043, 28.84, "1ère circonscription", 301, "Allier", 3)
        second_congress_person = self.__construct_congress_person("PRUD'HOMME", "Loïc", "MASCULIN", "UG", 30664, 49.83, "3ème circonscription", 3303, "Gironde", 33)
        third_congress_person = self.__construct_congress_person("RECALDE", "Marie", "FEMININ", "UG", 27564, 35.24, "6ème circonscription", 3306, "Gironde", 33)
        fourth_congress_person = self.__construct_congress_person("DAVID", "Alain", "MASCULIN", "UG", 27092, 42.36, "4ème circonscription", 3304, "Gironde", 33)
        fifth_congress_person = self.__construct_congress_person("GOT", "Pascale", "FEMININ", "UG", 26631, 31.79, "5ème circonscription", 3305, "Gironde", 33)
        congress_persons = [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person, fifth_congress_person]
        ug_party = self.__construct_party("UNION DE LA GAUCHE", "UG", 2, 5, congress_persons)
        return ug_party
    
    def __construct_ens_party(self) : 
        first_congress_person = self.__construct_congress_person("CAZENAVE", "Thomas", "MASCULIN", "ENS", 28564, 38.31, "1ère circonscription", 3301, "Gironde", 33)
        second_congress_person = self.__construct_congress_person("PANONACLE", "Sophie", "FEMININ", "ENS", 26881, 31.71, "8ème circonscription", 3308, "Gironde", 33)
        third_congress_person = self.__construct_congress_person("POULLIAT", "Eric", "MASCULIN", "ENS", 25636, 32.78, "6ème circonscription", 3306, "Gironde", 33)
        fourth_congress_person = self.__construct_congress_person("METTE", "Sophie", "FEMININ", "ENS", 21714, 30.03, "9ème circonscription", 3309, "Gironde", 33)
        congress_persons = [first_congress_person, second_congress_person, third_congress_person, fourth_congress_person]
        ens_party = self.__construct_party("Ensemble ! (Majorité présidentielle)", "ENS", 3, 4, congress_persons)
        return ens_party
    
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
    
    def __construct_congress(self, year, mode, stability_majority, representative_congress, parties):
        congress = Congress()
        congress.year = year
        congress.mode = mode
        congress.stability_majority = stability_majority
        congress.representative_congress = representative_congress
        congress.parties = parties
        return congress