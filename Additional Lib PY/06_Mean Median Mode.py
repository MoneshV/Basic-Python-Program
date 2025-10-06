# Mean, Median, and Mode
'''
Mean, Median, and Mode

Mean: The average value of a dataset.
Median: The middle value of a dataset when sorted in ascending order.
Mode: The most frequently occurring value in a dataset.

'''
import pandas as pd
df = pd.read_csv('Additional Lib PY\dirtydata.csv')
x = df['Calories'].mean ()
df['Calories'].fillna(x, inplace = True) 
#(or)
# df['Calories'].fillna(df['Calories'].mean(), inplace = True)
print(df['Calories'].to_string())


# Median
df['Calories'].fillna(df['Calories'].median(), inplace = True) 
print(df['Calories'].to_string())


# Mode
df['Calories'].fillna(df['Calories'].mode()[0], inplace = True) 
print(df['Calories'].to_string())