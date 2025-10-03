'''
Recursion:
Recursion is a process in which a function calls itself directly or indirectly.
'''
def add(n):
    print(n)
    return n + add(n - 1)

#print(add(5))

'''
infinite recursion:
Infinite recursion occurs when a function calls itself indefinitely, 
Refer to the above example.
'''

def sum(n):
    # Base case   
    if n == 0:
        return 0
    
    # Recursive case
    return n + sum(n - 1)
    
print(sum(5))

# Factorial of a number
def factorial(n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))

a = 5 * 4 * 3 * 2 * 1
print(a)