"""
Write a program  to determine if the python shell is executing on 32bit or 64bit
"""

import struct
print(struct.calcsize("P") * 8)
