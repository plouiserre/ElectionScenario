from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort

class ProportionalNationalElectionService(ProportionalNationalElectionPort):
    def __init__(self):
        pass

    def Determinate(self, year):
        return super().Determinate(year)