import json
import random
import os
from datetime import datetime

# ✅ محل دیتای قابل‌نوشتن روی Render
# اجازه می‌دهی با ENV هم override شود (برای آینده)
DATA_FILE = os.getenv("DATA_FILE", "/tmp/mindful_moments_data.json")

QUOTES = [
    "Breathe. You are exactly where you need to be.",
    "Peace comes from within, not from the outside world.",
    "You are doing your best — and that is enough.",
    "Each breath is a new beginning.",
    "Calm is your superpower. Use it today."
]

BREATH_EXERCISES = [
    {"name": "Box Breathing", "pattern": "Inhale 4s, hold 4s, exhale 4s, hold 4s."},
    {"name": "4-7-8 Breathing", "pattern": "Inhale 4s, hold 7s, exhale 8s."},
    {"name": "Relaxed Focus", "pattern": "Inhale 5s, exhale 5s, focus on your breath."}
]


def _init_file():
    """Ensure the data file exists and is valid JSON."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"users": {}}, f)
        return

    # اگر خراب یا خالی بود، ریستش می‌کنیم
    try:
        with open(DATA_FILE, "r") as f:
            json.load(f)
    except Exception:
        with open(DATA_FILE, "w") as f:
            json.dump({"users": {}}, f)


def load_data():
    _init_file()
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"users": {}}


def save_data(data):
    # نوشتن اتمیکِ ساده: اول temp بعد rename
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=4)
    os.replace(tmp, DATA_FILE)


def get_quote():
    return random.choice(QUOTES)


def start_breathwork():
    return random.choice(BREATH_EXERCISES)


def track_progress(user_id: str):
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    if user_id not in data["users"]:
        data["users"][user_id] = {"sessions": 0, "last_session": None, "streak": 0}

    user = data["users"][user_id]
    user["sessions"] += 1

    if user["last_session"]:
        try:
            last = datetime.strptime(user["last_session"], "%Y-%m-%d")
            delta = (datetime.now() - last).days
            if delta == 1:
                user["streak"] += 1
            elif delta > 1:
                user["streak"] = 1
        except Exception:
            user["streak"] = 1
    else:
        user["streak"] = 1

    user["last_session"] = today
    save_data(data)

    return {
        "message": "Progress updated 🌿",
        "total_sessions": user["sessions"],
        "streak": user["streak"],
        "last_session": today
    }
