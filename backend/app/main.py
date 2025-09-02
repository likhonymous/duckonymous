from fastapi import FastAPI
from agents.duckonymous import DuckonymousAgent

app = FastAPI(title="Duckonymous API")

@app.get("/")
async def root():
    return {"message": "Welcome to Duckonymous API. Try /duckonymous"}


@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/duckonymous")
async def duckonymous():
    """
    Run the Duckonymous agent and return the result.
    """
    agent = DuckonymousAgent()
    result = await agent.run()
    return result
