from src.backend.domain.models.congress import Congress

class BuildCongress : 
    def __init__(self):
       pass

    def Build(self, year, mode, parties): 
        congress = self.__build_congress(year, mode, parties)
        is_percentage_correct = self.__check_and_correct_parties_percentages(congress)
        if is_percentage_correct == False: 
            congress = self.__remove_percentage_to_have_one_hundred_percentage(congress)
        return congress

    def __build_congress(self, year, mode, parties):
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        return congress
    
    def __check_and_correct_parties_percentages(self, congress):
        percentage = 0.0
        for party in congress.parties : 
            percentage += party.percentage
        if percentage == 100 :
            return True
        else :
            return False
        
    def __remove_percentage_to_have_one_hundred_percentage(self, congress): 
        low_percentage = 100
        party_code_with_low_percentage = ''
        for party in congress.parties : 
            if party.percentage < low_percentage:
                low_percentage = party.percentage 
                party_code_with_low_percentage = party.code
        for party in congress.parties : 
            if party.code == party_code_with_low_percentage : 
                party.percentage = party.percentage -  0.01
        return congress