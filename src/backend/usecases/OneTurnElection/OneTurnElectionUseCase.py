from src.backend.domain.models.factory import factory_congress, factory_congress_person, factory_district, factory_party

class OneTurnElectionUseCase : 
    def __init__(self):
        pass

    def Determinate(self):
        parties = self.__build_parties()
        congress = factory_congress(2024, "OneTurn", parties)
        return congress
    
    
    def __build_parties(self):
        parties = [self.__build_rn_party(), self.__build_lr_party(), self.__build_ens_party(), 
                   self.__build_ug_party(), self.__build_uxd_party()]
        return parties

    def __build_rn_party(self): 
        congress_persons = [self._build_first_congress_person_rn(), self._build_second_congress_person_rn(), 
        self._build_fourth_congress_person_rn(), self._build_seventh_congress_person_rn(), 
        self.__build_nineth_candidate_rn()]
        rn_party = factory_party("Rassemblement National", "RN", 50.0, congress_persons)
        return rn_party
    
    def _build_first_congress_person_rn(self):
        first_district = factory_district("2ème circonscription", 302, "Allier", 3)
        first_congress_man = factory_congress_person("BOVET", "Jorys", "MASCULIN", "RN", 17810, 34.33, first_district )
        return first_congress_man

    def _build_second_congress_person_rn(self):
        second_district = factory_district("15ème circonscription", 1315, "Bouches-du-Rhône", 13)
        second_congress_man = factory_congress_person("BAUBRY", "Romain", "MASCULIN", "RN", 37493, 49.48, second_district)
        return second_congress_man
    
    def _build_fourth_congress_person_rn(self):
        fourth_district = factory_district("11ème circonscription", 3311, "Gironde", 33)
        fourth_congress_woman = factory_congress_person("DIAZ", "Edwige", "FEMININ", "RN", 34590, 53.33, fourth_district)
        return fourth_congress_woman    

    def _build_seventh_congress_person_rn(self):
        seventh_district = factory_district("4ème circonscription", 6304, "Puy-de-Dôme", 63)
        seventh_congress_man = factory_congress_person("CHALUS", "BENJAMIN", "MASCULIN", "RN", 22290, 31.62, seventh_district)
        return seventh_congress_man
    
    def __build_nineth_candidate_rn(self):
        nineth_district = factory_district("7ème circonscription", 8307, "Var", 83)
        nineth_congress_man = factory_congress_person("BOCCALETTI", "Frédéric", "MASCULIN", "RN", 32748, 48.3, nineth_district)
        return nineth_congress_man

    def __build_lr_party(self):
        congress_persons = [self.__build_fifth_candidate_lr(), self.__build_eighth_candidate_lr()]
        lr_party = factory_party("Les Républicains", "LR", 20.0, congress_persons)
        return lr_party
    
    def __build_fifth_candidate_lr(self):
        fifth_district = factory_district("1ère circonscription", 4301, "Haute Loire", 43)
        fifth_congress_man = factory_congress_person("WAUQUIEZ", "Laurent", "MASCULIN", "LR", 27013, 36.80, fifth_district)
        return fifth_congress_man    

    def __build_eighth_candidate_lr(self):
        eighth_district = factory_district("3ème circonscription", 7304, "Savoie", 73)
        eighth_congress_woman = factory_congress_person("BONNIVARD", "Emilie", "FEMININ", "LR", 21605, 40.86, eighth_district)
        return eighth_congress_woman        
    
    def __build_ens_party(self): 
        congress_persons = [self.__build_sixth_candidate_ens()]
        ens_party = factory_party("Ensemble ! (Majorité présidentielle)", "ENS", 10.0, congress_persons)
        return ens_party
    
    def __build_sixth_candidate_ens(self):
        sixth_district = factory_district("2ème circonscription", 5302, "Mayenne", 53)
        sixth_congress_woman = factory_congress_person("BANNIER", "Géraldine", "FEMININ", "ENS", 18746, 35.17, sixth_district)
        return sixth_congress_woman    
    
    def __build_ug_party(self):
        congress_persons = [self.__build_tenth_candidate_ug()]
        ug_party = factory_party("Union de la gauche", "UG", 10.0, congress_persons)
        return ug_party   
        
    def __build_tenth_candidate_ug(self):
        tenth_district = factory_district("11ème circonscription", 9311, "Seine-Saint-Denis", 93)
        tenth_congress_woman = factory_congress_person("AUTIN", "Clémentine", "FEMININ", "UG", 22209, 62.65, tenth_district)
        return tenth_congress_woman
    
    def __build_uxd_party(self):
        congress_persons = [self.__build_third_congress_person_uxd()]
        uxd_party = factory_party("Union de l\'extrême droite", "UXD", 10.0, congress_persons)
        return uxd_party

    def __build_third_congress_person_uxd(self):
        third_district = factory_district("1ère circonscription", 2301, "Creuse", 23)
        third_congress_man = factory_congress_person("LENOIR", "Bartolomé", "MASCULIN", "UXD", 20403, 33.35, third_district)
        return third_congress_man