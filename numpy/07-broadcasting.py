import numpy as np

# broadcast let us manipulate arrays of different shapes

x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
a = np.array([1,0,2])
y = x * a
print(y)
y = x + a
print(y)