import streamlit as st
import requests

# --- Page config ---
st.set_page_config(page_title="Mindful Moments 🌿", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🌸 Mindful Moments")
page = st.sidebar.radio("Choose an activity:", ["Home", "Calming Quote", "Breathwork", "Progress"])

API_URL = "https://mindful-moments-1txj.onrender.com"  # API backend address

# --- Home Page ---
if page == "Home":
    st.title("🌿 Mindful Moments")
    st.write("A gentle space for quotes, breathing, and reflection 🌸")

    st.success("Mindful Moments API is running")
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        caption="Take a deep breath 🌅",
        use_container_width=True
    )
    st.markdown("Take a deep breath, center yourself, and enjoy your mindful journey 🧘‍♀️")

# --- Calming Quote Page ---
elif page == "Calming Quote":
    st.title("💬 Calming Quote")
    try:
        res = requests.get(f"{API_URL}/quote")
        if res.status_code == 200:
            data = res.json()
            st.success(f"✨ {data.get('quote', 'Keep calm and breathe.')}")
            st.caption(f"- {data.get('author', 'Unknown')}")
        else:
            st.warning("⚠️ Unable to connect to quote service.")
    except Exception as e:
        st.error("Could not connect to API ❌")

# --- Breathwork Page ---
elif page == "Breathwork":
    st.title("🌬️ Breathwork")
    st.write("Follow this simple breathing rhythm:")
    st.markdown("**Inhale** for 4s → **Hold** for 4s → **Exhale** for 4s 🌿")
    if st.button("Start Session"):
        st.balloons()
        st.info("Keep breathing mindfully 💫")

# --- Progress Page ---
elif page == "Progress":
    st.title("📊 Progress Tracker")
    st.write("Track your mindfulness journey 🪷")
    st.info("Progress tracking will be added soon ✨")

# --- Footer ---
st.markdown("---")
st.caption("Made with 💕 | A space to nurture mindfulness and peace ✨")
