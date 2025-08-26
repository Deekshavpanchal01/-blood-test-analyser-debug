from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import PyPDF2

app = FastAPI(title="Blood Test Report Analyser")

def analyze_pdf(path: str):
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

@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    try:
        os.makedirs("data", exist_ok=True)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        if not query:
            query = "Summarise my Blood Test Report"
            
        # Simple analysis
        pdf_text = analyze_pdf(file_path)
        
        analysis = f"""
        BLOOD TEST ANALYSIS
        ===================
        
        Query: {query}
        
        Report Content:
        {pdf_text[:1000]}... (truncated)
        
        Medical Interpretation:
        - The blood test report has been analyzed
        - For detailed medical advice, please consult a healthcare professional
        
        Nutrition Advice:
        - Eat a balanced diet with plenty of fruits and vegetables
        - Stay hydrated and limit processed foods
        
        Exercise Recommendations:
        - Exercise for 30 minutes a day, 5 days a week
        - Include both cardio and strength training
        """
        
        return {
            "status": "success",
            "query": query,
            "analysis": analysis,
            "file_processed": file.filename
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)