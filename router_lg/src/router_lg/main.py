import random
from typing import Literal, TypedDict
from langgraph.func import entrypoint, task

class RouterInput(TypedDict):
    query : str

class RouterOutput(TypedDict):
    query : str
    category : Literal["math", "writing", "general"]
    response : str


@task
def route_query(input_data : RouterInput) -> Literal["math", "writing","general"]:
    categories = ["math", "writing", "general"]
    return random.choice(categories)

@task
def handle_math(query : str) -> str:
    return f"Math handler processing: {query}"

@task
def handle_writing(query : str) -> str:
    return f"Writing handler processing: {query}"

@task
def handle_general(query : str) -> str:
    return f"General handler processing: {query}"

@entrypoint()
def router_workflow(input_data : RouterInput) -> RouterOutput:
    category = route_query(input_data).result()
    if category == "math":
        response = handle_math(input_data["query"]).result()
    elif category == "writing":
        response = handle_writing(input_data["query"]).result()
    else:
        response = handle_general(input_data["query"]).result()
    return {
            "query": input_data["query"],
            "category": category,
            "response": response}


    
def call_router():
    input_data = {"query": "What is the capital of France?"}
    res = router_workflow.invoke(input_data)
    print(res)

