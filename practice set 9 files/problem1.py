f = open("poem.txt", "r")
data = f.read()
if("twinkle" in data):
    print("Yes, the word twinkle is present" )
else:
    print("No, the word twinkle is not present")
f.close()