# Closing a file

"""
It is a good practice to close a file after the desired operations are done on it as 
this will free up all the resources used in that file and be allocated somewhere else by 
the Operating System. For closing a file in Python, the close() method is used.

Although it is not mandatory to close a file as the Python uses the garbage collector
to clean the unreferenced objects, but it is a good practice, and we must do it.

"""
#Syntax: 
"""file.close()"""

# Example:

file = open ("abc.txt", 'a') 
file.write ("apend the text") 
file.close()

"""
It does not take any parameter like opening a file, but this method is not totally safe as in 
case of exceptions, it might exit the code without closing a file. 
For this, it is better to use the close() method in the finally block so that it will run every time, 
even in case of exceptions.
"""

# Example using try and finally

try : 

    file = open("abc.txt","w") 

finally:

    file.close()