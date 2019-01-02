"""
Write a Python program to append values to the end of an array.

Expected Output:
Original array:
[10, 20, 30]
After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]

"""

import numpy as np

myarray = np.array([10, 20, 30])
print("Original array is :", myarray)

np.append(myarray, 40)
np.append(myarray, 50)
np.append(myarray, 60)

print(myarray)