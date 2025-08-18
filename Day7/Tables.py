def generateTable(n):
    table = ""
    for i in range(1, 11):
        table = table + f"{n} x {i} = {n * i}\n"

    with open(f"Day7/Tables/table_of_{n}.txt", "w") as f:
        f.write(table)

for i in range(1, 21):
    generateTable(i)