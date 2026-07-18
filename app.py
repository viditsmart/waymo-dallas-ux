import streamlit as st
import requests

def calculate_sensor_risk(rain, visibility):
    # Convert text data to math-ready floats
    rain_val = float(rain)
    vis_val = float(visibility)
    
    # Simple algorithmic scoring rule
    # High rain or very low visibility = High Risk
    if rain_val > 5.0 or vis_val < 3.0:
        return "High Risk"
    
    # Moderate rain or moderate visibility = Medium Risk
    elif rain_val > 1.0 or vis_val < 8.0:
        return "Medium Risk"
    
    # Clear conditions = Low Risk
    else:
        return "Low Risk"

# YOUR TASK: Call this function using your live variables 
# and display the result using st.metric()


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
current_rain = weather_data["current_condition"][0]["precipMM"]
current_visibility = weather_data["current_condition"][0]["visibility"]
st.write(f"Current Temperature: {current_temp} degrees F")
risk_level = calculate_sensor_risk(current_rain, current_visibility)
st.metric(label="Waymo Sensor Risk Level ", value = risk_level)
sdi_score = (float(current_rain) * 2) + (10/float(current_visibility))
st.metric(label="SDI score", value=sdi_score)