import streamlit as st
import requests

# Streamlit UI
st.title("Model Prediction App")

# Define inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Button to make prediction
if st.button("Predict"):
    # Send a request to the Flask API
    url = 'http://127.0.0.1:5000/predict'  # URL of the Flask app
    data = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.write(f"Prediction: {prediction}") 
        else: 
            raise Exception(f" {response} - Code: {response.status_code}")
    except Exception as e:
        st.error(f"Bad request: {e}")
