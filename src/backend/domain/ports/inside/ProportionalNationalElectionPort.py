from abc import ABC, abstractmethod

class ProportionalNationalElectionPort(ABC):
    @abstractmethod
    def Determinate(self, year):
        pass