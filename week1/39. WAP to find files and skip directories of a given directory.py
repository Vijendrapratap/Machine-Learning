"""
Write a program to find files and skip directories 
"""

from os import listdir
from os.path import isfile, join


def find_skip_files(path):
    skip_files_list = [f for f in listdir(path) if isfile(join(path, f))]
    return skip_files_list


path = 'your/path'
result = find_skip_files(path)
print("Skip files list are,", result)
