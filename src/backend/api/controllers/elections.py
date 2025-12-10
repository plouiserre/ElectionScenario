from fastapi import APIRouter, Depends, HTTPException
from src.backend.api.controllers.dependency import get_one_turn_election_service, get_proportional_national_election_service
from src.backend.api.mapper.MapperCongress import to_mapper_congress_response

router = APIRouter()

@router.get("/elections/{year}/results/{mode}", tags=["elections"])
async def get_results_elections(year : str, mode : str, one_election_service = Depends(get_one_turn_election_service), 
                                proportional_nationalElection_service = Depends(get_proportional_national_election_service)):
    year_param = int(year)
    if mode == "oneTurnMajority":
        congress_domain = one_election_service.Determinate(year_param)
        congress = to_mapper_congress_response(congress_domain)
        return {"congress":{"year": congress.year, "mode": congress.mode, "parties" : congress.parties, "stability_majority" : congress.stability_majority, "representative_congress" : congress.representative_congress}}
    elif mode =="proportionalNational":
        congress_domain = proportional_nationalElection_service.Determinate(year_param)
        congress = to_mapper_congress_response(congress_domain)
        return {"congress":{"year": congress.year, "mode": congress.mode, "parties" : congress.parties, "stability_majority" : congress.stability_majority, "representative_congress" : congress.representative_congress}}
    else : 
        raise HTTPException(status_code=404, detail="Results Mode unknown")