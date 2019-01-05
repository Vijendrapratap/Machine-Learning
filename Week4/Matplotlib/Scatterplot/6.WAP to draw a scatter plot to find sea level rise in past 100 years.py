"""
Write a Python program to draw a scatter plot to find sea level rise in past 100 years.
"""
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('sea_level_data.csv')
year = data['year']
sea_levels = data[['CSIRO_sea_level']]

plt.scatter(year, sea_levels, edgecolors='g', facecolor = 'b')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sealevel')
plt.show()