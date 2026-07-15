from crewai import Crew, Process

from agents import research_agent
from tasks import research_task

from crewai import Crew, Process

from agents import (
    research_agent,
    summary_agent,
    report_agent
)

from tasks import (
    research_task,
    summary_task,
    report_task
)

news_crew = Crew(
    agents=[
        research_agent,
        summary_agent,
        report_agent
    ],

    tasks=[
        research_task,
        summary_task,
        report_task
    ],

    process=Process.sequential,

    verbose=True
)