# Walmart Sales Prediction using Decision Tree Regression

A Machine Learning web application that predicts Walmart sales based on historical sales data using **Decision Tree Regression**. This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict Walmart sales in real time
- Interactive Streamlit web interface
- Decision Tree Regression model
- Instant sales prediction
- Model performance evaluation
- Lightweight and user-friendly interface

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

---

## Dataset

The project uses the **Walmart Sales Dataset**.

### Input Features

The dataset contains sales-related information such as:

- Store information
- Date
- Holiday Flag
- Temperature
- Fuel Price
- CPI
- Unemployment
- Weekly Sales and other relevant attributes

### Target Variable

- Weekly Sales

---

## Machine Learning Model

**Algorithm**

- Decision Tree Regression

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

## Project Workflow

1. Dataset Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Selection
5. Train-Test Split
6. Decision Tree Regression Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter sales-related parameters
- Predict weekly Walmart sales
- View prediction instantly

---

## Project Structure

```text
Walmart Sales (DTR)
│
├── app.py
├── model.pkl
├── Walmart_Sales.csv
├── Walmart_Sales.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/adiba0-0/Supervised_ML_Models.git
```

Move into the project

```bash
cd "Walmart Sales (DTR)"
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Skills Demonstrated

- Data preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Decision Tree Regression
- Regression Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Random Forest and Gradient Boosting comparison
- Feature importance visualization
- Time-series forecasting integration
- Interactive dashboard enhancements
- Cloud deployment
