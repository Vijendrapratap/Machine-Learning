"""
Write a Python program to create a contiguous flattened array.

Original array:
[[10 20 30]
[20 40 50]]
New flattened array:
[10 20 30 20 40 50]
"""
import numpy as np

myarray = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array:")
print(myarray)

y = np.ravel(myarray)
print("New flattened array:")
print(y)