"""
Write a Python program to draw a line with suitable label in the x axis, y axis and a title
"""

import matplotlib.pyplot as plt

X = range(1, 25)
Y = [value * 2 for value in X]
print("Values of X:")
print(*range(1,25))
print("Values of Y (twice of X):")

print(Y)
plt.plot(X, Y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')
plt.title('Draw a line.')

plt.show()