from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
import joblib

model=joblib.load('model.pkl')
vectorizer=joblib.load('vectorizer.pkl')
Client=MongoClient("mongodb://localhost:27017/")
db=Client['job_data']
collection=db['predictions']

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        description = request.form['description']
        vec=vectorizer.tranform([description])
        prediction=model.predict(vec)[0]
        result="Fraud" if prediction==1 else "Not Fraud"

        # Save Data 
        collection.insert_one({"description":description,"prediction":result})
        return render_template("index.html",prediction=result)
    
if __name__=="__main__":
    app.run(debug=True)
