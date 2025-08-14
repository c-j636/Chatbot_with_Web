from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools) 
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

@tool
def some_function(extra_features_beyond_web_search: str) -> str:
    """Example placeholder tool."""
    return f"Got these features: {extra_features_beyond_web_search}"

def get_tools():
    return [
        TavilySearchResults(max_results=2),
        some_function
    ]

def create_tool_node(tools):
    return ToolNode(tools=tools)


