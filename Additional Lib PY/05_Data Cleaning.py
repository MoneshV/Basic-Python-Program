# Data Cleaning
import pandas as pd
df = pd.read_csv('Additional Lib PY\dirtydata.csv')

# Remove rows with NULL values
x = df.dropna() # by default, which means that creating a new variable, rows with NULL values will be dropped without affecting the original DataFrame
print(x)
#(or)
# df.dropna(inplace = True) # inplace=True means that the changes will be made directly to the DataFrame without creating a new one
# print(df)

# Replace NULL values with the value 1300
# y = df.fillna(1300)
# print(y)
# (or)
df.fillna(1300, inplace = True)
print(df)