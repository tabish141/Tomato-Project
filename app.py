import streamlit as st
import time
import random

# Set initial temperature values
temperature = 18
cold_storage_temp = round(random.uniform(27, 31), 2)

# Function to update cold storage temperature
def update_cold_storage():
    return round(random.uniform(27, 31), 2)

# Streamlit UI
st.title("🍅 Tomato Cold Storage Temperature Control 🍅")

# Display temperature box
st.subheader("Set Temperature")
temp_box = st.empty()

# Temperature adjustment buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Increase Temperature 🔼"):
        if temperature < 23:
            temperature += 1
        else:
            st.warning("It is not an ideal temperature for tomatoes 🍅")
with col2:
    if st.button("Decrease Temperature 🔽"):
        if temperature > 13:
            temperature -= 1
        else:
            st.warning("It is not an ideal temperature for tomatoes 🍅")

# Cold Storage Temperature
st.subheader("Cold Storage Temperature")
cold_temp_box = st.empty()

# Function to continuously update temperature
while True:
    temp_box.markdown(f"### 🍅 {temperature}°C 🍅")

    cold_storage_temp = update_cold_storage()
    cold_temp_box.markdown(f"### ❄️ {cold_storage_temp}°C ❄️")

    time.sleep(3)  # Update every 3 seconds
