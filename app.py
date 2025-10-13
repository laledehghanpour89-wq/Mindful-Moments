import streamlit as st
import requests

# 🌿 آدرس API شما روی Render (لینک FastAPI)
API_BASE = "https://mindful-moments-1txj.onrender.com"

# 🌸 تنظیمات صفحه
st.set_page_config(page_title="Mindful Moments", page_icon="🌸", layout="centered")

# 🎨 استایل سفارشی برای ظاهر نرم و آرامش‌بخش
st.markdown("""
    <style>
    body {
        background-color: #fafafa;
    }
    img {
        border-radius: 20px;
    }
    .stButton>button {
        background-color: #C1E1C1;
        color: black;
        font-weight: 600;
        border-radius: 10px;
        height: 3em;
        width: 12em;
    }
    .stButton>button:hover {
        background-color: #A3D9A5;
        color: black;
    }
    h1, h2, h3 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 🌿 عنوان اصلی برنامه
st.title("🌿 Mindful Moments")
st.write("A gentle space for quotes, breathing, and reflection 🌸")

# 🎋 منوی سمت چپ
menu = st.sidebar.radio("🪷 Choose an activity", ["Home", "Calming Quote", "Breathwork", "Track Progress"])

# 🏡 صفحه‌ی اصلی (Home)
if menu == "Home":
    st.header("Welcome 🌷")
    st.write("Take a deep breath, center yourself, and enjoy your mindful journey 🌞")
    
    # 🌄 عکس از Unsplash (نسخه جدید بدون هشدار)
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        use_container_width=True
    )

# 🌸 صفحه نقل‌قول‌ها
elif menu == "Calming Quote":
    st.header("✨ Calming Quote")
    if st.button("Give me a calming quote"):
        try:
            res = requests.get(f"{API_BASE}/quote")
            if res.status_code == 200:
                data = res.json()
                st.success(f"💬 {data.get('quote', 'No quote found.')}")
            else:
                st.error(f"Error {res.status_code}: {res.text}")
        except Exception:
            st.error("⚠️ Could not connect to the API. Please check your internet or API link.")

# 🌬️ صفحه تمرین تنفس
elif menu == "Breathwork":
    st.header("🧘‍♀️ Guided Breathwork")
    if st.button("Start a short breathing exercise"):
        try:
            res = requests.get(f"{API_BASE}/breathwork")
            if res.status_code == 200:
                data = res.json()
                st.info(f"🫁 {data.get('exercise', 'No exercise found.')}")
            else:
                st.error(f"Error {res.status_code}: {res.text}")
        except Exception:
            st.error("⚠️ Couldn't connect to API.")

# 📈 صفحه پیشرفت کاربر
elif menu == "Track Progress":
    st.header("📊 Track Your Progress")
    user_id = st.text_input("Enter your user ID:", placeholder="e.g. laleh")
    
    if st.button("Show Progress"):
        if user_id:
            try:
                res = requests.get(f"{API_BASE}/progress", params={"user_id": user_id})
                if res.status_code == 200:
                    data = res.json()
                    st.success("Here's your progress 💚")
                    st.json(data)
                else:
                    st.error(f"Error fetching progress: {res.status_code}")
            except Exception:
                st.error("⚠️ Error connecting to server.")
        else:
            st.warning("Please enter your user ID.")
