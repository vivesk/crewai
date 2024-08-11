from tools import tool
from crewai import Agent, Task, Crew, Process
from agents import Researcher,new_writer

# Research Task
research_task= Task(
    description="""
    Conduct a comprehensive research analysis on the provided {topic}.
    Identify key findings, trends, and insights related to the {topic}.
    Provide a detailed report outlining the findings and their implications.
    """,
    expected_output="A comprehensive  3 paragragh research report on the provided {topic} including latest AI trends on it.",
    tools=[tool],
    agent=Researcher,
    #async_execution=False
)
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=new_writer,
  async_execution=False,
  output_file='{topic}_new-blog-post.md'  # Example of output customization
)