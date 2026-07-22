# Banknote Authentication using Random Forest Classification

A Machine Learning web application that predicts whether a banknote is **Authentic** or **Forged** using **Random Forest Classification**. This project demonstrates the complete Machine Learning pipeline, including data preprocessing, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict banknote authenticity instantly
- Interactive Streamlit web interface
- Random Forest Classification model
- Real-time prediction
- Model performance evaluation
- Lightweight deployment

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

The project uses the **Banknote Authentication Dataset**.

### Input Features

- Variance
- Skewness
- Curtosis
- Entropy

These statistical image features are extracted from wavelet-transformed images of banknotes.

### Target Variable

- Authentic
- Forged

---

## Machine Learning Model

**Algorithm**

- Random Forest Classification

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
4. Feature Selection
5. Train-Test Split
6. Random Forest Classification Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter banknote feature values
- Predict whether the banknote is authentic or forged
- View prediction instantly

---

## Project Structure

```text
banknote_authentication (RFC)
│
├── app.py
├── model.pkl
├── data_banknote_authentication.csv
├── Banknote_authentication.ipynb
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
cd "banknote_authentication (RFC)"
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
- Feature Selection
- Random Forest Classification
- Classification Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- Feature importance visualization
- ROC Curve analysis
- Enhanced user interface
- Cloud deployment
