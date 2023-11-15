import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum(axis=1)) # axis=None is default
print(a.sum(axis=0)) 
print(a.mean(axis=None)) 
print(a.min(axis=None)) 
print(a.max(axis=None)) 
print(a.var(axis=None)) # variance
print(a.std(axis=None)) # standard deviation