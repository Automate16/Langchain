from langchain_openai import ChatOpenAI 
from langchain.agents import create_agent
#from langchain_community.tools import TavilySearchResults
from langchain_tavily import TavilySearch
import datetime
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

Search_tool = TavilySearch(search_depth='basic')


def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Returns the current date and time in the specified format"""

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

agent = create_agent(tools= [Search_tool,get_system_time], model = llm )
response = agent.invoke({"messages": [{"role": "user", "content": "When was SpaceX's last launch and how many days ago was that from this instant give me in IST timezone?"}]})
#print(response)
print(response["messages"][-1].content)




# response = llm.invoke([
#     ("give me tweet about today weather in banglore with the current temperature ")
# ])
# print(response.content)