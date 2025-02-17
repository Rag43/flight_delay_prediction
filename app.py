import streamlit as st
import pandas as pd
import sqlite3
import pickle

#Load trained model
with open("flight_delay_model.pkl", "rb") as file:
    model, feature_names = pickle.load(file)

#Streamlit UI
st.title("Flight Delay Prediction App")

#User input fields
month = st.number_input("Month", min_value=1, max_value=12, value=2)
day = st.number_input("Day", min_value=1, max_value=31, value=15)
departure_time = st.number_input("Departure Time (HHMM Format)", min_value=0, max_value=2359, value=800)
distance = st.number_input("Distance (miles)", min_value=50, max_value=5000, value=500)

#Predict button
if st.button("Predict Delay"):
    #Create input dataframe
    input_data = pd.DataFrame([[month, day, departure_time, distance]], 
                              columns=["month", "day", "departure_time", "distance"])
    # One-hot encode categorical features (airline, origin, destination)
    input_data = pd.get_dummies(input_data)

    # Ensure it has the same columns as training data
    for col in feature_names:
        if col not in input_data.columns:
            input_data[col] = 0  # Add missing columns with value 0
    input_data = input_data[feature_names]

    # Check model type
    print(type(model))

    #Make prediction
    prediction = model.predict(input_data)
    result = "Delayed" if prediction[0] == 1 else "On Time"

    #Display result
    st.subheader(f"Prediction: {result}")