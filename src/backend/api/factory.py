from src.backend.api.response.CongressResponse import CongressResponse
from src.backend.api.response.CongressPersonResponse import CongressPersonResponse
from src.backend.api.response.PartyResponse import PartyResponse
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.domain.services.ProportionalNationalElection.DeterminateSeatsByParty import DeterminateSeatsByParty
from src.backend.domain.services.ProportionalNationalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from src.backend.domain.services.ProportionalNationalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.ProportionalNationalElection.ProportionalNationalElectionService import ProportionalNationalElectionService
from src.backend.domain.services.ProportionalNationalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.ProportionalNationalElection.RemoveSmallParties import RemoveSmallParties
from src.backend.domain.services.ProportionalNationalElection.SelectCongressPerson import SelectCongressPersons
from src.backend.infrastructure.files.JsonFiles import JsonFiles
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection


def factory_congress_person(last_name, first_name, district):
    response = CongressPersonResponse()
    response.last_name = last_name
    response.first_name = first_name
    response.district = district
    return response

def factory_party(name, code, congressmans):
    response = PartyResponse()
    response.name = name
    response.code = code
    response.congressmans = congressmans
    return response

def factory_congress(year, mode, parties):
    response = CongressResponse()
    response.mode = mode
    response.year = year
    response.parties = parties
    return response

def factory_json_results_election():
    json_files = JsonFiles()
    json_service = JsonResultsElection(json_files)
    return json_service

def factory_one_turn_election_service(json_service):
    build_congress = BuildCongress()
    elected_persons_by_district = DeterminateElectedPersonByDistrict()
    all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
    election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
    return election

def factory_proportional_national_election_service(json_service):
    determine_vote_by_party = DetermineVoteByParty()
    determine_percentage_vote_by_party = DeterminePercentageVoteByParty()
    remove_small_parties = RemoveSmallParties()
    #TODO externalize conf
    determine_seats_by_parties = DeterminateSeatsByParty(577)
    select_congress_persons = SelectCongressPersons()
    regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
    election = ProportionalNationalElectionService(json_service, determine_vote_by_party, determine_percentage_vote_by_party, remove_small_parties, 
                                                    determine_seats_by_parties, select_congress_persons, regroup_congress_persons_by_parties)
    return election