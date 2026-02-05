from abc import ABC, abstractmethod

class ProportionalDepartmentElectionPort(ABC):
    @abstractmethod
    def Simulate(self, year):
        pass