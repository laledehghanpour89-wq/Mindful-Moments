import streamlit as st
import requests

# ===============================
# 🌐 Backend API (Render)
# ===============================
API_BASE = "https://mindful-moments-1txj.onrender.com"  # آدرس بک‌اند خودت

# ===============================
# ⚙️ Page Setup
# ===============================
st.set_page_config(page_title="Mindful Moments", page_icon="🌿", layout="centered")
st.title("🌿 Mindful Moments")
st.write("A gentle space for quotes, breathing, and reflection 🌸")

# ===============================
# 🔎 Helper: safe GET
# ===============================
def api_get(path: str, params: dict | None = None, timeout: int = 10):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=timeout)
        return r.status_code, r.json()
    except Exception as e:
        return None, {"error": str(e)}

# ===============================
# 🔌 API Status (always visible)
# ===============================
status_code, status_payload = api_get("/")
col1, col2 = st.columns([1, 4])
with col1:
    if status_code == 200:
        st.success("API: Online")
    elif status_code is None:
        st.error("API: Unreachable")
    else:
        st.warning(f"API: {status_code}")
with col2:
    if isinstance(status_payload, dict) and "message" in status_payload:
        st.caption(status_payload["message"])

st.divider()

# ===============================
# 🧭 Tabs (visible even without sidebar)
# ===============================
tab_home, tab_quote, tab_breath, tab_progress = st.tabs(
    ["🏠 Home", "💬 Calming Quote", "🌬️ Breathwork", "📈 Progress"]
)

# ===============================
# 🏠 HOME (with a button too)
# ===============================
with tab_home:
    st.subheader("Welcome 🌸")
    st.write("Take a deep breath, center yourself, and enjoy your mindful journey 🧘‍♀️")
    # تصویر اختیاری — اگر قبلاً دردسر داشت حذفش کن
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        use_column_width=True,
    )

    st.markdown("### Quick action")
    if st.button("✨ Give me a calming quote (here)"):
        code, data = api_get("/quote")
        if code == 200 and isinstance(data, dict):
            st.success(f"_{data.get('quote', 'Take a deep breath…')}_")
            st.caption(f"— {data.get('author', 'Unknown')}")
        elif code is None:
            st.error("Could not reach API.")
            st.code(data, language="json")
        else:
            st.warning(f"Server responded with {code}")
            st.code(data, language="json")

# ===============================
# 💬 QUOTE
# ===============================
with tab_quote:
    st.subheader("Calming Quote")
    if st.button("Get a Calming Quote"):
        code, data = api_get("/quote")
        if code == 200 and isinstance(data, dict):
            st.success(f"_{data.get('quote', 'Take a deep breath…')}_")
            st.caption(f"— {data.get('author', 'Unknown')}")
        elif code is None:
            st.error("Could not reach API.")
            st.code(data, language="json")
        else:
            st.warning(f"Server responded with {code}")
            st.code(data, language="json")

# ===============================
# 🌬️ BREATHWORK
# ===============================
with tab_breath:
    st.subheader("Guided Breathwork")
    st.write("Follow along this short breathing routine to find calm 🌤️")
    if st.button("Start Breathing Exercise"):
        code, data = api_get("/breathwork")
        if code == 200 and isinstance(data, dict):
            st.info(data.get("exercise", "Inhale… Exhale…"))
        elif code is None:
            st.error("Could not reach API.")
            st.code(data, language="json")
        else:
            st.warning(f"Server responded with {code}")
            st.code(data, language="json")

# ===============================
# 📈 PROGRESS
# ===============================
with tab_progress:
    st.subheader("Track Your Mindfulness Progress")
    user_id = st.text_input("User ID", placeholder="e.g. laleh")
    if st.button("Show Progress"):
        if not user_id:
            st.warning("Please enter a user ID.")
        else:
            code, data = api_get("/progress", params={"user_id": user_id})
            if code == 200:
                st.success("Progress loaded")
                st.code(data, language="json")
            elif code is None:
                st.error("Could not reach API.")
                st.code(data, language="json")
            else:
                st.warning(f"Server responded with {code}")
                st.code(data, language="json")
