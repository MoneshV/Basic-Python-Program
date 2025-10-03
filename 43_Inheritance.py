'''
# Inheritance
# Inheritance is a mechanism in object-oriented programming that allows a new class to be based on an existing class.
# The new class, called the derived class or subclass, inherits the attributes and methods of the existing class,
# called the base class or superclass.
# Inheritance promotes code reuse and allows for the creation of a hierarchy of classes that share common features.

# Types of Inheritance
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
'''

# Inheritance Example:
# Single Inheritance

class vechicle :
    no_of_wheels = 4

    def movingforward(self):
        print('Vechicle is moving forward')

class car(vechicle):
    no_of_doors = 4
    no_of_airbags = 5

car1 =car()
print(car1.no_of_wheels)
print(car1.no_of_doors)
print(car1.no_of_airbags)
car1.movingforward()

# Multilevel Inheritance
class grand_father: # parent class
    hair_color = 'White'
    
class father(grand_father): # parent class / base class
    eye_color = 'Blue'
    
class son(father): # child class
    no_of_fingers = 11

son1 = son()
print(son1.hair_color)
print(son1.eye_color)
print(son1.no_of_fingers)

# Multiple Inheritance

class father: # parent class
    eye_color = 'Blue'
    hair_color = 'white'

class mother: # parent class
    hair_color = 'Black'
    
class son(father,mother): # Which class declare or inherit first, that class attribute will be inherited.
    no_of_fingers = 11

son1 = son()
print(son1.hair_color)
print(son1.eye_color)
print(son1.no_of_fingers)


# Hierarchical Inheritance
class grand_father: # parent class
    hair_color = 'White'
    eye_color = 'green'
    
class father(grand_father): # parent class / base class
    eye_color = 'Blue'
    
class son(grand_father): # child class
    no_of_fingers = 11

son1 = son()
print(son1.hair_color)
print(son1.no_of_fingers)
print(son1.eye_color)

# Quiz

class father: # parent class
    eye_color = 'Blue'
    hair_color = 'white'

    def music(self):
        print('Kuthu songs')
        
class mother: # parent class
    hair_color = 'Black'
    
    def music(self):
        print('Melody songs')
    
class son(father,mother): # Which class declare or inherit first, that class attribute will be inherited.
    no_of_fingers = 11

son1 = son()
print(son1.hair_color)
son1.music()