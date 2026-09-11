from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from rich.console import Console
from rich.markdown import Markdown
from langchain_tavily import TavilySearch
### Nesse arquivo estamos utilizando uma ferramenta ja da propria tavily

load_dotenv()

llm = ChatOllama(temperature=0, model="qwen3:1.7b")
tools = [TavilySearch()]

agent = create_agent(
	model=llm,
	tools=tools
)

def main():
	print(f"Usando modelo: {llm.model}")
	result = agent.invoke({"messages": [HumanMessage(content="search for 5 job postings for an ai enginee and python with django, and using langchain in the São Paulo on linkedin and list their details, Focus only in São Paulo")]})
	Console().print(Markdown(result["messages"][-1].text))


if __name__ == "__main__":
	main()