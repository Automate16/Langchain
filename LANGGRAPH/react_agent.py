from langchain_openai import ChatOpenAI 
from langchain.agents import create_agent
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ["EURI_API_KEY"],
    base_url="https://api.euron.one/api/v1/euri",
    temperature=0.7,
)

agent = create_agent(tools= [], model = llm )
response = agent.invoke({"messages": [{"role": "user", "content": "what the weather in banglore now write a tweet"}]})
print(response)
#"Give me tweet about today weather in banglore with the current temperature ")



# response = llm.invoke([
#     ("give me tweet about today weather in banglore with the current temperature ")
# ])
# print(response.content)