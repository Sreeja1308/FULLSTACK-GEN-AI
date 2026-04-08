import streamlit as st
import plotly.express as px
from prepare_data import load_and_merge_data
from forecast_model import train_prophet
from mongo_utils import save_forecast

# Setup
st.set_page_config(layout="wide")
st.title("📊 Supply Chain Sales Dashboard")

# Load data
df = load_and_merge_data()
store_ids = df['Store'].unique()
dept_ids = df['Dept'].unique()

# Sidebar filters
st.sidebar.header("Filters")
selected_store = st.sidebar.selectbox("Select Store", store_ids)
selected_dept = st.sidebar.selectbox("Select Department", dept_ids)

# Filtered Data
filtered = df[(df["Store"] == selected_store) & (df["Dept"] == selected_dept)]

# Sales Trend
st.subheader(f"📈 Weekly Sales - Store {selected_store}, Dept {selected_dept}")
fig = px.line(
    filtered,
    x="Date",
    y="Weekly_Sales",
    title="Sales Trend",
    labels={"Date": "Date", "Weekly_Sales": "Weekly Sales"}
)
st.plotly_chart(fig, use_container_width=True)

# Forecast
st.subheader("🔮 Forecast (Next 90 Days)")
forecast = train_prophet(selected_store, selected_dept)

try:
    forecast_data = forecast.to_dict(orient="records")
    save_forecast(int(selected_store), int(selected_dept), forecast_data)
    st.success("✅ Forecast data stored in MongoDB.")
except Exception as e:
    st.error(f"❌ MongoDB Error: {e}")

fig2 = px.line(forecast, x="ds", y="yhat", title="Forecast Sales")
fig2.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode="lines", name="Upper")
fig2.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode="lines", name="Lower")
st.plotly_chart(fig2, use_container_width=True)

# Markdown Impact
st.subheader("📝 MarkDown Impact")
markdown_cols = [col for col in filtered.columns if "MarkDown" in col]

if markdown_cols:
    st.bar_chart(filtered[markdown_cols].mean())
else:
    st.info("ℹ️ No MarkDown data available for this selection.")
