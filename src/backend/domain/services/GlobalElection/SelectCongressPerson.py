class SelectCongressPersons(): 
    def __init__(self):
        self.all_candidates = []

    def Choose(self, partys_seats, all_candidates): 
        all_candidates_elected = []
        self.all_candidates = all_candidates
        for party in partys_seats :
            number_seats = partys_seats[party]
            if(number_seats > 0) :
                all_candidates_this_party = self.__get_all_candidates_for_specific_party(party)
                best_candidates = self.__keep_best_candidates(number_seats, all_candidates_this_party)
                elected_persons_sorted = self.__sorted_best_candidates(best_candidates)
                for candidate_elected in elected_persons_sorted : 
                    all_candidates_elected.append(candidate_elected)
        return all_candidates_elected

    def __get_all_candidates_for_specific_party(self, party):
        candidates_belongs_this_party = []
        for candidate in self.all_candidates :
            if candidate.parti_code == party: 
                candidates_belongs_this_party.append(candidate)
        return candidates_belongs_this_party
    

    def __keep_best_candidates(self, number_seat, all_candidates_in_this_party):
        pre_selected_candidates = []
        for candidate in all_candidates_in_this_party : 
            if len(pre_selected_candidates) < number_seat : 
                pre_selected_candidates.append(candidate)
            else : 
                worst_candidate = self.__get_worst_candidate_pre_selected(pre_selected_candidates)                
                if worst_candidate.vote_percentage < candidate.vote_percentage : 
                    pre_selected_candidates.remove(worst_candidate)
                    pre_selected_candidates.append(candidate)
        return pre_selected_candidates
    
    def __get_worst_candidate_pre_selected(self, candidates_pre_selected):
        worst_candidate = None
        for candidate in candidates_pre_selected:
            if worst_candidate == None : 
                worst_candidate = candidate
            else :
                if candidate.vote_percentage < worst_candidate.vote_percentage : 
                    worst_candidate = candidate
        return worst_candidate
    
    def __sorted_best_candidates(self, elected_persons):
        elected_persons_sorted = sorted(elected_persons, key=lambda x: x.vote_percentage, reverse=True)
        return elected_persons_sorted
