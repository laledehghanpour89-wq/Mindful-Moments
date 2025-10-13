import json
import random
import os
from datetime import datetime

# ✅ Render-safe data path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

# Mindfulness quotes
QUOTES = [
    "Breathe. You are exactly where you need to be.",
    "Peace comes from within, not from the outside world.",
    "You are doing your best — and that is enough.",
    "Each breath is a new beginning.",
    "Calm is your superpower. Use it today."
]

# Breathing exercises
BREATH_EXERCISES = [
    {"name": "Box Breathing", "pattern": "Inhale 4s, hold 4s, exhale 4s, hold 4s."},
    {"name": "4-7-8 Breathing", "pattern": "Inhale 4s, hold 7s, exhale 8s."},
    {"name": "Relaxed Focus", "pattern": "Inhale 5s, exhale 5s, focus on your breath."}
]


# 🧩 Utility: safely load JSON data
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"users": {}}, f)
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"users": {}}


# 🧩 Utility: safely save JSON data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# 🌸 Function: return a mindfulness quote
def get_quote():
    return random.choice(QUOTES)


# 🌬️ Function: return a breathing exercise
def start_breathwork():
    return random.choice(BREATH_EXERCISES)


# 📈 Function: update & return progress for a user
def track_progress(user_id: str):
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    if user_id not in data["users"]:
        data["users"][user_id] = {"sessions": 0, "last_session": None, "streak": 0}

    user = data["users"][user_id]
    user["sessions"] += 1

    # If last session was yesterday, continue streak
    if user["last_session"]:
        last = datetime.strptime(user["last_session"], "%Y-%m-%d")
        delta = (datetime.now() - last).days
        if delta == 1:
            user["streak"] += 1
        elif delta > 1:
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
