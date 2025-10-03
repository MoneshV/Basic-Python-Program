'''
Modules:
Modules are files containing Python code that can be imported and used in other Python programs.

Packages:
Packages are directories that contain multiple modules.
'''
'''
# 1 ST METHOD
import add    #| or import add , CalFun
import CalFun #|

print(add.adder(4, 6)) # add - Represents a file name & .adder - Represents a Function name.
print(CalFun.sub(4, 6))
print(CalFun.mul(4, 6))
print(CalFun.div(6, 2))
'''

'''
# 2 ND METHOD
from add import adder
from CalFun import sub, mul, div

print(adder(4, 6))
print(sub(4, 6))
print(mul(4, 6))
print(div(4, 6))
'''

# 3 RD METHOD

from CalFun import  *

print(sub(4, 6))
print(mul(4, 6))
print(div(4, 6))
print(num1)
print(num2)

import math

print(math.sqrt(9))
print(math.pow(2, 3))
print(math.pi)
