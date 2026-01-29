import numpy as np
import pandas as pd
import streamlit as st
import joblib

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🩺 Diabetes Prediction App")

st.write("Enter patient details to predict diabetes")

# Input fields
pregnancies = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=17,
    value=1
)

glucose = st.number_input(
    "Glucose (mg/dL)",
    min_value=50,     # avoid 0 (missing)
    max_value=200,
    value=120
)

blood_pressure = st.number_input(
    "Blood Pressure (mm Hg)",
    min_value=40,
    max_value=130,
    value=70
)

skin_thickness = st.number_input(
    "Skin Thickness (mm)",
    min_value=5,
    max_value=99,
    value=20
)

insulin = st.number_input(
    "Insulin (µU/mL)",
    min_value=10,
    max_value=846,
    value=80
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=67.1,
    value=25.0
)

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.078,
    max_value=2.42,
    value=0.5
)

age = st.number_input(
    "Age",
    min_value=21,
    max_value=81,
    value=30
)


# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame(
        [[pregnancies, glucose, blood_pressure, skin_thickness,
          insulin, bmi, dpf, age]],
        columns=[
            'Pregnancies', 'Glucose', 'BloodPressure',
            'SkinThickness', 'Insulin', 'BMI',
            'DiabetesPedigreeFunction', 'Age'
        ]
    )

    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Not Diabetic")
