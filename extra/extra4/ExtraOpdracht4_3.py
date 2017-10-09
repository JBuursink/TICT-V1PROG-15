getallenrij = [23,35,31,26,73,75,84,29,42,46]

def totaal(getallenrij):
    som = 0
    som1 = 0
    for getal in getallenrij:
        if getal % 2 == 0:
            som += getal
        else:
            som1 += getal
    return (som,som1)

totaal(getallenrij)
print('De som van de even getallen bedraagt {}, {}'.format(),(s))

