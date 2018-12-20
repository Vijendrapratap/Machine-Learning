"""
Write a Python program to reverse a tuple. 

"""
new_tuple = ("thing", "of", "beauty", "is", "joy", "forever")
print(new_tuple)

list1 = list(new_tuple)
list1 = list1[::-1]

new_tuple = tuple(list1)
print("reverse tuple is:",new_tuple)