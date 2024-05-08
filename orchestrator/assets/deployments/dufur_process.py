# orchestrator/assets/deployments/demo.py
from prefect import serve
from typing import NoReturn

from orchestrator.tasks.backend_tasks import workflow


def main() -> NoReturn:
    dufur_process = workflow.to_deployment(
        name="my-first-deployment",
        paused=True,
        is_schedule_active=False,
        description="Whole Dufur process (app config, webpage scrapping, formatting, email sending).",
        tags=["testing", "tutorial", "dufur"],
        version="1.0",
    )
    serve(dufur_process)


if __name__ == "__main__":
    main()
else:
    pass
