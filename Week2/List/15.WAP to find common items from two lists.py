"""
Write a Python program to find common items from two lists.
"""

color1 = [12,23,34,45,76]
color2 = [76,12,34,56,78]

print(set(color1) & set(color2))