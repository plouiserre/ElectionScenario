from src.backend.domain.models.district import District

class CongressPerson : 
    def __init__(self):
        self.last_name = ''
        self.first_name = ''
        self.sexe = ''
        self.parti_code = ''
        self.vote = 0
        self.vote_percentage = 0.0
        self.district = District()