'''
# Polymorphism
# Polymorphism it refers to the ability of an object to take on many forms.
# In other words, it allows us to use a single interface to represent different types of objects.
# Polymorphism is achieved in Python through method overloading and method overriding.
# Method overloading is the ability to define multiple methods with the same name but different parameters.
# Method overriding is the ability to redefine a method in a derived class that is already defined in the base class.
'''

# Method overloading in Python
class summation:
    '''
    how to implement method overloading in C ?
    Example:
    int add(int a, int b) {
        return a + b;
    }
    int add(int a, int b, int c) {
        return a + b + c;
    }
    '''
    def add(self, a, b, c=0):
        return a + b + c

        #OR we can use for loop for method overloading for n number of parameters.
    def add(self,*args):
        added = 0
        for i in args:
            added += i
        return added
        # OR we can use sum() function to add the elements of the list.
    #   return sum(args)
        
summ = summation()
print(summ.add(1,2))
print(summ.add(1,2,3))

print(summ.add(1,2,3,4,5,6,7,8,9,10)) # for loop and sum() function

# Method overriding in Python

class father:
    def __init__ (self):
        print('This is constructor of father class')

    def say_hello(self):
        print('Hello from father !')

class son(father):
    def __init__(self): 
        print('This is constructor of son class')
    def say_hello(self): # same method name as in father class. But, it will override the say_hello() method of the father class.
        print('Hello from son !')

son1 = son()
son1.say_hello() #father class is inherit. But, it will override the say_hello() method of the father class.
Father = father()
Father.say_hello()