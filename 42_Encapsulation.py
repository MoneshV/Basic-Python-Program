'''
# Encapsulation
Encapsulation it refers to the process of binding the data (attributes) and methods that operate on the data into a single unit, i.e., a class.
.Encapsulation is the process of hiding the implementation details of an object from the outside world.
It is done to prevent the accidental modification of the object's state.
..We can achieve encapsulation in Python by using private attributes and methods.
Private attributes and methods are those that are prefixed with a double underscore (__).
Encapsulation allows us to control access to the object's attributes and methods.
...This will make the attribute or method inaccessible from the outside world.
.... We can access the private attributes and methods using the getter and setter methods.

.....Getter methods are used to get the value of a private attribute.
.....Setter methods are used to set the value of a private attribute.

'''

class car :
    def __init__(self,carname, no_of_wheels,no_of_airbags):
        print('This is constructor')
        self.carname = carname
        self.__no_of_wheels = no_of_wheels # Private attribute.
        self.no_of_airbags = no_of_airbags 
    
    def __str__(self):
        return (self.carname)
    
    def get_no_of_wheels(self): # To access the private attribute __no_of_wheels
        return('No of wheels : ',self.__no_of_wheels) 

    def set_no_of_wheels(self, no_of_wheels):
        self.__no_of_wheels = no_of_wheels
        
# Creating an object of the car class
car1 = car('BMW',4, 5)
print(car1)
# print(car1.__no_of_wheels)
print(car1.get_no_of_wheels(),car1.no_of_airbags)


# To update the private attribute __no_of_wheels
__no_of_wheels = 5 # This is not the way to update the private attribute.
print(__no_of_wheels) # It creates a new local variable __no_of_wheels.
print(car1.get_no_of_wheels())

# To update the private attribute __no_of_wheels using setter method.
car1.set_no_of_wheels(6)
print(car1.get_no_of_wheels())



car2 = car('Audi',6, 5)
print(car2)
# print(car2.__no_of_wheels,car2.no_of_airbags)
print(car2.get_no_of_wheels(),car2.no_of_airbags)