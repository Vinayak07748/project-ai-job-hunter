# Import the resume extraction function
from resume_parser import extract_resume_text

# Set the PDF path
pdf_path = "resume/my_resume.pdf"

# Extract resume text
resume_text = extract_resume_text(pdf_path)

# Display the extracted text
print(resume_text)