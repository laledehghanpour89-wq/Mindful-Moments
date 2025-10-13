import streamlit as st
import requests

# ===============================
# 🌐 تنظیم آدرس API آنلاین (Render backend)
# ===============================
API_BASE = "https://mindful-moments-1txj.onrender.com"  # ✅ آدرس دقیق سرور FastAPI

# ===============================
# 🎨 عنوان و هدر
# ===============================
st.set_page_config(page_title="Mindful Moments", page_icon="🌿", layout="centered")

st.title("🌿 Mindful Moments")
st.write("A gentle space for quotes, breathing, and reflection 🌸")

# ===============================
# 🎯 منوی کناری
# ===============================
st.sidebar.title("💫 Choose an activity")
page = st.sidebar.radio("Select", ["Home", "Calming Quote", "Breathwork", "Track Progress"])

# ===============================
# 🏡 صفحه Home
# ===============================
if page == "Home":
    st.header("Welcome 🌸")
    st.write("Take a deep breath, center yourself, and enjoy your mindful journey 🧘‍♀️")

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        use_column_width=True
    )

# ===============================
# 💭 Calming Quote
# ===============================
elif page == "Calming Quote":
    st.header("💬 Calming Quote")

    try:
        res = requests.get(f"{API_BASE}/quote", timeout=10)
        if res.status_code == 200:
            data = res.json()
            if "quote" in data:
                st.success(f"_{data['quote']}_")
                st.caption(f"— {data.get('author', 'Unknown')}")
            else:
                st.warning("No quote found.")
        else:
            st.error(f"Server returned an error: {res.status_code}")

    except Exception as e:
        st.warning("⚠️ Unable to connect to quote service.")
        st.text(f"Error: {e}")

# ===============================
# 🌬️ Breathwork
# ===============================
elif page == "Breathwork":
    st.header("🌬️ Guided Breathwork")
    st.write("Follow along a calming breathing exercise.")

    try:
        res = requests.get(f"{API_BASE}/breathwork", timeout=10)
        if res.status_code == 200:
            st.info(res.json().get("exercise", "Breathe deeply."))
        else:
            st.warning("Unable to load breathing exercise.")
    except Exception as e:
        st.error("Error connecting to breathwork service.")
        st.text(e)

# ===============================
# 📈 Track Progress
# ===============================
elif page == "Track Progress":
    st.header("📈 Track Your Mindfulness Progress")

    user_id = st.text_input("Enter your user ID:")
    if st.button("Show Progress"):
        if user_id:
            try:
                res = requests.get(f"{API_BASE}/progress", params={"user_id": user_id})
                if res.status_code == 200:
                    st.json(res.json())
                else:
                    st.error("Error fetching progress.")
            except Exception as e:
                st.error("Error fetching progress.")
                st.text(e)
        else:
            st.warning("Please enter your user ID.")
