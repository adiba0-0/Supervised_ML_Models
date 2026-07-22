import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Dry Bean Classification",
    layout="wide"
)


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


class_names = {
    0: "BARBUNYA",
    1: "BOMBAY",
    2: "CALI",
    3: "DERMASON",
    4: "HOROZ",
    5: "SEKER",
    6: "SIRA"
}


st.title("Dry Bean Classification")
st.write("Predict the bean variety using a Support Vector Classifier (SVC).")

st.divider()

left, right = st.columns([2, 1])


with left:

    st.header("Enter Bean Features")

    area = st.number_input("Area", value=50000.0)
    perimeter = st.number_input("Perimeter", value=800.0)
    major_axis = st.number_input("MajorAxisLength", value=300.0)
    minor_axis = st.number_input("MinorAxisLength", value=180.0)
    aspect_ratio = st.number_input("AspectRation", value=1.6)
    eccentricity = st.number_input("Eccentricity", value=0.8)
    convex_area = st.number_input("ConvexArea", value=51000.0)
    equiv_diameter = st.number_input("EquivDiameter", value=250.0)
    extent = st.number_input("Extent", value=0.75)
    solidity = st.number_input("Solidity", value=0.98)
    roundness = st.number_input("Roundness", value=0.85)
    compactness = st.number_input("Compactness", value=0.80)
    shape_factor_1 = st.number_input("ShapeFactor1", value=0.006)
    shape_factor_2 = st.number_input("ShapeFactor2", value=0.0015)
    shape_factor_3 = st.number_input("ShapeFactor3", value=0.65)
    shape_factor_4 = st.number_input("ShapeFactor4", value=0.99)

    if st.button("Predict Bean Class", use_container_width=True):

        input_data = pd.DataFrame([{
            "Area": area,
            "Perimeter": perimeter,
            "MajorAxisLength": major_axis,
            "MinorAxisLength": minor_axis,
            "AspectRation": aspect_ratio,
            "Eccentricity": eccentricity,
            "ConvexArea": convex_area,
            "EquivDiameter": equiv_diameter,
            "Extent": extent,
            "Solidity": solidity,
            "roundness": roundness,
            "Compactness": compactness,
            "ShapeFactor1": shape_factor_1,
            "ShapeFactor2": shape_factor_2,
            "ShapeFactor3": shape_factor_3,
            "ShapeFactor4": shape_factor_4
        }])

        scaled_input = scaler.transform(input_data)

        prediction = model.predict(scaled_input)[0]

        st.success(f"Predicted Bean Type: **{class_names[prediction]}**")



with right:

    st.header("Model Information")

    st.markdown("""
### Algorithm
Support Vector Classifier (SVC)

### Dataset
Dry Bean Dataset

### Target Variable
Bean Class

### Kernel
RBF

### Evaluation Metric
Accuracy
""")

    st.divider()

    st.info(
        "Enter the bean measurements on the left and click "
        "'Predict Bean Class' to identify the bean variety."
    )