import numpy as np

a = np.array([1,2,3])

a = a + np.array([4]) # adds 4 to each element
a = a *2 # multiplies each element by 2
a = np.log(a) # log each element
a = np.sqrt(a) # sqrt each element
"""print(a)"""
# numpy array modification is elements based

# dot product in py
l1 = [1,2,3]   
l2 = [4,5,6]
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
"""print(dot)"""

# dot product in numpy
a1 = np.array(l1) # passing in l1 array
a2 = np.array(l2) # passing in l2 array
dot = np.dot(a1,a2) # multiples elements by index for 2 arrays and sums them a[1]*b[1] + a[n]*b[n]
dot = a1 @ a2 # this also works
"""print(dot)"""


# MD arrays (multi-dimensional)
