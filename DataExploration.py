#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 08:09:53 2019

@author: rahulsaha
"""
import pandas as pd

teledata = pd.read_csv("~/git/SahaRahul/practicePython/telecom_churn.csv")

''' Step 1: '''
# What is the numbers of rows and columns
teledata.shape

# Are there is any suspesious variable
teledata.columns.values

# Display the variable format or datatype
teledata.dtypes

# Print first few observations
teledata.head(10)

# Do we have any unique identifiers
teledata.columns.values

''' Step 2: '''
# Identify categorical variables
# Finding frequency of the categorical variables
teledata['state'].value_counts()
teledata['area code'].value_counts(sort = False)
teledata['international plan'].value_counts()
teledata['voice mail plan'].value_counts()
teledata['number vmail messages'].value_counts()
teledata['total day calls'].value_counts()
teledata['total eve calls'].value_counts()
teledata['total night calls'].value_counts()
teledata['total intl calls'].value_counts()
teledata['customer service calls'].value_counts()
teledata['churn'].value_counts()

# Are there any missing value
teledata.isnull().sum()
teledata.isnull().sum()/len(teledata)   # percentage of missing value

''' Step 3: '''
# Identify continuous variables
import matplotlib.pyplot as plt

teledata.describe()

plt.boxplot(teledata['total day minutes'])
plt.boxplot(teledata['number vmail messages'])
plt.boxplot(teledata['total intl calls'])

''' Outlier imputation with median '''
tot_day_min_percentile = teledata['total day minutes'].quantile([0.05,0.1,0.25,0.5,0.75,0.9,0.95,1])
round(tot_day_min_percentile,2)

w_least_tot_day_min_percentile = teledata['total day minutes'] < 89.00
w_least_tot_day_min_percentile.value_counts()

median_tot_day_min = teledata['total day minutes'].median()

teledata['new_tot_day_min'] = teledata['total day minutes']

teledata['new_tot_day_min'][w_least_tot_day_min_percentile] = median_tot_day_min

teledata['new_tot_day_min'].describe()

plt.boxplot(teledata['new_tot_day_min'])

# In the above imputation we can see that the mean value is higher that median
# We are now imputing with more closer value
lowerQuantile_tot_day_min = float(teledata['total day minutes'].quantile([0.15]))

teledata['new1_tot_day_min'] = teledata['total day minutes']
teledata['new1_tot_day_min'][w_least_tot_day_min_percentile] = lowerQuantile_tot_day_min

teledata['new1_tot_day_min'].describe()

plt.boxplot(teledata['new1_tot_day_min'])

# Impute based on category

crosstab_custServCalls_churn = pd.crosstab(teledata['customer service calls'],
                                           teledata['churn'])

crosstab_custServCalls_churn_percnt = crosstab_custServCalls_churn.astype(float).div(
        crosstab_custServCalls_churn.sum(axis = 1), axis = 0)
round(crosstab_custServCalls_churn_percnt,2)

# percentage of customer service calls of 0 is close to the 2, lets impute 0 with 2

teledata['new_customer_service_calls'] = teledata['customer service calls']
teledata['new_customer_service_calls'][teledata['new_customer_service_calls']==0] = 2

teledata['new_customer_service_calls'].value_counts()


