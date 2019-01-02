"""
Write a Python program to convert a Panda module Series to Python list and it's type.
"""
import pandas as pd

myseries = pd.Series([2, 4, 6, 8, 10])

print("Pandas Series and type")
print(myseries)
print(type(myseries))

print("Convert Pandas Series to Python list")
print(myseries.tolist())
print(type(myseries.tolist()))