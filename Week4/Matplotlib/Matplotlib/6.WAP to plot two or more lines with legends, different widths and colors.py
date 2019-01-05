"""
Write a Python program to plot two or more lines with legends, different widths and colors.
"""

import matplotlib.pyplot as plt

x1 = [10,20,30]
y1 = [22,33,66]

x2 = [10,20,30]
y2 = [77,55,88]

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Two or more lines with different widths and colors with suitable legends ')

plt.plot(x1,y1, color='green', linewidth = 3,  label = 'line1')
plt.plot(x2,y2, color='orange', linewidth = 2,  label = 'line2', linestyle = 'dotted')

plt.legend()
plt.grid()
plt.show()