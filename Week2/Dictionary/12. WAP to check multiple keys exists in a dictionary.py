"""
Write a Python program to check multiple keys exists in a dictionary.
"""

student = {
  'name': 'Alfa',
  'class': '10',
  'roll_id': '2'
}

print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alfa'})
print(student.keys() >= {'roll_id', 'name'})