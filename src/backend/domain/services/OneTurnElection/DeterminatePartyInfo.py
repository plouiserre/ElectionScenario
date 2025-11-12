class DeterminatePartyInfo : 
    def __init__(self, parties_info):
        self.parties_info = parties_info
        self.elected_persons = []
        self.elected_persons_count = 0

    def Calculate(self, elected_persons):
        self.elected_persons = elected_persons
        self.elected_persons_count = len(elected_persons)
        self.__add_elected_persons_in_parties()
        self.__update_parties_info()
        self.__delete_empty_parties_info()
        return self.parties_info
    
    def __add_elected_persons_in_parties(self):
        for elected_person in self.elected_persons:
            for party in self.parties_info: 
                if party.code == elected_person.parti_code: 
                    party.congress_persons.append(elected_person)
                else :
                    continue

    def __update_parties_info(self):
        for party in self.parties_info: 
            party.elected_congress_persons = len(party.congress_persons)              

    def __delete_empty_parties_info(self):
        parties = []
        for party in self.parties_info : 
            if len(party.congress_persons) > 0 : 
                parties.append(party)
        self.parties_info = parties