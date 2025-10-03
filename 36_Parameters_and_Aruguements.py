# Parameters and Arguments
'''
Parameters are the variables that are defined in the function definition.
Arguments are the values that are passed to the function when it is called.
'''
def rectangle(length, width): # length and width are parameters
    area = length * width
    return area

rectangle(4, 5) # 4 and 5 are arguments
print(rectangle(4, 5))

'''
Types of Parameters or aruguments:
1. Positional Parameters
2. Default Parameters
3. Keyword Parameters
'''

'''
1. Positional Parameters:
The arguments are passed to the function in the same order as the parameters are defined in the function.
refer above example.
'''

'''
2. Default Parameters:
The parameters that have a default value are called default parameters.
If the value of the default parameter is not passed to the function, then the default value is used.
'''
def rectangle(length, width = 5): # width is a default parameter
    area = length * width
    return area

rectangle(3) # 4 is passed to length parameter and default value 5 is passed to width parameter
print(rectangle(3))

'''
3. Keyword Parameters:
The arguments are passed to the function in the form of key = value.
The order of the arguments does not matter.
'''
def rectangle(length, width = 5): # width is a default parameter
    area = length * width
    return area

rectangle(width = 3, length = 4) # 4 is passed to length parameter and 3 is passed to width parameter
print(rectangle(width = 3, length = 4))

# Combine of positionsl and default parameters
'''
In this case first positional arugument value is passed then last only default parameter value is passed.
'''
def rectangle(length, a, width = 5): # width is a default parameter
    print(a)
    area = length * width
    return area

rectangle(4, 3) # 4 is passed to length parameter and 3 is passed to width parameter
print(rectangle(4, 3))