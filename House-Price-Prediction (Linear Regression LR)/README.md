# House Price Prediction

A Machine Learning web application that predicts house prices based on various property features using **Linear Regression**. The project includes data preprocessing, model training, evaluation, and a clean Streamlit interface for real-time predictions.

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Pickle

---

## Features

- Predict house prices instantly
- Interactive and responsive Streamlit interface
- Machine Learning model trained using Linear Regression
- Income vs House Price visualization
- Download prediction report
- Clean dashboard layout
- Model performance information

---

## Dataset

This project uses the **House Price Dataset** obtained from Kaggle.

The dataset contains information such as:

- Average Area Income
- House Age
- Number of Rooms
- Number of Bedrooms
- Area Population
- House Price

The Address column was removed during preprocessing since it was not useful for prediction.

---

## Model Performance

Algorithm:
- Linear Regression

Evaluation Metrics:

- R² Score: **0.9086**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

The model achieved over **90% accuracy (R² score)** on the test dataset.

---

# What Users Can Do

Users can:

- Enter property details
- Predict the estimated market price of a house
- View the relationship between income and house prices
- Download a prediction report
- Explore a clean dashboard interface

---

# Project Workflow

### 1. Dataset Collection

Downloaded the House Price dataset from Kaggle.

---

### 2. Data Exploration

Explored the dataset using:

- `df.head()`
- `df.info()`
- `df.describe()`
- `df.shape`
- `df.columns`
- Missing value detection
- Duplicate detection

---

### 3. Data Preprocessing

- Removed unnecessary columns
- Selected relevant features
- Split dataset into input (X) and output (y)

---

### 4. Train-Test Split

Used an **80-20 split** to train and evaluate the model.

---

### 5. Model Training

Trained a **Linear Regression** model using Scikit-learn.

---

### 6. Model Evaluation

Evaluated the model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

### 7. Model Serialization

Saved the trained model as:

```
model.pkl
```

using Python's Pickle library.

---

### 8. Streamlit Web Application

Developed a user-friendly interface where users can:

- Enter property details
- Predict prices
- View visualizations
- Download prediction reports

---

## What I Learned

This project helped me understand the complete Machine Learning workflow from raw data to deployment.

Some of the concepts I learned include:

- Reading datasets using Pandas
- Exploring and understanding datasets
- Data preprocessing
- Feature selection
- Train-test splitting
- Linear Regression
- Model evaluation
- MAE, MSE and R² Score
- Saving trained models using Pickle
- Building interactive web apps using Streamlit
- Deploying Machine Learning projects

---

## Future Improvements

Some possible improvements include:

- Using Random Forest or XGBoost for comparison
- Hyperparameter tuning
- Better feature engineering
- Improved dashboard design
- Additional data visualizations
- Prediction confidence intervals
- User authentication
- Dark mode support

---

## Installation

Clone the repository

```bash
git clone https://github.com/adiba0-0/House_Price_Prediction_Model.git
```

Move into the project folder

```bash
cd House-Price-Prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

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

## Project Structure

```
House-Price-Prediction
│
├── app.py
├── model.pkl
├── House_price.csv
├── House_Price_Prediction.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```
