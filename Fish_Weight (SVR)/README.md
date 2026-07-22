# Fish Weight Prediction using Support Vector Regression

A Machine Learning web application that predicts the weight of a fish based on its physical measurements using **Support Vector Regression (SVR)**. This project demonstrates the complete Machine Learning workflow, including data preprocessing, feature scaling, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict fish weight in real time
- Interactive Streamlit web interface
- Support Vector Regression (SVR) model
- Feature scaling for improved prediction accuracy
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

The project uses the **Fish Market Dataset**.

### Input Features

- Species
- Length1
- Length2
- Length3
- Height
- Width

### Target Variable

- Weight

Categorical features were encoded and numerical features were scaled before training the model.

---

## Machine Learning Model

**Algorithm**

- Support Vector Regression (SVR)

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

## Project Workflow

1. Dataset Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Encoding
5. Feature Scaling
6. Train-Test Split
7. Support Vector Regression Model Training
8. Model Evaluation
9. Model Serialization using Pickle
10. Streamlit Application Development

---

## Application

Users can:

- Enter fish characteristics
- Predict fish weight
- View prediction instantly

---

## Project Structure

```text
Fish_Weight (SVR)
│
├── app.py
├── model.pkl
├── scaler.pkl
├── Fish.csv
├── Fish_Weight.ipynb
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
cd "Fish_Weight (SVR)"
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
- Feature Encoding
- Feature Scaling
- Support Vector Regression
- Regression Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Kernel comparison (Linear, Polynomial, RBF)
- Advanced feature engineering
- Interactive visualizations
- Cloud deployment
