zin = 'all animals are equal but some animals are more equal than others'
aantal = {}
for woord in zin.split():
    if woord in aantal:
        aantal[woord] += 1
    else:
        aantal[woord] = 1
for woord in aantal:
    print ('{} komt {:3} keer voor' .format(woord,aantal[woord]))