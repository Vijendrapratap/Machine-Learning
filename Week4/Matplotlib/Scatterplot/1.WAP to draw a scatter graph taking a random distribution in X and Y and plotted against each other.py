"""
Write a Python program to draw a scatter graph
taking a random distribution in X and Y and plotted against each other.
"""

import matplotlib.pyplot as plt
import numpy as np

X = np.random.rand(200)
Y = np.random.rand(200)

plt.scatter(X,Y, color='b')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()