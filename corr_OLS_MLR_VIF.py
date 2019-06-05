#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:34:32 2019

@author: rahulsaha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

housePrice = pd.read_csv("~/git/SahaRahul/practicePython/HousePrices.csv")

housePrice.shape

housePrice.columns.values
housePrice.head(10)
housePrice.describe()

''' Correlation '''

np.corrcoef(housePrice.Price, housePrice.SqFt)

plt.scatter(housePrice.Price, housePrice.SqFt)

# Below correlation is not good since Bedroom data is discreate not continous
np.corrcoef(housePrice.Price, housePrice.Bedrooms)

plt.scatter(housePrice.Price, housePrice.Bedrooms)


''' Single Linear Regression '''

import statsmodels.api as sm
Y = housePrice[['Price']]
X = housePrice[['SqFt']]

X1 = sm.add_constant(X)

model = sm.OLS(Y, X1)

fitted1 = model.fit()

fitted1.summary()

plt.scatter(housePrice.SqFt, housePrice.Price)
plt.plot(housePrice.SqFt, fitted1.fittedvalues, c = 'r')


fitted1.predict([1,1780])    


''' Multiple Linear Regression '''

Y = housePrice[['Price']]
X = housePrice[['SqFt']+['Bedrooms']+['Bathrooms']+['Offers']]

X1 = sm.add_constant(X)

model = sm.OLS(Y, X1)

fitted1 = model.fit()

fitted1.summary()

'''R-squared: 0.698 '''

fitted1.predict([1,1780,5,2,2])    



pollution = pd.read_table("~/git/SahaRahul/datasets/Additional Datasets/Pollute.txt")

pollution.shape

pollution.columns.values

Y = pollution[['Pollution']]
X = pollution[['Temp']+['Industry']+['Population']+['Wind']+['Rain']+['Wet.days']]

X1 = sm.add_constant(X)

pollu_model = sm.OLS(Y, X1).fit()

pollu_model.summary()

pollu_model.rsquared

VIF = round(1/(1-pollu_model.rsquared))
print(VIF)

''' Alternative way to get the model '''
y=pollution[['Pollution']]
x=pollution[pollution.columns.drop(['Pollution'])]

import statsmodels.formula.api as smf
model2 = smf.ols(formula="y~x", data=pollution).fit()
model2.summary()


def vif_cal(input_data, dependent_col):
    import statsmodels.formula.api as smf
    x_vars = input_data.drop([dependent_col], axis=1)
    xvar_names = x_vars.columns
    for i in range(0,xvar_names.shape[0]):
        y = x_vars[xvar_names[i]]
        x = x_vars[xvar_names.drop(xvar_names[i])]
        rsq=smf.ols(formula="y~x", data=x_vars).fit().rsquared
        vif=round(1/(1-rsq),2)
        print(xvar_names[i], " VIF = ", vif)

vif_cal(input_data=pollution, dependent_col="Pollution")

y=pollution[['Pollution']]
x=pollution[pollution.columns.drop(['Pollution', 'Industry', 'Wet.days'])]

import statsmodels.formula.api as smf
model2 = smf.ols(formula="y~x", data=pollution).fit()
model2.summary()

vif_cal(input_data=pollution.drop(['Industry'], axis = 1), dependent_col="Pollution")