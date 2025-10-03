'''
# Abstract class
# Abstract class is a class that cannot be instantiated.
# It is used to define a common interface for a set of subclasses.
# Abstract class is a class that has at least one abstract method.
# Abstract method is a method that has no implementation.
# We can use abstract class to define a common interface for a set of subclass.
# Abstract class is used to provide a blueprint for the subclasses.
# Subclasses must implement the abstract methods of the abstract class.
# If a subclass does not implement the abstract methods of the abstract class, then it will be considered as an abstract class.
# We can use abstract class to define a common interface for a set of subclasses.
# Abstract class is used to provide a blueprint for the subclasses.
# Subclasses must implement the abstract methods of the abstract class.
# Any method that is decorated with @abstractmethod is considered as an abstract method.
# Method without abstract method, we call it as concreed method and occur error while printed.
# Once we create an abstract method in a class, then we must implement that method in all the subclasses.
'''
from abc import ABC, abstractmethod 
# To create abstract class, we need to import ABC and abstractmethod from abc module.

class car(ABC):
    @abstractmethod 
    # To create abstract method, we need to use @abstractmethod decorator.
    # Abstract method must have pass statement.
    # Without abstract method, we cannot create abstract class.
    def MoveForward(self):
        pass

    @abstractmethod
    def MoveBackward(self):
        pass
    
    @abstractmethod
    def MoveLeft(self):
        pass
    
    @abstractmethod
    def MoveRight(self):
        pass

class swift(car):
    def MoveForward(self):
        print('Swift is moving forward')

    def MoveBackward(self):
        print('Swift is moving backward')
    
    def MoveLeft(self):
        print('Swift is moving left')
    
    def MoveRight(self):
        print('Swift is moving right')

class BMW(car):
    def MoveForward(self):
        print('BMW is moving forward')

    def MoveBackward(self):
        print('BMW is moving backward')

    def MoveLeft(self):
        print('BMW is moving left')

    def MoveRight(self):
        print('BMW is moving right')


Swift = swift()
Swift.MoveForward()
Swift.MoveBackward()
Swift.MoveLeft()
Swift.MoveRight()

Bmw = BMW()
Bmw.MoveForward()
Bmw.MoveBackward()
Bmw.MoveLeft()
Bmw.MoveRight()