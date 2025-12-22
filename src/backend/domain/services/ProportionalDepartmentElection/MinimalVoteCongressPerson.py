import math

class MinimalVoteCongressPerson : 
    def __init__(self):
        pass

    def Calculate(self, number_congress_persons): 
        if number_congress_persons == 1 :
            return 50
        elif number_congress_persons == 2 :
            return 35
        elif number_congress_persons == 3 :
            return 25
        else : 
            return self.__determinate_minimal_vote_for_many_siege_congress_persons(number_congress_persons)

    def __determinate_minimal_vote_for_many_siege_congress_persons(self, number_congress_person):
        ratio = 100 / number_congress_person
        minimal_percentage_vote = ratio - 5
        return math.floor(minimal_percentage_vote)