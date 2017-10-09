import random
invoersom = eval(input('Wat wil je als som hebben: '))
aantalGelukt = eval(input('Hoe vaak moet de som {} zijn: '.format(invoersom)))

def diceprob(invoersom,aantalGelukt):
    poging = 0
    gelukt = 0
    while gelukt < aantalGelukt + 1:
        dob1 = random.randrange(1, 7)
        dob2 = random.randrange(1, 7)
        poging += 1
        if dob1 + dob2 == invoersom:
            gelukt += 1
    return poging

if invoersom >= 1 and invoersom <= 12:
    print('Na {} worpen'.format(diceprob(invoersom,aantalGelukt)))
else:
    print('Voer een getal in tussen 1 en 12')