from src.backend.domain.models.factory import  factory_congress_datas
from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort

class ProportionalNationalElectionService(ProportionalNationalElectionPort):
    def __init__(self, json_results_election, seats_results, remove_small_parties, allocate_seats_by_parties, select_congress_person, 
                 regroup_by_parties, build_congress):
        self.json_results_election = json_results_election
        self.seats_results = seats_results
        self.remove_small_parties = remove_small_parties
        self.allocate_seats_by_parties = allocate_seats_by_parties
        self.select_congress_person = select_congress_person
        self.regroup_by_parties = regroup_by_parties
        self.build_congress = build_congress
        self.all_parties = []
        self.candidates_results = []
        self.year = 0
        self.mode = "PROPORTIONALITYNATIONAL"

    def Simulate(self, year):
        self.year = year
        results_data_all_years = self.json_results_election.get_results()
        all_datas_needed = results_data_all_years[year]
        self.all_parties = all_datas_needed.all_parties
        self.candidates_results = self.__mixed_all_candidates_from_everywhere(all_datas_needed.all_candidates)
        _votes_by_parties = self.__calculate_each_party_votes()
        _percentage_by_parties = self.__calculate_each_vote_percentage(_votes_by_parties)
        _percentages_for_parties_importants = self.__keep_only_important_parties(_percentage_by_parties)
        _number_congress_persons_elected_by_parties = self.__calculate_number_congress_persons_elected_by_parties(_percentages_for_parties_importants)
        _congress_persons_elected = self.__choose_congress_persons_elected_for_parties(_number_congress_persons_elected_by_parties)
        _parties_with_congress_persons = self.__regroup_congress_persons_by_parties(_congress_persons_elected)
        congress_datas = factory_congress_datas(year, self.mode, _parties_with_congress_persons, None)
        congress = self.build_congress.Build(congress_datas, results_data_all_years)
        return congress    
    
    def __mixed_all_candidates_from_everywhere(self, all_candidates_by_districts): 
        all_candidates_mixed = []
        for all_candidates_from_specific_district in all_candidates_by_districts: 
            for candidate in all_candidates_from_specific_district :
                all_candidates_mixed.append(candidate)
        return all_candidates_mixed

    def __calculate_each_party_votes(self):
        results = self.seats_results.calculate_vote_each_party(self.candidates_results)
        return results
    
    def __calculate_each_vote_percentage(self, parties_by_vote):
        results = self.seats_results.calculate_percentage(parties_by_vote)
        return results
    
    def __keep_only_important_parties(self, percentage_by_parties):
        importantes_parties_with_percentage = self.remove_small_parties.execute(percentage_by_parties)
        return importantes_parties_with_percentage
    
    def __calculate_number_congress_persons_elected_by_parties(self, percentages_for_parties_importants):
        number_congress_persons_by_parties = self.allocate_seats_by_parties.allocate(percentages_for_parties_importants)
        return number_congress_persons_by_parties
    
    def __choose_congress_persons_elected_for_parties(self, number_congress_persons_elected_by_parties): 
        congress_persons_elected = self.select_congress_person.Select(number_congress_persons_elected_by_parties, self.candidates_results, self.mode)
        return congress_persons_elected
    
    def __regroup_congress_persons_by_parties(self, congress_persons_elected):
        parties_with_congress_persons_elected = self.regroup_by_parties.sort(congress_persons_elected, self.all_parties)
        return parties_with_congress_persons_elected