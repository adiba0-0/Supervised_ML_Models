import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Heart Attack Prediction",
    layout="centered"
)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.markdown("""
<style>
div.stButton > button{
    width:100%;
    height:3em;
    font-size:18px;
    font-weight:bold;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

st.title("Heart Attack Prediction using KNN Classifier")
st.write("Enter the patient's details to predict the risk of a heart attack.")

age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox(
    "Gender",
    ["Female", "Male"]
)
sex = 0 if sex == "Female" else 1

cp_dict = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-Anginal Pain": 2,
    "Asymptomatic": 3
}

cp = st.selectbox("Chest Pain Type", list(cp_dict.keys()))
cp = cp_dict[cp]

trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Serum Cholesterol (mg/dl)",
    min_value=100,
    max_value=600,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    ["No", "Yes"]
)
fbs = 0 if fbs == "No" else 1

restecg_dict = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}

restecg = st.selectbox(
    "Resting ECG Result",
    list(restecg_dict.keys())
)
restecg = restecg_dict[restecg]

thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=60,
    max_value=220,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)
exang = 0 if exang == "No" else 1

oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope_dict = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    list(slope_dict.keys())
)
slope = slope_dict[slope]

ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3, 4]
)

thal_dict = {
    "Normal": 0,
    "Fixed Defect": 1,
    "Reversible Defect": 2,
    "Unknown": 3
}

thal = st.selectbox(
    "Thalassemia",
    list(thal_dict.keys())
)
thal = thal_dict[thal]

if st.button("Predict Heart Attack Risk"):

    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Heart Attack")
    else:
        st.success("Low Risk of Heart Attack")