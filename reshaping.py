import numpy as np

a = np.arange(1,7)
print(a) # 1d array with numbers from 1 to 6
print(a.shape)
b = a.reshape((2,3)) # makes it 2 rows 3 columns
print(b)