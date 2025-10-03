'''
# Class and Object
Class is a blueprint for creating objects.
Object is an instance of a class.
'''
class car :
    no_of_wheels = 4  # Default values 
    no_of_airbags = 5  # Data Members.
    no_of_milage = 10

    def move_forward(self): # Class Methods
        print("The car is moving forward")
        
    def move_backward(self):
        print("The car is moving backward")

# Creating an object of the car class
car1 = car()
print(car1.no_of_wheels)
print(car1.no_of_airbags)
print(car1.no_of_milage)
car1.move_forward()
car1.move_backward()

car2 = car()
print(car2.no_of_wheels)
car2.no_of_wheels = 6
print(car2.no_of_wheels)
print(car1.no_of_wheels)

#QUIZ

class bank_account:
    customer_name = ''
    balance = 0
    account_number = 0
# create an object for this class and the member variables
customer1 = bank_account()
customer1.customer_name = 'John Doe'
customer1.balance = 1000
customer1.account_number = 123456
print(customer1.customer_name)
print(customer1.balance)
print(customer1.account_number)
