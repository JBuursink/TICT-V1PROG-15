import csv
with open('inloggers.csv','w',newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        naam = input('Wat is je naam:')
        if naam == 'einde':
            break
        voorL = input('Wat zijn je voorletters:')
        geboortedatum = input('Wat is je geboortedatum:')
        email = input('Wat is je email adres:')
        writer.writerow((naam,voorL,geboortedatum,email))
