#  Averages of marks 

mark1 =  float(input('Enter mark1: '))
mark2 =  float(input('Enter mark2: '))
mark3 =  float(input('Enter mark3: '))

total_marks = mark1 + mark2 + mark3
avg_mark = total_marks / 3

print('Avg mark is :',avg_mark)


# problem 1

a = int(input('Enter the A value: '))
b = int(input('Enter the B value: '))
c = int(input('Enter the C value: '))

eq = a**3 + 2*(b*c) + c**2    # a^3 + 2bc + c^2
print('Equation answer is:',eq)

#  problem 2 
#  eq = 3a^2 + b - 2c
d = int(input('Enter the d value: '))
e = int(input('Enter the e value: '))
f = int(input('Enter the f value: '))

eq1 = 3 * (d**2) + e -(2*f)   # 3a^2 + b - 2c
print('Equation answer is:',eq1)