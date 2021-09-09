# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:54:46 2021

@author: Atrey
"""

import numpy as np
import os
from flask import Flask, request, render_template
import pickle 


app = Flask(__name__, template_folder = 'template')
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    if output < 0:
        return render_template('index.html', prediction_text = "Predicted Price is negative, values entered not reasonable")
    elif output >= 0:
        return render_template('index.html', prediction_text = 'Predicted Price of the house is: ${}'.format(output))   

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        message = request.form.get('name')  # access the data inside 
        return render_template('index.html', message=message)
if __name__ == "__main__":
    app.run(debug=True)