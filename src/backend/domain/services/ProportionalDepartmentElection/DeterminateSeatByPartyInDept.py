class DeterminateSeatsByPartyInDept : 
    def __init__(self):
        pass

    def Determinate(self, parties_votes, mode_design, number_congress_persons):
        parties_votes_ordered_by_scores = self.__ordered_by_scores(parties_votes)
        parties_votes_selected = self.__keep_selected_parties(parties_votes_ordered_by_scores, number_congress_persons)
        seats_by_parties = self.__determinate_each_party_candidates_elected(parties_votes_selected)
        return seats_by_parties
    
    def __ordered_by_scores(self, parties_votes): 
        parties_votes_ordered_by_scores = sorted(parties_votes.items(),  key=lambda item: item[1], reverse=True)
        return parties_votes_ordered_by_scores
    
    def __keep_selected_parties(self, parties_vote, number_congress_persons) : 
        parties_votes_selected = {}
        i = 0
        for party in parties_vote : 
            if i < number_congress_persons :
                parties_votes_selected[party[0]] = party[1]
                i += 1
            else :
                break
        return parties_votes_selected
    
    def __determinate_each_party_candidates_elected(self, parties_votes_selected): 
        results = {}
        for party in parties_votes_selected : 
            if party in results : 
                results[party] += 1
            else : 
                results[party] = 1
        return results