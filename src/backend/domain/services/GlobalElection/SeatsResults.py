class SeatsResults : 
    def __init__(self):
        self.all_votes = {}
        pass

    def calculate_percentage(self, all_votes): 
        percentages = {}
        self.all_votes = all_votes
        all_votes_number = self.__determinate_all_votes()
        for key in self.all_votes :
            percentage = round(self.all_votes[key]/ all_votes_number * 100, 2)
            percentages[key] = percentage
        return percentages
    


    def __determinate_all_votes(self) :
        all_votes_number = 0
        for key in self.all_votes :
            all_votes_number += self.all_votes[key]
        return all_votes_number