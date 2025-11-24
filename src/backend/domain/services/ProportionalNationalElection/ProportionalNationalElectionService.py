from src.backend.domain.models.factory import  factory_congress, factory_congress_person, factory_district
from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort

class ProportionalNationalElectionService(ProportionalNationalElectionPort):
    def __init__(self, determinate_vote_by_party, determine_percentage_vote_by_party, remove_small_parties, 
                 determinate_seats_by_party, select_congress_person, regroup_by_parties):
        self.determinate_vote_by_party = determinate_vote_by_party
        self.determine_percentage_vote_by_party = determine_percentage_vote_by_party
        self.remove_small_parties = remove_small_parties
        self.determinate_seats_by_party = determinate_seats_by_party
        self.select_congress_person = select_congress_person
        self.regroup_by_parties = regroup_by_parties
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
        _congress_persons_elected = self.__choose_congress_persons_elected_for_parties(_number_congress_persons_elected_by_parties)
        _parties_with_congress_persons = self.__regroup_congress_persons_by_parties(_congress_persons_elected)
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
        importantes_parties_with_percentage = self.remove_small_parties.Choose(percentage_by_parties)
        return importantes_parties_with_percentage
    
    def __calculate_number_congress_persons_elected_by_parties(self, percentages_for_parties_importants):
        number_congress_persons_by_parties = self.determinate_seats_by_party.Calculate(percentages_for_parties_importants)
        return number_congress_persons_by_parties
    
    def __choose_congress_persons_elected_for_parties(self, number_congress_persons_elected_by_parties): 
        congress_persons_elected = self.select_congress_person.Choose(number_congress_persons_elected_by_parties, self.candidates_results)
        return congress_persons_elected
    
    def __regroup_congress_persons_by_parties(self, congress_persons_elected):
        parties_with_congress_persons_elected = self.regroup_by_parties.sort(congress_persons_elected, self.all_parties)
        return parties_with_congress_persons_elected
    
    def __build_congress_elected(self, year, parties) : 
        _congress = factory_congress(year, "PROPORTIONALITYNATIONAL", parties)
        return _congress