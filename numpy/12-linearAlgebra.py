import numpy as np

a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a) # compute the eigenvalues and right eigenvectors of a square array

print(eigenvalues)
print()
print(eigenvectors) # column vector

# e_vec * e_val = A . e_vec
b = eigenvectors[:,0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:,0]
print(c)

# print(b == c) wrong way to test
print(np.allclose(b,c)) # right way to test
print()

# solving linear systems
'''
| (1 * x1) + (1*x2) = 2200
| (1.5*x1) + (4*x2) = 5050
'''

# manual way
A = np.array([[1,1], [1.5, 4.0]])
b = np.array([2200,5050])
x = np.linalg.inv(A).dot(b)
print(x)

# better way
x = np.linalg.solve(A,b)
print(x)