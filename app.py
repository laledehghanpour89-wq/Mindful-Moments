import streamlit as st
import requests

# ===============================
# 🌐 API Backend Configuration
# ===============================
API_BASE = "https://mindful-moments-1txj.onrender.com"  # Backend address on Render

# ===============================
# 🎨 Streamlit Page Setup
# ===============================
st.set_page_config(page_title="Mindful Moments", page_icon="🌿", layout="centered")

st.title("🌿 Mindful Moments")
st.write("A gentle space for quotes, breathing, and reflection 🌸")

# ===============================
# 🧭 Sidebar Navigation
# ===============================
st.sidebar.title("💫 Choose an activity")
page = st.sidebar.radio(
    "Select a section:",
    ["Home", "Calming Quote", "Breathwork", "Track Progress"],
)

# ===============================
# 🏡 Home Page
# ===============================
if page == "Home":
    st.header("Welcome 🌸")
    st.write("Take a deep breath, center yourself, and enjoy your mindful journey 🧘‍♀️")
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        use_column_width=True,
    )

# ===============================
# 💬 Calming Quote
# ===============================
elif page == "Calming Quote":
    st.header("💬 Calming Quote")

    if st.button("Get a Calming Quote"):
        try:
            res = requests.get(f"{API_BASE}/quote", timeout=10)
            if res.status_code == 200:
                data = res.json()
                st.success(f"_{data.get('quote', 'Take a deep breath and relax.')}_")
                st.caption(f"— {data.get('author', 'Unknown')}")
            else:
                st.error("The quote service is currently unavailable.")
        except Exception as e:
            st.warning("⚠️ Unable to connect to the quote service.")
            st.text(f"Error: {e}")

# ===============================
# 🌬️ Breathwork Page
# ===============================
elif page == "Breathwork":
    st.header("🌬️ Guided Breathwork")
    st.write("Follow along this short breathing routine to find calm 🌤️")

    if st.button("Start Breathing Exercise"):
        try:
            res = requests.get(f"{API_BASE}/breathwork", timeout=10)
            if res.status_code == 200:
                data = res.json()
                st.info(data.get("exercise", "Inhale... Exhale..."))
            else:
                st.warning("Unable to load breathing exercise right now.")
        except Exception as e:
            st.error("Error connecting to the breathwork service.")
            st.text(e)

# ===============================
# 📈 Track Progress Page
# ===============================
elif page == "Track Progress":
    st.header("📈 Track Your Mindfulness Progress")

    user_id = st.text_input("Enter your user ID to see your progress:")
    if st.button("Show Progress"):
        if user_id:
            try:
                res = requests.get(f"{API_BASE}/progress", params={"user_id": user_id}, timeout=10)
                if res.status_code == 200:
                    st.json(res.json())
                else:
                    st.error("Error retrieving progress data.")
            except Exception as e:
                st.error("Could not connect to the progress tracking service.")
                st.text(e)
        else:
            st.warning("Please enter a user ID to continue.")
