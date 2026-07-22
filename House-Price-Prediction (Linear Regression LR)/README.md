# House Price Prediction using Linear Regression

A Machine Learning web application that predicts residential house prices based on property features using **Linear Regression**. This project demonstrates the complete end-to-end Machine Learning workflow—from data preprocessing and model training to evaluation and deployment through an interactive **Streamlit** application.

---

## Features

- Real-time house price prediction
- Interactive Streamlit web interface
- Income vs House Price visualization
- Linear Regression prediction model
- Fast and lightweight deployment
- Model performance evaluation

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

## Dataset

The project uses the **House Price Dataset** from Kaggle.

### Input Features

- Average Area Income
- House Age
- Number of Rooms
- Number of Bedrooms
- Area Population

### Target Variable

- House Price

During preprocessing, the **Address** column was removed because it does not contribute to price prediction.

---

## Machine Learning Model

**Algorithm**

- Linear Regression

### Evaluation Metrics

- R² Score: **0.9086**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

The model explains approximately **90.86% of the variance** in house prices on the test dataset.

---

## Project Workflow

1. Dataset Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Selection
5. Train-Test Split (80:20)
6. Model Training using Linear Regression
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Application Development

---

## Application

Users can:

- Enter property details
- Predict estimated house prices
- View Income vs House Price visualization

---

## Project Structure

```text
House-Price-Prediction (Linear Regression LR)
│
├── app.py
├── model.pkl
├── House_price.csv
├── House_Price_Prediction.ipynb
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
cd "House-Price-Prediction (Linear Regression LR)"
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

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
- Linear Regression
- Model Evaluation
- Model Serialization using Pickle
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## Future Improvements

- Hyperparameter tuning
- Advanced feature engineering
- Ensemble models (Random Forest, XGBoost)
- Additional visualizations
- Prediction confidence intervals
- Download prediction reports
- Improved UI/UX
- Cloud deployment
