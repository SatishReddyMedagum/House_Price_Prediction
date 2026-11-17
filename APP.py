
import streamlit as st
import pandas as pd
import pickle

# Load Model
with open("house_price_prediction.pkl", "rb") as file:
    model = pickle.load(file)

st.title("House Price Prediction")
st.write("Predict House Prices using Machine Learning")

st.subheader("Enter House Details")

area = st.number_input("Area (Sqft)", min_value=100, max_value=10000, value=1500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
age = st.number_input("Age (Years)", min_value=0, max_value=100, value=5)
parking = st.number_input("Parking", min_value=0, max_value=10, value=1)
floors = st.number_input("Floors", min_value=1, max_value=20, value=2)

location = st.selectbox(
    "Location",
    ["Outskirts", "Suburban", "Metro Area", "Town", "City Center"]
)

location_mapping = {
    "Outskirts": 0,
    "Suburban": 1,
    "Metro Area": 2,
    "Town": 3,
    "City Center": 4
}

if st.button("Predict Price"):

    new_data = pd.DataFrame({
        "Area_sqft": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Age_years": [age],
        "Parking": [parking],
        "Floors": [floors],
        "Location": [location_mapping[location]]
    })

    prediction = model.predict(new_data)

    st.success(f"Predicted House Price: {prediction[0][0]:,.2f}")
