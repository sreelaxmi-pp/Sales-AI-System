import streamlit as st
import pandas as pd
import datetime
from agents.hiring_agent import scrape_hiring
from agents.pricing_agent import detect_pricing_changes
from agents.strategy_agent import generate_strategy

# -----------------------------
# Streamlit Page Setup
# -----------------------------
st.set_page_config(
    page_title="Sales Intelligence AI",
    layout="wide",
    page_icon="🤖"
)

st.title("🤖 AI Competitive Intelligence Dashboard")
st.markdown("---")

# -----------------------------
# 1️⃣ Run the agents
# -----------------------------
hiring_count = scrape_hiring("HubSpot")  # current function: 1 argument
pricing_changes = detect_pricing_changes()
strategy_output = generate_strategy(hiring_count, pricing_changes)

# -----------------------------
# 2️⃣ Top Metrics (Cards)
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💼 Hiring Mentions", hiring_count)

with col2:
    st.metric("💰 Pricing Changes Detected", len(pricing_changes))

with col3:
    st.metric("🧠 Strategy Alerts", len(strategy_output))

st.markdown("---")

# -----------------------------
# 3️⃣ Pricing Changes Panel
# -----------------------------
st.subheader("💰 Pricing Changes")
if pricing_changes:
    for change in pricing_changes:
        st.warning(change, icon="💵")
else:
    st.success("No pricing changes detected.", icon="✅")

# -----------------------------
# 4️⃣ Strategy Recommendations
# -----------------------------
st.subheader("🧠 Strategy Recommendations")
for line in strategy_output:
    st.info(line, icon="💡")

# -----------------------------
# 5️⃣ Hiring Trend Over Time
# -----------------------------
# Persistent memory CSV
today = datetime.date.today()
history_file = "data/history.csv"

# Create dataframe for today
new_data = pd.DataFrame({
    "date": [today],
    "hiring_count": [hiring_count]
})

# Save or append
try:
    if not pd.io.common.file_exists(history_file):
        new_data.to_csv(history_file, index=False)
    else:
        new_data.to_csv(history_file, mode="a", header=False, index=False)
except:
    st.warning("History folder/file not found. Creating data folder.")
    import os
    os.makedirs("data", exist_ok=True)
    new_data.to_csv(history_file, index=False)

# Load history
history = pd.read_csv(history_file)
history['date'] = pd.to_datetime(history['date'])

st.subheader("📊 Hiring Trend Over Time")
st.line_chart(history.set_index("date"), use_container_width=True)

# -----------------------------
# 6️⃣ Last Updated
# -----------------------------
st.caption(f"Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")