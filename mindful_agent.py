import json
import random
import os
from datetime import datetime, timedelta

DATA_FILE = "data.json"

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
    {"name": "Relaxed Focus", "pattern": "Inhale 5s, exhale 5s, focus on the breath."}
]


# --- Data handling ---
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"users": {}}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# --- Features ---
def get_quote():
    return random.choice(QUOTES)


def start_breathwork():
    return random.choice(BREATH_EXERCISES)


def track_progress(user_id="default_user"):
    """Track and update user progress with streak logic"""
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    user = data["users"].get(user_id, {
        "sessions": 0,
        "last_session": None,
        "streak": 0
    })

    # Check if user already logged today
    if user["last_session"] == today:
        return {
            "message": "You’ve already logged a session today 🌼",
            "total_sessions": user["sessions"],
            "streak": user["streak"],
            "last_session": user["last_session"]
        }

    # Update streak logic
    if user["last_session"]:
        last_date = datetime.strptime(user["last_session"], "%Y-%m-%d")
        if (datetime.now() - last_date).days == 1:
            user["streak"] += 1  # continued streak
        else:
            user["streak"] = 1  # reset streak
    else:
        user["streak"] = 1

    # Update session count and date
    user["sessions"] += 1
    user["last_session"] = today
    data["users"][user_id] = user
    save_data(data)

    return {
        "message": "Progress updated 🌿",
        "total_sessions": user["sessions"],
        "streak": user["streak"],
        "last_session": user["last_session"]
    }
