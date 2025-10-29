from src.backend.domain.district import District

class CongressPerson : 
    def __init__(self):
        self.last_name = ''
        self.first_name = ''
        self.sexe = ''
        self.party_code = ''
        self.vote = 0
        self.vote_percentage = 0.0
        self.district = District()