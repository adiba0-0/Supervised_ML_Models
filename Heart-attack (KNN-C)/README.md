# Heart Attack Prediction using K-Nearest Neighbors Classification

A Machine Learning web application that predicts the likelihood of a heart attack based on patient health indicators using **K-Nearest Neighbors Classification (KNN Classification)**. This project demonstrates the complete Machine Learning workflow, including data preprocessing, feature scaling, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict heart attack risk in real time
- Interactive Streamlit web interface
- K-Nearest Neighbors Classification model
- Feature scaling for improved classification accuracy
- Instant prediction results
- Model performance evaluation

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

The project uses the **Heart Attack Dataset**.

### Input Features

The dataset contains patient health indicators such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression
- Other clinical attributes

### Target Variable

- Heart Attack Risk

Numerical features were standardized before training the model.

---

## Machine Learning Model

**Algorithm**

- K-Nearest Neighbors Classification (KNN Classification)

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Project Workflow

1. Dataset Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Scaling
5. Train-Test Split
6. K-Nearest Neighbors Classification Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter patient health information
- Predict heart attack risk
- View prediction instantly

---

## Project Structure

```text
Heart-attack (KNN-C)
│
├── app.py
├── model.pkl
├── scaler.pkl
├── Heart Attack Data Set.csv
├── Heart-attack.ipynb
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
cd "Heart-attack (KNN-C)"
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
- Feature Scaling
- K-Nearest Neighbors Classification
- Classification Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Weighted KNN implementation
- ROC Curve visualization
- Feature importance analysis
- Enhanced dashboard
- Cloud deployment
