"""
Write a Python program to find the number of elements of an array,
length of one array element in bytes and total bytes consumed by the elements.

Expected Output:
Size of the array: 3
Length of one array element in bytes: 8
Total bytes consumed by the elements of the array: 24
"""
import numpy as np

myarray = np.array([1, 2, 3], dtype=np.int8)

print("Size of the array: ", myarray.size)
print("Length of one array element in bytes: ", myarray.itemsize)
print("Total bytes consumed by the elements of the array: ", myarray.nbytes)
