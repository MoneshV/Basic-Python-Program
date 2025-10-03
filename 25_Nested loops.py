#  Nested Loops 
'''
1
1 2
1 2 3
1 2 3 4
'''
n = int(input('Enter no of rows :'))

for i in range(1,n+1):    # | This statement says how many lines wants to print in o/p.  
    for j in range(1,i):  # | This statement says how many print in one line or         
        print(j,end=' ')  # | This statement says in one line how many wants to print.   
    print()
