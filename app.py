import streamlit as st
import random
import time

# Initialize session state variables
if "temperature" not in st.session_state:
    st.session_state.temperature = 18

if "cold_storage_temp" not in st.session_state:
    st.session_state.cold_storage_temp = round(random.uniform(27, 31), 2)

# Function to update cold storage temperature
def update_cold_storage():
    st.session_state.cold_storage_temp = round(random.uniform(27, 31), 2)

# Streamlit UI
st.title("🍅 Tomato Cold Storage Temperature Control 🍅")

# Display current temperature
st.subheader("Set Temperature")
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
st.subheader("Cold Storage Temperature")
st.markdown(f"### ❄️ {st.session_state.cold_storage_temp}°C ❄️")

# Auto update cold storage temperature every 3 seconds
time.sleep(3)  # Simulating the delay
update_cold_storage()
st.rerun()
