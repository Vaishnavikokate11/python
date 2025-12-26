with open("D:/My Workspace/python/practice set 9 files/old.txt", "r") as f:
    content1 = f.read()

with open("D:/My Workspace/python/practice set 9 files/new.txt", "w") as f:
     f.write(content1)