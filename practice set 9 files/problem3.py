import os

def generatetable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    

    with open(f"D:/My Workspace/python/practice set 9 files/tables/table_{n}.txt", "w") as f:
        f.write(table)
    # print("Files created here:", os.getcwd())


for i in range(1, 21):
    generatetable(i)
