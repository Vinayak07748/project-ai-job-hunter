# Import the PDF reader
from pypdf import PdfReader


# Extract text from a PDF resume
def extract_resume_text(pdf_path):
    # Open the PDF
    reader = PdfReader(pdf_path)

    # Extract text from every page
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text