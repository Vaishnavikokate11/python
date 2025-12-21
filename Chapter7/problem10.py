#print multiplication table in reverse order

n = int(input("enter your number: "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
    