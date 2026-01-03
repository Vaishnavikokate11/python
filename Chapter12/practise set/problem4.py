

try:
    a = int(input("enter your number"))
    b = int(input("enter your number"))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")
    