from crewai_tools import TavilySearchTool

search_tool = TavilySearchTool(
    max_results=5,
    search_depth="advanced"
)