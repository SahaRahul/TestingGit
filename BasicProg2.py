#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 05:17:00 2019

@author: rahulsaha
"""
import pandas as pd

''' Importing csv file '''
diamondData = pd.read_csv('/home/rahulsaha/pythonCode/diamond.csv')

diamondData.shape

diamondData.columns.values

diamondData1 = diamondData.iloc[[2,34,5]]

diamondData2 = diamondData[["color", "cut"]]

diamondData3 = diamondData[["color", "cut"]][0:12]

diamondData4 = diamondData3.drop_duplicates()

diamondData4.shape

diamondData5 = diamondData.drop(["color"], axis=1)[0:12]
diamondData6 = diamondData.drop(["Unnamed: 0"], axis=1)

diamondData7 = diamondData6[(diamondData6['color'] == "E") & 
                            (diamondData6['price'] > 2000)]
diamondData7.shape

diamondData8 = diamondData6[(diamondData6['color'] == "E") | 
                            (diamondData6['color'] == "I")]
diamondData8.shape
