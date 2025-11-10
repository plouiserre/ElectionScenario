import json
from src.backend.domain.ports.outside.ResultsElectionsPort import ResultsElectionsPort
from src.backend.domain.models.factory import factory_elections
from src.backend.infrastructure.models.factory_record import factory_candidate_record, factory_department_record, factory_district_record, factory_election_result_record, factory_party_record
from src.backend.infrastructure.services.mapper_to_domain import mapper_all_elections_results
from src.backend.infrastructure.services.mockData.election_2022 import construct_election_2022
from src.backend.infrastructure.services.mockData.election_2024 import construct_election_2024

class JsonResultsElection(ResultsElectionsPort):
    def __init__(self, json_files):
       self.json_files = json_files

    def get_results(self):
        elections_results = self.json_files.get_elections_data()
        all_elections = mapper_all_elections_results(elections_results)
        return all_elections