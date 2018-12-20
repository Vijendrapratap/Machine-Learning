"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases. 

"""
def conversion(word):
	print(word.upper())
	print(word.lower())

word = input("Enter word : ")
conversion(word)