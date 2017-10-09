import csv
with open('gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        print(row[0],row[2])