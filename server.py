from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mindful_agent import get_quote, start_breathwork, track_progress

app = FastAPI(
    title="Mindful Moments API",
    description="API for the Mindful Moments Agent (quotes, breathing, and progress tracking).",
    version="1.0.0",
)

# CORS آزاد (برای GPT و هر کلاینتی)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
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
def progress(user_id: str = Query(..., description="Unique user id")):
    """
    نمونه: /progress?user_id=laleh
    """
    try:
        result = track_progress(user_id)
        return result
    except Exception as e:
        # لاگ شفاف برای Render
        print("ERROR in /progress:", repr(e))
        # پاسخ استاندارد
        return {"error": "internal_error", "detail": str(e)}

# healthcheck برای Render (اختیاری)
@app.get("/healthz")
def health():
    return {"ok": True}
