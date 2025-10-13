from fastapi import FastAPI
from mindful_agent import get_quote, start_breathwork, track_progress

app = FastAPI(
    title="Mindful Moments API",
    description="API for the Mindful Moments Agent (quotes, breathing, and progress tracking).",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Mindful Moments API is running"}

@app.get("/quote")
def quote():
    return {"quote": get_quote()}

@app.get("/breathwork")
def breathwork():
    return {"exercise": start_breathwork()}

@app.get("/progress")
def progress():
    return {"progress": track_progress()}


