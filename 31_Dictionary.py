# Dictionary
'''
Dictionary is a collection of key value pairs.
Keys are unique and immutable.
Values can be of any type (int, float, string, list, tuple, dictionary).

1. Creating a dictionary
2. Accessing values
3. Modifying values
4. Adding key value pairs
5. Removing key value pairs
6. Dictionary methods
7. Dictionary comprehensions
QUiz
'''

# 1. Creating a dictionary
# empty dictionary
dict1 = {}
print(dict1)

# dictionary with key value pairs
dict2 = {'name': 'Demi', 'age': 25, 'city': 'New York'}
print(dict2)

# using dict() function
dict3 = dict(name='Demi', age=25, city='New York')
print(dict3)

# 2. Accessing values
print(dict2['name'])
print(dict2.get('age'))
# if key is not present, it will return None
print(dict2.get('gender'))
# if key is not present, it will raise KeyError
# print(dict2['gender'])

# 3. Modifying values
dict2['age'] = 26
print(dict2)

# 4. Adding key value pairs
dict2['gender'] = 'female'
print(dict2)

# 5. Removing key value pairs
del dict2['city'] # or dict2.pop('city')
print(dict2)


# 6. Dictionary methods
print(dict2.keys())
print(dict2.values())
print(dict2.items())

# 7. Dictionary comprehensions
dict4 = {k: v for k, v in dict2.items()}
print(dict4)

# Quiz
map = {5 : {'P' : {5 : "P"}, 6 : 'Q'},
        7 : 'R',
        'Q': 'S',
        'S' : 'T'  }
print(map[map[map[5][6]]])