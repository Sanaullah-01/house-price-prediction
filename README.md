🏡 House Price Prediction – Machine Learning Project

This project builds a Machine Learning model to predict house prices using the California Housing Dataset.
It includes data loading, preprocessing, exploratory data analysis (EDA), visualization, model training, model comparison, and feature importance analysis.

📌 Project Overview

This project demonstrates:

Loading and understanding the California Housing dataset

Performing basic exploratory data analysis (EDA)

Visualizing correlations using a Heatmap

Training two ML models:

Linear Regression

Random Forest Regressor

Evaluating model performance using:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

Extracting feature importance from the Random Forest model

📁 Dataset Used

The project uses the built-in California Housing dataset from sklearn.datasets.

Features

MedInc – Median Income

HouseAge

AveRooms

AveBedrms

Population

AveOccup

Latitude

Longitude

Target

Median house value (in $100,000s)

🔍 Exploratory Data Analysis (EDA)

The project performs:

Dataset shape and column inspection

Summary statistics

Correlation matrix

Heatmap visualization showing feature relationships

This helps identify which features influence house prices most strongly.

🤖 Models Trained
1. Linear Regression

A basic regression model used as a baseline.

2. Random Forest Regressor

An advanced ensemble ML model that helps improve performance and capture non-linear patterns.

The model also provides feature importance, which highlights which features influence prediction the most.

📊 Evaluation Metrics

Both models are evaluated using:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

R² Score

These metrics help compare model accuracy and performance.

🧪 Technologies Used

Python

NumPy

Pandas

Matplotlib

Seaborn (if used for visuals)

Scikit-Learn

▶️ How to Run the Project
1. Clone the Repository
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
2. Install Dependencies
pip install -r requirements.txt
3. Run the Notebook

Open the Jupyter Notebook:

jupyter notebook

Run the notebook cells to train models and view results.

📈 Feature Importance Example

The Random Forest model ranks features by importance.
Typical top contributors include:

Median Income

Latitude

House Age

Average Rooms

This helps understand which factors affect housing prices the most.

🗂️ Project Structure
│-- AI_Project.ipynb            # Main notebook
│-- README.md                    # Project documentation
│-- requirements.txt (optional)
📬 Future Improvements

Add hyperparameter tuning (GridSearchCV, RandomizedSearch)

Build a Flask / FastAPI web app for live predictions

Add more visualizations

Deploy the model on cloud

🙌 Author

Created by Sana Ullah
Machine Learning Project – House Price Prediction
