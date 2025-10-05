# Series
'''
Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating-point numbers, Python objects, etc.).
It is similar to a column in a spreadsheet or a database table.
'''

import pandas as pd

a = [1,3,5,7,9]

y = pd.Series(a,index=['a','b','c','d','e']) # capital S used for Series
print(y)
# print(y[1])


b = [1,'mrm',2,3]
z = pd.Series(b,index=['a','1','c','d'])
print(z)
print(z['c'])



calories = {'day1': 420, 'day2': 380, 'day3': 390}
x = pd.Series(calories)
x = pd.Series(calories, index=['day1']) # if you give exceed index it will shown an error. 
print(x)