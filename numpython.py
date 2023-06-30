import numpy as np

# A 2-dimensional array of 2 x 3, composed of 4-byte integer elements: 
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(type(x)) # <class 'numpy.ndarray'>
print(x.shape) # (2, 3)
print(x.dtype) # int32
print(x[1]) # [4 5 6]
print(x[1, 1]) # 5

