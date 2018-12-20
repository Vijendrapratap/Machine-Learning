"""
Write a Python program to get the number of occurrences of a specified element in an array.  
"""

arr = [12, 12, 23, 34, 23, 34, 12, 56]
result = [[x,arr.count(x)] for x in set(arr)]
print(result)