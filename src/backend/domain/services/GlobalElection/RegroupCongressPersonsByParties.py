class RegroupCongressPersonsByParties: 
    def __init__(self):
        self.all_parties = []
        self.parties_elected = []

    def sort(self, congress_persons, parties):
        self.all_parties = parties
        all_parties_with_congress_persons = self.__regroup_all_congress_persons_by_parties(congress_persons) 
        self.parties_elected = self.__build_all_parties_elected(all_parties_with_congress_persons)       
        return self.parties_elected

    def __regroup_all_congress_persons_by_parties(self, congress_persons) : 
        all_parties_with_congress_persons = {} 
        for congress_person in congress_persons:
            for party in self.all_parties :            
                if party.code == congress_person.parti_code : 
                    if party.code not in all_parties_with_congress_persons : 
                            all_parties_with_congress_persons[party.code] = []
                    all_parties_with_congress_persons[party.code].append(congress_person)
        return all_parties_with_congress_persons
    
    def __build_all_parties_elected(self, all_parties_with_congress_persons):
        parties_selected = []
        for party_with_congress_persons in all_parties_with_congress_persons : 
            for party in self.all_parties :
                if party_with_congress_persons == party.code : 
                        party.congress_persons = all_parties_with_congress_persons[party_with_congress_persons]
                        party.elected_congress_persons = len(party.congress_persons)
                        parties_selected.append(party)
        return parties_selected