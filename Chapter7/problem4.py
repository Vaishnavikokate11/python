# print prime number means number only divide itself

n = int(input("enter your number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")