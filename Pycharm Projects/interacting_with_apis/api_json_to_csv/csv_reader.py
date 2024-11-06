import csv
from pprint import pprint

with open("csv_file.csv",'r') as fp:
    csv_r = csv.reader(fp, delimiter="|")
    rows = []
    for row in csv_r:
        rows.append("".join(row))


pprint(rows)