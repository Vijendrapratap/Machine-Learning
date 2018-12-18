"""
Write a program to access and print a URL content to the console
"""


from http.client import HTTPConnection

conn = HTTPConnection("example.com")
conn.request("GET", "/")  

result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 

print(contents)
