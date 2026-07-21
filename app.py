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


# 1. Define the URL for Dallas weather in JSON format
url = "https://wttr.in/Dallas?format=j1"

# 2. Make the request to the internet
response = requests.get(url)

# 3. Convert the response into a Python dictionary
weather_data = response.json()


passenger_msg = ""
current_temp = weather_data["current_condition"][0]["temp_F"]
current_rain = weather_data["current_condition"][0]["precipMM"]
current_visibility = weather_data["current_condition"][0]["visibility"]
risk_level = calculate_sensor_risk(current_rain, current_visibility)
sdi_score = (float(current_rain) * 2) + (10/float(current_visibility))

col1, col2 = st.columns(2)
with col1:
    st.subheader("Live Weather Telemetry")
    st.write(f"Current Temperature: {current_temp} degrees F")
    st.write(f"Current rain: {current_rain} mm")
    st.write(f"Current visibility: {current_visibility}")
with col2:
    st.subheader("Sensor Risk Level")
    st.metric(label="SDI score", value=sdi_score)
    st.metric(label="Waymo Sensor Risk Level ", value = risk_level)
    if sdi_score > 8.0:
        passenger_msg = f"Waymo Alert: High risk detected due to heavy weather (Rain: {current_rain} mm, Visibility: {current_visibility} km). Safely pulling over."
        st.error(passenger_msg)
    elif sdi_score > 4.0:
        passenger_msg = f"Waymo Alert: Caution advised. Adjusting operational speed (Rain: {current_rain} mm, Visibility: {current_visibility} km)."
        st.warning(passenger_msg)
    else:
        passenger_msg = f"Waymo Alert: Conditions clear. Vehicle operating normally."
        st.success(passenger_msg)

    