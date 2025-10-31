from decimal import Decimal
from src.backend.domain.models.congress import Congress

class BuildCongress : 
    def __init__(self):
       self.difference_to_correct = Decimal(0.0)
       self.percentage_congress_parties = Decimal(0.0)
       self.is_above_one_hundred_percent = False

    def Build(self, year, mode, parties): 
        congress = self.__build_congress(year, mode, parties)
        is_percentage_correct = self.__check_and_correct_parties_percentages(congress)
        if is_percentage_correct == False: 
            self.__determine_difference_to_ajust_for_parties_percentage()
            congress = self.__remove_percentage_to_have_one_hundred_percentage(congress)
        return congress

    def __build_congress(self, year, mode, parties):
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        return congress
    
    def __check_and_correct_parties_percentages(self, congress):
        for party in congress.parties : 
            self.percentage_congress_parties += Decimal(str(party.percentage))
        if self.percentage_congress_parties == 100 :
            return True
        else :
            return False
        
    def __determine_difference_to_ajust_for_parties_percentage(self):
        if self.percentage_congress_parties > 100 :
            self.is_above_one_hundred_percent = True
            self.difference_to_correct = Decimal(self.percentage_congress_parties - 100) 
        else:
            self.difference_to_correct = (100 - self.percentage_congress_parties)
        
    def __remove_percentage_to_have_one_hundred_percentage(self, congress): 
        low_percentage = 100
        party_code_with_low_percentage = ''
        for party in congress.parties : 
            if party.percentage < low_percentage:
                low_percentage = party.percentage 
                party_code_with_low_percentage = party.code
        for party in congress.parties : 
            if party.code == party_code_with_low_percentage : 
                #I prefer store in float because it is more simple to compare but I calculate in Decimal because it is more accurate
                if self.is_above_one_hundred_percent :
                    party.percentage = float(Decimal(str(party.percentage)) -  self.difference_to_correct)
                else :
                    party.percentage = float(Decimal(str(party.percentage)) +  self.difference_to_correct)
        return congress