class DeterminateSeatsByPartyInDept : 
    def __init__(self):
        self.number_congress_persons = 0
        self.mode_design = None

    def Determinate(self, parties_votes, mode_design, number_congress_persons):
        self.mode_design = mode_design
        self.number_congress_persons = number_congress_persons
        parties_votes_ordered_by_scores = self.__ordered_by_scores(parties_votes)
        parties_votes_selected = self.__keep_selected_parties(parties_votes_ordered_by_scores)
        seats_by_parties = self.__determinate_each_party_candidates_elected(parties_votes_selected)
        return seats_by_parties
    
    def __ordered_by_scores(self, parties_votes): 
        parties_votes_ordered_by_scores = sorted(parties_votes.items(),  key=lambda item: item[1], reverse=True)
        return parties_votes_ordered_by_scores
    
    def __keep_selected_parties(self, parties_vote) : 
        parties_votes_selected = {}
        i = 0
        for party in parties_vote : 
            if i < self.number_congress_persons and self.mode_design.minimal_vote <= party[1] :
                parties_votes_selected[party[0]] = party[1]
                i += 1
            else :
                break
        return parties_votes_selected
    
    def __determinate_each_party_candidates_elected(self, parties_votes_selected): 
        results = self.__give_bonus_winner(parties_votes_selected)
        while self.number_congress_persons > 0:
            for party in parties_votes_selected : 
                if self.number_congress_persons > 0 :
                    if party in results : 
                        results[party] += 1
                        self.number_congress_persons -= 1
                    else : 
                        results[party] = 1
                        self.number_congress_persons -= 1
                else :
                    break
        return results
    
    def __give_bonus_winner(self, parties_votes_selected):
        results = {}
        if self.mode_design.type == "winner" : 
            is_first_iteration = True
            for party in parties_votes_selected : 
                if is_first_iteration : 
                    results[party] = 1
                    self.number_congress_persons -= 1
                    is_first_iteration = False
                else : 
                    break
        return results
