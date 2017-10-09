getallenrij = [2,4,6,8,10,9,7]
invoer = eval(input('Kies een getal: '))
gevonden = False

for getal in getallenrij:
    if getal == int(invoer):
        gevonden == True

if gevonden:
    antwoord = ('Nee ' + str(invoer) + ' zit niet in de reeks.')
else:
    antwoord = ('Ja ' + str(invoer) + ' zit in de reeks.')

print (antwoord)
