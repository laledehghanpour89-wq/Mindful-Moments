from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    title="Mindful Moments API",
    description="A mindfulness API for quotes and simple breathing reminders 🌿",
    version="1.0.0"
)

# Allow all origins (for testing and UI connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "🌿 Welcome to Mindful Moments API",
        "available_routes": ["/", "/quote", "/health"]
    }

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running fine"}

@app.get("/quote")
def get_quote():
    quotes = [
        "Breathe deeply and let go.",
        "Peace begins with a single breath.",
        "You are right where you need to be.",
        "Be present, be kind, be you."
    ]
    return {"quote": random.choice(quotes)}
