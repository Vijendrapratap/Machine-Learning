"""
Write a Python program to concatenate two 2-dimensional arrays.

Expected Output:
Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
Expected Output:
[[ 0 1 3 0 2 4]
[ 5 7 9 6 8 10]]
"""
import numpy as np

array_a = np.array([[0, 1, 3], [5, 7, 9]])

array_b = np.array([[0, 2, 4], [6, 8, 10]])

array_c = np.concatenate((array_a, array_b), 1)
print(array_c)