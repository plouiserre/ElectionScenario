from abc import ABC, abstractmethod

class ProportionalDepartmentElectionPort(ABC):
    @abstractmethod
    def Determinate(self, year):
        pass