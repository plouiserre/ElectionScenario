from fastapi import APIRouter

router = APIRouter()

@router.get("/elections/{year}/results/{mode}", tags=["elections"])
async def get_results_elections(year : str, mode : str):
    return {"year": year, "mode": mode} 