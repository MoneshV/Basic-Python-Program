'''
# File Handling
# File handling is the process of working with files in a computer.
# We can read, write, append, and delete files using Python.
# We can use the open() function to open a file.
# We can use the close() method to close a file.
# We can use the read() method to read the contents of a file.
# We can use the write() method to write to a file.
# We can use the append() method to append to a file.
# We can use the delete() method to delete a file.
'''
# Open a file
# It has two parameters: filename and mode.
# Mode is optional. Default mode is read (r).
# We can use the following modes:
# r - Read
# w - Write
# a - Append
# x - Create
# r+ - Read and Write
# w+ - Write and Read
# a+ - Append and Read
# x+ - Create and Read

# Two Types to open a file:

'''
# 1 st Method
#file = open('File Handling\info.txt','r') # Relative Path
#print(file.read())
# file.close()

# 2 nd Method
file = open('D:\PYTHON program\File Handling\info.txt','r') # Absolute Path
# File read 
#print(file.read())
#print(file.read(5)) # It will read only 5 characters.


# File read line by line
print(file.readline())
print(file.readline())

# File readlines
print(file.readlines())
file.close()
'''
'''
# Write a file
file = open('File Handling\info.txt','w')
file.write('Hello World') # Overwrite the file by clearing a existing file.
file.close()
'''
'''
# Append a file
file = open('File Handling\info.txt','a')
file.write('Hello Demi') # Append the file by adding a new line.
lst= ['Adding a word to the file.\n','slash n moves to next line.']
file.writelines(lst)

file.close()
'''

# cusor position
file = open('File Handling\info.txt','r')
print(file.read())
print(file.tell()) # It will show the cursor position.
print(file.seek(0)) # cursor move to the 0 th index of the file.
print(file.tell())
print(file.read())
file.close()

# 2 nd Method did not close the file automatically.
with open('File Handling\info.txt','r') as file:
    print(file.read())
    print(file.tell()) # It will show the cursor position.
    print(file.seek(0)) # cursor move to the 0 th index of the file.
    print(file.tell())
    print(file.read())

file.flush() # It will clear the buffer.
file.close()