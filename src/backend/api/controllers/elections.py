from fastapi import APIRouter
from src.backend.api.mapper.MapperCongress import to_mapper_congress_response
from src.backend.api.response.CongressPersonResponse import CongressPersonResponse
from src.backend.api.response.CongressResponse import CongressResponse
from src.backend.api.response.DistrictResponse import DistrictResponse
from src.backend.api.response.PartyResponse import PartyResponse
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.infrastructure.files.JsonFiles import JsonFiles
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

router = APIRouter()

@router.get("/elections/{year}/results/{mode}", tags=["elections"])
async def get_results_elections(year : str, mode : str):
    year_param = int(year)
    json_files = JsonFiles()
    json_service = JsonResultsElection(json_files)
    build_congress = BuildCongress()
    elected_persons_by_district = DeterminateElectedPersonByDistrict()
    all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
    if mode == "oneTurnMajority":
        election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
        congress_domain = election.Determinate(year_param)
        congress = to_mapper_congress_response(congress_domain)
        return {"congress":{"year": congress.year, "mode": congress.mode, "parties" : congress.parties, "stability_majority" : congress.stability_majority}}
    else : 
        congress = __simulate_proportionnel_response()
        return {"congress":{"year": congress.year, "mode": congress.mode, "parties" : congress.parties, "stability_majority" : congress.stability_majority}}
    
def __simulate_proportionnel_response():
    first_district = __construct_district_response("3310", "33", "Gironde", "10ème circonscription")
    first_congress_person = __construct_congress_person_response("BOUDIÉ", "Florent", 17128, 29.96, first_district)
    first_party = __construct_party_response("ENS", "Ensemble ! (Majorité présidentielle)", first_congress_person)
    second_district = __construct_district_response("2502", "25", "Doubs", "2ème circonscription")
    second_congress_person = __construct_congress_person_response("VOYNET", "Dominique", 19160, 34.16, second_district)
    second_party = __construct_party_response("UG", "Union de la gauche", second_congress_person)
    third_district = __construct_district_response("5502", "55", "Meuse", "2ème circonscription")
    third_congress_person = __construct_congress_person_response("Goulet", "Florence", 19011, 50.63, third_district)
    third_party = __construct_party_response("RN", "Rassemblement National", third_congress_person)
    parties = [first_party, second_party, third_party]
    congress = __construct_congress_response("proportionalElectionNational", 2024, "LOW", parties)
    return congress
                                                                 

def __construct_district_response(code, department_code, department_name, name):
    district = DistrictResponse()
    district.code = code
    district.department_code = department_code
    district.department_name = department_name
    district.name = name
    return district

def __construct_congress_person_response(first_name, last_name, vote, vote_percentage, district):
    congress_person = CongressPersonResponse()
    congress_person.first_name = first_name
    congress_person.last_name = last_name
    congress_person.vote = vote
    congress_person.vote_percentage = vote_percentage
    congress_person.district = district
    return congress_person

def __construct_party_response(code, name, congress_person):
    party = PartyResponse()
    party.code = code
    party.name = name
    party.elected_congress_persons = 1
    party.elected_congress_persons = []
    party.elected_congress_persons.append(congress_person)
    return party

def __construct_congress_response(mode, year, stability_majority, parties):
    congress = CongressResponse()
    congress.mode = mode
    congress.year = year
    congress.stability_majority = stability_majority
    congress.parties = parties
    return congress