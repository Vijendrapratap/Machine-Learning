"""
Write a Python program to check whether an element exists within a tuple. 
"""
new_tuple = (12, 23, 34, 45, 56, 67, 78)
element = int(input("Enter element : "))
if element in new_tuple:
	print("{} is present in tuple ".format(element))
else:
	print("{} is not present in tuple".format(element))