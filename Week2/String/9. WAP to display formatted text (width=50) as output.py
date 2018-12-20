"""
Write a Python program to display formatted text (width=50) as output. 

"""

import textwrap
sample_text = '''
  it start with one thing i dont know why it doesnt even matter how hard you try keep that in mind i design this 
  rhyme to remind myself
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()