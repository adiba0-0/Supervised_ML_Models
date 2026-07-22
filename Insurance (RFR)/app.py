import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Insurance Cost Prediction",
    layout="wide"
)


model = joblib.load("model.pkl")


st.title("Medical Insurance Cost Prediction")
st.write("Predict medical insurance charges using a Random Forest Regressor.")

st.divider()


left, right = st.columns([2, 1])


with left:

    st.header("Enter Customer Details")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    children = st.number_input(
        "Children",
        min_value=0,
        max_value=10,
        value=0
    )

    smoker = st.selectbox(
        "Smoker",
        ["No", "Yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]
    )


    sex = 0 if sex == "Male" else 1
    smoker = 1 if smoker == "Yes" else 0

    region_northwest = 1 if region == "northwest" else 0
    region_southeast = 1 if region == "southeast" else 0
    region_southwest = 1 if region == "southwest" else 0


    if st.button("Predict Insurance Cost", use_container_width=True):

        input_data = pd.DataFrame([{
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "children": children,
            "smoker": smoker,
            "region_northwest": region_northwest,
            "region_southeast": region_southeast,
            "region_southwest": region_southwest
        }])

        prediction = model.predict(input_data)

        st.success(
            f"Estimated Insurance Cost: **${prediction[0]:,.2f}**"
        )


with right:

    st.header("Feature Importance")

    feature_names = [
        "Age",
        "Sex",
        "BMI",
        "Children",
        "Smoker",
        "Region (NW)",
        "Region (SE)",
        "Region (SW)"
    ]

    importance = pd.Series(
        model.feature_importances_,
        index=feature_names
    ).sort_values()

    fig, ax = plt.subplots(figsize=(7, 4.8))

    importance.plot(
        kind="barh",
        ax=ax
    )

    ax.set_title("Feature Importance")
    ax.set_xlabel("Importance Score")

    st.pyplot(fig)

    st.divider()

    st.subheader("Model Information")

    st.markdown("""
**Algorithm:** Random Forest Regressor

**Dataset:** Medical Insurance Cost Dataset

**Target Variable:** Insurance Charges

**Evaluation Metric:** R² Score

**Training Score:** **0.974**

**Testing Score:** **0.879**
""")