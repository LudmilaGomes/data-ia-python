import numpy as np

# initializing arrays
a = np.zeros((2,3), dtype=np.int32) # default data type is float
print(a)
a = np.ones((2,3), dtype=np.int32)
print(a)

a = np.full((2,3), 5)
print(a)

a = np.eye(3)
print(a)

a = np.arange(5)
print(a)

a = np.linspace(0, 20, 5) # equally space
print(a)

a = np.random.random((3,3)) # default 0-1
print(a)

a = np.random.randn(1000) # normal/Gaussian distribution of mean 0 and variance 1
print(a)

a = np.random.randint(3, 10, size=(3,3)) # [low, high)
print(a)

a = np.random.choice(5, size=10) # [low, high)
print(a)
a = np.random.choice([9,8,7], size=10) # [low, high)
print(a)