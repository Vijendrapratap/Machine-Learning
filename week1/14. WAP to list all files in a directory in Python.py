"""
Write a program to list all files in a directory
"""

#importing OS module to perform system operations
from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
print(files_list);
