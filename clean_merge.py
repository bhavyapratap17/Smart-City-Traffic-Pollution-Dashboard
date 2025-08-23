import pandas as pd

# Load datasets
traffic = pd.read_csv("data/traffic_data.csv")
aqi = pd.read_csv("data/air_quality_data.csv")
weather = pd.read_csv("data/weather_data.csv")

# Convert datetime columns
for df in [traffic, aqi, weather]:
    df['datetime'] = pd.to_datetime(df['datetime'])

# Merge datasets on datetime + location
merged = traffic.merge(aqi, on=["datetime","location"])
merged = merged.merge(weather, on=["datetime","location"])

# Save merged dataset
merged.to_csv("data/merged_city_data.csv", index=False)

print("✅ Merged dataset saved as merged_city_data.csv")
