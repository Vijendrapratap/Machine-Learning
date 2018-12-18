"""
Write a program to empty a variable without destroying it
"""


def empty_variable(l_var_1, l_var_2):
    print("Before empty is ", l_var_1, "After empty is", type(l_var_1)())
    print("Before empty is ", l_var_2, "After empty is", type(l_var_2)())


g_var_1 = 20
g_var_2 = {1: 'Test'}
empty_variable(g_var_1, g_var_2)
