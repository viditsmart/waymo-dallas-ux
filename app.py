import streamlit as st
import requests


st.title("Waymo Dallas Weather-UX Dashboard")

# Fake data that mimics a real weather API response
fake_weather_data = {
    "city": "Dallas",
    "main": {
        "temperature_f": 98.5,
        "humidity": 75
    },
    "weather_conditions": [
        {"type": "Rain", "severity": "Heavy"}
    ]
}

# YOUR TASK: Extract data from the dictionary above
# Hint: To get the city, you would write: fake_weather_data["city"]
st.write(fake_weather_data["main"]["temperature_f"])
st.write(fake_weather_data["weather_conditions"][0]["severity"])