import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
uber_df = pd.read_csv("uber_sample_data.csv")

# 2. Features and target
X = uber_df[['distance_km', 'rush_hour', 'weather_numeric', 'num_cars_available']]
y = uber_df['price']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Train the RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
print("Model Evaluation:")
print("R² score:", r2_score(y_test, y_pred))

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)

# 6. Get user input
print("\n--- Predict Price for New Ride ---")
try:
    distance_km = float(input("Enter distance in km: "))
    rush_hour = int(input("Is it rush hour? (0 = No, 1 = Yes): "))
    weather_numeric = int(input("Weather (0 = clear, 1 = rain, 2 = snow): "))
    num_cars_available = int(input("Number of cars available: "))

    # 7. Make prediction (fixes the warning)
    new_data = pd.DataFrame([[distance_km, rush_hour, weather_numeric, num_cars_available]],
                            columns=['distance_km', 'rush_hour', 'weather_numeric', 'num_cars_available'])
    predicted_price = model.predict(new_data) * 90

    print(f"\nEstimated price for the ride: ₹{predicted_price[0]:.2f}")

except Exception as e:
    print("Invalid input!", e)
