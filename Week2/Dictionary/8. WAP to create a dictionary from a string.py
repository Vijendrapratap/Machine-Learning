"""
Write a Python program to create a dictionary from a string.
"""


str1 = 'hakunamatata' 
my_dict = {}

for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)