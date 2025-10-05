# Read CSV Files
'''
CSV (Comma Separated Values) is a common file format used to store tabular data.
Each line in a CSV file represents a row, and the values within the line are separated by commas.
'''
import pandas as pd

df = pd.read_csv('Additional Lib PY\(a)_data.csv')
print(df)
print(df.to_string())