from abc import ABC, abstractmethod

class OneTurnElectionPort(ABC):
    @abstractmethod
    def Determinate(self, year):
        pass