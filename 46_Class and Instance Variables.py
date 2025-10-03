'''
Class and Instance Variables

Class variables are variables that are shared by all the instances of the class.
Instance variables are variables that are unique to each instance of the class.
We can define instance variables in the constructor method __init__(self).
We can access instance variables using the self keyword.
We can define class variables outside the constructor method.
We can access class variables using the class name.
'''

class Father():

    age = 0 # Class variable


    def __init__(self,name):
        self.name = 'John' # Instance variable
        self.hair_color = 'Blue'
        print('This is the Father constructor method')

father1 = Father('demi')
father2 = Father('god')

print(father1.name)
print(father1.age)
#father1.age = 30 # create a new variable and assign the value
print(father2.age)

Father.age = 40 # change the value of the whole class variable. We did same as static method.
print(father1.age)
print(father2.age)