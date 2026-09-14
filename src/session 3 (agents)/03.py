from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from rich.console import Console
from rich.markdown import Markdown
from langchain_tavily import TavilySearch
### Nesse arquivo estamos aprendendo como estruturar um Output

load_dotenv()


class Source(BaseModel):
	"""
		Schema for a source used by the agent
	"""
	url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
	"""
		Schema for agent response with answer and sources
	"""
	answer:str = Field(description="The agent's answer to the query")
	sources:list[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


llm = ChatOllama(temperature=0, model="qwen3:1.7b")
tools = [TavilySearch()]

agent = create_agent(
	model=llm,
	tools=tools,
	response_format= AgentResponse
)

def main():
	print(f"Usando modelo: {llm.model}")
	result = agent.invoke({"messages": [HumanMessage(content="search for 5 job postings for an ai enginee and python with django, and using langchain in the São Paulo on linkedin and list their details, Focus only in São Paulo, é necessario ter o link das vagas")]})
	Console().print(Markdown(result["messages"][-1].text))


if __name__ == "__main__":
	main()