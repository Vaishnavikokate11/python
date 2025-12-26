#read line where python word is present



with open("D:/My Workspace/python/practice set 9 files/log.txt", "r") as f:
    lines = f.readlines()

lineno = 1   

for line in lines:
    if("Python" in line):
        print(f"Python is Present {lineno}")
        break
    lineno += 1
    
    
else:
    print("something went wrong")