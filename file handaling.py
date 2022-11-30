# create new file
f = open('demo.txt', 'w')
f.write('Welcome to file handaling')
f.close()

# store integer file as a string
##g = open('example.txt', 'a')
##a = 3
##b = 15
##c = a + b
##g.write('Welcome to write mode. ')
##g.write(str(c))
##g.write("")
##g.close()


# open existing file
##file = open('example.txt', 'r')
####print(g.readline())
##for line in file:
##    print(line)
##
##file.close()

##with open('example.txt', 'r') as file:
##    d = file.read()
##    print(d)
##    file.close()


with open('example.txt', 'r') as file:
    d = file.readlines()
    for line in d:
        words = line.split()
        print(words)
file.close()
