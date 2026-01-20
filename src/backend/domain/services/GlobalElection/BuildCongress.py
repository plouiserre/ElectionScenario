from src.backend.domain.models.congress import Congress

class BuildCongress : 
    def __init__(self, study_stability, study_representative):
       self.parties_ordered = []
       self.total_congress_person = 0
       self.study_stability = study_stability
       self.study_representative = study_representative

    def Build(self, congress_datas, votes_results): 
        parties = congress_datas.parties
        year = congress_datas.year
        mode = congress_datas.mode
        departmental_assemblies = congress_datas.departmental_assemblies
        self.votes_results = votes_results
        self.__ordered_parties_by_percentage(parties)
        self.__count_congress_person_totality()
        congress = self.__build_congress(year, mode, self.parties_ordered, departmental_assemblies)
        congress.stability_majority = self.study_stability.Calculate(congress)
        congress.representative_congress = self.study_representative.Calculate(congress, self.votes_results, year)
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
   
    def __build_congress(self, year, mode, parties, departmental_assemblies):
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        congress.departmental_assemblies = departmental_assemblies
        return congress