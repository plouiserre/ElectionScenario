from src.backend.domain.models.factory import factory_mode_design

class RulesDesignatedCongressPerson : 
    def __init__(self):
        self.minimal_vote = 12.5

    def find(self, number_congress_persons, percentage_parties_results): 
        big_difference_winner = self.__determine_big_difference_for_bonus_winner(number_congress_persons)
        is_bonus_winner = self.__is_bonus_winner(percentage_parties_results, big_difference_winner)
        if number_congress_persons == 1 :
            return factory_mode_design("order", self.minimal_vote)
        else : 
            if is_bonus_winner :
                return factory_mode_design("winner", self.minimal_vote)
            else :
                return factory_mode_design("order", self.minimal_vote)    
        
    def __determine_big_difference_for_bonus_winner(self, number_congress_persons) : 
        if number_congress_persons == 2 :
            return 40        
        elif number_congress_persons == 3:
            return 25    
        elif number_congress_persons == 4:
            return 17.5    
        else :
            return 15
        
    def __is_bonus_winner(self, percentage_parties_results, difference_percentage_winner) : 
        percentage_biggest = 0
        percentage_second = 0
        for party in percentage_parties_results:            
            percentage = percentage_parties_results[party]
            if percentage > percentage_biggest : 
                percentage_biggest = percentage

        for party in percentage_parties_results:            
            percentage = percentage_parties_results[party]
            if percentage > percentage_second and percentage != percentage_biggest: 
                percentage_second = percentage

        if percentage_biggest - percentage_second >= difference_percentage_winner :
            return True 
        else :
            return  False