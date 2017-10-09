def seizoen(maand):
    if maand <= 2 and maand > 0 or maand == 12:
        seizoen = 'Winter'
    elif maand <= 5 and maand >= 3:
        seizoen = 'lente'
    elif maand <= 8 and maand >= 6:
        seizoen = 'Zomer'
    elif maand <= 11 and maand >= 9:
        seizoen = 'Herfst'
    if maand <= 0 or maand >= 13:
        seizoen = 0
    return seizoen

maand = eval(input('wat is het maandnummer : '))
if seizoen(maand) != 0:
    print('Maandnummer {} is tijdens de {}.'.format (maand,seizoen(maand)))
else:
	print('Error: Het maandnummer moet tussen 1 en 12 zijn.')
