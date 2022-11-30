#mode means situation that means what to do in this file
#for example-
#r means read mode, w means write mode
#in the same way r+ means reading and writting mode, w+ means writting and reading mode
# a+ means appending and reading mode

# +mode

# file = open('User file.txt','r+')

# print(file.read())
# file.write(' He is a good guy.')
# file.seek(0,0)
# print(file.read())
# file.close()

# file = open('User file.txt','w+')

# print(file.read())
# file.write(' He is a good guy.')
# file.seek(0,0)
# print(file.read())
# file.close()

file = open('User file.txt','a+')
file.seek(0,0)
print(file.read())
file.write(' He is a good guy.')
file.seek(0,0)
print(file.read())
file.close()




