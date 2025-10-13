import random

QUOTES = [
    "Take a deep breath. You are doing great.",
    "Be present. You are exactly where you need to be.",
    "Calm is your superpower.",
    "Inhale peace, exhale tension."
]

BREATHWORKS = [
    {"inhale": 4, "hold": 4, "exhale": 4},
    {"inhale": 4, "hold": 7, "exhale": 8}
]

PROGRESS = {"streak": 3, "total_sessions": 12}


def get_quote():
    """Return a random mindfulness quote"""
    return random.choice(QUOTES)


def start_breathwork():
    """Return a random breathing exercise"""
    return random.choice(BREATHWORKS)


def track_progress():
    """Return current progress stats"""
    return PROGRESS
