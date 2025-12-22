# multiplication of given numb

def multiplication(n):
    for i in range(1,n+1):
        print(f"{n} X {i} = {n*i}")
    
numb = int(input("Enter your number: "))
print(multiplication(numb))