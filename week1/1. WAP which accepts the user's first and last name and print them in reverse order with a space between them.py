"""
Take user's name as input and print in reverse order

Example:
    name: alfa singh
    output : afla hgnis

    Author : vijendra pratsp singh
    Email : pratap.vijendrasingh96@gmail.com
"""

def reverse_name():
    f_name = input("Enter your first name : ")
    l_name = input("Enter your last name : ")

    f_name.split()
    l_name.split()

    f_name = f_name[::-1]
    l_name = l_name[::-1]

    print("Hello! {} {}".format(f_name, l_name))

reverse_name()

