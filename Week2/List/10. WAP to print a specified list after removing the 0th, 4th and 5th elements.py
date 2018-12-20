"""
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
"""
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in range(len(color)):
	if (i == 0) or (i == 4) or(i == 5):
		pass
	else:
		print(color[i])