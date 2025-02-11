from langgraph.func import entrypoint, task
from dotenv import load_dotenv, find_dotenv
from litellm import completion
_:bool = load_dotenv(find_dotenv())

@task
def func1():
    response = completion(
        model = "gemini/gemini-1.5-flash",
        messages = [{"role":"user",
                    "content":"Give any random city name in pakistan"}]
    )
    city_name = response["choices"][0]["message"]["content"]
    print("function 1 : generate city")
    return city_name

@task
def func2(city_name : str):
    response = completion(
        model = "gemini/gemini-1.5-flash",
        messages = [{"role":"user",
                    "content":f"Tell me 3 fun facts about {city_name} city"}]
    )
    fun_fact = response["choices"][0]["message"]["content"]
    print("function 2 : generate fun fact")
    return fun_fact   

@task
def func3(fun_fact : str):
    with open("fun_fact.md", "w") as f:
        f.write(fun_fact)
    print("function 3 : save fun fact")
    
    

@entrypoint()
def run_flow(input : str):
    city = func1().result()
    print(city)
    fun_fact = func2(city).result()
    print(fun_fact)
    func3(fun_fact)

def kickoff():
    run_flow.invoke(input="pak")