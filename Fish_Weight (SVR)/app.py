import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Fish Weight Prediction",
    layout="wide"
)


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


st.title("Fish Weight Prediction")
st.write("Predict the weight of a fish using a Support Vector Regressor (SVR).")

st.divider()

left, right = st.columns([2, 1])

with left:

    st.header("Enter Fish Details")

    species = st.selectbox(
        "Species",
        [
            "Bream",
            "Roach",
            "Whitefish",
            "Parkki",
            "Perch",
            "Pike",
            "Smelt"
        ]
    )

    species_map = {
        "Bream": 0,
        "Parkki": 1,
        "Perch": 2,
        "Pike": 3,
        "Roach": 4,
        "Smelt": 5,
        "Whitefish": 6
    }

    length1 = st.number_input(
        "Length1",
        min_value=0.0,
        value=20.0
    )

    length2 = st.number_input(
        "Length2",
        min_value=0.0,
        value=22.0
    )

    length3 = st.number_input(
        "Length3",
        min_value=0.0,
        value=25.0
    )

    height = st.number_input(
        "Height",
        min_value=0.0,
        value=8.0
    )

    width = st.number_input(
        "Width",
        min_value=0.0,
        value=4.0
    )

    if st.button("Predict Fish Weight", use_container_width=True):

        input_data = pd.DataFrame([{
            "Species": species_map[species],
            "Length1": length1,
            "Length2": length2,
            "Length3": length3,
            "Height": height,
            "Width": width
        }])

        scaled_input = scaler.transform(input_data)

        prediction = model.predict(scaled_input)

        st.success(f"Estimated Fish Weight: **{prediction[0]:.2f} grams**")


with right:

    st.header("Model Information")

    st.markdown("""
### Algorithm
Support Vector Regressor (SVR)

### Dataset
Fish Weight Dataset

### Target Variable
Weight (grams)

### Evaluation Metric
R² Score

### Kernel
RBF (Radial Basis Function)

### Features Used
- Species
- Length1
- Length2
- Length3
- Height
- Width
""")

    st.divider()

    st.info(
        "Enter the fish measurements on the left and click "
        "'Predict Fish Weight' to estimate its weight."
    )