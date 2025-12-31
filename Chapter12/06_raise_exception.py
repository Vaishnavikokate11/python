a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

if (b == 0):
    raise ZeroDivisionError("Hey your program is not meant to divide by zero")
else:
    print(f"The division is {a/b}")