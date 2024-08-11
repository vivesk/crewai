from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"),
                           verbose=True)

## Create a research agent 
Researcher = Agent(
    role='Senior Researcher',
    goal='uncover groundbreaking technology in {topic}',
    backstory=(
        "You are driven by curiosity and a thirst for knowledge. "
        "You are a senior researcher who is very interested in {topic}. "
        "You are eager to share your knowledge."
    ),
    tools=[tool],
    allow_delegation=True,
    verbose=True,
    llm=llm,
    memory=False
)

## Create a writer agent with custom tools responsible for creating news blog
new_writer = Agent(
    role='News writer',
    goal='create news blog about {topic}',
    backstory=(
        "You are a talented news writer who is very interested in {topic}. "
        "You are responsible for creating news blog about {topic}."
    ),
    tools=[tool],
    allow_delegation=True,
    verbose=True,
    llm=llm,
    memory=False
)
