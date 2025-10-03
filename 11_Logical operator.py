# Logical operator
'''
1. And (&)
2. Or (|)
3. Not (!)
'''
a = 5
b = 10
print(a < b and b > a)
print(a > b and b > a)
# or
print(a < b or b > a)
print(a > b or b > a) 
# not
print(not(False))
print(not(True))

num = 10
print(num > 5 and num < 15)
print(num % 2 == 0 or  num % 3 == 0)
print(not(num == 0))