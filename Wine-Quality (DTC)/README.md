# Wine Quality Prediction using Decision Tree Classification

A Machine Learning web application that predicts the quality of wine based on its physicochemical properties using **Decision Tree Classification**. This project demonstrates the complete Machine Learning pipeline from data preprocessing and model training to evaluation and deployment through an interactive Streamlit application.

---

## Features

- Predict wine quality instantly
- Interactive Streamlit web interface
- Decision Tree Classification model
- Real-time predictions
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

The project uses the **Wine Quality Dataset**.

### Input Features

The dataset contains physicochemical properties such as:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

### Target Variable

- Wine Quality

---

## Machine Learning Model

**Algorithm**

- Decision Tree Classification

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
3. Data Cleaning
4. Feature Selection
5. Train-Test Split
6. Decision Tree Classification Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter wine characteristics
- Predict wine quality
- View prediction instantly

---

## Project Structure

```text
Wine-Quality (DTC)
│
├── app.py
├── model.pkl
├── winequalityN.csv
├── Wine-Quality.ipynb
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
cd "Wine-Quality (DTC)"
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
- Decision Tree Classification
- Classification Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Random Forest and XGBoost comparison
- Cross-validation
- Feature importance visualization
- Enhanced UI/UX
- Cloud deployment
