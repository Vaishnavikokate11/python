# make the copy of this.txt file

with open("D:/My Workspace/python/practice set 9 files/this.txt", "r") as f:
    content = f.read()

with open("D:/My Workspace/python/practice set 9 files/thiscopy.txt", "w") as f:
    f.write(content)

