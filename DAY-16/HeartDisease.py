import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv('heart_disease.csv')
print("Dataset loaded successfully")
print(df.head())

# Clean data
df.dropna(inplace=True)

# Convert categorical columns if any (e.g., 'sex')
df['sex'] = df['sex'].map({'male': 1, 'female': 0})

# Features and target
X = df.drop("heart_disease", axis=1)
Y = df["heart_disease"]

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train model (XGBoost Classifier instead of Regressor)
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, Y_train)

# Predict
Y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(Y_test, Y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(Y_test, Y_pred))

# User input
print("\nEnter patient details below to predict heart disease (0 = No, 1 = Yes):")
user_input = {}
for col in X.columns:
    while True:
        try:
            val = float(input(f"Enter {col}: "))
            user_input[col] = val
            break
        except ValueError:
            print("Please enter a valid numeric value.")

user_df = pd.DataFrame([user_input])
predicted_disease = model.predict(user_df)[0]
print(f"\nPredicted heart disease (0 = No, 1 = Yes): {int(predicted_disease)}")