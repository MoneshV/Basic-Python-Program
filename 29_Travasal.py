# Traversal 
'''
Travasal is the process of visiting each element of a collection (like a list, tuple, or string) exactly once.
'''

name = 'Hello world'
# 1st method of travasal
for i in range(len(name)):
    print(name[i], end ='')
print()

# 2nd method of travasal
for i in name:
    print(i, end ='')
print()

# list travasal
lst = [1, 2, 3, 4, 5, 6]
for i in lst:
    print(i, end='')
print()

# tuple travasal
tup = (1, 2, 3, 4, 5, 6)
for i in tup:
    print(i, end='')
print()

