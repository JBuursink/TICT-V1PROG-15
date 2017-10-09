def convert(Celcius):
        Fahrenheit = Celcius * 1.8 + 32
        return Fahrenheit

def table():
    getallen = range(-30,41,10)
    for getal in getallen:
        print('{:5} {:5}' .format(convert(getal),getal))


print('{:5} {:5}'.format('  F', '   C'))
table()
