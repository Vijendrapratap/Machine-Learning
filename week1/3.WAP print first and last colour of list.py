"""
Make a program to print first and last colour from a list of colours

Author : vijendra pratap singh
Email : pratap.vijendrasingh96@gmail.com
"""

def colour_display():
    colour_list = ["Red", "Blue", "Black", "White", "Yellow", "Green"]

    #print first and last element of the list
    print("First colour is : {}  \nLast colour is : {}".format(colour_list[0], colour_list[-1]))

colour_display()