"""
Write a program to check whether a file exist or not
"""

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
