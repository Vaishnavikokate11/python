#using python list
import numpy as np
import time
size = 1_000_000

l1 = list(range(size))
l2 = list(range(size))

start = time.time()
add = [X+y for X,y in zip(l1,l2)]
end = time.time()
print(end - start)

#using numpy array
import numpy as np
import time
size = 1_000_000

l1 = np.array(list(range(size)))
l2 = np.array(list(range(size)))

start = time.time()
add = l1 + l2
print(add [0:10])
end = time.time()
print(end - start)

#python zip explain
l1 = [1,2,3]
l2 = [4,5,6]
list(zip(l1,l2))

#using python list
import numpy as np
import time
list1 = [1,2,3,4,5,6,7]
start = time.time()
list_squares = [x**2 for x in list1]
end = time.time()
print(end - start)

#using python list
import numpy as np
import time
arr = np.array([[1,2,3],[4,5,6]])
start = time.time()
numpy_squre = arr ** 2
end = time.time()
print(end - start)