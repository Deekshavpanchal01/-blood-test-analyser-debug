import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import BloodTestReportTool, NutritionTool, ExerciseTool

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

doctor = Agent(
    role="Doctor",
    goal="Analyze blood test reports: {query}",
    verbose=True,
    backstory="You are an experienced doctor specializing in blood test analysis.",
    tools=[BloodTestReportTool()],
    llm=llm,
)

verifier = Agent(
    role="Verifier",
    goal="Verify blood test reports",
    verbose=True,
    backstory="You are a medical records specialist with expertise in verifying blood test reports.",
    tools=[BloodTestReportTool()],
    llm=llm,
)

nutritionist = Agent(
    role="Nutritionist",
    goal="Provide nutrition advice",
    verbose=True,
    backstory="You are a certified clinical nutritionist with 15+ years of experience.",
    tools=[NutritionTool()],
    llm=llm,
)

exercise_specialist = Agent(
    role="Exercise Specialist",
    goal="Create exercise plans",
    verbose=True,
    backstory="You are an exercise physiologist with expertise in creating personalized fitness plans.",
    tools=[ExerciseTool()],
    llm=llm,
)