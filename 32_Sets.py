'''
set it is refer to unordered collection of unique elements.
set is mutable and did not allow duplicates.
1. Creating a set
2. Accessing elements
3. Modifying elements
4. Set methods
5. Set operations
'''
# 1. Creating a set
# empty set
set1 = set()
print(set1)

# set with elements
set2 = {1, 2, 3, 4, 5}
print(set2)

# 2. Accessing elements
# set is unordered, so we cannot access elements by index

# using for loop
for i in set2:
    print(i)

# 3. Modifying elements
# we can add elements to a set using add() method
set2.add(6)
print(set2)

# we can remove elements from a set using remove() or discard() method
set2.remove(6)
print(set2)

# 4. Set methods
# add()
# remove() or discard()
# pop()
# clear()
# len()
# copy()
# union()
# intersection()
# difference()
# symmetric_difference()

# clear()
# removes all elements from the set
set2.clear()
print(set2)

# using set() function
set3 = set([1, 2, 3, 4, 5])
print(set3)

# len()
# returns the number of elements in the set
print(len(set3))

# Union()
# returns a new set with all elements from both sets
set4 = { 3, 7, 8, 9}
set5 = {1, 2, 3}
print(set4.union(set5))

# Intersection()
# returns a new set with elements common to both sets
print(set4.intersection(set5))

# Difference()
# returns a new set with elements in the first set but not in the second set
print(set4.difference(set5))

# Symmetric_difference()
# returns a new set with elements in either of the sets but not in both
print(set4.symmetric_difference(set5))

