from src.backend.domain.models.congress import Congress

class BuildCongress : 
    def __init__(self, study_stability, study_representative, votes_results):
       self.parties_ordered = []
       self.total_congress_person = 0
       self.study_stability = study_stability
       self.study_representative = study_representative
       self.votes_results = votes_results

    # def __init__(self, study_stability):
    #    self.parties_ordered = []
    #    self.total_congress_person = 0
    #    self.study_stability = study_stability

    def Build(self, year, mode, parties): 
        self.__ordered_parties_by_percentage(parties)
        self.__count_congress_person_totality()
        congress = self.__build_congress(year, mode, self.parties_ordered)
        congress.stability_majority = self.study_stability.Calculate(congress)
        congress.representative_congress = self.study_representative.Calculate(congress, self.votes_results)
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
   
    def __build_congress(self, year, mode, parties):
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        return congress