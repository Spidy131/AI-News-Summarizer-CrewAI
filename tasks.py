from crewai import Task
from agents import (
    research_agent,
    summary_agent,
    report_agent
)

research_task = Task(
    description="""
    Search the internet using the Tavily Search Tool.

    Find the latest 5 AI news articles published recently.

    For each article provide:

    - Title
    - Source
    - Publication Date
    - Summary
    - Why it is important

    Only use information found through the search tool.
    """,

    expected_output="""
    A structured markdown report of the latest AI news.
    """,

    agent=research_agent
)
summary_task = Task(
    description="""
    Read the research results.

    Summarize each news article into
    4-5 concise bullet points.

    Keep the important information only.
    """,

    expected_output="""
    Concise summaries for every AI news article.
    """,

    agent=summary_agent
)
report_task = Task(
    description="""
    Create a professional markdown report.

    Include:

    # Today's AI News

    - Headlines
    - Summaries
    - Why Important
    - Overall Trends

    Format everything neatly.
    """,

    expected_output="""
    A beautiful markdown report.
    """,

    agent=report_agent,

    output_file="output/ai_news_report.md"
)