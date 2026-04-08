
import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#load the dataset
df = pd.read_csv('house_price_prediction_dataset.csv') #your uploaded file
print(" Data loaded successfullt!")
print(df.head())

# drop misssing values(if any)
df.dropna(inplace=True)

#separate features
x=df.drop("Price", axis=1)
y=df["Price"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"\n model RMSE: {mse:.2f}")
print(f"\n model R^2 Score: {r2:.2f}")

print("\n Enter details of the house below to predict price:")

user_input ={}
for col in x.columns:
  while True:
    try:
      val = float(input(f"Enter {col} "))
      user_input[col]= val
      break
    except ValueError:
      print("please enter a valid numeric value.:")

user_df = pd.DataFrame([user_input])
predicted_price = model.predict(user_df)[0]
print(f"\n predicated House price:{predicted_price:,.2f}")
X = df.drop("Price", axis=1)
y = df["Price"]
