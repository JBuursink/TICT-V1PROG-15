leeftijd = input('Wat is je leeftijd: ')
paspoort = input('Ben je in bezit van een geldig Nederlands paspoort?')

if int(leeftijd) > 17 and paspoort == ('ja'):
    print('Gefeliciteerd, je mag stemmen!')
else:
    if int(leeftijd) < 18:
        print('Helaas ben je nog te jong om te stemmen.')
    else:
        print('Helaas heb je een geldig Nederlands paspoort nodig om te stemmen.')