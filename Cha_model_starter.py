from langchain_openai import ChatOpenAI 
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

response = llm.invoke([
    ("best city in india with low AQI ")
])
print(response.content)