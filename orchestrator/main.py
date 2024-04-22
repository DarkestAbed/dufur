# main.py
from tasks.demo import repo_info

from typing import NoReturn


def main() -> NoReturn:
    repos_to_review = [
        ("PrefectHQ", "prefect"),
        ("DarkestAbed", "dufur"),
        ("microsoft", "github"),
    ]
    for repo in repos_to_review:
        repo_info(repo_owner=repo[0], repo_name=repo[1])
    return None
if __name__ == "__main__":
    main()
