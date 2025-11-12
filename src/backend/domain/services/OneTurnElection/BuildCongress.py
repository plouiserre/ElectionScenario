from decimal import Decimal
from src.backend.domain.models.congress import Congress

class BuildCongress : 
    def __init__(self):
       self.parties_ordered = []

    def Build(self, year, mode, parties): 
        self.__ordered_parties_by_percentage(parties)
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

    def __build_congress(self, year, mode, parties):
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        return congress