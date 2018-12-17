"""
Wrirte a program to check whether a specific value is in group of values or not

Example: 3--> [3,4,6,7,9,23,456,678,78]  True
         1--> [23,345,46,786,89,89789,]  False

Author : vijendra pratap singh
Email : pratap.vijendrasingh96@gmail.com
"""

def check(element, group_of_elements):
    if element in group_of_elements:
        return True
    else:
        return False

group = [2,4,7,9,12,23,34,45,56,67,78,89,90]
element = input("Enter a number : ")
result = check(element, group)
print(result)