#   Tuples
'''
1. create a tuple
2. len()
3. access tuple elements
4. find min and max in tuple
5. count
6. index
7. slice
8. single element tuple
9. concatenate
10. list to tuple
11. tuple to list

'''

# create a tuple
tup = (170 , 100, 90, 200, 600, 999)
print(type(tup))
print(tup)

# len() of tuple
print(len(tup))

# access tuple elements
print(tup[0])

# find min and max in tuple
print(min(tup), max(tup))

# count
print(tup.count(100))

# index
print(tup.index(170))

# slice
print(tup[: 5])


# single element tuple
tup2 = (100)
print(type(tup2))
# output: <class 'int'>
tup2 = (100,)
print(type(tup2))


# concatenate 2  methods
# 1 st method 
num1 =(1, 2, 3)
num2 =(4,)
num3 = num1 + num2
print(num3)

# 2 nd method
fruits = ('apple', 'orange', 'mango')
fruits += ('banana',)
print(fruits)


# list to tuple
lst = [1, 2, 3]
mr = tuple(lst)
print(type(mr))


# tuple to list
mr1 = (4, 5, 6)
lst1 = list(mr1)
print(type(lst1))
