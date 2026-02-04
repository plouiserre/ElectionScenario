from abc import ABC, abstractmethod

class OneTurnElectionPort(ABC):
    @abstractmethod
    def Simulate(self, year):
        pass