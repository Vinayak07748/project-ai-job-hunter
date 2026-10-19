from fastapi import FastAPI

app = FastAPI(
    title = 'AI Job Hunter',
    description = 'An AI-powered job hunting application that helps users find suitable job opportunities based on their skills and preferences.',
    version = '1.0.0',
)


@app.get("/")
def home():
    return {"message": "Welcome to the AI Job Hunter API!",
            "status": "Running"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}