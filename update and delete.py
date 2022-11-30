#r+ means reading and writing

file = open('python.txt','r+')

print(file.read())
file.seek(0,0)
file.write('\nMd.Mahbub Alam is my best friend.')
file.seek(0,0)
print(file.read())
file.close()
