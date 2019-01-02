"""
Write a Python program to remove specific elements in a numpy array.

Expected Output:
Original array:
[ 10 20 30 40 50 60 70 80 90 100]
Delete first, fourth and fifth elements:
[ 20 30 60 70 80 90 100]

"""

import numpy as np

myaaray = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = [0, 1, 8]
print("Original array:")
print(myaaray)

print("Delete first, second and eighth elements:")
new_array = np.delete(myaaray, index)
print(new_array)