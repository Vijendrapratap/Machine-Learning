"""
Write a Python program to count number of items in a dictionary value that is a list.
"""

dict =  {'Alfa': ['subj1', 'subj2', 'subj3'], 'beta': ['subj1', 'subj2']}

ctr = sum(map(len, dict.values()))
print(ctr)
