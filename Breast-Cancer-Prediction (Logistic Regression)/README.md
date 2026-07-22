# Breast Cancer Prediction using Logistic Regression

A Machine Learning web application that predicts whether a breast tumor is **Benign** or **Malignant** using **Logistic Regression**. The project demonstrates the complete Machine Learning pipeline, including data preprocessing, model training, evaluation, and deployment through an interactive **Streamlit** application.

---

## Features

- Breast cancer prediction
- Logistic Regression classifier
- Interactive Streamlit interface
- Instant predictions
- Model performance evaluation
- User-friendly prediction interface

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

The project uses the **Breast Cancer Wisconsin Dataset**.

### Input Features

The dataset contains multiple diagnostic measurements extracted from digitized images of breast cell nuclei, including:

- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Compactness
- Concavity
- Symmetry
- Fractal Dimension
- and other computed features.

### Target Variable

- Benign
- Malignant

---

## Machine Learning Model

**Algorithm**

- Logistic Regression

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Project Workflow

1. Dataset Collection
2. Exploratory Data Analysis
3. Data Cleaning
4. Feature Selection
5. Train-Test Split
6. Logistic Regression Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter tumor measurements
- Predict whether the tumor is Benign or Malignant
- View prediction instantly

---

## Project Structure

```text
Breast-Cancer-Prediction (Logistic Regression)
│
├── app.py
├── model.pkl
├── breast-cancer.csv
├── breast-cancer-prediction.ipynb
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
cd "Breast-Cancer-Prediction (Logistic Regression)"
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

- Binary Classification
- Logistic Regression
- Data Preprocessing
- Feature Selection
- Model Evaluation
- Classification Metrics
- Pickle Model Serialization
- Streamlit Deployment

---

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- ROC Curve visualization
- Probability confidence scores
- Feature importance analysis
- Improved UI/UX
- Cloud deployment
