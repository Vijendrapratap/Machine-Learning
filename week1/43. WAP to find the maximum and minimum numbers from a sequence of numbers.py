"""
Write a program to print maximum and minimum of given list
"""

def min_max(list_elements):
    for i in range(len(list_elements)):
        for j in range(len(list_elements)):
            if list_elements[i] < list_elements[j]:
                list_elements[i], list_elements[j] = list_elements[j], list_elements[i]

    print("Minimum number is : {} \nMaximum number is : {}".format(list_elements[0], list_elements[-1]))

list_elements = [2,3,5,6,8,9,90,87,76,53,342,122,7856,245]
result = min_max(list_elements)
