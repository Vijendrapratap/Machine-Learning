"""
Write a Python program to change the data type of an array.

Expected Output:
[[ 2 4 6]
[ 6 8 10]]
Data type of the array x is: int32
New Type: float64
[[ 2. 4. 6.]
[ 6. 8. 10.]]

"""
import numpy as np

myarray = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(myarray)
print("Data type of the array x is:", myarray.dtype)

# Change the data type of x
y = myarray.astype(float)
print("New Type: ",y.dtype)
print(y)