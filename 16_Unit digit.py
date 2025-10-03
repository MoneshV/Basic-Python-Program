#  To Print Unit digits of a value or number.

#  first method
num = input()
print(num[len(num)-1])
# or
print(num[-1])

#  2nd method
num1 = int(input('enter num1:'))
num1 = num1 % 10
print(num1)



#  To print Tenth digit of a number
# 1 st method
val = input()
print(val[len(val)-2])
# or
print(val[-2])

# 2 nd method
val1 = int(input())
val1 = val1 // 10
val1 = val1 % 10
print(val1)
