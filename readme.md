# Heart Disease Prediction System 🫀

A Python-based machine learning project that predicts heart disease using **Support Vector Machine (SVM)** and **Logistic Regression** models. The project includes a **Streamlit web application** that allows users to input patient health metrics and get instant predictions.

---

## Features

- Predicts heart disease risk based on 13 clinical features:
  - Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol
  - Fasting Blood Sugar, Resting ECG, Max Heart Rate, Exercise Induced Angina
  - ST Depression (Oldpeak), Slope of ST Segment, Number of Major Vessels, Thalassemia
- Uses **SVM** and **Logistic Regression** for prediction.
- Standardizes input features using the same scaler as the training dataset.
- Displays predictions in a **clean tabular format** showing model results and heart condition.
- Web interface built with **Streamlit** for easy interaction.

---

## Dataset

The dataset `heart.csv` contains heart disease patient records with the following columns:

age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target


- `target` is the label: `0 = Healthy`, `1 = Non Healthy`.

---

## Requirements

- Python >= 3.8
- Libraries:
  - pandas
  - numpy
  - scikit-learn
  - streamlit
  - joblib

Install dependencies using:

```bash
pip install -r requirements.txt
How to Run
Clone the repository:

git clone https://github.com/Hasnainyt/HeartDiseasePrediction.git
cd HeartDiseasePrediction
Run the Streamlit web app:

streamlit run app.py
Open the URL shown in the terminal (usually http://localhost:8501) to access the app.

Input the patient details and click Predict to see results from SVM and Logistic Regression models.

File Structure
heart-disease-prediction/
│
├─ app.py                 # Streamlit web app
├─ heart_model.pkl        # Logistic Regression model
├─ svm_model.pkl          # SVM model
├─ scaler.pkl             # StandardScaler for input
├─ heart.csv              # Dataset
├─ README.md              # Project documentation
└─ requirements.txt       # Python dependencies


Accuracy
Model	Accuracy (Test Set)
SVM	81.95%
Logistic Regression	80.49%
Contributing
Contributions are welcome! Feel free to:

Improve model accuracy

Add more visualization

Enhance the Streamlit app interface

License
This project is licensed under the MIT License.

Author
Your Hasnain

GitHub: Hasnainyt