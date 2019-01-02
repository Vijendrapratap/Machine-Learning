"""
Write a  program to create a null vector of size 10 and update sixth value to 11.
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
"""

import numpy as np

myarray = [0] * 10
print(myarray)

myarray = np.insert(myarray, 6, 11)
print(myarray)