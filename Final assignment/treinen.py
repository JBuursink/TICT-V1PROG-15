stations =['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam','Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
           'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    begin = input('Wat is je beginstation? ')
    while begin not in stations:
        begin = input('Wat is je beginstation? ')
    return begin

def inlezen_eindstation(stations):
    eind = input('Wat is je eindstation? ')
    while eind not in stations:
        eind = input('Wat is je beginstation? ')
    return eind

def omroepen_reis(stations):
    beginIndex = stations.index(inlezen_beginstation(stations))
    eindIndex = stations.index(inlezen_eindstation(stations))
    veschil = eindIndex-beginIndex
    print('Het beginstation {} is het {}e station in het traject.'.format(stations[beginIndex],beginIndex+1))
    print('Het eindstation {} is het {}e station in het traject.'.format(stations[eindIndex],eindIndex+1))
    print('De afstand bedraagt {} station(s).'.format(veschil))
    print('De prijs van het kaartje is {} euro.'.format(5*(veschil)))
    print('\n')
    print('Jij stapt in de trein in: {}'.format(stations[beginIndex]))
    for i in range(veschil-1):
        print('- {}'.format(stations[beginIndex+i+1]))
    print('Jij stapt uit in: {}'.format(stations[eindIndex]))

omroepen_reis(stations)