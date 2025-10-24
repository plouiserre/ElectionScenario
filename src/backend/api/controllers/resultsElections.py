from fastapi import APIRouter

router = APIRouter()

@router.get("/resultsElections/", tags=["resultsElections"])
async def get_elections():
    return {"results":"none results implements for the moment"} 