import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide"
)

model = pickle.load(open("model.pkl", "rb"))
df = pd.read_csv("House_price.csv")


st.markdown(
    """
    <h1 style='text-align:center;'>House Price Prediction</h1>
    <h4 style='text-align:center; color:gray;'>
    Estimate the market value of a house using Machine Learning
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()


left, right = st.columns([2, 1])

with left:

    st.subheader("Property Details")

    st.write(
        "Enter the property details below and click **Predict Price** "
        "to estimate the house value."
    )

    area = st.number_input(
        "Average Area Income",
        min_value=25000.0,
        max_value=100000.0,
        value=50000.0,
        step=5000.0
    )

    age = st.slider(
        "House Age (Years)",
        0,
        50,
        5
    )

    rooms = st.number_input(
        "Number of Rooms",
        min_value=1.0,
        max_value=25.0,
        value=2.0,
        step=1.0
    )

    bedrooms = st.number_input(
        "Number of Bedrooms",
        min_value=1.0,
        max_value=25.0,
        value=2.0,
        step=1.0
    )

    population = st.number_input(
        "Area Population",
        min_value=10000.0,
        max_value=100000.0,
        value=50000.0,
        step=5000.0
    )

    predict = st.button(
        "Predict Price",
        use_container_width=True
    )

with right:

    st.subheader("House Price Distribution")

    fig, ax = plt.subplots(figsize=(5,3))

    ax.scatter(
    df["Avg. Area Income"],
    df["Price"],
    alpha=0.5
    )

    ax.set_xlabel("Average Area Income")
    ax.set_ylabel("House Price")
    ax.set_title("Income vs Price")

    st.pyplot(fig)

    st.divider()

    st.caption("**Model Information**")

    st.caption("Algorithm : Linear Regression")

    st.caption("Features : 5")

    st.caption("R² Score : 0.9086")


st.divider()

if predict:

    result = model.predict([[area, age, rooms, bedrooms, population]])

    st.markdown(
        "<h2 style='text-align:center;'>Estimated House Price</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            border:2px solid #2ecc71;
            border-radius:10px;
            padding:20px;
            text-align:center;
            font-size:34px;
            font-weight:bold;
        ">
        ${result[0]:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )