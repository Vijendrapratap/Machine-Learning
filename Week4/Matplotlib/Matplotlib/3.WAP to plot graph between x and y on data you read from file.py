"""
Write a Python program to draw a line using given axis values taken from a text file,
with suitable label in the x axis, y axis and a title.
Test Data:
test.txt
1 2
2 4
3 1

"""

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('test.txt', index_col=0)
df.plot(x = df.index, y = df.columns)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')

plt.show()