import csv
import pandas as pd
df = pd.read_csv('foo.csv')

for i in df:
    print(i)
