gewicht = eval(input('Wat is je gewicht : '))
lengte = eval(input('Wat is je lengte (in meter) : '))
bmi = gewicht/(lengte**2)

if bmi <= 18.5:
    print('ondergewicht')
elif (bmi > 18.5) and (bmi <= 25):
    print('normaal')
else:
    print('Overgewicht')
