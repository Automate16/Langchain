from langchain_openai import ChatOpenAI 
from langchain.agents import create_agent
from langchain_community.tools import TavilySearchResults
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

search_tool = TavilySearchResults(search_depth='basic')

agent = create_agent(tools= [search_tool], model = llm )
response = agent.invoke({"messages": [{"role": "user", "content": "what the weather in banglore now write a tweet"}]})
print(response["messages"][-1].content)

#"Give me tweet about today weather in banglore with the current temperature ")



# response = llm.invoke([
#     ("give me tweet about today weather in banglore with the current temperature ")
# ])
# print(response.content)