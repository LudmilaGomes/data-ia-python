import numpy as np

# a = x1 + y1 + z1; b = x2 + y2 + z2
# dot product: a . b = x1x2 + y1y2 + z1z2

l1 = [1,2,3]
l2 = [4,5,6]

dot = 0 
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

a1 = np.array(l1)
a2 = np.array(l2)

dot = np.dot(a1, a2)
print(dot)

# or

sum1 = a1 * a2       # [x1x2, y1y2, z1z2]
print(sum1)          
dot = np.sum(sum1)   # x1x2 + y1y2 + z1z2
print(dot)

# or

dot = a1 @ a2
print(dot)