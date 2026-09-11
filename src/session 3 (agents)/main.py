from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from rich.console import Console
from rich.markdown import Markdown


load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str):
	"""Tool that searches over internet

	Args:
		query (str): The query to search for

	"""
	print(f"Searching for {query}")
	return tavily.search(query=query)

llm = ChatOllama(temperature=0, model="qwen3:1.7b")
tools = [search]

agent = create_agent(
	model=llm,
	tools=tools
)

def main():
	print(f"Usando modelo: {llm.model}")
	result = agent.invoke({"messages": [HumanMessage(content="search for 5 job postings for an ai enginee and python with django, and using langchain in the São Paulo on linkedin and list their details")]})
	Console().print(Markdown(result["messages"][-1].text))


if __name__ == "__main__":
	main()