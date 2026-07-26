from fastapi import FastAPI

from backend.app.routers import health
from backend.app.routers import github

app = FastAPI(title="RepoSage API")

app.include_router(health.router)
app.include_router(github.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to RepoSage API"
    }