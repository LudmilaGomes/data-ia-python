import numpy as np

a = np.array([1,2,3])
b = a
print(a)
print(b)
b[0] = 34 # modify both arrays; copy reference to the same location in the memory
print(a)
print(b)
print()

a = np.array([1,2,3])
b = a.copy()
print(a)
print(b)
b[0] = 34 # modify only b
print(a)
print(b)