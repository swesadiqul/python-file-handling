# Reading a File
"""
To read a file in Python, we need to open it first in the read mode. 
There are several methods of reading a file provided by Python.

"""
# Let’s understand them one by one:
"""
1. read() method: ​This method reads the whole file at a time. This method returns \n for the new line. 
Once the whole file is completed, we get a whole empty string, 
so we need to set the cursor again using seek() and tell() methods.

"""
# Example

# File:
"""
This is line 1
This is line 2

"""
file = open ("abc.txt", "r") 
print(file.read())  
#This is line 1
#This is line 2


# 2. readline() method: 
"""
This method is used to read the file one line at a time till the​ \n character is found in the file. 
It adds \n at the end of the line.

"""
# ​Example?

file = open ("abc.txt" , "r") 
print(file.readline())
#This is line 1


# 3. readlines() method: ​
"""
This method is used to read the whole file but line by line. 
It updates the file by each line that is returned.

"""
# Example

file = open ("abc.txt", "r") 
print(file.readlines())

# ​This is line 1
# ​This is line 2


# 4. read(n) method:
"""
This method is used if we want to read a specified length of​ characters in a file.

"""

file = open ("abc.txt", "r") 
print(file.read(5))

# ​‘This ‘ (including 1 space after s) (read 5 characters of a file)
