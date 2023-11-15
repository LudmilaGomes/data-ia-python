'''
 - core library for scientific computing in python
 - data science, machine learning, deep learning, scikit-learn, matplotlib, pandas, ...
 - high performance multidimensional array -> fast
 - mathematical operations with arrays
 - a lot of code written in C
 - array/matrix operations - linear algebra
 - dot product
 - matrix multiplications
 - linear systems
 - inverse, determinant
 - eigenvectors
 - random numbers
 - images represented as arrays
...

'''
import numpy as np

print(np.__version__)

a = np.array([1, 2, 3, 4]) # array of numpy
print(a)
print(a.shape)      # analize the array; return tuple with number of dimensions and of elements
print(a.dtype)      # return data type
print(a.ndim)       # return number of dimensions
print(a.size)       # return number of elements
print(a.itemsize)   # return bytes of one element

# access for each element of array is done with index (like normal lists in Python)
print(a[0])  # first element
print(a[-1]) # last element

b = a * np.array([2, 0, 4, 1]) # [1, 2, 3, 4] * [2, 0, 4, 1]
print(b) # [2, 0, 12, 4]
