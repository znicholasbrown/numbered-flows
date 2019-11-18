from inflect import engine
from prefect import Flow, task


@task
def dynamic_task(i):
    print(engine(i) + " Task")


with Flow("One Task Flow") as OneTask_Flow:
    j = 0
    for i in range(20):
        dynamic_task(i, task_args=dict(name=f"Task-{i}"), upstream_tasks=[f"Task-{j}"])
        j += 1

OneTask_Flow.deploy(
    "Flow Schematics", 
    base_image="python:3.7",
    python_dependencies=["inflect"],
    registry_url="znicholasbrown",
    image_name="prefect_flow",
    image_tag="onetask-flow",
)