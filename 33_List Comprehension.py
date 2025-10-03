'''
List comprehension is refers to a concise way of creating a list in Python.
It is a way of creating a new list by applying an expression to each element of an existing list.

'''

arr = [1, 2, 3, 4, 5, 6]
odd = []

for i in arr:
    print(i)

for i in arr:
    if i % 2 == 1:
        odd.append(i)
print(odd)

# using list comprehension
odd = [i for i in arr  if i % 2 == 1]
print(odd)

# QUIz 
even = [ i for i in arr if i % 2 != 1]
print(even)

# Example
lst = []
for i in range(1, 101):
    lst.append(i)
print(lst) 

# using list comprehension
lst =[i for i in range(1, 101)]
print(lst)