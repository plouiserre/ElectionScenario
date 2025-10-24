from fastapi import FastAPI
from api.controllers import elections

app = FastAPI()

app.include_router(elections.router)

@app.get("/")
async def root():
    return {"greeting":"hello world"}