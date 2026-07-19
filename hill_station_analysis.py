# Tamil Nadu Hill Station Tourism and Climate Analytics
# By Vijaya Lakshmi

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("=" * 60)
print("TN HILL STATION TOURISM AND CLIMATE ANALYTICS")
print("By Vijaya Lakshmi")
print("Fetching Real Climate Data...")
print("=" * 60)

hill_stations = {
    'Ooty': {'lat': 11.4102, 'lon': 76.6950},
    'Kodaikanal': {'lat': 10.2381, 'lon': 77.4892},
    'Yercaud': {'lat': 11.7751, 'lon': 78.2098},
    'Coonoor': {'lat': 11.3530, 'lon': 76.7959},
    'Valparai': {'lat': 10.3271, 'lon': 76.9554}
}

months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']

month_numbers = ['2023-01','2023-02','2023-03',
                 '2023-04','2023-05','2023-06',
                 '2023-07','2023-08','2023-09',
                 '2023-10','2023-11','2023-12']

temp_data = {'Month': months}
rain_data = {'Month': months}

print("Fetching climate data...")

for station, coords in hill_stations.items():
    print(f"Getting data for {station}...")
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": coords['lat'],
        "longitude": coords['lon'],
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "daily": ["temperature_2m_mean", "rain_sum"],
        "timezone": "Asia/Kolkata"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    df_daily = pd.DataFrame({
        'date': pd.to_datetime(data['daily']['time']),
        'temp': data['daily']['temperature_2m_mean'],
        'rain': data['daily']['rain_sum']
    })
    
    df_daily['month'] = df_daily['date'].dt.month
    
    monthly_temp = df_daily.groupby('month')['temp'].mean().round(1).tolist()
    monthly_rain = df_daily.groupby('month')['rain'].sum().round(1).tolist()
    
    temp_data[station] = monthly_temp
    rain_data[station] = monthly_rain

print("Real climate data fetched successfully!")

df_temp = pd.DataFrame(temp_data)
df_rain = pd.DataFrame(rain_data)

footfall_data = {
    'Month': months,
    'Ooty': [45,40,55,70,90,60,50,55,65,75,50,60],
    'Kodaikanal': [40,35,50,65,85,55,45,50,60,70,45,55],
    'Yercaud': [30,25,35,45,60,40,35,38,42,50,35,40],
    'Coonoor': [35,30,42,55,75,48,40,45,52,62,40,48],
    'Valparai': [20,18,25,35,50,35,28,30,38,45,28,32]
}
df_foot = pd.DataFrame(footfall_data)
station_names = list(hill_stations.keys())
colors = ['blue','green','red','orange','purple']

plt.figure(figsize=(14,6))
for i, station in enumerate(station_names):
    plt.plot(months, df_temp[station],
             marker='o', linewidth=2,
             label=station, color=colors[i])
plt.title('Real Monthly Temperature - TN Hill Stations 2023')
plt.xlabel('Month')
plt.ylabel('Temperature Celsius')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_trends.png')
plt.show()
print("Chart 1 saved!")

plt.figure(figsize=(14,6))
for i, station in enumerate(station_names):
    plt.plot(months, df_rain[station],
             marker='s', linewidth=2,
             label=station, color=colors[i])
plt.title('Real Monthly Rainfall - TN Hill Stations 2023')
plt.xlabel('Month')
plt.ylabel('Rainfall mm')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('rainfall_patterns.png')
plt.show()
print("Chart 2 saved!")

plt.figure(figsize=(14,6))
for i, station in enumerate(station_names):
    plt.plot(months, df_foot[station],
             marker='^', linewidth=2,
             label=station, color=colors[i])
plt.title('Monthly Tourist Footfall - TN Hill Stations')
plt.xlabel('Month')
plt.ylabel('Tourists thousands')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('tourist_footfall.png')
plt.show()
print("Chart 3 saved!")

score_data = {}
for station in station_names:
    scores = []
    for i in range(12):
        temp = df_temp[station][i]
        rain = df_rain[station][i]
        foot = df_foot[station][i]
        score = (foot/10) - (rain/50) + (1/abs(temp-18+1))
        scores.append(round(score, 2))
    score_data[station] = scores

df_score = pd.DataFrame(score_data, index=months)

plt.figure(figsize=(12,6))
sns.heatmap(df_score.T,
            annot=True,
            fmt='.1f',
            cmap='RdYlGn',
            xticklabels=months,
            yticklabels=station_names)
plt.title('Best Time to Visit Score Green is Best Red is Avoid')
plt.tight_layout()
plt.savefig('best_time_heatmap.png')
plt.show()
print("Chart 4 saved!")

print("\n" + "=" * 60)
print("BEST TIME TO VISIT RECOMMENDATIONS")
print("=" * 60)

for station in station_names:
    best_month = df_score[station].idxmax()
    worst_month = df_score[station].idxmin()
    avg_temp = round(df_temp[station].mean(), 1)
    avg_rain = round(df_rain[station].mean(), 1)
    print(f"\n{station}")
    print(f"   Best Month   : {best_month}")
    print(f"   Avoid Month  : {worst_month}")
    print(f"   Avg Temp     : {avg_temp} Celsius")
    print(f"   Avg Rainfall : {avg_rain} mm")

print("\n" + "=" * 60)
print("Analysis Complete!")
print("=" * 60)