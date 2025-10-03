'''
Void Function:
A function that does not return any value is called a void function.
It is used to perform some action or task that does not require a result.

Non-void Function:
A function that returns a value is called a non-void function.
It is used to perform some action or task that requires a result.  
'''
# Void Function
def add1():
    a = int(input('Enter a first number :' ))
    b = int(input('Enter a second number :' ))
    print( a + b)

sum1 = add1()
print(type(sum1))

# Non-void Function
def add2(a, b):
    return a + b
sum2 = add2(4, 6)
print(sum2)
print(type(sum2))
