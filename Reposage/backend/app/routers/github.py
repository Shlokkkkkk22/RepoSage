from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.github_service import (
    clone_repository,
    analyze_repository_structure,
)

router = APIRouter()


class RepositoryRequest(BaseModel):
    github_url: str


@router.post("/analyze")
def analyze_repository(request: RepositoryRequest):

    # Clone the repository
    cloned = clone_repository(request.github_url)

    # Analyze the cloned repository
    analysis = analyze_repository_structure(
        cloned["local_path"]
    )

    # Return both clone and analysis results
    return {
        "message": "Repository analyzed successfully",
        "clone": cloned,
        "analysis": analysis,
    }