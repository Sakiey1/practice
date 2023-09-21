import numpy as np

a = np.array([[1,2,6], [3,4,8]])
print(a.shape) # prints (row,column) of array
print(a[0][0]) # same as java, can also do a[0,0]
print(a[:,0]) # slicing (all rows, column 0)
print(a[0,:]) # vice-versa
print("transposed array")
print( a.T) # flips r and c

# other funcs
b = np.array([[1,2], [3,4]])
print(np.linalg.inv(b)) # inverse
print(np.linalg.det(b)) # determinant
print(np.diag(b)) # returns diagonal elements of an array, else diagonalizes 1d array