"""
Write a Python program to remove an item from a set if it is present in the set. 
"""

new_set = {1,2,3,4,5,6,7}
element = int(input("Enter number : "))
if element in new_set:
	print("Element is present in given set ")
	new_set.discard(element)
else:
	print("Element is nort present in set ")

print(new_set)

