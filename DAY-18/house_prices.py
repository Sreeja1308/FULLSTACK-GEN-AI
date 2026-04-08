import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import streamlit as st
df=pd.read_csv("house_prices.csv")
X=df[["Area_sqft","Bedrooms","Bathrooms"]]
y=df["Price"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)

joblib.dump(model,"houseprice.pkl")
print("model training done and saved in pkl")

model=joblib.load("houseprice.pkl")
st.title("House Price🏠")

area=st.number_input("Enter Area (Sqft)", min_value=500,max_value=5000,step=100)
bedrooms=st.number_input("Enter number of Bedrooms", min_value=1,max_value=10,step=1)
bathrooms=st.number_input("Enter number of Bathrooms", min_value=1,max_value=10,step=1)

if st.button("Predict Price"):
    prediction = model.predict([[area,bedrooms,bathrooms]])[0]
    st.success(f"Predicted House Price : {prediction:,.2f}")

