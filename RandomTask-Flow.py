from inflect import engine
from prefect import Flow, task
from random import uniform


@task
def dynamic_task(i):
    print(engine(i) + " Task")


with Flow("Random Task Dependencies Flow") as RandomTask_Flow:
    j = 0
    for i in range(50):
        k = uniform(0, j)
        dynamic_task(i, task_args=dict(name=f"Task-{i}"), upstream_tasks=[f"Task-{k}"])
        j += 1

RandomTask_Flow.deploy(
    "Flow Schematics", 
    base_image="python:3.7",
    python_dependencies=["inflect"],
    registry_url="znicholasbrown",
    image_name="prefect_flow",
    image_tag="randomtask-flow",
)