import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Banknote Authentication",
    layout="wide"
)

model = joblib.load("model.pkl")

st.title("Banknote Authentication")
st.write("Predict whether a banknote is Genuine or Fake using a Random Forest Classifier.")

st.divider()


left, right = st.columns([2, 1])


with left:

    st.header("Enter Banknote Details")

    variance = st.number_input(
        "Variance",
        value=2.0,
        format="%.4f"
    )

    skewness = st.number_input(
        "Skewness",
        value=3.0,
        format="%.4f"
    )

    curtosis = st.number_input(
        "Curtosis",
        value=1.0,
        format="%.4f"
    )

    entropy = st.number_input(
        "Entropy",
        value=0.0,
        format="%.4f"
    )

    if st.button("Authenticate Banknote", use_container_width=True):

        input_data = pd.DataFrame([{
            "Variance_Wavelet": variance,
            "Skewness_Wavelet": skewness,
            "Curtosis_Wavelet": curtosis,
            "Image_Entropy": entropy
        }])

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)

        if prediction[0] == 1:
            st.success("Genuine Banknote")
        else:
            st.error("Fake Banknote")

        st.subheader("Prediction Confidence")

        st.write(f"Fake : **{probability[0][0]*100:.2f}%**")
        st.write(f"Genuine : **{probability[0][1]*100:.2f}%**")

        st.progress(float(max(probability[0])))


with right:

    st.header("Feature Importance")

    feature_names = [
        "Variance",
        "Skewness",
        "Curtosis",
        "Entropy"
    ]

    importance = pd.Series(
        model.feature_importances_,
        index=feature_names
    ).sort_values()

    fig, ax = plt.subplots(figsize=(7,4.5))

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
**Algorithm:** Random Forest Classifier

**Dataset:** Banknote Authentication Dataset

**Target Variable:** Class

**Evaluation Metric:** Accuracy

**Training Accuracy:** **100%**

**Testing Accuracy:** **98.52%**
""")