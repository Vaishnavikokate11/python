with open("D:/My Workspace/python/practice set 9 files/file1.txt", "r") as f:
    content1 = f.read()

with open("D:/My Workspace/python/practice set 9 files/file2.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("match")
else:
    print("not match")