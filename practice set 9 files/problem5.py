# make list and replace word

words = ["Donkey", "ganda", "Cat", "Monkey"]

with open("D:/My Workspace/python/practice set 9 files/file1.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("D:/My Workspace/python/practice set 9 files/file1.txt", "w") as f:
    content = f.write(content)