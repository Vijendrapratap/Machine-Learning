"""
Write a Python program to add textures (black and white) to bars and wedges.
Note: Use bottom to stack the womens bars on top of the mens bars.
"""

import matplotlib.pyplot as plt
fig = plt.figure()
patterns = [ "|" , "\\" , "/" , "+" , "-", ".", "*","x", "o", "O" ]

ax = fig.add_subplot(111)
for i in range(len(patterns)):
    ax.bar(i, 3, color='white', edgecolor='black', hatch=patterns[i])

plt.show()