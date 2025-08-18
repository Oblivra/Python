f = open("Day7/myfile.txt")
#data = f.readlines()        # List class output
# print(data)

# line1 = f.readline()  # String class output
# print(line1)
# line2 = f.readline()  # String class output
# print(line2)
# line3 = f.readline()  # String class output
# print(line3)
# line4 = f.readline()  # String class output
# print(line4)
# f.close()


line = f.readline()  
while (line != ""):
    print(line,end="")
    line = f.readline()  # Read next line
f.close()