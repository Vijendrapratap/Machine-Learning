"""
Write a Python program to display the current axis limits values and set new axis values.
"""
import matplotlib.pyplot as plt
X = range(1, 75)
Y = [i * 3 for i in X]

plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')

print(plt.axis())

plt.axis([0, 100, 0, 200])
plt.grid()
plt.show()
