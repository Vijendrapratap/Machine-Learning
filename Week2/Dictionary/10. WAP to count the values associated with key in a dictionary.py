"""
Write a Python program to count the values associated with key in a dictionary.
"""
student = [{'id': 1, 'success': True, 'name': 'alfa'},
 {'id': 2, 'success': False, 'name': 'beta'},
 {'id': 3, 'success': True, 'name': 'gama'}]
 
print(sum(d['success'] for d in student))