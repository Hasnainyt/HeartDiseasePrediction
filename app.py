import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load saved model and scaler

scaler = joblib.load("scaler.pkl")
svm_model = joblib.load("heart_classifier.pkl")           # SVM model
logreg_model = joblib.load("heart_model.pkl")      # Logistic Regression model

st.title("Heart Disease Prediction System 🫀")
st.write("Enter the patient details below to predict heart condition using SVM and Logistic Regression models.")

# Input fields for features
age = st.number_input("Age", min_value=34, max_value=71, value=50)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Resting Blood Pressure", min_value=100, max_value=180, value=120)
chol = st.number_input("Cholesterol", min_value=131, max_value=360, value=200)
fbs = st.number_input("Fasting Blood Sugar", min_value=0, max_value=2, value=0)
restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2, value=0)
thalach = st.number_input("Max Heart Rate Achieved", min_value=105, max_value=192, value=150)
exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=5.6, value=1.0)
slope = st.number_input("Slope of ST Segment (0-2)", min_value=0, max_value=2, value=1)
ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4, value=0)
thal = st.number_input("Thalassemia (0-3)", min_value=0, max_value=3, value=2)


# Predict button
if st.button("Predict"):
    input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                           thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
    input_scaled = scaler.transform(input_data)
      # Predict with both models
    svm_pred = int(svm_model.predict(input_scaled)[0])
    logreg_pred = int(logreg_model.predict(input_scaled)[0])
    
    # Map predictions to readable labels
    svm_condition = "Healthy" if svm_pred == 0 else "Non Healthy"
    logreg_condition = "Healthy" if logreg_pred == 0 else "Non Healthy"
    
    # Create results DataFrame
    results = pd.DataFrame({
        "Model": ["SVM", "Logistic Regression"],
        "Prediction": [svm_pred, logreg_pred],
        "Heart Condition": [svm_condition, logreg_condition]
    })
    
    # Display results
    st.subheader("Prediction Results:")
    st.table(results)
    
    if logreg_pred == 0:
        st.success("Healthy Heart")
    else:
        st.error("Non Healthy Heart")
        

        
        
