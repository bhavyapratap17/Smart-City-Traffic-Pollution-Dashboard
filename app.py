import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart City Traffic & Pollution Dashboard", layout="wide")

st.title("🚦 Smart City Traffic & Pollution Dashboard")

# Load datasets
@st.cache_data
def load_data():
    traffic = pd.read_csv("data/traffic_data.csv")
    air = pd.read_csv("data/air_quality.csv")
    weather = pd.read_csv("data/weather_data.csv")
    return traffic, air, weather

try:
    traffic, air, weather = load_data()
except Exception as e:
    st.error("Please place traffic_data.csv, air_quality.csv, and weather_data.csv inside the data/ folder.")
    st.stop()

# Tabs for different datasets
tab1, tab2, tab3 = st.tabs(["🚗 Traffic Data", "🌫️ Air Quality", "☀️ Weather"])

with tab1:
    st.subheader("Traffic Data Overview")
    st.dataframe(traffic.head())
    if 'Date' in traffic.columns:
        fig = px.line(traffic, x='Date', y=traffic.columns[1], title="Traffic Trend")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Air Quality Data Overview")
    st.dataframe(air.head())
    if 'Date' in air.columns:
        fig = px.line(air, x='Date', y=air.columns[1], title="Air Quality Trend")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Weather Data Overview")
    st.dataframe(weather.head())
    if 'Date' in weather.columns:
        fig = px.line(weather, x='Date', y=weather.columns[1], title="Weather Trend")
        st.plotly_chart(fig, use_container_width=True)
