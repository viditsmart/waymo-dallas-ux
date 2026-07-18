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

# 1. Define the URL for Dallas weather in JSON format
url = "https://wttr.in/Dallas?format=j1"

# 2. Make the request to the internet
response = requests.get(url)

# 3. Convert the response into a Python dictionary
weather_data = response.json()
st.json(weather_data)

current_temp = weather_data["current_condition"][0]["temp_F"]
st.write(f"Current Temperature: {current_temp} degrees F")