from abc import ABC, abstractmethod

class ProportionalNationalElectionPort(ABC):
    @abstractmethod
    def Simulate(self, year):
        pass