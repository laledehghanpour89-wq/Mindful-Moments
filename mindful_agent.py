import json
import random
from datetime import datetime

# 🧘 Quotes dataset
quotes = [
    "You are not your thoughts.",
    "Just breathe. Everything is okay.",
    "Let go of what you can’t control.",
    "Inhale calm, exhale stress.",
    "You are enough, exactly as you are."
]

# 🗂 محل ذخیره داده‌ها
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"streak": 0, "last_session": None}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# 🎯 Intent 1: جمله آرام‌بخش
def get_quote():
    return random.choice(quotes)

# 🧘 Intent 2: تمرین تنفس
def start_breathwork():
    return "🫁 Let’s do 2 minutes of box breathing.\nInhale 4s → Hold 4s → Exhale 4s → Hold 4s.\nRepeat 4 times."

# 📆 Intent 3: پیگیری پیشرفت
def track_progress():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    if data["last_session"] != today:
        data["streak"] += 1
        data["last_session"] = today
        save_data(data)
        return f"✅ Great job! You’ve completed {data['streak']} day(s) in a row!"
    else:
        return "🌼 You already completed today’s session — great consistency!"
