# orchestrator/tasks/demo.py
import httpx   # an HTTP client library and dependency of Prefect
from prefect import flow, task


@task(retries=2)
def get_repo_info(repo_owner: str, repo_name: str) -> dict:
    """Get info about a repo - will retry twice after failing"""
    url: str = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    api_response: httpx.Response = httpx.get(url)
    api_response.raise_for_status()
    repo_info: dict = api_response.json()
    return repo_info


@task
def get_contributors(repo_info: dict) -> dict:
    """Get contributors for a repo"""
    contributors_url: str = repo_info["contributors_url"]
    response: httpx.Response = httpx.get(contributors_url)
    response.raise_for_status()
    contributors: dict = response.json()
    return contributors


@flow(log_prints=True)
def repo_info(repo_owner: str = "PrefectHQ", repo_name: str = "prefect"):
    """
    Given a GitHub repository, logs the number of stargazers
    and contributors for that repo.
    """
    print(f"> Checking repo {repo_owner}/{repo_name}...")
    repo_info: dict = get_repo_info(repo_owner=repo_owner, repo_name=repo_name)
    print(f"Stars 🌠 : {repo_info['stargazers_count']}")

    contributors: dict = get_contributors(repo_info)
    print(f"Number of contributors 👷: {len(contributors)}")


if __name__ == "__main__":
    repo_info()
else:
    pass
