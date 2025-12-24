# no need to write f.close()

with open("myfile.txt") as f:
    print(f.read())