'''
Scope of variable:
The scope of a variable is the region of the program where the variable is defined and can be accessed.
'''

# Local variable    
def add():  
    a = 10      
    b = 20
    print( a + b)

add ()

a = 5
b = 6
print(a + b)

# Global variable
def sub():
    global c
    c = c -1
    d = 5
    print(c - d)

c = 10
sub()
print(c)
