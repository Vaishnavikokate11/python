import numpy as np
arr = np.array([1,2,3,4])

np.zeros((3,4))
np.ones((3,4))
np.full((3,4),6)
np.eye((4))
np.arange(1,100,2)
np.linspace(1,100,5)

myarr = np.array([[1,2,3],[5,4,6]])
myarr.dtype

myarr.shape
myarr.size

myarr.ndim

myarr = np.array([[1,2,3],[5,4,6]], dtype='float32')
myarr

myarr.astype('float32')

myarr = np.array([[1,2,3],[5,4,6]])
reshaped = myarr.reshape((2,3))
reshaped