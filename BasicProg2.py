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
