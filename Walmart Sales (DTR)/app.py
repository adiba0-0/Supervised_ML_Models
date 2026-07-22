import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn import tree

st.set_page_config(
    page_title="Walmart Weekly Sales Predictor",
    layout="wide"
)

model = pickle.load(open("model.pkl", "rb"))
df = pd.read_csv("Walmart_Sales.csv")

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

st.title("Walmart Weekly Sales Prediction")
st.write("Predict Walmart's weekly sales using a **Decision Tree Regressor**.")

st.divider()

left, right = st.columns([2, 1])

with left:

    st.subheader("Enter Sales Details")

    store = st.number_input(
        "Store Number",
        min_value=1,
        value=1
    )

    holiday = st.selectbox(
        "Holiday Week",
        ["No", "Yes"]
    )

    temperature = st.number_input(
        "Temperature (°F)",
        value=60.0
    )

    fuel = st.number_input(
        "Fuel Price ($)",
        value=3.0
    )

    cpi = st.number_input(
        "CPI",
        value=float(df["CPI"].mean())
    )

    unemployment = st.number_input(
        "Unemployment",
        value=float(df["Unemployment"].mean())
    )

    day = st.slider(
        "Day",
        1,
        31,
        1
    )

    month = st.slider(
        "Month",
        1,
        12,
        1
    )

    year = st.selectbox(
        "Year",
        sorted(df["Year"].unique())
    )

    predict = st.button(
        "Predict Weekly Sales",
        use_container_width=True
    )

with right:

    st.subheader("Decision Tree")

    fig, ax = plt.subplots(figsize=(7, 5))

    tree.plot_tree(
        model,
        max_depth=2,
        filled=True,
        rounded=True,
        impurity=False,
        precision=0,
        fontsize=7,
        feature_names=[
            "Store",
            "Holiday",
            "Temp",
            "Fuel",
            "CPI",
            "Unemp",
            "Day",
            "Month",
            "Year"
        ],
        ax=ax
    )

    st.pyplot(fig)

    st.divider()

    st.subheader("Model Information")

    st.markdown("""
**Algorithm:** Decision Tree Regressor

**Training Score:** **1.0000**

**Testing Score:** **0.9364**

**Features Used:** **9**

**Target Variable:** **Weekly Sales**
""")

    st.divider()

    if predict:

        holiday = 1 if holiday == "Yes" else 0

        features = [[
            store,
            holiday,
            temperature,
            fuel,
            cpi,
            unemployment,
            day,
            month,
            year
        ]]

        prediction = model.predict(features)

        st.subheader("Sales Prediction")

        st.metric(
            label="Estimated Weekly Sales",
            value=f"${prediction[0]:,.2f}"
        )