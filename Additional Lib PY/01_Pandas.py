# Pandas
'''
pandas it is refers to a software library written for the Python programming language,
primarily for data manipulation and analysis. It provides data structures like DataFrame and Series,
which are optimized for handling tabular data, and tools for reading and writing data from various file formats.
'''

import pandas as pd

print(dir(pd))

data = {
    'cars' : ['bmw','audi','mercedes'],
    'price' : [200,300,400]
}

x = pd.DataFrame(data)
print(type(x))
print(x)
print(x['cars'])
print(x['price'])
print(pd.__version__)
