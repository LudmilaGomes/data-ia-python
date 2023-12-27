import numpy as np

a = np.array([[1,7,9], [2,4,5], [6, 8,0]])

print(a.shape) # matrix[rows X columns]
print(a[0])    # first row
print(a[0][0]) # first element of first row
print(a[0, 0]) # first element of first row - other way to write the line above
print(a[:,0])  # elements of first column
print()

print(a)
print(a.T) # transpose
print()

print(np.linalg.inv(a)) # inverse; arrays must be square: matrix[N X N]
print(np.linalg.det(a)) # determinant
print(np.diag(a))       # return elements of diagonal
print()