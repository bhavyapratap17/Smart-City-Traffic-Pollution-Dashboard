# 🌆 Smart City Traffic & Pollution Dashboard

## 📌 Project Overview
Developed an interactive Power BI dashboard analyzing **traffic density, air quality, and weather data** to study their correlation with pollution levels.  
The dashboard provides **predictive insights** for optimal travel routes and time slots, helping reduce congestion and emissions.

---

## 📂 Project Structure
```
Smart-City-Traffic-Pollution-Dashboard/
│── README.md
│── data/
│   ├── traffic_data.csv
│   ├── air_quality_data.csv
│   ├── weather_data.csv
│   └── merged_city_data.csv (generated after running clean_merge.py)
│
│── preprocessing/
│   └── clean_merge.py
│
│── dashboard/
│   └── SmartCity_Dashboard.pbix (Power BI file - add manually)
│
│── images/
│   ├── dashboard_overview.png
│   ├── correlation_plot.png
│   └── map_view.png
```

---

## 📊 Dashboard Features
- Interactive **map view** of traffic + pollution hotspots.
- **Time-series analysis** of AQI vs traffic vs weather.
- **Correlation analysis** (scatter plots, regression).
- **Forecasting model** to predict AQI & congestion.
- **KPIs**: Current AQI, congestion %, best travel time.

---

## 🛠️ Tools & Skills
- **Power BI** → Dashboarding, DAX, Data Modeling
- **Excel / Power Query** → Data Cleaning
- **Python (pandas)** → Preprocessing & merging data
- **Data Analytics** → Correlation, Time-series Forecasting

---

## 📑 Datasets
- `traffic_data.csv` → vehicle count, avg speed, congestion
- `air_quality_data.csv` → AQI, pollutants, category
- `weather_data.csv` → temp, humidity, wind, rainfall
- `merged_city_data.csv` → combined dataset for dashboard

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/bhavyapratap17/Smart-City-Traffic-Pollution-Dashboard.git
   ```
2. Run preprocessing (optional):
   ```bash
   python preprocessing/clean_merge.py
   ```
3. Open `dashboard/SmartCity_Dashboard.pbix` in **Power BI Desktop**.
4. Explore interactive reports & filters.

---

## 📸 Screenshots
*(Add images here from /images folder)*  
![Dashboard Overview](images/dashboard_overview.png)

---

## 🔮 Future Enhancements
- Real-time dashboard using APIs
- IoT sensor data integration
- Advanced ML pollution forecasting

---

## 📜 License
MIT License
