"""
Write a Python program to remove an item from a tuple. 
"""
tuple1 = ("thing", "of", "beauty", "is", "joy", "forever")
print(tuple1)

#convert tuple into a list
list1 = list(tuple1)
#remove element from list
list1.remove("joy")

#update list into a tuple
tuple1 = tuple(list1)
print(tuple1)
