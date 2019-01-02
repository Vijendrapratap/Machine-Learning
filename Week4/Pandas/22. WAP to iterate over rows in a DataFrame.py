"""
Write a Python program to iterate over rows in a DataFrame.
"""
import pandas as pd

exam_data = [{'name':'Anastasia', 'score':12.5},
             {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
data = pd.DataFrame(exam_data)
for index, row in data.iterrows():
    print(row['name'], row['score'])