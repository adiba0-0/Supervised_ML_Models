import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


st.set_page_config(
    page_title="Wine Type Prediction",
    layout="wide"
)

model = joblib.load("model.pkl")


st.title("Wine Type Prediction")
st.write("Predict whether a wine is **Red** or **White** using a Decision Tree Classifier.")


features = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
    "quality"
]

st.header("Enter Wine Details")

user_input = []

col1, col2 = st.columns(2)

for i, feature in enumerate(features):

    if i % 2 == 0:
        with col1:
            value = st.number_input(feature, value=0.0)
    else:
        with col2:
            value = st.number_input(feature, value=0.0)

    user_input.append(value)


if st.button("Predict"):

    input_df = pd.DataFrame([user_input], columns=features)

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    st.subheader("Prediction")

    if prediction[0] == 0:
        st.success("Red Wine")
    else:
        st.success("White Wine")

    st.subheader("Prediction Confidence")

    st.write(f"Red Wine : **{probability[0][0]*100:.2f}%**")
    st.write(f"White Wine : **{probability[0][1]*100:.2f}%**")

    st.progress(float(max(probability[0])))


st.divider()

st.subheader("Decision Tree")

fig, ax = plt.subplots(figsize=(24, 12))

plot_tree(
    model,
    feature_names=features,
    class_names=["Red", "White"],
    filled=True,
    rounded=True,
    fontsize=8,
    ax=ax
)

st.pyplot(fig)