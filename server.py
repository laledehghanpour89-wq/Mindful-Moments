from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mindful_agent import get_quote, start_breathwork, track_progress

app = FastAPI(
    title="Mindful Moments API",
    description="API for the Mindful Moments Agent (quotes, breathing, and progress tracking).",
    version="1.0.0"
)

# =========================
# 🌐 Enable CORS (for frontend access)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ برای تست همه مجازن (بعداً می‌تونی محدودش کنی)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# 🌸 ROUTES
# =========================
@app.get("/")
def home():
    return {"message": "Mindful Moments API is running 💖"}

@app.get("/quote")
def quote():
    """Return a calming mindfulness quote"""
    try:
        data = get_quote()
        return {"quote": data.get("quote", "Take a deep breath and relax."), "author": data.get("author", "Unknown")}
    except Exception as e:
        return {"error": str(e)}

@app.get("/breathwork")
def breathwork():
    """Start a breathing exercise"""
    try:
        exercise = start_breathwork()
        return {"exercise": exercise}
    except Exception as e:
        return {"error": str(e)}

@app.get("/progress")
def progress(user_id: str = None):
    """Track user’s mindfulness progress"""
    if not user_id:
        return {"error": "Missing user_id"}
    try:
        progress_data = track_progress(user_id)
        return {"user_id": user_id, "progress": progress_data}
    except Exception as e:
        return {"error": str(e)}
