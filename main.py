from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pd.read_pickle('forecast_ARIMA.pkl')
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Month = int(request.form['Month'])
        date = str(Year) + '-' + str(Month)
        date = pd.to_datetime(date, format='%Y-%m')
        prediction = model.loc[date]['forecast']
        output = round(prediction,2)
        return render_template('index.html',prediction_text=f"prediction : {output}")
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

