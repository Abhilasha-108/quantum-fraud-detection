# File: train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

print("Starting model training process...")

# 1. Load and preprocess the dataset [cite: 43, 44]
try:
    df = pd.read_csv('creditcard.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'creditcard.csv' not found. Please download it and place it in the project folder.")
    exit()

scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))
df.drop(['Time', 'Amount'], axis=1, inplace=True)

X = df.drop('Class', axis=1)
y = df['Class']
print("Data has been preprocessed.")

# 2. Split data for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Train a lightweight Logistic Regression model for the 'edge' layer [cite: 49]
model = LogisticRegression(solver='liblinear', class_weight='balanced', random_state=42)
print("Training the model...")
model.fit(X_train, y_train)
print("Model training complete.")

# 4. Save the trained model to a file
joblib.dump(model, 'fraud_model.pkl')
print("Model saved as 'fraud_model.pkl'.")