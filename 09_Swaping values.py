# Swaping variables or values
a = 5
b = 7
print(a, b)
# normal code 
temp = a
a = b 
b = temp
print(a, b)

# another method
a, b = b, a
print(a, b)