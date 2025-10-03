#  List (complex data types in python)
# list is similar to array,But in python there is no array but we use list.
# list and array are same meaning collection of elements.
# But there is a difference in array and list are
# array is a collection of same datatypes elements or homogeneous elements is called array.
# list is a collecton of different datatypes elements or hetrogeneous element is called list.

# How to create a list?
height = []
print(height)
print(type(height))

# how to store a value in a list?
height = [10, 20, 30, 40, 50]
print(height) 

# how to store a different value in a list?
height = ['hi', 10, 20, 30, 'demi', 25.5]
print(height)

# how to access a value in the list?  access a value in the list is also called indexing (string indexing)
dif_lst = [10, 20, 30, 40, 50]
print(dif_lst[0])
print(dif_lst[1])
print(dif_lst[-1])
print(dif_lst[-4]) # backward indexing is called negative indexing.

# how to add two different list?  Adding two different list  is also called list concatenation (String concatenation)
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)
lst3 = lst2 + lst1
print(lst3)

# how to multiply list? Multiply a list is also called list replication (string replication)

dummy_lst = [7, 8, 9]
print(dummy_lst * 3)