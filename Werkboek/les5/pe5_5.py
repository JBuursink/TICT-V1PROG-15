def gemiddelde(zin):
    totaal = 0
    aantalWoorden = 0
    nieuw = zin.split()
    for woord in nieuw:
        totaal += len(woord)
        aantalWoorden += 1
    gemiddeld = round(totaal/aantalWoorden)
    return gemiddeld

zin = input('zin: ')
print('Het gemiddelde aantal tekens per woord is {} tekens.'.format(gemiddelde(zin)))