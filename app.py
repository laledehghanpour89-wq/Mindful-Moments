import streamlit as st
import requests

# ======================
# 🌿 Basic Page Setup
# ======================
st.set_page_config(
    page_title="Mindful Moments",
    page_icon="🌸",
    layout="centered"
)

API_BASE = "https://mindful-moments-1txj.onrender.com"  # 👈 آدرس backend خودت رو بذار

# ======================
# 🌼 Sidebar Menu
# ======================
st.sidebar.title("🌸 Choose an activity")
menu = st.sidebar.radio("Go to", ["Home", "Calming Quote", "Breathwork", "Track Progress"])

# ======================
# 🏠 HOME PAGE
# ======================
if menu == "Home":
    st.markdown("## 🌿 Mindful Moments")
    st.markdown("A gentle space for quotes, breathing, and reflection 🌷")
    st.markdown("---")
    st.markdown("### Welcome 🌺")
    st.markdown("Take a deep breath, center yourself, and enjoy your mindful journey 🧘‍♀️")

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        use_column_width=True
    )

# ======================
# 🌞 CALMING QUOTE
# ======================
elif menu == "Calming Quote":
    st.header("💬 Calming Quote")
    try:
        res = requests.get(f"{API_BASE}/quote")
        if res.status_code == 200:
            data = res.json()
            st.success(f"✨ *{data['quote']}* — {data['author']}")
        else:
            st.error("Couldn't fetch a quote. Try again later 🌱")
    except Exception:
        st.warning("⚠️ Unable to connect to quote service.")

# ======================
# 🌬️ BREATHWORK
# ======================
elif menu == "Breathwork":
    st.header("🧘‍♀️ Guided Breathwork")
    st.markdown("Follow the rhythm — breathe in calm, breathe out tension 💨")
    st.image(
        "https://images.unsplash.com/photo-1557683316-973673baf926",
        caption="Breathe deeply and slowly 🌬️",
        use_column_width=True
    )
    st.info("🕊️ Try: Inhale 4s — Hold 4s — Exhale 4s — Rest 4s")

# ======================
# 📊 TRACK PROGRESS
# ======================
elif menu == "Track Progress":
    st.header("📈 Track Your Progress")

    user_id = st.text_input("Enter your user ID:", placeholder="e.g. laleh")
    if st.button("Show Progress"):
        if user_id:
            try:
                res = requests.get(f"{API_BASE}/progress", params={"user_id": user_id})
                if res.status_code == 200:
                    data = res.json()
                    st.json(data)
                else:
                    st.error("Error fetching progress.")
            except Exception:
                st.warning("⚠️ Unable to reach the progress API.")
        else:
            st.warning("Please enter your user ID 🙏")

# ======================
# 💖 Footer
# ======================
st.markdown("---")
st.caption("Made with love 🌸 | A space to nurture mindfulness and peace ✨")
