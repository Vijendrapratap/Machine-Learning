"""
Write a Python program to print all unique values in a dictionary. 
"""

L = [{"A":"Alfa"}, {"B": "Beta"}, {"C": "Comet"}, {"D": "Delta"}, {"E":"Episilone"}, {"F":"Fantom"},{"G":"Gama"}]

print("Original List: ",L)

u_value = set( val for dic in L for val in dic.values())

print("Unique Values: ",u_value)
