# -*- coding: utf-8 -*-
#Import necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle 
import numpy as np
import matplotlib.pyplot as plt
import seaborn

#THIS IS THE DIRECTORY OF YOUR DATA IN YOUR LOCAL FILE
data = pd.read_csv(r'C:\Users\Atrey\Documents\USA_Housing.csv')


#Get X and Y targets
x = data.loc[:,'Avg. Area Income':'Area Population']
x = x.astype(int)

y = data.loc[:,'Price']
y = y.astype(int)

#Split data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#INitialize regressor for regression analysis
regressor = LinearRegression()

#Fit model 
regressor.fit(X_train, y_train)

#Save model for application
pickle.dump(regressor, open('model.pkl', 'wb'))
