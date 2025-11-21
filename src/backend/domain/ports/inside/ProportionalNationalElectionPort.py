from abc import ABC, abstractmethod

class ProportionalNationalElectionPort(ABC):
    @abstractmethod
    def Determinate(self, year, all_candidates_datas):
        pass