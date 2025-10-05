# Read CSV Files
'''
CSV (Comma Separated Values) is a common file format used to store tabular data.
Each line in a CSV file represents a row, and the values within the line are separated by commas.
'''
import pandas as pd

df = pd.read_csv('Additional Lib PY\(a)_data.csv')
print(df)
print(df.to_string())

#  Part 2 

print(df.info()) # return the information about the dataframe

print(df.head()) # return the first 5 rows
print(df.head(10)) # return the first 10 rows
print(df.tail()) # return the last 5 rows
print(df.tail(10)) # return the last 10 rows