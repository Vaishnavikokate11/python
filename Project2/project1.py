# guess the number

import random
n = random.randint(1,100)
a = -1
gusses = 0

while(a != n):
   
    a = int(input("Enter your number"))
    if(a > n):
        print("Please enter lower number")
        gusses += 1
    elif(a<n):
        print("Please enter Higher number")
        gusses += 1

print(f"You have gussed the number is {n} correctly in {gusses} attempt")