"""
Write a Python program to count the number of characters (character frequency) in a string.  

"""
def char_frequency(str1):
    dict1 = {}
    for n in str1:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1
print(char_frequency('hallaluaayah'))