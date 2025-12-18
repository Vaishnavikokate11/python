# check tuple type cannot chnage

a = (23, 45, "vaishu", 33.5)
a[0] = 34
print(a[0])  # got error because tuple cannot chnage