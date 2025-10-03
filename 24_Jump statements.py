#  Pass statements
'''
Jump statements it has two types are:
1. continue
2. Break
'''

#  1. continue

for i in range(5):
    if(i == 3):
        continue
    print(i)

# 2. break

for i in range(5):
    if(i == 3):
        break
    print(i)


while True :
    print('Inside loop')
    break
print('outside loop')
    
#  else clause in loops

for i in range(5):
    print(i)
else:   # when the loop normally terminiated then only else block will execute.
    print('succesfully completed.')


# 2 example

for i in range(5):
    if (i == 3):
        continue
    print(i)
else:   # when the loop normally terminiated then only else block will execute.
    print('succesfully completed.')


#  3  example

for i in range(5):
    if i == 3 :
        break
    print(i)

else:    # in this condition else block will not execute because loop is not properly terminiated.
    print('succesfully completed.')


#  4 example

a = 5
while (a > 0):
    print(a)
    a -= 1 
else:
    print('Successfully completed')


# 5 example

a = 3
while (a > 0):
    print(a)
    a -= 1
    if(a == 1):
        break
else:
    print('Successfully completed')
    