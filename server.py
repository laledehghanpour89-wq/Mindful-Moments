from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    title="Mindful Moments API",
    description="A simple API that serves calming quotes and mindfulness support 🌿",
    version="1.0.0"
)

# Allow requests from any origin (important for Render + Streamlit UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Mindful Moments API is running"}

# ✅ Calming quotes list
quotes = [
    "Breathe deeply and let go.",
    "Peace begins with a single breath.",
    "You are right where you need to be.",
    "Be present, be kind, be you.",
    "Inhale calm, exhale stress.",
    "Small steps lead to big peace."
]

@app.get("/quote")
def get_quote():
    quote = random.choice(quotes)
    return {"quote": quote}

# ✅ Root route (for quick API test)
@app.get("/")
def root():
    return {
        "message": "🌿 Welcome to Mindful Moments API!",
        "routes": ["/", "/health", "/quote"],
        "status": "online"
    }
