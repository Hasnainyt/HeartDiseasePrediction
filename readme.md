# Diabetes Prediction

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green)](https://streamlit.io/)

A machine learning project that predicts whether a person is likely to have diabetes based on health data. The project includes data analysis, model training, and a simple **Streamlit web app** for predictions.

---

## 📊 Project Overview

- **Objective:** Predict diabetes using health-related features.
- **Dataset:** Pima Indians Diabetes Database (`diabetes.csv`)  
- **Techniques Used:**  
  - Data preprocessing and exploration  
  - Machine Learning models (e.g., Logistic Regression, Svm, etc.)  
  - Model evaluation (accuracy)  
  - Streamlit for web app interface

---

## 🗂 Repository Structure

DiabetesPrediction/
│
├── diabetes.ipynb # Jupyter notebook with data analysis and model training
├── diabetes.csv # Dataset
├── diabetes_model.pkl # Trained ML model
├── scaler.pkl # Preprocessing scaler
├── app.py # Streamlit web app
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Hasnainyt/DiabetesPrediction.git
cd DiabetesPrediction
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run Jupyter Notebook
jupyter notebook diabetes.ipynb
4️⃣ Run the Streamlit App
streamlit run app.py
Open the URL displayed in the terminal to access the app.

📈 Model Performance
Accuracy: ~[80%]
Trained using the Pima Indians Diabetes dataset


⚡ Features
Simple user interface to input health parameters

Predicts diabetes probability

Easy to extend with new models or features

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

💡 Future Improvements
Hyperparameter tuning for better accuracy

Add more ML models for comparison

Deploy as a cloud web app (e.g., Streamlit Cloud)

📫 Contact
Created by Hasnain YT – GitHub
