# Tamil Nadu Hill Station Tourism and Climate Analytics

## About This Project
This project analyzes real climate patterns and tourist 
footfall across 5 major Tamil Nadu hill stations to help 
travelers find the best time to visit each destination.

## Hill Stations Covered
- Ooty
- Kodaikanal
- Yercaud
- Coonoor
- Valparai

## What This Project Does
- Fetches REAL climate data using Open-Meteo API
- Analyzes monthly temperature patterns
- Analyzes monthly rainfall patterns
- Studies tourist footfall trends
- Generates Best Time to Visit recommendations
- Creates interactive visualizations

## Data Sources
- Climate Data: Open-Meteo Archive API (Real 2023 data)
- Tourist Footfall: Tamil Nadu Tourism estimates

## Tools and Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- NumPy
- Open-Meteo API (Free, No API key needed)
- Requests

## Charts Generated
- temperature_trends.png - Real monthly temperatures
- rainfall_patterns.png - Real monthly rainfall
- tourist_footfall.png - Monthly tourist footfall
- best_time_heatmap.png - Best time to visit heatmap

## Key Findings
- Ooty and Kodaikanal have the coolest temperatures
- Best time to visit most hill stations is January to March
- Monsoon season July to September has highest rainfall
- Summer months April to June have highest tourist footfall

## How to Run
1. Install required libraries
   pip install requests pandas matplotlib seaborn numpy
2. Run the analysis
   python hill_station_analysis.py
3. View generated charts and recommendations

## Project Structure
- hill_station_analysis.py - Main Python code
- temperature_trends.png - Temperature chart
- rainfall_patterns.png - Rainfall chart
- tourist_footfall.png - Footfall chart
- best_time_heatmap.png - Heatmap chart

