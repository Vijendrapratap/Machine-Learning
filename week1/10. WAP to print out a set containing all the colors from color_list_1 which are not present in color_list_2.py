"""
Write a program to print out a set containing elements of list1 which are not present in list2
"""

list_1 = ["Blue","Green", "White", "Black", "Yellow"]
list_2 = ["Red", "Blue", "Yellow", "Green"]
list_3 = set()

for i in list_1:
    if i not in list_2:
        list_3.add(i)

print(list_3)