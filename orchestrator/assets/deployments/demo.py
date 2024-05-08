# orchestrator/assets/deployments/demo.py
from prefect import serve
from typing import NoReturn

from orchestrator.tasks.demo import repo_info


def main() -> NoReturn:
    my_first_deployment = repo_info.to_deployment(
        name="my-first-deployment",
        paused=True,
        is_schedule_active=False,
        description="Given a GitHub repository, logs repository statistics for that repo.",
        tags=["testing", "tutorial"],
        version="0.1",
    )
    serve(my_first_deployment)


if __name__ == "__main__":
    main()
else:
    pass
