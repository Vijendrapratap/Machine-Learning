"""
write a program to print calendar of given month and year

Author : vijendra pratsp singh
Email : pratap.vijendrasingh96@gmail.com
"""

import calendar as c

def calendar():
    l_month = int(input("Enter month :"))
    l_year = int(input("Enter year : "))

    print(c.month(l_year, l_month))

calendar()