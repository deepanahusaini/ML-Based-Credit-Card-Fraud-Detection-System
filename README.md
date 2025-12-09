# ML-Based-Credit-Card-Fraud-Detection-System
A Machine Learning–based Credit Card Fraud Detection System that analyzes transaction patterns, identifies anomalies, and predicts fraudulent activities with high accuracy. Includes data preprocessing, model training, performance evaluation, and real-time fraud prediction.

Credit Card Fraud Detection System

A Machine Learning–based system designed to detect fraudulent credit card transactions with high accuracy. This project focuses on improving financial security by analyzing transaction patterns and classifying them as fraud or legitimate using industry-standard ML techniques.

🚀 Features

Data Preprocessing: Handles missing values, scaling, and class imbalance using SMOTE.

Exploratory Data Analysis (EDA): Understands trends, correlations, and fraud distribution.

Model Training: Uses algorithms like Logistic Regression, Random Forest, XGBoost, and SVM.

Performance Metrics:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

ROC-AUC Curve

Real-Time Prediction: Upload a CSV or enter values to predict fraud probability.

User-Friendly Interface (Optional): Streamlit / Flask web app support.

📂 Project Structure
Credit-Card-Fraud-Detection/
│── data/
│   └── creditcard.csv
│── notebooks/
│   └── eda.ipynb
│   └── model_training.ipynb
│── src/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│── models/
│   └── fraud_model.pkl
│── app.py (If Streamlit/Flask UI used)
│── requirements.txt
│── README.md

🛠️ Technologies Used

Languages: Python
Libraries:

NumPy

Pandas

Scikit-learn

Matplotlib

Seaborn

Imbalanced-Learn (SMOTE)

XGBoost (optional)

Streamlit / Flask (for UI)

🧪 How It Works

Load Dataset: Highly imbalanced dataset with anonymized features.

Preprocess:

Normalize values

Handle imbalance with SMOTE

Train Models: Train multiple ML models and compare performance.

Select Best Model: Based on Recall & ROC-AUC (important for fraud detection).

Predict: User inputs or uploaded data will be classified as Fraud or Legitimate.

📊 Model Performance (Example)
Model	Accuracy	Recall	F1-Score	ROC-AUC
Logistic Regression	94%	89%	88%	0.96
Random Forest	99%	97%	96%	0.995
XGBoost	99.2%	98%	97.6%	0.997

(You can update these values based on your model results.)

▶️ Run the Project
1. Install Requirements
pip install -r requirements.txt

2. Train the Model
python src/train_model.py

3. Run Prediction
python src/predict.py

4. (Optional) Start Streamlit App
streamlit run app.py

🧾 Dataset

This project uses the Credit Card Fraud Detection dataset by Kaggle, containing European card transaction records labeled as fraud or normal.

🎯 Project Goals

Reduce financial fraud losses by early detection

Build an ML model with extremely high recall

Provide an easy-to-use interface for practical usage

Demonstrate real-world ML application for portfolio & resume

📌 Future Enhancements

Deploy model using AWS / Azure

Add deep learning models (LSTM, Autoencoders)

Integrate API for banking systems

Real-time streaming using Kafka

If you want, I can also generate:
✅ requirements.txt
✅ Project description for your resume
✅ Architecture diagram
✅ Streamlit UI
