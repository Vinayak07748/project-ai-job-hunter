# Import FastAPI tools
from fastapi import FastAPI, UploadFile, File, HTTPException

# Import the PDF reader
from pypdf import PdfReader

# Import tools for reading the PDF from memory
import io

# Create the FastAPI application
app = FastAPI(
    title="AI Job Hunter",
    description="An AI-powered job discovery and career assistant",
    version="0.1.0",
)

# Upload a resume and extract its text
@app.post("/upload-resume",tags=["Resume"])
async def upload_resume(file: UploadFile = File(...)):

    # Check whether the uploaded file is a PDF
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF file.",
        )

    # Read the uploaded file
    contents = await file.read()

    try:
        # Open the PDF from memory
        reader = PdfReader(io.BytesIO(contents))

        # Extract text from every page
        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text() or ""

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Could not read the PDF file.",
        )

    # Return the extracted text
    return {
        "filename": file.filename,
        "resume_text": resume_text,
    }