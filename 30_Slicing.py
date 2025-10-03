# Slicing
'''
Slicing is the process of extracting a portion of a sequence (like a list, tuple, or string) by specifying a range of indices.
'''

# String
Str = 'DemiGod'
print(Str[0:5:2]) # 0 is start index, 4 is end index, 2 is step
print(Str[: 6]) # 0 is start index, 6 is end index, 1 is step
print(Str[::-1]) # reverse the string

# List same as tuple
lst = [1, 2, 3, 4, 5, 6]
print(lst[: 6]) # 0 is start index, 6 is end index, 1 is step
print(lst[1: 60]) # 1 is start index, 60 is end index, 1 is step
print(lst[10: 60]) # 10 is start index, 60 is end index, 1 is step
print(lst[::]) # start index is 0, end index is len(lst), step is 1, so it will print the whole list
print(lst[::-1]) # start index is len(lst)-1, end index is -1, step is -1, so it will print the whole list in reverse order

# Quiz 
numbers = [2, 5, 1, 8, 4]
print(numbers[1:4])

numbers[2:4] = [3, 7]
print(numbers)