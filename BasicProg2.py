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

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue', 'Rahul'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR', 'Analytics']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue', 'Sudipta'],
                    'hire_date': [2004, 2008, 2012, 2014, 2018]})
display('df1', 'df2')

df1_df2merge = pd.merge(df1, df2, on = 'employee', how = 'inner' )
df1_df2merge

df1_df2merge1 = pd.merge(df1, df2, on = 'employee', how = 'left' )
df1_df2merge1

df1_df2merge2 = pd.merge(df1, df2, on = 'employee', how = 'outer' )
df1_df2merge2

df1_df2merge1.to_csv('~/git/SahaRahul/practicePython/leftjoin.csv')
df1_df2merge2.to_csv('~/git/SahaRahul/practicePython/fullouter.csv')

teledata = pd.read_csv("~/git/SahaRahul/practicePython/telecom_churn.csv")
teledata.shape

trainData = teledata.sample(n=2000)
trainData.shape
trainData.columns.values

''' Central Tendency '''
trainData['total day minutes'].mean()
trainData['total intl calls'].mean()


trainData['total day minutes'].median()
trainData['total intl calls'].median()


df3 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue', 'Sudipta'],
                    'salary': [24000, 28000, 21200, 14200, 18200]})

df3 = df3.append(pd.DataFrame({'employee': ['Rahul', 'Som', 'Avilin', 'Jayanta', 'Soz'],
                    'salary': [24000, 25000, 28200, 14500, 18900]}), ignore_index=True)
    
df3 = df3.append(pd.DataFrame({'employee': ['Lison', 'Bobby', 'Lee', 'Joo', 'John'],
                    'salary': [24500, 28200, 29200, 24200, 38200]}), ignore_index=True)

    
df1 = df1.append(
        pd.DataFrame({
                'employee': ['Rahul Sen', 'Som', 'Avilin', 'Jayanta',
                             'Soz', 'Lison', 'Bobby', 'Lee', 'Joo','John'],
                'group': ['Accounting', 'Engineering', 'Engineering', 'HR', 
                           'Analytics', 'Accounting', 'Engineering', 'Engineering', 
                              'HR', 'Analytics']}), ignore_index = True)
 
meanSalary = df3["salary"].mean()
meanSalary
    
''' Dispersion '''    
var_salary = df3["salary"].var()

std_salary = df3["salary"].std()


df1_df3merge = pd.merge(df1, df3, on = "employee", how = "inner")

accountingProf = df1_df3merge[df1_df3merge["group"] == 'Accounting']
accountingProf.shape

df1_df3merge[(df1_df3merge["employee"] == 'Rahul Sen') & (df1_df3merge["group"] == 'Accounting')]

df1_df3merge[(df1_df3merge["employee"] == 'Rahul Sen') & (df1_df3merge["group"] == 'Accounting')]['salary']


nonAccountingProf = df1_df3merge[df1_df3merge["group"] != 'Accounting']
nonAccountingProf.shape

accountingProf["salary"].var()
accountingProf["salary"].std()

nonAccountingProf["salary"].var()
nonAccountingProf["salary"].std()


df1_df3merge.describe()

df1_df3merge['salary'].quantile([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])


import matplotlib.pyplot as plt

plt.boxplot(df1_df3merge['salary'])

age = [33, 34, 49, 33, 24, 55, 27, 28, 30, 40, 25, 55, 27, 28, 39]

df1_df3merge["Age"] = age

df1_df3merge.columns.values

df1_df3merge['Age'].describe()

''' Line Plot '''
plt.plot(df1_df3merge.Age, df1_df3merge.salary)

''' Scatter Plot '''
plt.scatter(df1_df3merge.Age, df1_df3merge.salary)


''' Bar Plot '''
freq = df1_df3merge.group.value_counts()
freq.values
freq.index

plt.bar(freq.index, freq.values)


''' Trend Plot '''
date = ['01-Jan-2018', '01-Feb-2018', '01-Mar-2018', '01-Apr-2018', '01-May-2018']
rate = [10, 15, 12, 16, 18]

rateTable = pd.DataFrame({'Date': date, 'Rate': rate})

plt.plot(rateTable.Rate)



