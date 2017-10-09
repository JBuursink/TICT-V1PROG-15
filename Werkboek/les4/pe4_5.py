def kwadraten_som():
    som = 0
    getallen = [4,5,3,-81]
    for i in getallen:
        if i > 0:
            som += i**2
    return som

print(kwadraten_som())