import streamlit as st
import random
import time
import pandas as pd

# Initialize session state variables
if "temperature" not in st.session_state:
    st.session_state.temperature = 18

if "cold_storage_temp" not in st.session_state:
    st.session_state.cold_storage_temp = round(random.uniform(27, 31), 2)

if "temperature_data" not in st.session_state:
    st.session_state.temperature_data = pd.DataFrame(columns=["Time", "Set Temperature", "Cold Storage Temperature"])

# Function to update cold storage temperature
def update_cold_storage():
    new_temp = round(random.uniform(27, 31), 2)
    st.session_state.cold_storage_temp = new_temp
    current_time = time.strftime("%H:%M:%S")  # Get current time
    
    # Append new data
    new_data = pd.DataFrame(
        [[current_time, st.session_state.temperature, new_temp]], 
        columns=["Time", "Set Temperature", "Cold Storage Temperature"]
    )
    st.session_state.temperature_data = pd.concat([st.session_state.temperature_data, new_data], ignore_index=True)

# Streamlit UI
st.title("🍅 Tomato Cold Storage Temperature Control 🍅")

# Display current temperature
st.subheader("SET TEMPERATURE")
st.markdown(f"### 🍅 {st.session_state.temperature}°C 🍅")

# Temperature adjustment buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Increase Temperature 🔼"):
        if st.session_state.temperature < 23:
            st.session_state.temperature += 1
        else:
            st.warning("It is not an ideal temperature for tomatoes 🍅")
with col2:
    if st.button("Decrease Temperature 🔽"):
        if st.session_state.temperature > 13:
            st.session_state.temperature -= 1
        else:
            st.warning("It is not an ideal temperature for tomatoes 🍅")

# Cold Storage Temperature
st.subheader("CURRENT COLD STORAGE TEMPERATURE.")
st.markdown(f"### ❄️ {st.session_state.cold_storage_temp}°C ❄️")

# Update temperature data
update_cold_storage()

# Display Temperature Graph
st.subheader("📊 Temperature Performance Over Time")
st.line_chart(st.session_state.temperature_data.set_index("Time"))

# Auto update cold storage temperature every 3 seconds
time.sleep(3)  
st.rerun()
