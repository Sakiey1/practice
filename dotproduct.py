import numpy as np

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

