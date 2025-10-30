from src.backend.domain.models.congressPerson import CongressPerson
class DeterminateElectedPersonByDistrict:
    def __init__(self):
        pass

    def Find(self, candidates):
        elected_person = CongressPerson()
        vote_percentage = 0.0
        for candidate in candidates:
            if(candidate.vote_percentage > vote_percentage):
                vote_percentage = candidate.vote_percentage
                elected_person = candidate
        return elected_person