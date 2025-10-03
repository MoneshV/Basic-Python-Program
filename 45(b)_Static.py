'''
# Static method
# Static method is a method that belongs to a class rather than an instance of the class.
# We can call a static method using the class name.
# We can define a static method using the @staticmethod decorator.
# Static method does not have access to the instance of the class.
# Static method does not have access to the class attributes.
# Static method is used to perform a task that does not depend on the instance of the class.
'''

class swift():
    def MoveForward(self): # self is instance or object  of the class.
        print('Swift is moving forward')
    
    @staticmethod
    def MoveBackward():
        print('Swift is moving backward')
    
    def MoveLeft(self):
        print('Swift is moving left')
    
    def MoveRight(self):
        print('Swift is moving right')

# Normal method to call any method by using the object of the class.
Swift = swift()
Swift.MoveForward()
Swift.MoveLeft()
Swift.MoveRight()

# Static method to call the MoveBackward method without creating an object of the class.
swift.MoveBackward()
