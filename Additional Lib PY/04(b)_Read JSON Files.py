# Read JSON Files
'''
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
It is commonly used for transmitting data between a server and a web application.
'''
import pandas as pd

df = pd.read_json('Additional Lib PY\(b)_opendata.json')
print(df)
print(df.to_string())