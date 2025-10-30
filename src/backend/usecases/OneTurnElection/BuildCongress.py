from src.backend.domain.congress import Congress

class BuildCongress : 
    def __init__(self):
       pass

    def Build(self, year, mode, parties): 
        congress = Congress()
        congress.year = year 
        congress.mode = mode 
        congress.parties = parties
        return congress