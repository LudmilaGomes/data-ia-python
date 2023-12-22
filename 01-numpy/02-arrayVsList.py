import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

# things we can do with lists (impossible with arrays)
l.append(34) # add a number as last element on list
l = l + [4]  # add a number as last element on list
l = l * 2    # repeat our list

a = a + np.array([4]) # each element of array is incremented with the number '4'
a = a * 2             # each element of array is multiplied by 2 

# operations are aplicated in lists; operations are aplicated in elements of arrays

print(a)
print(l)