# syntax: open('filename','mode')
# If you write something into the file using by the code,then it will be overwrite. there are code already.
# Create the file if it does not exit.

# file_w = open('basic.txt','w')
# file_w.write('Name: Sadiqul Islam')
# file_w.close()

# file_r = open('basic.txt','r')
# print(file_r.read())
# file_r.close()

# py_w = open('python.txt','w')
# py_w.write('Name: Sadiqul Islam \nDepertment: CMT \nSemester: 7th \nShift: 1st \nRoll: 900243 \nRegistration: 899748')
# py_w.close()

# py_r = open('python.txt','r')
# # print(py_r.read())
# py_r.close() # if you use the close method,so unknow person can't access (read and write) your file.
# print(py_r.readline())

#append mode,it will be add data or info end of the last data or info.
#create the file if it does not exits.

py_a = open('python.txt','a')
py_a.write('\nGroup: B')
py_a.close()

py_r = open('python.txt','r')
print(py_r.read())
py_r.close()