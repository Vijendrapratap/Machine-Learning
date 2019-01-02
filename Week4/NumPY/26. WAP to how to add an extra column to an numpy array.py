"""
Write a Python program to how to add an extra column to an numpy array.

Expected Output:
[[ 10 20 30 100]
[ 40 50 60 200]]
"""
import numpy as np

array_a = np.array([[10,20,30], [40,50,60]])
print(array_a)

array_b = np.array([[100], [200]])

print(np.append(array_a, array_b, axis=1))