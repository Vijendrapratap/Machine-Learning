"""
Write a program to print histogram of list

Author : vijendra pratap singh
Email : pratap.vijendrasingh96@gmail.com
"""
def histrogram(numbers_list):
    char = ''
    for i in numbers_list:
        for j in range(i):
            char += '@'
        print(char)
        char = ''


list_elements = [5,8,2,7,3,9,6,4]
histrogram(list_elements)
