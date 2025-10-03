# BITWISE OPERATOR 
'''
Bitwise and &
Bitwise or |
Bitwise not ~
Bitwise xor ^
Bitwise right shift >>
Bitwise left shift <<
'''

# Bitwise and &
a = 2
b = 3
print(a & b)
'''
How its work ?
 value of 2 covert to binary value= 10
                                     _
 value of 3 covert to binary value= 11
                                     _
Compare each bit value and perform and operator value of  print(a & b) is 10 thats equal to  2.
'''
# Bitwise or |
print(a | b)

# Bitwise not ~
print(~a,~b)

# Bitwise xor ^
print(a ^ b)

# Bitwise right shift >>
print(a >> 1)

# Bitwise left shift <<
print(a << 1)

# Example
x = 10 # 1010 in binary
y =  4 # 0100 in binary
print(x & y)
print(x | y)
print(x ^ y)