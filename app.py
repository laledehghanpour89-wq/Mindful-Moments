import streamlit as st
import requests

# 🌿 عنوان برنامه
st.set_page_config(page_title="Mindful Moments", page_icon="🧘‍♀️", layout="centered")
st.title("🧘‍♀️ Mindful Moments")
st.write("Take a deep breath and find a moment of calm 🌸")

# 🌐 آدرس سرور (همون Render API)
API_URL = "https://mindful-moments-1txj.onrender.com"

# 🫁 دکمه برای گرفتن نقل‌قول
if st.button("✨ Get a Mindful Quote"):
    try:
        response = requests.get(f"{API_URL}/quote")
        if response.status_code == 200:
            data = response.json()
            quote = data.get("quote", "No quote found.")
            st.success(f"💬 {quote}")
        else:
            st.error("⚠️ Could not fetch quote. Try again later.")
    except Exception as e:
        st.error(f"❌ Error connecting to server: {e}")

# 🩺 وضعیت سرور (health check)
st.divider()
st.write("### 🔍 API Status Check")
try:
    health = requests.get(f"{API_URL}/health")
    if health.status_code == 200:
        st.info("✅ API is online and working!")
    else:
        st.warning("⚠️ API seems offline or not responding correctly.")
except:
    st.error("❌ Could not connect to API.")
