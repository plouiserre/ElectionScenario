import copy
from src.backend.domain.models.factory import factory_congress_datas
from src.backend.domain.ports.inside.OneTurnElectionPort import OneTurnElectionPort

class OneTurnElectionService(OneTurnElectionPort) : 
    def __init__(self, json_results_election, all_elected_persons, build_congress, one_turn_congress_person_elected_by_dpt, construct_departmental_assemblies):
        self.json_results_election = json_results_election
        self.all_elected_persons = all_elected_persons
        self.build_congress = build_congress
        self.one_turn_congress_person_elected_by_dpt = one_turn_congress_person_elected_by_dpt
        self.contruct_departmental_assemblies = construct_departmental_assemblies
        self.mode = "OneTurn"

    def Simulate(self, year):
        results_data_all_years = self.json_results_election.get_results()
        results_data = results_data_all_years[year]
        congress_persons = self.all_elected_persons.Select(None, results_data.all_candidates, self.mode)
        data_parties = self.one_turn_congress_person_elected_by_dpt.regroup(congress_persons)
        departmental_assemblies = self.contruct_departmental_assemblies.Build(data_parties, results_data.all_parties, results_data.all_departments)
        parties = self.__get_all_data_parties_good(departmental_assemblies)
        congress_datas = factory_congress_datas(year, self.mode, parties, departmental_assemblies)
        congress = self.build_congress.Build(congress_datas, results_data_all_years)
        return congress

    def __get_all_data_parties_good(self, departmental_assemblies): 
        all_parties = {}
        data_parties = []
        for departmental_assembly in departmental_assemblies : 
            parties = copy.deepcopy(departmental_assembly.parties)
            for party in parties : 
                if (party.code in all_parties) == False : 
                    all_parties[party.code] = party
                else : 
                    for congress_person in party.congress_persons : 
                        all_parties[party.code].congress_persons.append(congress_person)
                        all_parties[party.code].elected_congress_persons += 1
        for party_code in all_parties : 
            party = all_parties[party_code]
            data_parties.append(party)
        return data_parties