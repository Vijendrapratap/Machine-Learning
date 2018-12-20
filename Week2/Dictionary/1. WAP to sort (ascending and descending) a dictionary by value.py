"""
Write a Python script to sort (ascending and descending) a dictionary by value. 
"""

a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}

a1_sorted_keys = sorted(a1, key=a1.get, reverse=False)

for r in a1_sorted_keys:
    print(r, a1[r])
