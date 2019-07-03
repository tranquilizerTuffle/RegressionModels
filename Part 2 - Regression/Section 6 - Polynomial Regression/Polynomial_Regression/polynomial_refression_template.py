# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:13:17 2019

@author: t H u n d e r
"""
#regression template

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting polynomial regression to dataset
#create youir regressor here

#predicting a new result
y_pred=regressor.predict(6.5)

#visualizing the regression results
plt.scatter (X,y,color="red")
plt.plot(X,regressor.predict(X),color="blue")
plt.title("Title")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#visualising the results for higher order regressionn models
X_grid=np.arrange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter (X,y,color="red")
plt.plot(X,regressor.predict(X),color="blue")
plt.title("Title")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


