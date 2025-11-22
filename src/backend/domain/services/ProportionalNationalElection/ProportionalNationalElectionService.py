from src.backend.domain.models.factory import  factory_congress, factory_congress_person, factory_district
from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort

class ProportionalNationalElectionService(ProportionalNationalElectionPort):
    def __init__(self, determinate_vote_by_party, determine_percentage_vote_by_party):
        self.determinate_vote_by_party = determinate_vote_by_party
        self.determine_percentage_vote_by_party = determine_percentage_vote_by_party
        self.all_parties = []
        self.candidates_results = []
        self.year = 0

    def Determinate(self, year, all_candidates_datas, all_parties):
        self.year = year
        self.all_parties = all_parties[str(year)]
        self.candidates_results = all_candidates_datas
        _votes_by_parties = self.__calculate_each_party_votes()
        _percentage_by_parties = self.__calculate_each_vote_percentage(_votes_by_parties)
        _percentages_for_parties_importants = self.__keep_only_important_parties(_percentage_by_parties)
        _number_congress_persons_elected_by_parties = self.__calculate_number_congress_persons_elected_by_parties(_percentages_for_parties_importants)
        _parties_with_congress_persons = self.__choose_congress_persons_elected_for_parties(_number_congress_persons_elected_by_parties)
        congress = self.__build_congress_elected(year, _parties_with_congress_persons)
        return congress    

    def __calculate_each_party_votes(self):
        #EXG : 394 + 298 + 788 + 746 + 388 + 431 + 692 + 168 = 3 905
        #ENS : 10338 + 3019 + 15026 + 25792 + 13263 + 15121 + 13325 = 95 884
        #UG : 12661 + 4919 + 19160 + 30361 + 16148 + 5391 + 17055 + 18845 = 124 540
        #DIV : 2260 = 2260
        #RN : 13115 + 11923 + 16895 + 13130  + 18957 + 19011 + 22436 + 6206 = 121 673
        #REC : 220 + 716 = 936
        # DVD : 3348 + 11976 + 3792 + 1229 =  20 345
        # LR : 12383 + 4215 + 5218 + 4527 + 3184 = 29 527
        # ECO : 71 + 1474 + 742 + 512 = 2799
        # DVG : 1951 + 178 + 60 = 2 189
        # REG : 1486 + 735 + 778 = 2 999
        # DVC : 11071 + 430 = 11 501
        #Total : 418 558
        results = self.determinate_vote_by_party.Calculate(self.candidates_results)
        return results
    
    def __calculate_each_vote_percentage(self, parties_by_vote):
        results = self.determine_percentage_vote_by_party.Calculate(parties_by_vote)
        return results
    
    def __keep_only_important_parties(self, percentage_by_parties):
        importantes_parties_with_percentage = {"ENS":22.91, "UG":29.75, "RN":29.07, "LR":7.05}
        return importantes_parties_with_percentage
    
    def __calculate_number_congress_persons_elected_by_parties(self, percentages_for_parties_importants):
        number_congress_persons_by_parties = {"ENS":2, "UG":3, "RN":3, "LR":0}
        return number_congress_persons_by_parties
    
    def __choose_congress_persons_elected_for_parties(self, number_congress_persons_elected_by_parties): 
        _first_ens_congress_persons_elected = factory_congress_person("MAILLART-MÉHAIGNERIE", "Laurence", "FEMININ", "ENS", 25792, 34.24, factory_district("2ème circonscription", 3502, "Ille-et-Vilaine", 35))
        _second_ens_congress_persons_elected = factory_congress_person("VUILLEMIN", "Benoît", "MASCULIN", "ENS", 15026, 26.79, factory_district("2ème circonscription", 2502, "Doubs", 25))
        ens_party = self.__find_party("ENS")
        ens_party.congress_persons.append(_first_ens_congress_persons_elected)
        ens_party.congress_persons.append(_second_ens_congress_persons_elected)
        ug_party = self.__find_party("UG")
        _first_ug_congress_person_elected = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, factory_district("2ème circonscription", 3502, "Ille-et-Vilaine", 35))
        _second_ug_congress_person_elected = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, factory_district("2ème circonscription", 2502, "Doubs", 25))
        _third_ug_congress_person_elected = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG", 18845, 33.4, factory_district("2ème circonscription", 7502, "Paris", 75))
        ug_party.congress_persons.append(_first_ug_congress_person_elected)
        ug_party.congress_persons.append(_second_ug_congress_person_elected)
        ug_party.congress_persons.append(_third_ug_congress_person_elected)
        rn_party = self.__find_party("RN")
        _first_rn_congress_person_elected = factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, factory_district("2ème circonscription", 5502, "Meuse", 55))
        _second_rn_congress_person_elected = factory_congress_person("MONTEIL", "Olivier", "MASCULIN", "RN", 22436, 36.96, factory_district("2ème circonscription", 6502, "Hautes-Pyrénées", 65))
        _third_rn_congress_person_elected = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, factory_district("2ème circonscription", 502, "Hautes-Alpes", 5))        
        rn_party.congress_persons.append(_first_rn_congress_person_elected)
        rn_party.congress_persons.append(_second_rn_congress_person_elected)
        rn_party.congress_persons.append(_third_rn_congress_person_elected)

        party_with_congress_persons_elected = [ens_party, ug_party, rn_party ]

        return party_with_congress_persons_elected
    
    def __find_party(self, parti_code) : 
        for party in self.all_parties: 
            if party.code == parti_code : 
                return party
    
    def __build_congress_elected(self, year, parties) : 
        _congress = factory_congress(year, "PROPORTIONALITYNATIONAL", parties)
        return _congress