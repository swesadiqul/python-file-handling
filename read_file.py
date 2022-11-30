# Assume we have the following file, located in the same folder as Python
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for
#  reading the content of the file:

'''
y = open('example.txt') # it will be open read mode by default

y = open('example.txt','rt') #this is the same code like above code, rt-means read text

print(y.read())
'''



# If the file is located in a different location, you will have to specify the file path,
#  like this:
# Open a file on a different location:
'''
x = open('H:\myfiles\welcome.txt', 'rt')

print(x.read())'''


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify
# how many characters you want to return:

# Return the 5 first characters of the file:

'''
z = open('simple.txt', 'rt') # this is a default mode - rt means read text

print(z.read(5)) # must be it will return 5 charecter from this file
'''

# You can return one line by using the readline() method:
# Read one line of the file:

'''
a = open('example.txt', 'r') # this is a default mode r-means read
print(a.readline()) # it will be return only one line from this file
'''


# By calling readline() two times, you can read the two first lines
# Read two lines of the file

'''
f = open('example.txt', 'r')
print(f.readline())
print(f.readline())
'''
# By looping through the lines of the file, you can read the whole file, line by line
# Loop through the file line by line

'''
h = open('example.txt', 'r')

for single_line in h:
    print(single_line)
'''
# It is a good practice to always close the file when you are done with it.
# Close the file when you are finish with it

'''
j = open('example.txt', 'rt')
print(j.readline())
j.close()
'''

