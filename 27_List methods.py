#  List Methods
'''
1. length of the list
2. append()
3. extend()
4. insert()
5. count()
6. index()
7. min()
8. max()
9. sort()
10. sum()
11. update()
12. remove()
13. pop()
14. reverse()
15. copy()
16. clear()
17. Nested list [topic]
'''

lst1 = [10, 20, 30]
lst2 = [40, 50, 60]

# length of the list
print(len(lst1))

# Insert an element at the end of the list using append() function
lst1.append(40)
print(lst1)
# 2 nd method to insert a list into a list at the end of the list using append() function is called nested list.
lst1.append(lst2)
print(lst1)
print(lst1[4])

# Insert multiple elements at the end of the list using extend() function
lst1.extend(lst2)
# lst1 = lst1 + lst2
print(lst1)

# Insert an element at a specific index using insert() function
lst1.insert(0, 0)
# insert(index, value)
print(lst1)

# Count the number of occurrences of an element in the list using count() function
print(lst1.count(40))
# if the element is not found in the list, count() function will return 0.

# Find the index of the first occurrence of an element in the list using index() function
print("Index:", lst1.index(40))
# index(element) repreaent the index of the element in the list.
# If the element is not found in the list, index() function will raise a ValueError exception.
# print(lst1.index(100))

# Find the minimum and maximum values in the list using min() and max() functions
numbers = [10, 20, 30, 40, 50]
print("Minimum value : ", min(numbers))
print("Maxmimunm value: ", max(numbers))

# Sort the list in ascending order using sort() function
my_number1 = [100, 500, 300, 700]
my_number2 = [200, 600, 400, 800]
my_number1.extend(my_number2)
print("Before sorting:", my_number1)
my_number1.sort()
print("After sorting:", my_number1)
my_number1.sort(reverse = True)
print("After sorting in descending order:", my_number1)


# Find the sum of all elements in the list using sum() function
print("Sum of list : ", sum(my_number1))

# Update the list using update() function
num =[0, 1, 2, 3, 4, 5, 6]
print(num)
num[0] = 100
print(num)

# Remove an element from the list using remove() function
num.remove(100)
print(num)

# Remove an element from the list using pop() function
num.pop()
print(num)

# Remove an element from the index position of the list using pop() function
num.pop(0)
print(num)

# reverse the list using reverse() function
num.reverse()
print(num)

# Copy the list using copy() function
num2 = num.copy()
print(num2)

# Clear all elements of the list using clear() function
lst1.clear()
print(lst1)


# Nested list [topic]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[0])
print(nested_list[0][0])
print(nested_list[1][2])
