from decimal import Decimal
from src.backend.domain.models.congress import Congress

class BuildCongress : 
    def __init__(self):
       self.parties_ordered = []
       self.stability_majority = ''
       self.total_congress_person = 0

    def Build(self, year, mode, parties): 
        self.__ordered_parties_by_percentage(parties)
        self.__count_congress_person_totality()
        self.__defined_stability_congress_majority()
        congress = self.__build_congress(year, mode, self.parties_ordered)
        return congress
    
    def __ordered_parties_by_percentage(self, parties):
        while(len(parties) > 0):
            party_to_delete = None
            max_elected_congress_persons = 0
            for party in parties : 
                if max_elected_congress_persons < party.elected_congress_persons : 
                    max_elected_congress_persons = party.elected_congress_persons
            for party in parties : 
                if max_elected_congress_persons == party.elected_congress_persons : 
                    self.parties_ordered.append(party)
                    party_to_delete = party
                    break
            parties.remove(party_to_delete)       
    
    def __count_congress_person_totality(self): 
        for party in self.parties_ordered : 
            self.total_congress_person += party.elected_congress_persons 

    def __defined_stability_congress_majority(self):
        is_majority_party = False
        is_better_than_thirty_percent = False
        for party in self.parties_ordered:
            percentage = party.elected_congress_persons / self.total_congress_person * 100
            if percentage >= 50 :
                is_majority_party = True 
                break
            elif percentage > 30:
                is_better_than_thirty_percent = True
        if is_majority_party :
            self.stability_majority = 'HIGH' 
        elif is_better_than_thirty_percent == False:
            self.stability_majority = 'LOW'
        else :
            self.stability_majority = 'MEDIUM'


    def __build_congress(self, year, mode, parties):
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        congress.stability_majority = self.stability_majority
        return congress