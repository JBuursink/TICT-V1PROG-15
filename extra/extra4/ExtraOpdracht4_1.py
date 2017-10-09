temperatuur = eval(input('Welke temperatuur is het? '))

def hoeWarm(temperatuur):
    if temperatuur <= 0:
        print('Het vriest vandaag')
    elif temperatuur <= 15:
        print('Het is koud vandaag')
    else:
        print('Het is lekker weer vandaag')

hoeWarm(temperatuur)
