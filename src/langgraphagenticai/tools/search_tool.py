from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

# Serper API 
# Tavily Search - Better accuracy

def get_tools():
    """
        Return the list of tools to be use in the chatbot
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and rerturns a tool node for the graph
    """
    return ToolNode(tools=tools)

