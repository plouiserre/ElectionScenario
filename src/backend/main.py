from fastapi import FastAPI
from api.controllers import resultsElections

app = FastAPI()

app.include_router(resultsElections.router)

@app.get("/")
async def root():
    return {"greeting":"hello world"}