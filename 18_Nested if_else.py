#  Nested if 
age = int(input('Enter a age: '))
eat_pizza = True
exercise = False

if(age < 30):
    if(eat_pizza):
        if(exercise):
            print('Fit')
        else:
            print('Unfit')
    else:
        if(exercise):
            print('Fit')
        else:
            print('unfit')
else:
    if(age > 30):
        if(exercise):
            print('Fit')
        else:
            print('Unfit')

print( (('fit' if (exercise) else 'unfit') if(eat_pizza) else (('fit' if (exercise) else 'unfit')))if(age<30) else ('fit' if(exercise) else 'unift'))