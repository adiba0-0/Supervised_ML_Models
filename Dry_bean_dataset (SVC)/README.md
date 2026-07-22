# Dry Bean Classification using Support Vector Classification

A Machine Learning web application that classifies dry bean varieties based on their morphological characteristics using **Support Vector Classification (SVC)**. This project demonstrates the complete Machine Learning workflow, including data preprocessing, feature scaling, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict dry bean variety in real time
- Interactive Streamlit web interface
- Support Vector Classification (SVC) model
- Feature scaling for improved classification performance
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

The project uses the **Dry Bean Dataset**.

### Input Features

The dataset contains several morphological measurements extracted from bean images, including:

- Area
- Perimeter
- Major Axis Length
- Minor Axis Length
- Aspect Ratio
- Eccentricity
- Convex Area
- Equivalent Diameter
- Extent
- Solidity
- Roundness
- Compactness
- Shape Factors

### Target Variable

- Dry Bean Class

Numerical features were standardized before training the model.

---

## Machine Learning Model

**Algorithm**

- Support Vector Classification (SVC)

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
6. Support Vector Classification Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter bean characteristics
- Predict the bean variety
- View prediction instantly

---

## Project Structure

```text
Dry_bean_dataset (SVC)
│
├── app.py
├── model.pkl
├── scaler.pkl
├── Dry_Bean_Dataset.csv
├── dry_bean.ipynb
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
cd "Dry_bean_dataset (SVC)"
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
- Support Vector Classification
- Classification Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Kernel comparison (Linear, Polynomial, RBF)
- Cross-validation
- Feature importance analysis
- Enhanced user interface
- Cloud deployment
