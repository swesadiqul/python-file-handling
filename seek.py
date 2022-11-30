#syntax: seek(offset,whence)
#offset: the seek() method sets the current file position in a file stream
#Whence(default)-0
# 0: sets the reference point at the beginning of the file
# 1: sets the reference point at the current file position
# 3: sets the reference point at the end of the file

file = open('basic.txt','r')
file.seek(6,0)
print(file.read(5))
file.seek(0,0)
print(file.read())
file.close()