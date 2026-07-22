import numpy as np
import streamlit as st
import joblib

st.set_page_config(
    page_title="Students Performance Predictor",
    layout="centered"
)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("Students Reading Score Predictor")
st.write("Predict the **Reading Score** of a student using the KNN Regressor model.")

gender = st.selectbox("Gender", ["Male", "Female"])

race = st.selectbox(
    "Race/Ethnicity",
    ["Group A", "Group B", "Group C", "Group D", "Group E"]
)

parent_edu = st.selectbox(
    "Parental Level of Education",
    [
        "High School",
        "Some High School",
        "Some College",
        "Associate Degree",
        "Bachelor's Degree",
        "Master's Degree"
    ]
)

lunch = st.selectbox(
    "Lunch",
    ["Standard", "Free/Reduced"]
)

prep = st.selectbox(
    "Test Preparation Course",
    ["None", "Completed"]
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=70,
    step=1
)

if st.button("Predict Reading Score"):

    data = np.array([[writing_score]])
    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Predicted Reading Score: **{prediction[0]:.2f}**")

    st.info(
        "Note: This model was trained using only the Writing Score "
        "to predict the Reading Score."
    )