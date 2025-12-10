from src.backend.domain.ports.inside.OneTurnElectionPort import OneTurnElectionPort
from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort
from src.backend.domain.ports.outside.ResultsElectionsPort import ResultsElectionsPort
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.domain.services.ProportionalNationalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from src.backend.domain.services.ProportionalNationalElection.DeterminateSeatsByParty import DeterminateSeatsByParty
from src.backend.domain.services.ProportionalNationalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.ProportionalNationalElection.ProportionalNationalElectionService import ProportionalNationalElectionService
from src.backend.domain.services.ProportionalNationalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.ProportionalNationalElection.RemoveSmallParties import RemoveSmallParties
from src.backend.domain.services.ProportionalNationalElection.SelectCongressPerson import SelectCongressPersons
from src.backend.infrastructure.files.JsonFiles import JsonFiles
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

def get_one_turn_election_service() -> OneTurnElectionPort:
    json_service = __get_json_service()
    stability_congress = StabilityCongress(577)
    representative_congress = RepresentativeCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    elected_persons_by_district = DeterminateElectedPersonByDistrict()
    all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
    election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
    return election

def get_proportional_national_election_service() -> ProportionalNationalElectionPort:
    json_service = __get_json_service()
    determine_vote_by_party = DetermineVoteByParty()
    determine_percentage_vote_by_party = DeterminePercentageVoteByParty()
    remove_small_parties = RemoveSmallParties()
    #TODO externalize conf
    determine_seats_by_parties = DeterminateSeatsByParty(577)
    select_congress_persons = SelectCongressPersons()
    regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
    representative_congress = RepresentativeCongress(577)
    stability_congress = StabilityCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    election = ProportionalNationalElectionService(json_service, determine_vote_by_party, determine_percentage_vote_by_party, remove_small_parties, 
                                                    determine_seats_by_parties, select_congress_persons, regroup_congress_persons_by_parties, build_congress)
    return election

def __get_json_service() -> ResultsElectionsPort: 
    json_files = JsonFiles()
    json_service = JsonResultsElection(json_files)
    return json_service