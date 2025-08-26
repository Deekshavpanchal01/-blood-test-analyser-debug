from crewai import Task
from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import BloodTestReportTool, NutritionTool, ExerciseTool

verification = Task(
    description="Verify the document is a blood test report",
    agent=verifier,
    tools=[BloodTestReportTool()],
)

help_patients = Task(
    description="Analyze the blood test report: {query}",
    agent=doctor,
    tools=[BloodTestReportTool()],
)

nutrition_analysis = Task(
    description="Provide nutrition advice: {query}",
    agent=nutritionist,
    tools=[NutritionTool()],
)

exercise_planning = Task(
    description="Create exercise plan: {query}",
    agent=exercise_specialist,
    tools=[ExerciseTool()],
)