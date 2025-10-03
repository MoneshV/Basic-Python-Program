#  Conditional statemets

#  Simple if only to check one condition
if(5 == 6):
    print('if condition is true this statement will execute')



# if else  this or that
if(5 == 5):
    print('if condition is true this statement will execute')

else:
    print('if condition is false this statement will execute')


#  elif to check more than one condition use elif
a = int(input('Enter a : '))
b = int(input('Enter b : '))
if( a == b):
    print('if condition 1 is true this statement will execute')
elif( a <= b ):
    print('if condition 2 is true this statement will execute')

else:
    print('if both condition is false this statement will execute')


# Example
num = int(input('Enter  num: '))

if num > 0 :
    print('positive number.')
    print(num,'is a positive number.')
elif(num == 0):
    print('Zero')
else:
    print('Negative number')

print('Done')


# Quiz 1
x = 5
y = 10

if(x > y):
    largest = x
else:
    largest = y
print('The largest number is :', largest)
