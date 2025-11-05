from fastapi import APIRouter
from src.backend.api.mapper.MapperCongress import to_mapper_congress_response
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

router = APIRouter()

@router.get("/elections/{year}/results/{mode}", tags=["elections"])
async def get_results_elections(year : str, mode : str):
    json_service = JsonResultsElection()
    build_congress = BuildCongress()
    elected_persons_by_district = DeterminateElectedPersonByDistrict()
    all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
    election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
    congress_domain = election.Determinate(2024, "OneTurn")
    congress = to_mapper_congress_response(congress_domain)
    return {"congress":{"year": congress.year, "mode": congress.mode, "parties" : congress.parties}}