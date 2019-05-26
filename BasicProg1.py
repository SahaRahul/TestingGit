#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 10:52:33 2019

@author: rahulsaha
"""

import pandas as pd

cldata = pd.read_csv('/home/rahulsaha/pythonCode/challenger.csv')

''' To check nos. of rows and nos. of column '''
cldata.shape # For dimension

''' To check the column names or header names '''
cldata.columns.values

''' To check first 6 rows in the dataframe '''
cldata.head()
cldata.head(10)

''' To check last 6 rows in the dataframe '''
cldata.tail()

''' Datatype of all the column '''
cldata.dtypes

''' Datatype of one particular column '''
cldata.temperature.dtypes


type(cldata)

type(cldata.temperature)

type(cldata.temperature[1])

cldata.describe()

cldata['temperature'].describe()

cldata.o_ring_ct.value_counts()
cldata.temperature.value_counts()

''' Importing csv file '''
diamondData = pd.read_csv('/home/rahulsaha/pythonCode/diamond.csv')

''' Checking dimension for the imported csv file '''
diamondData.shape

''' Checking the datatype for the dataframe '''
diamondData.dtypes
diamondData.carat.dtypes
type(diamondData.carat[0])

''' Checking for the top 6 rows in the dataframe '''
diamondData.head()

''' Count of missing values for a particular column '''
sum(diamondData.color.isnull())

''' Basic check of distribution of numeric fields in the dataframe '''
diamondData.describe()  # Only work with numeric columns

''' Randomly selecting 10 rows from the dataframe '''
diamondData.sample(n = 10)

''' Frequency check for categorical fields '''
diamondData.color.value_counts() 
diamondData.cut.value_counts() 
diamondData.clarity.value_counts() 





