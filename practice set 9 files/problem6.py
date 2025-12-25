

with open("D:/My Workspace/python/practice set 9 files/log.txt", "r") as f:
    content = f.read()
if("Python" in content):
    print("Python is Present ")
else:
    print("something went wrong")