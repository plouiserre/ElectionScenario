class RegroupPartiesFromDepartment : 
    def __init__(self):
        self.parties = {}

    def execute(self, parties_by_departments): 
        for dpt in parties_by_departments : 
            parties = parties_by_departments[dpt]
            for party in parties:
                if party.code not in self.parties : 
                    party.elected_congress_persons = len(party.congress_persons)
                    self.parties[party.code] = party
                else : 
                    self.__add_congress_persons_in_parties(party) 
        return self.parties

    def __add_congress_persons_in_parties(self, party): 
        number_congress_persons = len(party.congress_persons)
        party_to_updated = self.parties[party.code]
        party_to_updated.elected_congress_persons += number_congress_persons
        for congress_person in party.congress_persons : 
            party_to_updated.congress_persons.append(congress_person)