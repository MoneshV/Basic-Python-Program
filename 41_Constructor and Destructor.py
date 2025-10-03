'''
# Constructor and Destructor
Constructor is a special method that is called when an object is created.
Destructor is a special method that is called when an object is destroyed.
self is a reference to the current instance of the class.
id(self), it represents a memory allocation eg : 179302...
__init__() is a constructor method that is called when an object is created.
__str__() is a special method that is called when an object is printed.

'''

class car :
    def __init__(self,carname,no_of_wheels, no_of_airbags, no_of_milage):
        print("The car is created")
        self.no_of_wheels = no_of_wheels
        self.no_of_airbags = no_of_airbags
        self.no_of_milage = no_of_milage
        self.carname = carname

    def __str__(self):
        return (self.carname)


    def move_forward(self, speed):
        print("The car is moving forward at speed", speed)
         
    def move_backward(self):
        print("The car is moving backward")
        
    def __del__(self):
        print("The car is destroyed",self)

# Creating an object of the car class
car1 = car('BMW',4, 5, 10)
print(car1)
print(car1.no_of_wheels)
print(car1.no_of_airbags)
print(car1.no_of_milage)
car1.move_forward(60)
car1.move_backward()
print(id(car1))



# QUIZ 
# Bank

class bank_account:
    def __init__(self,customer_name,balance,account_number):
        self.customer_name = customer_name
        self.balance = balance
        self.account_number = account_number
        print("The bank account is created")
        
    def __str__(self):
        return (self.customer_name)

customer1 = bank_account('John Doe',1000,123456)
print(customer1)
print(customer1.balance)
print(customer1.account_number)
