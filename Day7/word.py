with open("Day7/word.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Python is mentioned in the file. Line no: {lineno}")
        break
    lineno += 1
else:
    print("Python is not mentioned in the file.")