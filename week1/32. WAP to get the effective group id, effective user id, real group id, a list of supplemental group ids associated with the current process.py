"""
Write a program to get the effective group id user id associated with current process
"""

import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()

