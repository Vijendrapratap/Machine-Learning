"""
Write a Python program to create bar plots with error bars on the same figure. Sample Date
Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645

"""
import numpy as np
import matplotlib.pyplot as plt
N = 4
meanVelocity = (0.2474, 0.1235, 0.1737, 0.1824)
stdVelocity = (0.3314, 0.2278, 0.2836, 0.2645)

ind = np.arange(N)

width = 0.35
plt.bar(ind, meanVelocity, width, color='red')
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')

plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()