import os
from dotenv import load_dotenv
load_dotenv()

import PyPDF2

# Simple BaseTool class to avoid dependency issues
class BaseTool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def _run(self, *args, **kwargs):
        raise NotImplementedError("This tool should implement _run method")

class BloodTestReportTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="Blood Test Report Reader",
            description="Reads a blood test report PDF file"
        )
    
    def _run(self, path: str) -> str:
        try:
            full_report = ""
            with open(path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    full_report += text + "\n"
            return full_report
        except Exception as e:
            return f"Error: {str(e)}"

class NutritionTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="Nutrition Analysis Tool",
            description="Provides nutrition advice"
        )
    
    def _run(self, blood_report_data: str) -> str:
        return "Based on your blood test, eat a balanced diet with plenty of fruits and vegetables."

class ExerciseTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="Exercise Planning Tool",
            description="Creates exercise plans"
        )
    
    def _run(self, blood_report_data: str) -> str:
        return "Based on your blood test, exercise for 30 minutes a day, 5 days a week."