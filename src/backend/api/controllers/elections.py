from fastapi import APIRouter
from api.mapper.MapperCongress import to_mapper_congress_response
from usecases.OneTurnElection.OneTurnElectionUseCase import OneTurnElectionUseCase

router = APIRouter()

@router.get("/elections/{year}/results/{mode}", tags=["elections"])
async def get_results_elections(year : str, mode : str):
    election = OneTurnElectionUseCase()
    congress_domain = election.Determinate()
    congress = to_mapper_congress_response(congress_domain)
    return {"congress":{"year": congress.year, "mode": congress.mode, "parties" : congress.parties}}