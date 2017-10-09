naam = input('Wat is je naam: ')
leeftijd = eval(input('Wat is je leeftijd: '))

if int(leeftijd) < 18:
    print(naam + ' jij mag niet stemmen.')
else:
    print(naam + ' jij mag wel stemmen.')