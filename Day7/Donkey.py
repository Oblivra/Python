words = ["donkey", "Donkey", "ganda"]

with open("Day7/Donkey.txt", "r") as f:
    content = f.read()
for word in words:
    with open("Day7/Donkey.txt", "w") as f:
        content = content.replace(word, "#" * len(word))
        f.write(content)  