# 2D and 3D array

import numpy as np

arr = np.array([[[1,2,3],[4,5,6], [7,8,9]],
                [[11,12,13], [14,15,16], [17,18,19]],
                [[19,20,21],[22,23,24],[25,26,27]]])
print(arr.ndim)
print(arr.shape)
print(arr[0][0][1])  # chain indexing

num = arr[0,0,0]+ arr[2,0,0]+ arr[2,0,0]
print(num)