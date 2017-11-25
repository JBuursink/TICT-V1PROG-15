try:
    bedrag = 4356
    aantal = eval(input('Geef bedrag:'))
    if aantal < 0:
        print('Negatieve getallen niet toegestaan')
    else:
        print(bedrag/aantal)
except ZeroDivisionError:
    print('Delen door 0 kan niet')
except NameError:
    print(' Gebruik cijfers')
except:
    print('Onjuiste invoer')
