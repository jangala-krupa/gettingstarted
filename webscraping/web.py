import csv

with open("cars.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])