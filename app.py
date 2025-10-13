import streamlit as st
import requests
import time

# ------------------- Settings -------------------
API_BASE = "https://mindful-moments-1txj.onrender.com"
st.set_page_config(page_title="Mindful Moments 🌿", page_icon="💚", layout="centered")

# ------------------- Custom CSS -------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #E8F8F5, #D6EAF8);
    color: #2E4053;
    font-family: "Trebuchet MS", sans-serif;
}
h1, h2, h3 {
    color: #1B4F72;
}
.stButton > button {
    background-color: #27AE60 !important;
    color: white !important;
    border: none !important;
    font-size: 18px !important;
    padding: 10px 20px !important;
    border-radius: 10px !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background-color: #1E8449 !important;
    transform: scale(1.05);
}
.footer {
    text-align: center;
    margin-top: 50px;
    color: #7DCEA0;
    font-size: 13px;
}
.breath-circle {
    height: 180px;
    width: 180px;
    border-radius: 50%;
    background: radial-gradient(circle, #82E0AA 0%, #27AE60 70%);
    margin: 30px auto;
    animation: breathe 6s ease-in-out infinite;
}
@keyframes breathe {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.3); opacity: 1; }
    100% { transform: scale(1); opacity: 0.8; }
}
</style>
""", unsafe_allow_html=True)

# ------------------- Sidebar Menu -------------------
st.title("🪷 Mindful Moments")
st.caption("A gentle space for quotes, breathing, and reflection 🌿")

menu = st.sidebar.radio("🌼 Choose an activity", ["Home", "Calming Quote", "Breathwork", "Track Progress"])

# ------------------- Pages -------------------
if menu == "Home":
    st.header("Welcome 🌸")
    st.write("Take a deep breath, center yourself, and enjoy your mindful journey 💫")
    st.image("lotus.jpg", use_container_width=True)

elif menu == "Calming Quote":
    st.header("💬 Calming Quote")
    try:
        res = requests.get(f"{API_BASE}/quote")
        if res.status_code == 200:
            st.success(res.json()["quote"])
        else:
            st.error("Couldn't fetch a quote 😢")
    except Exception as e:
        st.warning("The API seems to be sleeping — try again soon 🌙")

elif menu == "Breathwork":
    st.header("🌬️ Mindful Breathing")
    st.markdown('<div class="breath-circle"></div>', unsafe_allow_html=True)
    st.write("Follow the animation — inhale as it expands, exhale as it contracts 🫶")
    for i in range(3, 0, -1):
        st.info(f"🌿 Breathing in... {i}")
        time.sleep(1)
    st.success("Beautiful. You did it 🌸")

elif menu == "Track Progress":
    st.header("📊 Track Your Progress")
    user_id = st.text_input("Enter your user ID:", placeholder="e.g. laleh")

    if st.button("🌱 Show My Progress"):
        if user_id:
            try:
                res = requests.get(f"{API_BASE}/progress", params={"user_id": user_id})
                if res.status_code == 200:
                    st.json(res.json())
                else:
                    st.error("Couldn't load your progress 😢")
            except Exception as e:
                st.error(f"Error fetching progress: {e}")
        else:
            st.warning("Please enter your user ID first 🌸")

# ------------------- Footer -------------------
st.markdown('<div class="footer">🌿 Made with calm and care | Mindful Moments © 2025</div>', unsafe_allow_html=True)
