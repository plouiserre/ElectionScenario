from src.backend.domain.models.factory import factory_congress, factory_congress_person, factory_district, factory_party
from src.backend.domain.services.OneTurnElection.DeterminatePartyInfo import DeterminatePartyInfo
from src.backend.domain.ports.inside.OneTurnElectionPort import OneTurnElectionPort


class OneTurnElectionService(OneTurnElectionPort) : 
    def __init__(self, json_results_election, all_elected_persons, build_congress):
        self.json_results_election = json_results_election
        self.all_elected_persons = all_elected_persons
        self.build_congress = build_congress
        self.mode = "OneTurn"

    def Determinate(self, year):
        results_data_all_years = self.json_results_election.get_results()
        results_data = results_data_all_years[year]
        congress_persons = self.all_elected_persons.find_them_all(results_data.all_candidates)
        self.determinate_party_info = DeterminatePartyInfo(results_data.all_parties)
        data_parties = self.determinate_party_info.Calculate(congress_persons)
        congress = self.build_congress.Build(year, self.mode, data_parties)
        return congress   