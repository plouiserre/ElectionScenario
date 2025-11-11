from src.backend.domain.ports.outside.ResultsElectionsPort import ResultsElectionsPort
from src.backend.infrastructure.services.mapper_to_domain import mapper_all_elections_results

class JsonResultsElection(ResultsElectionsPort):
    def __init__(self, json_files):
       self.json_files = json_files

    def get_results(self):
        elections_results = self.json_files.get_elections_data()
        all_elections = mapper_all_elections_results(elections_results)
        return all_elections