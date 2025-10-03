# ODD or EVEN 

num = int(input('Enter num:'))

if(num % 2 == 0):
    print(num,'is even number')
else:
    print(num,'is odd number')

# By using Ternary operator

print(num,'is even' if(num % 2 == 0) else num,'is odd')