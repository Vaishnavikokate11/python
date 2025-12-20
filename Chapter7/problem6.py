# factorial of number 
# 5! = 1*2*3*4*5

n = int(input("enter your number: "))
product = 1

for i in range(1, n+1):
    product = product*i
    
print(f"the factorial of {n} is {product}")
    