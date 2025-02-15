from langgraph.func import task, entrypoint
 
@task
def multiply_by_two(num : int) -> int:
    return num * 2

@task
def multiply_by_three(num : int) -> int:
    return num * 3


@entrypoint()
def parallel_workflow(num : int):
    futures = [multiply_by_two(num), multiply_by_three(num)]
    result = [future.result() for future in futures]
    return {"results":result}

def call_parallel():
    result = parallel_workflow.invoke(10)
    print(result)

