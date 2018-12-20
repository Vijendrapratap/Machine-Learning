"""
Write a Python program to remove the first occurrence of a specified element from an array. 
"""	

arr = ["12", "23", "45" , "56", "67", "23", "12"]
for i in arr:
	if arr.count(i) > 1:
		arr.remove(i)

print(arr)