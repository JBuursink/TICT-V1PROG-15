totaal = 0
getal = eval(input('Geef een getal: '))
aantal = 1
while getal != 0:
    totaal += getal
    getal = eval(input('Geef een getal: '))
    aantal += 1

if aantal > 1:
    print('Er zijn {} getallen ingevoerd, de som is: {}'.format(aantal,totaal))
elif aantal == 1:
    print('Er is 1 getal ingevoerd, dit getal is {}'.format(totaal))