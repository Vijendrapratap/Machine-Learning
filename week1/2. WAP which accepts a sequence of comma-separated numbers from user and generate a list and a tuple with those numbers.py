"""
Write a program which accepts a sequence of comma-separated numbers from user and
 generate a list and a tuple with those numbers.

 Example : input 3, 5, 7, 23
           output : list = [3, 5, 7, 23]
                    tupple = (3, 5, 7, 23)

Aurthor : vijendra pratap singh
Email : pratap.vijendrasingh96@gmail.com
"""

def convert_list_and_tupple():
    list_nmb = 3, 5, 7, 23

    #printing elements in form of list and tuple
    print("List : {} \nTupple : {}".format(list(list_nmb), tuple(list_nmb)))

convert_list_and_tupple()