from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load the pre-trained spam detection model
model = joblib.load('spam_model.pkl')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        output = model.predict([message])
        if output == [0]:
            result = "This message is NOT spam"
        else:
            result = "This message is SPAM"
        return render_template('index.html', result=result, message=message)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
