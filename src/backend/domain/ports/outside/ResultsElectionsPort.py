from abc import ABC, abstractmethod


class ResultsElectionsPort(ABC):
    @abstractmethod
    def get_results():
        pass