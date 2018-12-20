"""
Write a Python program to sum all the items in a list.  

"""

def sum(list_num):
	sum = 0
	for i in list_num:
		sum += i
	return sum

list1 = [2,54,56,98,-12]
result = sum(list1)
print(result)