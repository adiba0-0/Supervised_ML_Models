# Insurance Cost Prediction using Random Forest Regression

A Machine Learning web application that predicts medical insurance charges based on personal and demographic information using **Random Forest Regression**. This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict medical insurance charges in real time
- Interactive Streamlit web interface
- Random Forest Regression model
- Instant prediction results
- Model performance evaluation
- Lightweight and user-friendly deployment

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

The project uses the **Medical Insurance Cost Dataset**.

### Input Features

- Age
- Sex
- Body Mass Index (BMI)
- Number of Children
- Smoking Status
- Region

### Target Variable

- Insurance Charges

Categorical variables were encoded during preprocessing before training the model.

---

## Machine Learning Model

**Algorithm**

- Random Forest Regression

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

## Project Workflow

1. Dataset Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Encoding Categorical Features
5. Train-Test Split
6. Random Forest Regression Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter personal and medical information
- Predict estimated insurance charges
- View prediction instantly

---

## Project Structure

```text
Insurance (RFR)
│
├── app.py
├── model.pkl
├── insurance.csv
├── Insurance_Cost.ipynb
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
cd "Insurance (RFR)"
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
- Categorical Data Encoding
- Random Forest Regression
- Regression Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Feature importance visualization
- Model comparison with XGBoost and Gradient Boosting
- Prediction confidence intervals
- Enhanced dashboard
- Cloud deployment
