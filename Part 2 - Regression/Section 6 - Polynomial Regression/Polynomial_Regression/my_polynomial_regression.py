# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 01:02:39 2019

@author: t H u n d e r
"""
#polynomial regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#fitting polynomial regression to dataset
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
X_poly= poly_reg.fit_transform(X)
lin_reg_2= LinearRegression()
lin_reg_2.fit(X_poly,y)




