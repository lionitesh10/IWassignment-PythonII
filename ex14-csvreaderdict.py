import csv
csvlist = []
with open("people.csv", 'r') as f:
    my_file = csv.DictReader(f)
    for row in my_file:
        csvlist.append(dict(row))
print(csvlist)
