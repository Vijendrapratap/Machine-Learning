"""
Write a Python program to multiplies all the items in a list.  

"""
def multiply(list_num):
	prod = 1
	for i in list_num:
		prod *= i
	return prod

list1 = [2,5,6,8,-1]
result = multiply(list1)
print(result)