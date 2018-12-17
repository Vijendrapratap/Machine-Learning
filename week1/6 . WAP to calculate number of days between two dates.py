"""
Write a program to calculate number of between two dates

Aurthor : vijendra pratap singh
Email : pratap.vijendrasingh96@gmail.com
"""
from datetime import date

start_day = int(input("Enter date : "))
start_month = int(input("Enter month : "))
start_year = int(input("Enter year : "))

print("Enter dates from which you wanna check number of days \n\n")

end_day = int(input("Enter date : "))
end_month = int(input("Enter month : "))
end_year = int(input("Enter year : "))

f_date = date(start_year, start_month, start_day)
l_date = date(end_year, end_month, end_day)
delta = l_date - f_date
print(abs(delta.days))