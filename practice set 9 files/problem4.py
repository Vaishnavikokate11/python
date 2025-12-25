word = "Donkey"

with open("D:/My Workspace/python/practice set 9 files/file1.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "Cat")

with open("D:/My Workspace/python/practice set 9 files/file1.txt", "w") as f:
    content = f.write(contentNew)