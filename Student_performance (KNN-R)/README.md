# Student Performance Prediction using K-Nearest Neighbors Regression

A Machine Learning web application that predicts student academic performance based on demographic, social, and educational factors using **K-Nearest Neighbors Regression (KNN Regression)**. This project demonstrates the complete Machine Learning workflow, including data preprocessing, feature scaling, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Features

- Predict student performance in real time
- Interactive Streamlit web interface
- K-Nearest Neighbors Regression model
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

The project uses the **Students Performance Dataset**.

### Input Features

The dataset contains student-related information such as:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

### Target Variable

- Math Score

Categorical variables were encoded and numerical features were standardized before training the model.

---

## Machine Learning Model

**Algorithm**

- K-Nearest Neighbors Regression (KNN Regression)

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
5. Feature Scaling
6. Train-Test Split
7. K-Nearest Neighbors Regression Model Training
8. Model Evaluation
9. Model Serialization using Pickle
10. Streamlit Application Development

---

## Application

Users can:

- Enter student information
- Predict the student's mathematics score
- View prediction instantly

---

## Project Structure

```text
Student_performance (KNN-R)
│
├── app.py
├── model.pkl
├── scaler.pkl
├── StudentsPerformance.csv
├── Student_Performance.ipynb
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
cd "Student_performance (KNN-R)"
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
- Categorical Feature Encoding
- Feature Scaling
- K-Nearest Neighbors Regression
- Regression Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Weighted KNN implementation
- Model comparison with Linear Regression and Random Forest
- Interactive visualizations
- Enhanced dashboard
- Cloud deployment
