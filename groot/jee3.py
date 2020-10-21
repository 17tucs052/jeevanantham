import csv
from itertools import islice

with open('cj.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in islice(reader, 10): 
        print(row['tweet'])
