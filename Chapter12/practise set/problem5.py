n = 5

table = [n*i for i in range(1,11)]
with open ("Chapter12/practise set/table.txt", "a")as f:
    f.write(f"The table of {n} {str(table)} \n")
    