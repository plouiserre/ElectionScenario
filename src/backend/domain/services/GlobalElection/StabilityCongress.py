class StabilityCongress : 
    def __init__(self, total_congress_persons):
        self.congress = None        
        self.total_congress_persons = total_congress_persons

    def Calculate(self, congress):
        self.congress = congress
        if self.__check_is_perfect() :
            return "PERFECT"
        elif self.__check_is_good_stability() :
            return "GOOD"
        elif self.__check_is_quite_stability() : 
            return "QUITE"
        else : 
            return "LOW"
    
    def __check_is_perfect(self):
        is_one_party_majority = False
        for party in self.congress.parties : 
            if party.elected_congress_persons > self.total_congress_persons /2 :
                is_one_party_majority = True
                break
        return is_one_party_majority    

    def __check_is_good_stability(self):
        is_one_family_majority = False
        i = 1
        while i < 6:
            all_parties = self.__get_all_parties_in_this_family(i)
            all_elected_persons = self.__get_all_elected_persons_in_this_family(all_parties)
            if all_elected_persons > self.total_congress_persons /2 : 
                is_one_family_majority = True
                break
            i += 1
        return is_one_family_majority
    
    def __check_is_quite_stability(self): 
        is_majority = False
        i = 1
        while i < 6: 
            is_majority = self.__is_majority_with_family_above(i)
            if is_majority : 
                break
            i += 1
        while i < 6 : 
            is_majority = self.__is_majority_with_family_below(i)
            if is_majority : 
                break
            i += 1
        return is_majority

    def __is_majority_with_family_above(self, id_family):
        all_elected_persons_above = 0
        all_elected_persons = self.__get_number_elected_persons_for_this_family(id_family)
        if id_family < 5 : 
            all_elected_persons_above = self.__get_number_elected_persons_for_this_family(id_family+1)
        all_group_elected_persons = all_elected_persons_above + all_elected_persons
        is_majority = all_group_elected_persons > self.total_congress_persons / 2
        return is_majority
    
    def __is_majority_with_family_below(self, id_family):
        all_elected_persons_below = 0
        all_elected_persons = self.__get_number_elected_persons_for_this_family(id_family)
        if id_family > 1 : 
            all_elected_persons_below = self.__get_number_elected_persons_for_this_family(id_family-1)
        all_group_elected_persons = all_elected_persons_below + all_elected_persons
        is_majority = all_group_elected_persons > self.total_congress_persons / 2
        return is_majority

    def __get_number_elected_persons_for_this_family(self, id_family):
        all_parties_this_family = self.__get_all_parties_in_this_family(id_family)
        all_elected_persons = self.__get_all_elected_persons_in_this_family(all_parties_this_family)
        return all_elected_persons

    def __get_all_parties_in_this_family(self, family_id) :
        family_parties = []
        for party in self.congress.parties : 
            if party.family == family_id : 
                family_parties.append(party)
        return family_parties
    
    def __get_all_elected_persons_in_this_family(self, all_parties) : 
        elected_congress_persons = 0
        for party in all_parties : 
            elected_congress_persons += party.elected_congress_persons
        return elected_congress_persons