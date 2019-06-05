#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:42:10 2019

@author: rahulsaha
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


genderDiscr = pd.read_csv("~/git/SahaRahul/practicePython/GenderDiscrimination.csv")

genderDiscr.columns.values
genderDiscr['Gender'].value_counts()


logistic = LogisticRegression()

logistic.fit(genderDiscr[['Experience']], genderDiscr['Gender'])

exp = 5
pred_Gender = logistic.predict([[exp]])
print(pred_Gender)


