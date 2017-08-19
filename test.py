import  cv2
import tensorflow as tf
import  numpy as np
# a= np.random.random((3,4))
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)
print(a[0:-1,4:5])

x = np.array([[1,2],[3,4]])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x
print(x)  # Compute sum of all elements; prints "10"
print(y)
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

