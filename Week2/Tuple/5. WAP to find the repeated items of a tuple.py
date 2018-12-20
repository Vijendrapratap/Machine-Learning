"""
Write a Python program to find the repeated items of a tuple. 
"""

new_tuple = (12, 23, 34, 45, 56, 67, 78, 56, 34, 23, 23)

result = dict((i, new_tuple.count(i)) for i in new_tuple)
print(result)