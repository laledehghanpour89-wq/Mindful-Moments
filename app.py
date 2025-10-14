import streamlit as st
import requests

# ===============================
# 🌐 Backend API
# ===============================
API_BASE = "https://mindful-moments-1txj.onrender.com"  # آدرس API بک‌اندت

# ===============================
# ⚙️ Page Setup
# ===============================
st.set_page_config(page_title="Mindful Moments", page_icon="🌿", layout="centered")

st.title("🌿 Mindful Moments")
st.caption("Find calm, breathe deeply, and stay mindful wherever you are 🌸")

# ===============================
# 🔎 Helper: Safe GET request
# ===============================
def api_get(path: str, params: dict | None = None, timeout: int = 10):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=timeout)
        return r.status_code, r.json()
    except Exception as e:
        return None, {"error": str(e)}

# ===============================
# 🧭 Sidebar Navigation
# ===============================
st.sidebar.title("🧘 Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["Home", "Calming Quote", "Breathwork", "Progress"],
    index=0,
)

# ===============================
# 🏠 HOME
# ===============================
if page == "Home":
    st.header("Welcome 🌸")
    st.write("Take a deep breath, center yourself, and enjoy your mindful journey 🕊️")

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
        use_column_width=True,
    )

    st.markdown("### Quick Start")
    if st.button("✨ Give me a calming quote"):
        code, data = api_get("/quote")
        if code == 200 and isinstance(data, dict):
            st.success(f"_{data.get('quote', 'Take a deep breath…')}_")
            st.caption(f"— {data.get('author', 'Unknown')}")
        else:
            st.error("Could not reach API or server returned an error.")

# ===============================
# 💬 QUOTE
# ===============================
elif page == "Calming Quote":
    st.header("💬 Calming Quote")
    st.write("Need a moment of calm? Click below to receive a mindful quote 🌿")

    if st.button("Get Quote"):
        code, data = api_get("/quote")
        if code == 200 and isinstance(data, dict):
            st.info(f"_{data.get('quote', 'Take a deep breath…')}_")
            st.caption(f"— {data.get('author', 'Unknown')}")
        else:
            st.warning("Could not retrieve quote from API.")

# ===============================
# 🌬️ BREATHWORK
# ===============================
elif page == "Breathwork":
    st.header("🌬️ Guided Breathwork")
    st.write("Breathe in... Breathe out... Let go of the tension 💫")

    if st.button("Start Breathing Exercise"):
        code, data = api_get("/breathwork")
        if code == 200 and isinstance(data, dict):
            st.info(data.get("exercise", "Inhale… Exhale…"))
        else:
            st.error("Could not load breathing exercise.")

# ===============================
# 📈 PROGRESS
# ===============================
elif page == "Progress":
    st.header("📈 Mindfulness Progress Tracker")
    st.write("Track your daily mindfulness journey 🌱")

    user_id = st.text_input("Enter your User ID", placeholder="e.g. laleh")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Progress"):
            if not user_id:
                st.warning("Please enter a user ID.")
            else:
                code, data = api_get("/progress", params={"user_id": user_id})
                if code == 200:
                    sessions = data.get("sessions", 0)
                    last_date = data.get("last_date", "N/A")
                    st.success(f"Sessions: {sessions} | Last Session: {last_date}")
                else:
                    st.error("Could not retrieve progress data.")
    with col2:
        if st.button("Add Session"):
            if not user_id:
                st.warning("Please enter a user ID.")
            else:
                try:
                    post = requests.post(f"{API_BASE}/progress", params={"user_id": user_id})
                    if post.status_code == 200:
                        result = post.json()
                        st.success(f"Progress updated for {user_id} 🌿")
                        st.json(result)
                    else:
                        st.error("Could not update progress.")
                except Exception as e:
                    st.error(f"Error: {e}")
