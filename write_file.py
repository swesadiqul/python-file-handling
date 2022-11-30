# To write to an existing file, you must add a parameter to the open() function
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# Open the file "simple.txt" and append content to the file

'''
x = open('simple.txt', 'a')
x.write(' ' + 'Hello Django Developer. How are you?' + ' ')
x.close()

y = open('simple.txt', 'r')
print(y.read())
'''

# Open the file "simple.txt" and overwrite the content

'''
z = open('simple.txt', 'w')
z.write("I'm Sadiqul  Islam. I'm 23 years old. I'm from Rangpur at Mithapurkur. I study in Thakurgaon Polytechnic Institute. My father is a teacher and my mother is a homemaker. We are three brothers and sisters. And I'm oldest in my family.")
z.close()

#open and read the file after the overwriting
f = open('simple.txt', 'rt')
print(f.read())
'''
# Note: the "w" method will overwrite the entire file.


