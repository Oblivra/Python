f = open("Day7/Twinkle.txt")
content = f.read()
if ("twinkle" in content):
    print("twinkle is found")
else:
    print("twinkle is not found")
f.close() 