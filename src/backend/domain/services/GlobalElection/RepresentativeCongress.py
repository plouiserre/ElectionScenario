class RepresentativeCongress : 
    def __init__(self, total_congress_persons, year):
        self.congress = None
        self.all_votes = None
        self.total_congress_persons = total_congress_persons
        self.year = year

    def Calculate(self, congress, all_votes):
        self.congress = congress
        self.all_votes = all_votes
        percentage_congress_persons_by_parties = self.__calculate_percentage_for_congress()  
        votes_by_parties = self.__group_votes_by_parties()  
        all_votes = self.__count_all_votes()
        percentage_votes_by_parties = self.__calculate_percentage_for_vote(votes_by_parties, all_votes)
        biggest_difference = self.__get_biggest_difference(percentage_votes_by_parties, percentage_congress_persons_by_parties)
        representative = self.__get_representative_from_big_difference(biggest_difference)
        return representative
    
    def __calculate_percentage_for_congress(self):
        all_percentage = {}
        for party in self.congress.parties : 
            percentage = party.elected_congress_persons  / self.total_congress_persons * 100
            all_percentage[party.code] = percentage
        return all_percentage

    def __group_votes_by_parties(self): 
        all_votes_by_parties = {}
        for candidate in self.all_votes[self.year].all_candidates : 
            if (candidate.parti_code in all_votes_by_parties.keys()) == False : 
                all_votes_by_parties[candidate.parti_code] = 0
            all_votes_by_parties[candidate.parti_code] += candidate.vote
        return all_votes_by_parties
    
    def __count_all_votes(self) : 
        all_votes = 0
        for candidate in self.all_votes[self.year].all_candidates : 
            all_votes += candidate.vote
        return all_votes

    def __calculate_percentage_for_vote(self, votes_by_parties, all_votes): 
        all_percentages_for_vote = {}
        for party in votes_by_parties : 
            votes = votes_by_parties[party]
            percentage = votes / all_votes * 100
            all_percentages_for_vote[party] = round(percentage,2)
        return all_percentages_for_vote
    
    def __get_biggest_difference(self, all_percentages_by_vote, all_percentages_by_congress): 
        biggest_difference = 0
        for party in all_percentages_by_vote : 
            percentage_by_vote = all_percentages_by_vote[party]
            if party in all_percentages_by_congress.keys() : 
                percentage_by_congress = all_percentages_by_congress[party]
                difference = abs(percentage_by_vote - percentage_by_congress)
                if difference > biggest_difference :
                    biggest_difference = difference
        return biggest_difference
    
    def __get_representative_from_big_difference(self, big_difference): 
        if big_difference < 5 : 
            return "PERFECT"
        elif big_difference < 10 : 
            return "GOOD"
        elif big_difference < 25 : 
            return "QUITE"
        else : 
            return "LOW"