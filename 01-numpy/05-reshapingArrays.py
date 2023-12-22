import numpy as np

a = np.arange(1, 7)
print(a)
print(a.shape)
print()

b = a.reshape((2, 3)) # reshape into 2 rows and 3 columns
print(b)
print(b.shape)
print()

b = a.reshape((3, 2)) # reshape into 2 rows and 3 columns
print(b)
print(b.shape)
print()

b = a[np.newaxis, :]
print(b)
print(b.shape)
print()

b = a[:, np.newaxis]
print(b)
print(b.shape)