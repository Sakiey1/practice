import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)

b = a[0,1:3] # row 1, columns 1 to 3
print(b)

x = np.array([1,2,3,4,5,6,7])
y = [1,3,5]
print(x[y]) # prints indicies reffered to in y
even = np.argwhere(x%2==0).flatten() # grabs even indicies, flattens to make 1d
print(x[even])