infile = open("hardlopers.txt", 'a')
import datetime

def tijd():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    return s

tijd = tijd()

naam = input('Wat is je naam: ')
infile.write('{}, {}\n ' .format(tijd,naam))

infile.close()