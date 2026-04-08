import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_csv('loan_cost_prediction_dataset.csv')
print("Dataset loaded successfully")
print("Column names:", df.columns.tolist())
df.dropna(inplace=True)
target_column = "loan_amount" 
if target_column not in df.columns:
    raise ValueError(f"Column '{target_column}' not found in the dataset.")
X_raw = df.drop(target_column, axis=1)
Y = df[target_column]
X = pd.get_dummies(X_raw, drop_first=True)
feature_columns = X.columns  
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
r2 = r2_score(Y_test, Y_pred)
print(f"\nModel RMSE: {rmse:.2f}")
print(f"Model R² Score: {r2:.2f}")
print("\nEnter loan details below to predict price:")
user_input = {}
for col in X_raw.columns:
    while True:
        try:
            val = input(f"Enter {col}: ")
            try:
                user_input[col] = float(val)
            except ValueError:
                user_input[col] = val  
            break
        except Exception as e:
            print(f"Invalid input for {col}. Error: {e}")
user_df = pd.DataFrame([user_input])
user_encoded = pd.get_dummies(user_df)
user_encoded = user_encoded.reindex(columns=feature_columns, fill_value=0)
predicted_price = model.predict(user_encoded)[0]
print(f"\nPredicted Loan Price: {predicted_price:,.2f}")
