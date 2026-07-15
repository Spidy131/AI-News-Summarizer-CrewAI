from crewai import Agent
from config import llm
from tools import search_tool

research_agent = Agent(
    role="AI News Researcher",

    goal="Find the latest AI news from the internet.",

    backstory="""
    You are an experienced AI journalist.
    You always search the web before writing.
    """,

    tools=[search_tool],

    llm=llm,

    verbose=False,

    allow_delegation=False
)

summary_agent = Agent(
    role="AI News Summarizer",

    goal="""
    Read AI news articles and create concise,
    easy-to-understand summaries.
    """,

    backstory="""
    You are an experienced editor.
    You transform technical AI news into
    short, clear summaries.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)
report_agent = Agent(
    role="AI Report Writer",

    goal="""
    Create a professional markdown report
    from summarized AI news.
    """,

    backstory="""
    You are a technical writer.

    Your reports are clean,
    professional,
    and easy to read.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)