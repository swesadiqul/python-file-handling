# Writing a file

"""
To write a file in Python, we need to first open the file either in write “w”, append “a”, 
or exclusion creation “x” mode.
"""

"""
There is a minor difference between append and write mode in Python, 
and one needs to be very careful about this that append method adds the content at the end of the file, 
i.e. it will not affect the data if the file is already created and have some data in it. 
The writing method will overwrite the file’s content if the file having some data is already present. 
This method does not return anything.
"""

# Example

file = open ("abc.txt", "r+") 
file.write("this is line 1\n") 
file.write ("this isline 2\n") 
file.close()


# 2. writelines() method: 

"""​writelines() method is also used to write a sequence of strings to a file.
"""

# Example:
file = open ("abc.txt", "w")
lines = ["this is line 1", "this is line 2"] 
file.writelines(lines)
file.close()