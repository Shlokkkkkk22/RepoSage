from pathlib import Path
from git import Repo

BASE_DIR = Path("backend/repositories")


def clone_repository(github_url: str):
    # Create the repositories folder if it doesn't exist
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    # Extract repository name from URL
    repo_name = github_url.rstrip("/").split("/")[-1]

    destination = BASE_DIR / repo_name

    # Clone only if it doesn't already exist
    if not destination.exists():
        Repo.clone_from(github_url, destination)

    return {
        "repository_name": repo_name,
        "local_path": str(destination)
    }


def analyze_repository_structure(repository_path: str):
    repo = Path(repository_path)

    files = []
    folders = []

    for item in repo.iterdir():
        if item.is_file():
            files.append(item.name)
        elif item.is_dir():
            folders.append(item.name)

    return {
        "total_files": len(files),
        "total_folders": len(folders),
        "files": files,
        "folders": folders,
    }