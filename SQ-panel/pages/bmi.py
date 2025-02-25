

import streamlit as st

# Set Page Title
st.title("⚖️ BMI Calculator")

# User Inputs for Height and Weight
height = st.number_input("Insert your height in feet", min_value=1.0, step=0.1)
weight = st.number_input("Insert your weight in KG", min_value=1.0, step=0.1)

if st.button("Calculate BMI"):
    # Convert height from feet to meters (1 feet = 0.3048 meters)
    height_meters = height * 0.3048

    # Calculate BMI
    bmi = weight / (height_meters ** 2)

    # Display BMI result
    st.success(f"📊 Your BMI is {bmi:.2f}")

    # Determine BMI Category
    if bmi < 18.5:
        st.warning("⚠️ You are underweight.")
    elif 18.5 <= bmi <= 24.9:
        st.success("✅ You have a normal weight.")
    elif 25 <= bmi <= 29.9:
        st.warning("⚠️ You are overweight.")
    else:
        st.error("🚨 You are obese.")
