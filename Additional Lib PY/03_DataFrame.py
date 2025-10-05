'''
DataFrame is a two-dimensional labeled data structure with columns of potentially different types.
It is similar to a spreadsheet or a SQL table.
dataframe it is a collection of series.
'''
import pandas as pd

data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0]) # .loc is used to access a group of rows and columns by label(s) or a boolean array.
print(df.loc[[0,1]]) # return the first and second row

df = pd.DataFrame(data, index=['day1','day2','day3'])
print(df.loc['day1'])
print(df.loc[['day1','day2']])# return the first and second row (or)
print(df.loc['day1':'day3']) # return the first, second, and third row
