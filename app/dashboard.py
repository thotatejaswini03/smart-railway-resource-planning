import sys
import os

# Fix import issue
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from src.recommendation import recommend_coaches

st.set_page_config(page_title="Smart Railway Control Center", layout="wide")

# Load data
df = pd.read_csv("data/railway_data.csv")
model = joblib.load("models/demand_model.pkl")

df["route"] = df["Source"] + " - " + df["Destination"]
df["Date"] = pd.to_datetime(df["Date"])
df["Hour"] = df["Time"].str.split(":").str[0].astype(int)

st.title("🚆 Smart Railway Resource Planning System")
st.markdown("AI-powered decision support dashboard for railway planners")

# ------------------------------------------------
# KPI METRICS (TOP CONTROL PANEL)
# ------------------------------------------------

total_passengers = df["Passenger_Count"].sum()
total_trains = df["Train_ID"].nunique()
avg_passengers = df["Passenger_Count"].mean()
avg_delay = df["Delay"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Passengers", f"{int(total_passengers):,}")
col2.metric("Active Trains", total_trains)
col3.metric("Avg Passengers/Train", int(avg_passengers))
col4.metric("Average Delay (min)", round(avg_delay,2))

st.divider()

# ------------------------------------------------
# DEMAND PREDICTION PANEL
# ------------------------------------------------

st.sidebar.header("🔮 Passenger Demand Prediction")

route = st.sidebar.selectbox("Route", df["route"].unique())
holiday = st.sidebar.selectbox("Holiday", [0,1])
month = st.sidebar.slider("Month",1,12)
day = st.sidebar.slider("Day of Week (0=Mon)",0,6)
coaches = st.sidebar.slider("Number of Coaches",10,16)

route_code = df[df["route"]==route]["route"].astype("category").cat.codes.iloc[0]

input_data = [[day,month,route_code,holiday]]

if st.sidebar.button("Predict Demand"):

    pred = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")

    st.metric("Predicted Passenger Demand", int(pred))

    recommendation = recommend_coaches(pred, coaches)

    st.success(recommendation)

    capacity = coaches * 72

    if pred > capacity * 0.9:
        st.error("⚠ High Overcrowding Risk!")

st.divider()

# ------------------------------------------------
# ROUTE DEMAND VISUALIZATION
# ------------------------------------------------

st.header("📈 Route Demand Analysis")

route_demand = df.groupby("route")["Passenger_Count"].mean().reset_index()

fig = px.bar(
    route_demand,
    x="route",
    y="Passenger_Count",
    color="Passenger_Count",
    title="Average Passenger Demand by Route"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------
# PASSENGER TREND
# ------------------------------------------------

st.header("📅 Passenger Demand Trend")

trend = df.groupby("Date")["Passenger_Count"].sum().reset_index()

fig2 = px.line(
    trend,
    x="Date",
    y="Passenger_Count",
    title="Total Passenger Demand Over Time"
)

st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------
# PEAK TRAVEL HOURS
# ------------------------------------------------

st.header("🔥 Peak Travel Time Detection")

peak_hours = df.groupby("Hour")["Passenger_Count"].mean().reset_index()

fig3 = px.line(
    peak_hours,
    x="Hour",
    y="Passenger_Count",
    markers=True,
    title="Average Passenger Demand by Hour"
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------
# PLATFORM UTILIZATION
# ------------------------------------------------

st.header("🚉 Platform Congestion Analysis")

platform_usage = df.groupby("Platform")["Train_ID"].count().reset_index()

fig4 = px.bar(
    platform_usage,
    x="Platform",
    y="Train_ID",
    color="Train_ID",
    title="Platform Utilization"
)

st.plotly_chart(fig4, use_container_width=True)

# ------------------------------------------------
# POPULAR ROUTES
# ------------------------------------------------

st.header("🏆 Most Popular Routes")

popular_routes = df.groupby("route")["Passenger_Count"].sum().reset_index()
popular_routes = popular_routes.sort_values(by="Passenger_Count", ascending=False)

st.dataframe(popular_routes.head(10))

# ------------------------------------------------
# AI ALERT SYSTEM
# ------------------------------------------------

st.header("🚨 AI Operational Alerts")

alerts = []

for _, row in df.iterrows():

    capacity = row["Coaches"] * 72
    occupancy = row["Passenger_Count"] / capacity

    if occupancy > 0.9:
        alerts.append(
            f"⚠ Train {row['Train_ID']} on route {row['Source']}–{row['Destination']} is overcrowded"
        )

if len(alerts) > 0:

    for a in alerts[:5]:
        st.warning(a)

else:
    st.success("No major operational alerts detected")