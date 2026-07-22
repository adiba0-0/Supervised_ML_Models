import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Breast Cancer Prediction",
    layout="wide"
)


model = joblib.load("model.pkl")


st.title("Breast Cancer Prediction System")

st.markdown("""
This application predicts whether a breast tumor is **Benign** or **Malignant**
using a **Logistic Regression Model**.
""")

st.sidebar.title("About")
st.sidebar.info("""
Project: Breast Cancer Prediction

Algorithm:
✔ Logistic Regression

Dataset:
Breast Cancer Wisconsin Dataset
""")


features = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "smoothness_mean",
    "compactness_mean",
    "concavity_mean",
    "concave points_mean",
    "symmetry_mean",
    "fractal_dimension_mean",

    "radius_se",
    "texture_se",
    "perimeter_se",
    "area_se",
    "smoothness_se",
    "compactness_se",
    "concavity_se",
    "concave points_se",
    "symmetry_se",
    "fractal_dimension_se",

    "radius_worst",
    "texture_worst",
    "perimeter_worst",
    "area_worst",
    "smoothness_worst",
    "compactness_worst",
    "concavity_worst",
    "concave points_worst",
    "symmetry_worst",
    "fractal_dimension_worst"
]


st.header("Enter Patient Details")

user_input = []

col1, col2 = st.columns(2)

for i, feature in enumerate(features):

    if i % 2 == 0:
        with col1:
            value = st.number_input(feature, value=0.0, format="%.5f")
    else:
        with col2:
            value = st.number_input(feature, value=0.0, format="%.5f")

    user_input.append(value)


if st.button("Predict"):

    input_df = pd.DataFrame([user_input], columns=features)

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.error("Malignant Tumor Detected")
    else:
        st.success("Benign Tumor Detected")

    st.subheader("Prediction Probability")

    st.write(f"Malignant : **{probability[0][0]*100:.2f}%**")
    st.write(f"Benign : **{probability[0][1]*100:.2f}%**")

    st.progress(float(max(probability[0])))

st.divider()