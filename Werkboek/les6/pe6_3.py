invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer = invoer.split('-')
invoer.sort()
aantal = 1
som = 0
for i in invoer:
    som += int(i)
    aantal += 1
print('Gesorteerde list van ints: {}'.format (invoer))
print('Grooste getal: {} en Kleinste getal: {}'.format(invoer[-1],invoer[0]))
print('Aantal getallen: {} en Som van de getallen: {}'.format (aantal,som))
print('Gemiddelde: {}'.format(som/aantal))