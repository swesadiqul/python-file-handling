# Opening a Python File
'''
The very first operation to work on a file is to open it.
In Python, the open() function (built-in function) is used to open a file in both read and write mode.
This function returns a file object. In the open() function, we define two arguments in which the first is the file name 
and the second is the mode in which we want to open that file.'''

#Syntax:
file = open("abc.txt", "r")


"""In the above example, the user wants to open a file named "abc.txt" in the read mode. 
Similarly, users can open a file in different modes like "w" for write mode and "a" for append mode. 
In Python, the user can also specify the binary or textual mode in which he wants to open a file. 
It is not mandatory for a user to specify the mode of the file; 
if no mode is specified, then by default Python will open a file in reading "r" mode."""


#Syntax:
file = open("abc.txt")


"""The above two ways of opening a file will perform the same action, i.e. open a Python file in read mode.
Let’s understand different file modes in Python:"""

"""
Mode	Function Description
"r"	    It opens a file in reading mode
"w"	    It opens a file in write mode
"a"	    Opens a file in append mode (adding text at the end of the file)
"x"	    Creates a specified file, returns an error if the file already exists
"r+"   	It opens a file in both reading and writing mode
"b"	    Opens a file in binary mode (in case of images, .exe files)
"t"	    It opens a file in text mode

"""

# Examples:

# 1.Read mode?

"""file = open("abc.txt", "r") 
for x in file:
    print(x) """               
# prints the whole content of each line stored in x one by one



# 2. Write mode

"""file = open("abc.txt", "w")
file.write ("hello I am learning file operations in Python") """
  
#write the content in file file.close()


# 3. Append mode
file = open ("abc.txt","a")
file.write (". hello this will append content in the file")    
#append content at the end of file.close()