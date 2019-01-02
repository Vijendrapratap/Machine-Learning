"""
Write a Python program to convert a NumPy array into Python list structure.

Expected Output:
Original array elements:
[[0 1]
[2 3]
[4 5]]
Array to list:
[[0, 1], [2, 3], [4, 5]]

"""
import numpy as np

myarray= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(myarray)

print("Array to list:")
print(myarray.tolist())