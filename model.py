# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle 
import numpy as np
import matplotlib.pyplot as plt
import seaborn

data = pd.read_csv(r'C:\Users\Atrey\Documents\USA_Housing.csv')


#Get X and Y targets
x = data.loc[:,'Avg. Area Income':'Area Population']
x = x.astype(int)


y = data.loc[:,'Price']
y = y.astype(int)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

regressor = LinearRegression()

regressor.fit(X_train, y_train)

regressor.score(X_train, y_train)

regressor.score(X_test, y_test)

pickle.dump(regressor, open('model.pkl', 'wb'))
